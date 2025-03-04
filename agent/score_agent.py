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
        sql_prompt = self.prompt_generator.generate(agent_state["用户问题"])
        SQL = self.llm.generate(sql_prompt)
        query_result = self.query(SQL)
        print(query_result)
        return query_result