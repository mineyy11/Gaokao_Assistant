from prompts.gk_prompt import ScorePromptGenerator
from model.llm.base import LLM
from tools.database_query_tool import DatabaseQueryTool


class ScoreAgent:
    def __init__(self,
                 llm,
                 prompt_generator = ScorePromptGenerator()):
        self.llm : LLM = llm
        self.prompt_generator = prompt_generator
        self.query = DatabaseQueryTool()
        pass


    def run(self, agent_state):
        count = 0
        while count < 3:
            try:
                sql_prompt = self.prompt_generator.generate(agent_state["用户问题"])
                sql_response = self.llm.generate(sql_prompt)
                print(sql_response)
                SQL = sql_response.split('```')[1].split('\n')[1].strip()
                print("SQL:", SQL)
                agent_state["sql_sentence"] = SQL
                query_result = self.query(sql_sentence = SQL)
                print(query_result)
                return query_result
            except Exception as e:
                print(f"重试第{count+1}次：", e)
                count += 1
                continue