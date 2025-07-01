import os
from dotenv import load_dotenv
from src.llms.groq_llm import ChatGroq
from src.utils.load_toml_utils import load_toml_files

load_dotenv()

class ReflectionPattern:
    def __init__(self, file):
        reflection_prompt = load_toml_files()

    def generator_llm(self):
        pass

    def reflector_llm(self):
        pass
    
    def __call__(self, *args, **kwargs):
         print("Okay, I am from reflection pattern")
         

if __name__ == "__main__":
     reflection_pattern = ReflectionPattern()
     reflection_pattern()