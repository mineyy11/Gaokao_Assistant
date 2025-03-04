from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.generation.utils import GenerationConfig
from peft import PeftModel
from model.llm.base import LLM

class Deepseek_Qwen(LLM):
    model_type = 'qwen'
    def __init__(self, cfg):
        model_path = cfg.get("model_path")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True, bf16=True)
        self.generation_config = GenerationConfig.from_pretrained(model_path, trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参

        
    
    def generate(self, prompt, history=None):
        with self.model.disable_adapter():
            response, _ = self.model.chat(self.tokenizer, prompt, history=history, generation_config=self.generation_config)
            return response
