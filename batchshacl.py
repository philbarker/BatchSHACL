#!/usr/bin/env python
from BatchSHACL import BatchValidate, parse_arguments, getFileNames

if __name__ == "__main__":
    args = parse_arguments()
    folder_name = args.folder_name
    shacl_file_name = args.shacl_file_name
    data_ext = args.data_ext
    results_ext = args.results_ext
    print(
        "\nChecking validation of files \n\twith extension",
        data_ext,
        "\n\tin folder",
        folder_name,
        "\n\tusing shacl file",
        shacl_file_name,
        "\n\tagainst results stored in .",
        results_ext,
        "files.\n",
    )
    file_list = getFileNames(folder_name, data_ext)
    bv = BatchValidate(file_list, shacl_file_name)
    diffs = bv.runValidations()
    for file in diffs.keys():
        (code, msg) = diffs[file]
        if code == 0 : #todo: colour code results
            print(file, msg)
        else :
            print(file, msg)
