from typing import Optional, List
from fastapi.encoders import jsonable_encoder
import json
from fastapi import HTTPException, status
import schemas, business
from langchain.llms import CTransformers

class BusinessRequest():
    def __init__(self):
        self.llm = CTransformers(
            model=".cache/huggingface/hub/models--TheBloke--Llama-2-7B-Chat-GGML/snapshots/76cd63c351ae389e1d4b91cab2cf470aab11864b/llama-2-7b-chat.ggmlv3.q2_K.bin",
            model_type="llama"
        )

    def create(self, request_in: schemas.RequestBase) -> str:
        """
        Makes a request.
        """
        result = self.llm.predict(request_in.content)
        return result


request = BusinessRequest()