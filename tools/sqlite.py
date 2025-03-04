import sqlite3
from typing import List, Tuple
from config.base_config import DB_FILE_PATH, logger

class Sqldb:
    def __init__(self, p_db_path: str) -> None:
        self.conn = sqlite3.connect(p_db_path)

    def __del__(self):
        self.conn.close()
    
    def commit(self) -> None:
        self.conn.commit()

    # 创建表
    def create_table(self,p_tb_name: str,p_tb_columns: List[str],p_tb_columns_type: List[str]) -> None:
        # 创建游标
        cur = self.conn.cursor()
        p_tb_column_lines = [column_name + ' ' + column_type for column_name, column_type in zip(p_tb_columns,p_tb_columns_type)]
        sql_str = f"CREATE TABLE {p_tb_name} ({','.join(p_tb_column_lines)})"
        logger.info('sql: ' + sql_str)
        cur.execute(sql_str)

    # 删除表
    def drop_table(self,p_tb_name: str) -> None:
        # 创建游标
        cur = self.conn.cursor()
        sql_str = 'DROP TABLE ' + p_tb_name
        logger.info('sql: ' + sql_str)
        cur.execute(sql_str)

    # 插入数据
    def insert_data(self, p_tb_name: str, p_data: List[Tuple]) -> None:
        # 创建游标
        cur = self.conn.cursor()
        sql_str = f"INSERT INTO {p_tb_name} VALUES({','.join(['?'] * len(p_data[0]))})"
        logger.info('sql: ' + sql_str)
        cur.executemany(sql_str,p_data)


    # 查询数据
    def select_data(self, p_sql_str: str) -> List[Tuple]:
        # 创建游标
        cur = self.conn.cursor()
        logger.info('sql: ' + p_sql_str)
        cur.execute(p_sql_str)
        sql_answer = cur.fetchall()
        if len(sql_answer) > 40:
            raise ValueError("too many query results")
        return sql_answer
    
def main():
    sqldb = Sqldb(DB_FILE_PATH)
    
    result = sqldb.select_data("select * from school_score where 最低分 > 650")
    print(result)


if __name__ == '__main__':
    main()