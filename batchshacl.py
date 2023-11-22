#!/usr/bin/env python
from BatchSHACL import BatchValidate, parse_arguments, getFileNames

if __name__ == "__main__":
    args = parse_arguments()
    print(args)
    folder_name = args.folder_name
    shacl_file_name = args.shacl_file_name
    data_ext = args.data_ext
    results_ext = args.results_ext
    print(
        "Checking validation of files with extension",
        data_ext,
        "in folder",
        folder_name,
        "using shacl file",
        shacl_file_name,
        "against results stored in ",
        results_ext,
        "files.",
    )
    file_list = getFileNames(folder_name, data_ext)
    bv = BatchValidate(file_list, shacl_file_name)
    bv.runValidations()
