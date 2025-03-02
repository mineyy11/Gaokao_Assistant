from agent.score_agent import ScoreAgent
from copy import deepcopy
from model.bert import BERT

AGENT_LIST = {'A': ScoreAgent()}

class GKAgentExecutor:
    def __init__(self):
        self._init_agents()
        self.agent_state = {}
        

    def _init_agents(self):
        self.agent_list = deepcopy(AGENT_LIST)
        self.classify = BERT()

    def run(self,
            user_inputs: str):
        self.agent_state["用户问题"] = user_inputs
        predicted_labels = self.classify.run(user_inputs)
        print(predicted_labels)

if __name__ == "__main__":
    gk_agent_executor = GKAgentExecutor()
    gk_agent_executor.run("20分对应位次？")
