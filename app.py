# Oracle
from itertools import groupby
import os

from py_logger.logger import log
from oracle_package_to_file.dao.oracle_dao import OracleDao
from oracle_package_to_file.config.config import get_ap_logger
from oracle_package_to_file.config.config import (
    DATA_SOURCE_USER,
    DATA_SOURCE_PASSWORD,
    DATA_SOURCE_HOST,
    DATA_SOURCE_PORT,
    DATA_SOURCE_SCHEMA_NAME,
    PKG_DIR,
)

os.makedirs(PKG_DIR, exist_ok=True)
logger = get_ap_logger(__name__)


# 轉換 Package Groups 列表
def to_package_group_list(data):
    result_list = []
    group_list = groupby(data, key=lambda x: (x["name"],))

    for key, group in group_list:
        result_list.append({"name": key, "lines": list(group)})

    return result_list


# 寫出檔案
def to_file(data):
    for group in data:
        output_file_path = os.path.join(PKG_DIR, group["name"][0] + ".pkg")
        is_package = True
        is_first_line = True
        with open(output_file_path, "w", encoding="utf-8") as f:
            for line in group["lines"]:
                if line["type"] != "PACKAGE" and is_package:
                    is_package = False
                    is_first_line = True
                    f.write("\n\n")

                if is_first_line :
                    f.write("CREATE OR REPLACE " + line["text"])
                    is_first_line = False
                else:
                    f.write(line["text"])
                    
        logger.info("Output Path: " + output_file_path)


# 主程式
@log(logger=logger)
def main():
    inputs = {
        "user": DATA_SOURCE_USER,
        "password": DATA_SOURCE_PASSWORD,
        "host": DATA_SOURCE_HOST,
        "port": DATA_SOURCE_PORT,
        "schema_name": DATA_SOURCE_SCHEMA_NAME,
    }

    with OracleDao(inputs) as oracleDao:
        data_list = oracleDao.list_package_line()
        data_list = to_package_group_list(data_list)
        to_file(data_list)


if __name__ == "__main__":
    main()
