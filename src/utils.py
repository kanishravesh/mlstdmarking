import os 
import sys
from src.exception import customException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import numpy as np
from dill import dump, load

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dump(obj, file_obj)
    except Exception as e:
        logging.error("Error occurred while saving object")
        raise customException(e, sys)
