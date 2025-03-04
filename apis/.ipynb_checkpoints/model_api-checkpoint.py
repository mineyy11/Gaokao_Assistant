from model.llm_factory import LLMFactory


model_name = 'Deepseek_Qwen'

llm = LLMFactory.build_llm(model_name,{})