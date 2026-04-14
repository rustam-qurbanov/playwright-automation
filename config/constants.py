from enum import Enum


class SystemRoles(str, Enum):
    ADMIN = "admin"
    USER = "user"


class Timeouts:
    SHORT = 5000
    MEDIUM = 15000
    LONG = 30000
