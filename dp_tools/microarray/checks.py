from pathlib import Path
from dp_tools.core.check_model import FlagCode, FlagEntry
import os
import pandas as pd

def check_if_valid_extensions(file: Path, valid_extensions: tuple[str]) -> FlagEntry:
    """ This function looks at the extension of the file and
        tells whether it is a valid extension or not.

    :param file: Input raw data file
    :type file: Path
    :param valid_extensions: Extensions that are allowed for the raw data files
    :type valid_extensions: tuple[str]
    :return: A required fields-only flag entry dictionary
    :rtype: FlagEntry
    """
    if file.name.endswith(valid_extensions):
        code = FlagCode.GREEN
        message = f"File is valid: {file.name}"
    else:
        code = FlagCode.HALT
        message = f"File does not have a valid extension!: {file.name}"
    return {"code": code, "message": message}


def check_file_size(file: Path) -> FlagEntry:
    """ This function looks at the raw data file to see if it has content.
        
    :param file: Input raw data file
    :type file: Path
    :return A required fields-only flag entry dictionary
    :rtype: FlagEntry
    """
    file_size = os.path.getsize(file)
    if file_size == 0:
        code = FlagCode.HALT
        message = f"This file is empty!: {file.name}, {file_size} bytes "
    else:
        code = FlagCode.GREEN
        message = f"This file is not empty: {file.name}, {file_size} bytes"
    return {"code": code, "message": message}


def check_if_file_exists(file: Path) -> FlagEntry:
    """ This function checks the output file to make sure that
    the files were generated.

    :param path_to_file: Absolute path to the file (including filename)
    :type path_to_file: Path
    :param valid_ext: File extensions to check for
    :type valid_ext: tuple[str]
    :return: A required fields-only flag entry dictionary
    :rtype: FlagEntry
    """    
    
    if file.is_file():
        code = FlagCode.GREEN
        message = f"The file exists!: {file.name}"
    else:
        code = FlagCode.HALT
        message = f"The file does not exist: {file.name}"
    return {"code": code, "message": message}


def check_colnames(file: Path, colnames: list[str]) -> FlagEntry:
    """A function that checks the output CSV file to make sure it contains the 
    correct columns.

    :param file: Absolute path to the file
    :type file: Path
    :param colnames: List of the column names to check for in the CSV file
    :type colnames: list[str]
    :return: A required fields-only flag entry dictionary
    :rtype: FlagEntry
    """    """"""
    code_list = [] # Will store the codes after each iteration
    message_list = [] # Will store the messages after each iteration
    file = pd.read_csv(file)
    header = file.columns.values.tolist() # Putting the column names into a list(file.columns)
    for name in colnames:
        if name in header:
            code = FlagCode.GREEN
            message = f"The column exists!: {name}"
            code_list.append(code)
            message_list.append(message)
        else:
            code = FlagCode.HALT
            message = f"The column does not exist!: {name}"
            code_list.append(code)
            message_list.append(message)
    return {"code": code_list, "message": message_list} 