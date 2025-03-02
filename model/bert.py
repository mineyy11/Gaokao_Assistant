from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

ID2LABEL = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
LABEL2ID = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
LABEL = ['A', 'B', 'C', 'D', 'E', 'F']
MODEL_PATH = '../bert-finetuned-sem_eval-english/checkpoint-876'

class BERT():
    model_type = 'bert'
    def __init__(self):
        self.model_path = MODEL_PATH
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_path, 
                                                           problem_type="multi_label_classification", 
                                                           num_labels=6,
                                                           device_map="cpu",
                                                           id2label=ID2LABEL,
                                                           label2id=LABEL2ID)


    def run(self, prompt):
        encoding = self.tokenizer(prompt, return_tensors="pt")
        encoding = {k: v.to(self.model.device) for k,v in encoding.items()}
        original_outputs = self.model(**encoding)
        original_logits = original_outputs.logits
        sigmoid = torch.nn.Sigmoid()
        probs = sigmoid(original_logits.squeeze().cpu())
        predictions = np.zeros(probs.shape)
        predictions[np.where(probs >= 0.5)] = 1
        predicted_labels = [ID2LABEL[idx] for idx, label in enumerate(predictions) if label == 1.]
        return predicted_labels
        

if __name__ == "__main__":
    bert = BERT()
    print(bert.classify("520分对应位次？"))