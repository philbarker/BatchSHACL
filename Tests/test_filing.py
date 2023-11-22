import pytest
from BatchSHACL import getFileNames


def test_getFiles():
    filelist = getFileNames("Tests/TestData/", "ttl")
    assert filelist == [
        "Tests/TestData/test1.ttl",
        "Tests/TestData/test2.ttl",
        "Tests/TestData/shacl.ttl",
        "Tests/TestData/test3.ttl",
    ]
    filelist = getFileNames("Tests/TestData/", "doc")
    assert filelist == []
    with pytest.raises(ValueError) as e:
        filelist = getFileNames("test", "doc")
    assert str(e.value) == "Must specify a directory for the data files."
