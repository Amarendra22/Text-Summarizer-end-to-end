import os
from pathlib import Path
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from textSummarizer.logging import logger
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns as ConfigBox.

    Args:
        path_to_yaml (Path): Path to YAML file.

    Raises:
        ValueError: If YAML file is empty.
        FileNotFoundError: If the file doesn't exist.
        yaml.YAMLError: If there's an error parsing the YAML.

    Returns:
        ConfigBox: Parsed YAML content as ConfigBox.
    """
    try:
        with open(path_to_yaml, 'r', encoding='utf-8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file '{path_to_yaml}' loaded successfully")
            return ConfigBox(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path_to_yaml}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML: {e}")
    except Exception as e:
        raise e

    


@ensure_annotations
def create_directories(path_to_directories: list, ignore_log=False):
    """Create directories if they don't exist.

    Args:
        path_to_directories (list): List of directory paths.
        ignore_log (bool, optional): Ignore logging. Defaults to False.
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if not ignore_log:
                logger.info(f"Created directory: {path}")
        except FileExistsError:
            logger.warning(f"Directory already exists: {path}")
        except Exception as e:
            logger.error(f"Failed to create directory: {path}. Error: {e}")




def get_size(path: Path) -> str:
    """Get size of file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of file in KB.
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~ {size_in_kb} KB"
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        return "File not found"
    except Exception as e:
        logger.error(f"Failed to get file size: {e}")
        return "Unknown error"


    