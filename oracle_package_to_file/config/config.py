import os
import configparser

from datetime import datetime
from dotenv import load_dotenv

from py_logger.logger import get_logger

load_dotenv()

conf = configparser.ConfigParser()
conf.read("resource/config.ini")

def get_param(config_name, param_name):
    return (
        os.getenv(param_name)
        if os.getenv(param_name)
        else conf.get(config_name, param_name)
    )

OUTPUTS_DIR = "output"
LOGS_DIR = "logs"
LOG_FILE = "oracle_package_to_file"

PKG_DIR = os.path.join(OUTPUTS_DIR, "pkgs/" + datetime.now().strftime("%Y%m%d%H%M%S"))
DATA_SOURCE_SCHEMA_NAME = get_param("data_source", "DATA_SOURCE_SCHEMA_NAME")
DATA_SOURCE_USER = get_param("data_source", "DATA_SOURCE_USER")
DATA_SOURCE_PASSWORD = get_param("data_source", "DATA_SOURCE_PASSWORD")
DATA_SOURCE_HOST = get_param("data_source", "DATA_SOURCE_HOST")
DATA_SOURCE_PORT = int(get_param("data_source", "DATA_SOURCE_PORT"))

def get_ap_logger(__name__):
    return get_logger(__name__, LOGS_DIR, LOG_FILE, True)