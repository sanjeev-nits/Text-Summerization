import os
from box.exceptions import BoxValueError
import yaml
from textsummerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file wrapped in a ConfigBox.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} read successfully.")
            return ConfigBox(content)
    except FileNotFoundError as e:
        raise ValueError(f"YAML file not found: {path_to_yaml}") from e
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_dirs: list,verbose=True):
    """
    create list of directories
    Args:
        path_to_dirs (list): List of directory paths to create.
        ignore_log (bool): If True, does not log the creation of directories.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")
    

@ensure_annotations
def get_size(path: Path) -> str:
    """ get size in kb
    
    Args:
        path (Path): Path to the file or directory.
    Returns:
        str: Size in kb.
    """
    size_in_kb=round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"