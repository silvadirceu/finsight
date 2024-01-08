from typing import Optional, List, Any

from pydantic import BaseModel


# Shared properties
class RequestBase(BaseModel):
    content: str
