from datetime import timedelta
from enum import Enum


class ActionTokenEnum(Enum):
    ACTIVATE = (
        'user_activation',
        timedelta(minutes=30)
    )

    RECOVERY_PASSWORD = (
        'user_recovery_password',
        timedelta(minutes=10)
    )

    def __init__(self, token_type, lifetime):
        self.token_type = token_type
        self.lifetime = lifetime