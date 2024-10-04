from dataclasses import dataclass
from datetime import datetime

@dataclass
class Like:
    id: int
    user_id: int
    property_id: int
    created_at: datetime