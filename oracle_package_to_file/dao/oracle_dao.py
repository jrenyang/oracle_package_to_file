import cx_Oracle


class OracleDao:
    def __init__(self, config):
        self.config = config

    def __enter__(self):
        self.__conn = cx_Oracle.connect(
            user=self.config["user"],
            password=self.config["password"],
            dsn=f"{self.config['host']}:{self.config['port']}/{self.config['schema_name']}",
            encoding="UTF-8"
        )

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__conn.close()

    def list_package_line(self):
        result_list = []

        sql = """SELECT  NAME, TYPE, LINE, TEXT
                 FROM USER_SOURCE
                 WHERE TYPE IN ('PACKAGE', 'PACKAGE BODY')
                 ORDER BY NAME, TYPE, LINE"""

        with self.__conn.cursor() as cur:
            cur.execute(sql)

            for row in cur.fetchall():
                result_list.append(
                    {
                        "name": row[0],
                        "type": row[1],
                        "line": row[2],
                        "text": row[3],
                    }
                )

        return result_list
