from pydantic import BaseModel


class Answer(BaseModel):
    ans: str