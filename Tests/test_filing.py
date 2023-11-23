import pytest
from BatchSHACL import getFileNames


def test_getFiles():
    filelist = getFileNames("Tests/TestData/", "ttl")
    assert len(filelist) == 5
    assert "Tests/TestData/test1.ttl" in filelist
    assert "Tests/TestData/test2.ttl" in filelist
    assert "Tests/TestData/shacl.ttl" in filelist
    assert "Tests/TestData/test3.ttl" in filelist
    assert "Tests/TestData/test4.ttl" in filelist
    filelist = getFileNames("Tests/TestData/", "doc")
    assert filelist == []
    with pytest.raises(ValueError) as e:
        filelist = getFileNames("test", "doc")
    assert str(e.value) == "Must specify a directory for the data files."
