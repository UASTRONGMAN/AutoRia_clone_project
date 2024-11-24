from dataclasses import dataclass
from datetime import datetime


@dataclass()
class UserProfile:
    id: int
    name: str
    surname: str
    phone_number: str
    created_at: datetime
    updated_at: datetime

@dataclass
class User:
    id: int
    email:str
    password:str
    is_active:bool
    is_premium_user:bool
    is_staff:bool
    is_superuser:bool
    last_login:datetime
    created_at:datetime
    updated_at:datetime
    profile:UserProfile