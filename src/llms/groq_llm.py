import os
from typing import List, Dict
from groq import Groq

class ChatGroq:
    model="llama-3.3-70b-versatile"
    temperature=0
    max_tokens=None
    
    def invoke(self, messages: List[Dict]):
        # TODO: Assertion for messages

        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY")
        )

        chat_completion = client.chat.completions.create(
            messages=messages,
            model=ChatGroq.model,
            temperature=ChatGroq.temperature,
            max_tokens=ChatGroq.max_tokens
        )

        return chat_completion.choices[0].message.content
    

if __name__ == "__main__":
    print("okay")
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ]
    llm = ChatGroq()
    response = llm.invoke(messages=messages)
    print(response)