from typing import Union, List
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Body
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Person(BaseModel):
    id: str
    name: str


DB: List[Person] = [
    Person(id="AXR210179", name="Adarsh Ramesh"),
    Person(id="DSU220000", name="Dane Ukken"),
    Person(id="RXJ220025", name="Rohan Jayachandran"),
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api")
def list_people():
    return DB


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


tokenizer = AutoTokenizer.from_pretrained("ukkendane/albert-medical-ner")
model = AutoModelForTokenClassification.from_pretrained(
    "ukkendane/albert-medical-ner")


@app.post("/predict")
async def predict_ner_tags(text: str):
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        return_attention_mask=True,
        return_tensors="pt"
    )
    tokenized_input = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
    tokenized_input = tokenized_input[1:-1]
    tokenized_input = [w.replace('▁', '') for w in tokenized_input]
    outputs = model(**inputs)
    predicted_labels = outputs.logits.argmax(dim=2)[0]
    predicted_labels = predicted_labels.tolist()
    predicted_labels = [model.config.id2label[label_id]
                        for label_id in predicted_labels]
    predicted_labels = predicted_labels[1:-1]
    return {"text": text, "tokens": tokenized_input, "tags": predicted_labels}
