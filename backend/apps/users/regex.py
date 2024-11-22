from enum import Enum


class ProfileRegex(Enum):
    PHONE_NUMBER = (
        r'^\+?1?\d{9,15}$',
        'The phone number should be in the format: +380XXXXXXXXX .Maximum 15 digits.'
    )

    def __init__(self, pattern:str, msg:str):
        self.pattern = pattern
        self.msg = msg