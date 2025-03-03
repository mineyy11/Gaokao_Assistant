from prompts.gk_prompt import ScorePromptGenerator


class ScoreAgent:
    def __init__(self,
                 llm,
                 prompt_generator: ScorePromptGenerator):
        self.llm = llm
        self.prompt_generator = prompt_generator
        pass


    def run(self, agent_state):
        SQL = self.prompt_generator.generate(agent_state["用户问题"])
        return "20分对应位次是1000"