from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from transformers.generation.utils import GenerationConfig
from peft import PeftModel
from model.llm.base import LLM

class Deepseek_Qwen(LLM):
    model_type = 'qwen'
    def __init__(self, cfg):
        model_path = cfg.get("model_path")
        self.quantization_config = BitsAndBytesConfig(load_in_8bit=True)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True, quantization_config= self.quantization_config)
        self.generation_config = GenerationConfig.from_pretrained(model_path, trust_remote_code=True, max_new_tokens = 512) # 可指定不同的生成长度、top_p等相关超参

        
    
    def generate(self, prompt, history=None):
        messages = [{'role': 'user', 'content': prompt}]
        print(messages)
        text = self.tokenizer.apply_chat_template(messages, tokenize=False)
        model_inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(**model_inputs, **self.generation_config.to_dict())
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
