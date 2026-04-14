from app.api.base_api import BaseApi
from models.auth import AuthRequest, AuthResponse


class AuthApi(BaseApi):
    def login(self, req: AuthRequest) -> AuthResponse:
        self.post("/login", {"username": req.username, "password": req.password})
        # Dummy response
        return AuthResponse(token="dummy-token", username=req.username)
