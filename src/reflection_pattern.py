from dotenv import load_dotenv
from src.llms.groq_llm import ChatGroq
from src.utils.load_toml_utils import load_toml_files
from src.schemas.message_schemas import MessageSchema

load_dotenv()

class ReflectionPattern:
    def __init__(self, file):
        reflection_prompt = load_toml_files(file)
        self._segregate_reflection_prompt(reflection_prompt=reflection_prompt['reflection_pattern'])
        self.llm = ChatGroq()
        self.messages = [
            MessageSchema(role="system", content=self.generator_prompt)
        ]

    def _segregate_reflection_prompt(self, reflection_prompt):
        self.generator_prompt = reflection_prompt['generator_prompt']
        self.reflection_prompt = reflection_prompt['reflection_prompt']

    
    def _format_user_prompt(self, user_prompt: str):
        self.messages.append(
            MessageSchema(role='user', content=user_prompt)
        )

    def _format_response_prompt(self, response: str):
        self.messages.append(
            MessageSchema(role='assistant', content=response)
        )

    def generator_llm(self, user_prompt: str):
        self._format_user_prompt(user_prompt)
        response = self.llm.invoke(messages=self.messages)
        self._format_response_prompt(response)

    def reflector_llm(self):
        critique_response = self.llm.invoke(messages=self.messages)
        return critique_response    
    
    def __call__(self, *args, **kwargs):
         user_prompt = kwargs.get('user_prompt', 'Explain the importance of fast language models')
         self.generator_llm(user_prompt=user_prompt)
        #  critique_reponse = self.reflector_llm()
         breakpoint()
         
if __name__ == "__main__":
     reflection_pattern = ReflectionPattern("prompts/prompt_template.toml")
     reflection_pattern()