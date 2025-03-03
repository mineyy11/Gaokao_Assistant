from prompts.gk_prompt import ScorePromptGenerator


if __name__ == "__main__":
    gk_agent_executor = ScorePromptGenerator()
    print(gk_agent_executor.generate("20分对应位次？"))