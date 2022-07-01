from pathlib import Path
from dp_tools.core.check_model import FlagCode, FlagEntry
import os

def check_file_exists(file: Path) -> FlagEntry:
    # check logic
    if file.is_file():
        code = FlagCode.GREEN
        message = f"File exists: {file.name} "
    else:
        code = FlagCode.HALT
        message = f"Missing file: {file.name} expected at {str(file)} "
    return {"code": code, "message": message}

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


    