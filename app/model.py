from pydantic import BaseModel, Field


# class UserSchema(BaseModel):
#     idadm: str = Field(...)
#     nama: str = Field(...)
#     username: str = Field(...)
#     password: str = Field(...)
#     notelp: str = Field(...)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "idadm": "A1",
#                 "nama": "Nurul Izza A",
#                 "username": "nuruliaf",
#                 "password": "123",
#                 "notelp": "0812525252"
#             }
#         }

class AdminLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "nuruliaf",
                "password": "123"
            }
        }