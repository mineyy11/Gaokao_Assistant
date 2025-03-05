from prompts.prompt import PromptGenerator

SCHEME_STRUCTURE_DICT = {
'school_score': 
'''
字段 类型
学校 TEXT 
年份 TEXT
录取批次 TEXT
招生类型 TEXT
最低分 TEXT
位次 TEXT
省控线 TEXT
专业组 TEXT
选科要求 TEXT
''',
'professional_score': 
'''
字段 类型
学校 TEXT
专业 TEXT
备注 TEXT
年份 TEXT
科目 TEXT
平均分 TEXT
最低分 TEXT
位次 TEXT
''',
'分数位次表': 
'''
字段 类型
省份 TEXT
分数 TEXT
位次 TEXT
人数 TEXT
'''
}

BS_SQL_GENERATOR_TEMPLATE="""你是一名高级数据库工程师，请你根据所提供的表结构说明以及用户问题，生成sql语句，SQL语句中的表名和字段名应该满足表结构中的字段名和表名，数据库为sqlite，你生成的sql语句格式必须符合sqlite格式。
------表结构说明开始------
{table_structure_introduction}
------表结构说明结束------

必须注意：答案只需要sql语句，不需要其他任何输出。
如：
用户问题：湖南大学2022年录取分数线。
输出：SELECT 学校, 年份, 录取批次, 招生类型,  最低分, 位次 FROM school_score WHERE 学校 = '湖南大学' AND 年份 = 2022
请回答：
用户问题：{user_question}。
输出：
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
    