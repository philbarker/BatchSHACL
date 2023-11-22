A program to batch-test RDF files against SHACL constraints, based on pyshacl.  Useful for running tests when developing an extensive set of SHACL rules for complex data sets.

Alpha version, please use with care, in a virtual environment, and report bugs.

## Usage
```
$batchshacl.py [-h] [-e <data file .ext>] [-r <results file .ext>] [<path/to/shacl/file>] [<path/to/data/files/>]
```

Checks that the results of shacl validation for files in a specified folder are as expected.

__Positional arguments:__

  `<path/to/shacl/file>` (defaults to current directory)

  `<path/to/data/files/>` (defaults to ./shacl.ttl)

options:

  `-h, --help`            show this help message and exit

  `-e <data file .ext>`, `--data_ext <data file .ext>` Sets the data file extension. Defaults to `.ttl`.

  `-r <results file .ext>`, `--results_ext <results file .ext>` Sets the expected results file extension. Defaults to `.rslt`. 

Expects a results file `[file].rslt` for every data file `[file].ttl` that contains the expected human readable SHACL results. Will complain if the actual SHACL results differ from this. 

## Current Known Limitations
Only tested with .ttl files.

Uses only default pyshacl settings. 