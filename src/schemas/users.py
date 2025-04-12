from pydantic import BaseModel, EmailStr

from models.users import RolesEnum


class UserRequestAdd(BaseModel):
    phone: str
    telagram: str
    role: RolesEnum
    name: str
    email: EmailStr | None = None
    password: str


class UserAdd(BaseModel):
    phone: str
    telagram: str
    role: RolesEnum
    name: str
    email: EmailStr | None = None
    hashed_password: str


class UserRead(BaseModel):
    id: int
    phone: str
    telagram: str
    role: str
    name: str
    email: EmailStr | None = None


class UserLogin(BaseModel):
    phone: str
    password: str


class UserPatch(BaseModel):
    phone: str = None
    telagram: str = None
    role: str = None
    name: str = None
    email: EmailStr | None = None
    password: str | None = None
