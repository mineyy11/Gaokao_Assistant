from tools.tool import Tool
from apis.database_api import sqldb
import re

PATTERN = r"SELECT\s+(.*?)\s+FROM"

class DatabaseQueryTool(Tool):
    description = '数据库查询'
    name = 'DatabaseQuery'
    parameters: list = [{
        'name': 'sql_sentence',
        'description': 'sql语句',
        'required': True
    }]

    def _local_call(self, *args, **kwargs):
        if kwargs.get("sql_sentence") is None:
            return {"result": "Error: 参数错误，请检查!sql_sentence: None"}
        sql = kwargs.get("sql_sentence")
        result = sqldb.select_data(sql)
        match = re.search(PATTERN, sql)
        if match:
            fields_str = match.group(1)
            fields_list = [field.strip() for field in fields_str.split(",")]
            fields_tuple = tuple(fields_list)
        print("查询结束！！")
        result.insert(0, fields_tuple)
        return {"result": result}