from dataclasses import dataclass
from typing import Optional

@dataclass
class Property:
    address: str
    city: str
    price: float
    description: str
    status_name: str