# Medical Named Entity Recognition using Fine-Tuned BERT and ALBERT

## Overview
This repository contains code and resources for Medical Named Entity Recognition (NER) using pre-trained BERT and ALBERT models. The project aims to fine-tune these language models on the i2b2/n2c2 dataset, containing annotated clinical notes, and evaluate their performance on medical NER tasks. The repository includes Jupyter Notebook files for data parsing, model fine-tuning, and model evaluation, along with saved model folders.

Finetuned models have been uploaded to Huggingface Repo.
* [BERT](https://huggingface.co/medical-ner-proj/bert-medical-ner-proj)
* [ALBERT](https://huggingface.co/medical-ner-proj/albert-medical-ner-proj)

## Table of Contents
1. [Overview](#overview)
2. [Dataset](#dataset)
3. [Installation and Requirements](#installation-and-requirements)
4. [Usage](#usage)
5. [Results](#results)
6. [References](#references)

## Dataset
The dataset used for this project is the i2b2/n2c2 dataset, which consists of annotated clinical notes. You can download the dataset from [here](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/).

## Installation and Requirements
1. Python 3.x
2. Jupyter Notebook
3. Huggingface Transformers
4. PyTorch

Install the required packages using:
\```bash
pip install -r requirements.txt
\```

## Usage
1. **Data Parsing**: Open and run `parsing_n2c2_to_conll.ipynb`.
2. **BERT Fine-tuning**: Open and run `bert_finetuning.ipynb`.
3. **ALBERT Fine-tuning**: Open and run `albert_finetuning.ipynb`.

After fine-tuning, the models will be saved in their respective folders.

## Results
* BERT: F1-score of 0.8726, Accuracy of 0.9557
* ALBERT: F1-score of 0.8667, Accuracy of 0.9518

For detailed results, check the Report.

## References
* [BioELECTRA: Pre-trained Biomedical Text Encoder](https://paperswithcode.com/paper/bioelectra-pretrained-biomedical-text-encoder)
* [Huggingface Guide](https://www.freecodecamp.org/news/getting-started-with-ner-models-using-huggingface/)
