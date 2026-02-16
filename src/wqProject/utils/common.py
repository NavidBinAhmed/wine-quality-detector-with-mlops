import os
import yaml
from box.exceptions import BoxValueError
from wqProject import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box import ConfigBox

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml files and returns:
    
    Args:
        path_to_yaml (str): path input
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type 
    """
    try:
        with open (path_to_yaml) as yaml_files:
            content=yaml.save_load(yaml_files)
            logger.info(f"yaml files: {path_to_yaml} is loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("empty yaml file")
    except Exception as e:
        raise e
 
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories
    
    Args:
    path_to_directories (list) : list of path to directories
    ignore_log (bool): ignore if multiple directories is created. Default is False
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves json data
    
    Args:
    path (str): path to json file
    data (dict): data to save in json file
    """
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        logger.info(f"json file saved at: {path}")
        

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load the data from json file and returns as ConfigBox
    
    Args:
    path (str): path to json file
    
    Returns:
    ConfigBox: data as class attributes instead of dictionary keys
    """
    with open(path) as f:
        content=json.load(f)
        logger.info(f"json file loaded from: {path}")
        return ConfigBox(content)
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    saves binary data
    
    Args:
    data (Any): data to be saved in binary format
    path (str): path to save the binary file
    """
    
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
    

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads binary data and returns it
    
    Args:
    path (str): path to binary file
    
    Returns:
    Any: data stored and loaded in the binary file
    """
    
    data=joblib.load(filename=path)
    logger.info(f"binary file loaded from: {path}")
    return data
    

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size of the file
    
    Args:
    path (str): path to the file
    
    Returns (str): size of the file
    """
    
    size_in_kb=round(os.path.getzize(path)/1024)
    return f"{size_in_kb} KB"
    