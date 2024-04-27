# Defines the model architecture, including any modifications to the RoBERTa model
from transformers import RobertaForSequenceClassification

model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2)
