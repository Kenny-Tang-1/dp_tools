
from pathlib import Path
from dp_tools.core.check_model import FlagCode
from dp_tools.microarray.checks import check_file_size, check_if_valid_extensions
import os

def test_check_if_valid_extensions():
    results = check_if_valid_extensions(file = Path("Some.txt"), valid_extensions = (".txt",".csv",".tsv"))
    assert results['code'] == FlagCode.GREEN
    assert results['message']


def test_check_file_size():
    result = check_file_size(file = Path("C:/Users/tangk/Desktop/Test.txt"))
    assert result['code'] == FlagCode.GREEN
    assert result['message'] == f"This file is not empty: Test.txt, 48 bytes"