from prompts.prompt import PromptGenerator

SCHEME_STRUCTURE_DICT = {
'学习分数线表': 
'''
字段 类型
校名 TEXT 
交易日期 TEXT
行业划分标准 TEXT
一级行业名称 TEXT
二级行业名称 TEXT
''',
'学校专业分数线表': 
'''
字段 类型
股票代码 TEXT
交易日 TEXT
[昨收盘(元)] REAL
[今开盘(元)] REAL
[最高价(元)] REAL
[最低价(元)] REAL
[收盘价(元)] REAL
[成交量(股)] REAL
[成交金额(元)] REAL
'''
}

BS_SQL_GENERATOR_TEMPLATE="""你是一名高级数据库工程师，请你根据所提供的表结构说明以及用户问题，生成sql语句，数据库为sqlite，你生成的sql语句格式必须符合sqlite格式。
------表结构说明开始------
{table_structure_introduction}
------表结构说明结束------

用户问题：{user_question}。
注意：答案只需要sql语句，不需要其他任何输出。
"""



class ScorePromptGenerator(PromptGenerator):

    def __init__(self,
                 task_template: str = BS_SQL_GENERATOR_TEMPLATE,
                 scheme_structure_dict: dict = SCHEME_STRUCTURE_DICT):
        self.task_template = task_template
        self.scheme_structure_dict = scheme_structure_dict

    def generate(self, user_input: str):
        sql_template = self.task_template.format(
            table_structure_introduction=self.scheme_structure_dict,
            user_question=user_input
        )
        return sql_template
    