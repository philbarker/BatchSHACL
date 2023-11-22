import pytest
from BatchSHACL import BatchValidate, result_ext

shacl_file_name = "Tests/TestData/shacl.ttl"
rslt = result_ext
data_file_list = [
    "Tests/TestData/test1.ttl",
    "Tests/TestData/test2.ttl",
    "Tests/TestData/test3.ttl",
]
expected_results = """Validation Report
Conforms: True"""
expected_vals = [
    (0, "Results are as expected."),
    (0, "Results are as expected."),
    (1, "Results are not as expected."),
]


def test_init():
    bv = BatchValidate(data_file_list, shacl_file_name)
    assert bv.shacl_file_name == shacl_file_name
    assert bv.data_file_list == data_file_list
    with pytest.raises(TypeError) as e:
        bv = BatchValidate("test.ttl", shacl_file_name)
    assert str(e.value) == "Data_file_list must be a list."
    with pytest.raises(FileExistsError) as e:
        bv = BatchValidate(data_file_list, "not_there.ttl")
    assert str(e.value) == "File not_there.ttl does not exist."


def test_read_result_file():
    bv = BatchValidate(data_file_list, shacl_file_name)
    results = bv._read_result_file("Tests/TestData/test1.rslt")
    assert results == expected_results
    results = bv._read_result_file("not_there")
    assert results == False
    with pytest.raises(TypeError) as e:
        results = bv._read_result_file(5)
    assert str(e.value) == "Result file name must be a string."


def test_compareResults():
    bv = BatchValidate(data_file_list, shacl_file_name)
    c = bv._compareResults("same", "same", "test.ttl")
    assert c == (0, "Results are as expected.")
    c = bv._compareResults("same", False, "test.ttl")
    assert c == (0, "No expected result file found for comparison.")
    c = bv._compareResults("same", "different", "test.ttl")
    assert c == (1, "Results are not as expected.")


def test_runValidations():
    bv = BatchValidate(data_file_list, shacl_file_name)
    vals = bv.runValidations()
    assert vals == expected_vals
