from dataclasses import dataclass


@dataclass
class AuthRequest:
    username: str
    password: str


@dataclass
class AuthResponse:
    token: str
    username: str
