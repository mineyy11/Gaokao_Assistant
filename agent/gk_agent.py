from agent.score_agent import ScoreAgent
from copy import deepcopy
from model.bert import BERT
from apis.model_api import llm

AGENT_LIST = {'A': ScoreAgent(llm)}

class GKAgentExecutor:
    def __init__(self):
        self._init_agents()
        self.agent_state = {}
        self.llm = llm
        

    def _init_agents(self):
        self.agent_list = deepcopy(AGENT_LIST)
        self.classify = BERT()

    def run(self,
            user_inputs: str):
        self.agent_state["用户问题"] = user_inputs
        agent_tasks = self.classify.run(user_inputs)
        print(agent_tasks) # ['A']
        response = ""
        for agent in agent_tasks:
            response = self.agent_list[agent].run(self.agent_state)
            self.agent_state["agent_response"] = {agent: response}
        
        


if __name__ == "__main__":
    gk_agent_executor = GKAgentExecutor()
    gk_agent_executor.run("20分对应位次？")
