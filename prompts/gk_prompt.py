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

GK_SQL_GENERATOR_TEMPLATE="""你是一名高级数据库工程师，请你根据所提供的表结构说明以及用户问题，生成sql语句，SQL语句中的表名和字段名应该满足表结构中的字段名和表名，数据库为sqlite，你生成的sql语句格式必须符合sqlite格式。
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
GK_GENERATOR_TEMPLATE = '''
你是一名专业的高考咨询顾问，请你根据用户的问题并结合所有查询的结果，完成对用户提问的回答。
要求如下：
1、若有查询结果则需要根据查询结果进行回答。
2、若没有查询结果则根据用户问题进行回答。
3、若有多个查询结果则需要根据多个查询结果综合进行回答。
------查询结果说明开始------
{search_result}
------查询结果说明结束------
用户问题：{user_question}
'''



class ScorePromptGenerator(PromptGenerator):

    def __init__(self,
                 task_template: str = GK_SQL_GENERATOR_TEMPLATE,
                 scheme_structure_dict: dict = SCHEME_STRUCTURE_DICT):
        self.task_template = task_template
        self.scheme_structure_dict = scheme_structure_dict

    def generate(self, user_input: str):
        sql_template = self.task_template.format(
            table_structure_introduction=self.scheme_structure_dict,
            user_question=user_input
        )
        return sql_template
    
class GKPromptGenerator(PromptGenerator):
    def __init__(self,
                 task_template: str = GK_GENERATOR_TEMPLATE,):
        self.task_template = task_template
    
    def generate(self, agent_state):
        sql_template = self.task_template.format(
            search_result=agent_state["agent_response"],
            user_question=agent_state["用户问题"]
        )
        return sql_template
    