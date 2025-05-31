from pydantic import BaseModel, model_validator, field_validator

from api.models import PublicModel
from exceptions import ValidationError


class LoginModel(PublicModel):
    username: str
    password: str


class RegisterModel(BaseModel):
    username: str
    password1: str
    password2: str

    @field_validator('username', mode='after')
    @classmethod
    def validate_x(cls, value: str) -> int:
        if not value.strip(): raise ValidationError("User name must be minimum 4 digits")
        return value

    @model_validator(mode='after')
    def validate(self):
        if len(self.password1) <= 8: raise ValidationError("Passwords must be minimum 8 digits")
        if self.password1 != self.password2: raise ValidationError("Passwords aren't same")
        if len(self.password1) != len(self.password1): raise ValidationError("Passwords aren't same")
        return self
