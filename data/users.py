from dataclasses import dataclass


@dataclass(frozen=True)
class UserData:
    username: str
    password: str
