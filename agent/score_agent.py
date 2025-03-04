from prompts.gk_prompt import ScorePromptGenerator
from model.llm.base import LLM


class ScoreAgent:
    def __init__(self,
                 llm,
                 prompt_generator = ScorePromptGenerator()):
        self.llm : LLM = llm
        self.prompt_generator = prompt_generator
        pass


    def run(self, agent_state):
        sql_prompt = self.prompt_generator.generate(agent_state["用户问题"])
        SQL = self.llm.generate(sql_prompt)
        print(SQL)
        return "20分对应位次是1000"