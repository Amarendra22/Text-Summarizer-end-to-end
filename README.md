# Text-Summarizer-end-to-end project

### This a end to end project made using NLP hugging face transformer in python. The model has been trained using ML in jupyter notebook (present inside "research" folder).

### The following libraries has been used (requirements.txt):
#### 1)transformers
#### 2)transformers[sentencepiece]
#### 3)datasets
#### 4)sacrebleu 
#### 5)rouge_score 
#### 6)py7zr
#### 7)pandas
#### 8)nltk
#### 9)tqdm
#### 10)PyYAML
#### 11)matplotlib
#### 12)torch
#### 13)notebook
#### 14)boto3
#### 15)mypy-boto3-s3
#### 16)python-box==6.0.2
#### 17)ensure==1.0.2
#### 18)fastapi==0.78.0
#### 19)uvicorn==0.18.3
#### 20)Jinja2==3.1.2

### After the "main.py" is run, the model training will start and a folder called "artifacts" will be created which will further have 5 folders: data_ingestion, data_transformation, data_validation, model_evaluation, model_trainer. This took 1 hour 15 minutes in my Laptop. After model training is completed, now run the "app.py", this will run the localhost on port 9082. Enter the text with max length of 128 words and click on "Summarize" button. This will create a summary of the text below the "Summary" title.

### I have used "Fast Api" as web framework for building APIs with Python 3.8. "Html and CSS" has been used to give basic style to the prediction page.



https://github.com/Amarendra22/Text-Summarizer-end-to-end/assets/120000271/d4351670-3e13-4914-be03-1c4bf4dcceca

