from os.path import isdir
from glob import iglob
from argparse import ArgumentParser


def getFileNames(p, ext):
    """Return a list of file names from the data directory at path p with extension ext."""
    file_list = []  # list of files to return
    if isdir(p):
        for filename in iglob(p + "*." + ext):
            file_list.append(filename)
    else:
        msg = "Must specify a directory for the data files."
        raise ValueError(msg)
    return file_list


def parse_arguments():
    parser = ArgumentParser(
        prog="batchshacl.py",
        description="Checks that the results of shacl validation for files in a specified folder are as expected.",
    )
    parser.add_argument(
        "shacl_file_name",
        nargs="?",
        type=str,
        metavar="<path/to/shacl/file>",
        default="shacl.ttl",
    )
    parser.add_argument(
        "folder_name", nargs="?", type=str, metavar="<path/to/data/files/>", default="."
    )
    parser.add_argument(
        "-e",
        "--data_ext",
        type=str,
        metavar="<data file .ext>",
        default="ttl",
    )
    parser.add_argument(
        "-r",
        "--results_ext",
        type=str,
        metavar="<results file .ext>",
        default="rslt",
    )
    return parser.parse_args()
