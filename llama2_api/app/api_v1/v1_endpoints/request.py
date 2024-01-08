from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
import schemas, business


router = APIRouter()

@router.post("/", response_model=str)
def create(
    request_in: schemas.RequestBase,
) -> Any:
    """
    Makes a request.
    """
    return business.request.create(request_in)
