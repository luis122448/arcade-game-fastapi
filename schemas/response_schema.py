from typing import Optional, TypeVar, Generic
from pydantic import BaseModel, Field
# from pydantic.generics import Generic?Model

# T = TypeVar('T', bound='BaseModel')
T = TypeVar('T')

class ResponseApi(BaseModel, Generic(T)):
    status: str
    message: str
    result: Optional[T]