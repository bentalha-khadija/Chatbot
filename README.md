# Rasa-Chatbot
Simple Chatbot with rasa 
### After you cloned the repo you can create a virtual env inside the main directory with python 3.8 already installed(rasa does not work with python > 3.8) 
virtualenv -p C:\Users\khadi\AppData\Local\Programs\Python\Python38\python.exe venv
### Activate the env 
```bash
venv\Scripts\activate
```
### Install rasa
```bash
pip install rasa 
```
### Make sure rasa is installed 
```bash
rasa -h 
```
### Train the model 
```bash
rasa train
```
### run a server for customized actions
```bash
rasa run actions  
```
### In a parallel terminal 
```bash
rasa run -m models --enable-api --cors "*"
```
### Now you can run the file app.py and communicate with the chatbot 
