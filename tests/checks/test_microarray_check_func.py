
from pathlib import Path
from dp_tools.core.check_model import FlagCode
from dp_tools.microarray.checks import check_colnames, check_file_size, check_if_file_exists, check_if_valid_extensions
import os

def test_check_if_valid_extensions():
    results = check_if_valid_extensions(file = Path("Some.txt"), valid_extensions = (".txt",".csv",".tsv"))
    assert results['code'] == FlagCode.GREEN
    assert results['message']


def test_check_file_size():
    result = check_file_size(file = Path("C:/Users/tangk/Desktop/Test.txt"))
    assert result['code'] == FlagCode.GREEN
    assert result['message'] == f"This file is not empty: Test.txt, 48 bytes"

def test_check_if_file_exists():
    results = check_if_file_exists(file = Path("C:/Users/tangk/Desktop/Agilent_Microarray/output_data/GLDS-41_output_data/Raw_gene_level_data-GLDS-41.csv"))
    assert results['code'] == FlagCode.GREEN
    assert results['message'] == f"The file exists!: Raw_gene_level_data-GLDS-41.csv"

def test_check_colnames():
    results = check_colnames(file = Path("C:/Users/tangk/Desktop/Agilent_Microarray/output_data/GLDS-41_output_data/Probe_level_annotated_DGE_with_Normalized_Intensities_GLDS_41.csv"), colnames = ["Row","Col","ProbeUID","Not a Column"])
    assert results ['code'] == [FlagCode.GREEN, FlagCode.GREEN, FlagCode.GREEN, FlagCode.YELLOW]