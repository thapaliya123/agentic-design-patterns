from pydantic import BaseModel

class MessageSchema(BaseModel):
    role: str
    content: str    