from pyshacl import validate
from os.path import exists, splitext

result_ext = ".rslt"  # default extension for result files


class BatchValidate:
    """Validate a batch of files against shacl."""

    def __init__(self, data_file_list, shacl_file_name):
        if type(data_file_list) is not list:
            msg = "Data_file_list must be a list."
            print(data_file_list)
            raise TypeError(msg)
        elif len(data_file_list) == 0:
            msg = "No files to check."
            print(msg)
            return
        # fix error that happens when shacl.ttl is in same dir as data files
        elif shacl_file_name in data_file_list:
            data_file_list.remove(shacl_file_name)
            self.data_file_list = data_file_list
        else:
            self.data_file_list = data_file_list
        if exists(shacl_file_name):
            self.shacl_file_name = shacl_file_name
        else:
            msg = "File " + shacl_file_name + " does not exist."
            raise FileExistsError(msg)

    def runValidations(self):
        data_file_list = self.data_file_list
        diff_list = []
        for data_file_name in data_file_list:
            print("Checking", data_file_name)
            stem = splitext(data_file_name)[0]
            result_file_name = stem + result_ext
            (conforms, results_graph, results_text) = self._validateFile(
                data_file_name, result_file_name
            )
            #           print(conforms, results_graph, results_text)
            expected_results = self._read_result_file(result_file_name)
            diff = self._compareResults(results_text, expected_results, data_file_name)
            diff_list.append(diff)
        return diff_list

    def _compareResults(self, results_text, expected_results, data_file_name):
        #        print("results:\n", results_text)
        #        print("expected results:\n", expected_results)
        if not expected_results:
            print("No expected result file found for " + data_file_name + ".")
            print("pyshacl results are:")
            print(results_text)
            return (0, "No expected result file found for comparison.")
        else:
            for result_line in results_text.split("\n"):
                if result_line in expected_results:
                    pass
                else:
                    print(
                        "Info: found ",
                        result_line,
                        "in pyshacl results but not in expected results.",
                    )
                    print("Results for " + data_file_name + " are as not as expected.")
                    return (1, "Results are not as expected.")
            print("Results for " + data_file_name + " are as expected.")
            return (0, "Results are as expected.")

    def _validateFile(self, data_file_name, result_file_name):
        shacl_file_name = self.shacl_file_name
        data_file_name = data_file_name
        r = validate(data_file_name, shacl_graph=shacl_file_name)
        return r

    def _read_result_file(self, file_name):
        if type(file_name) is not str:
            msg = "Result file name must be a string."
            print(file_name)
            raise TypeError(msg)
        elif exists(file_name):
            with open(file_name) as f:
                results = f.read()
        else:
            print("No results file found called " + file_name + ".")
            results = False
        return results
