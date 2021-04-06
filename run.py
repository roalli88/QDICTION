from qdiction.__main__ import main
import json
import nltk

def config_checker():
    
    nltk.download('wordnet')
    with open("config.json", "r+") as f:
        

main()
