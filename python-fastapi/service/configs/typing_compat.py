from typing import TypeVar, Optional, Tuple
from .errors import ServiceError

T = TypeVar("T")
ResultWithErr = Tuple[Optional[T], Optional[ServiceError]]