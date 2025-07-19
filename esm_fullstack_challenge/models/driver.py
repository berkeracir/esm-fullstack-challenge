from typing import Any

from pydantic import BaseModel, Field, field_validator


class DriverBaseDTO(BaseModel):
    driver_ref: str
    number: str = Field(coerce_numbers_to_str=True, default='\\N')
    code: str
    forename: str
    surname: str
    dob: str
    nationality: str
    url: str

    @field_validator('number', mode='before')
    @classmethod
    def ensure_not_null(cls, value: Any) -> str:
        if value is None:
            return '\\N'
        elif not isinstance(value, str):
            return str(value)
        else:
            return value


class DriverCreateDTO(DriverBaseDTO):
    pass


class DriverUpdateDTO(DriverBaseDTO):
    pass


class DriverDTO(DriverBaseDTO):
    id: int
