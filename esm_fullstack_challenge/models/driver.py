from pydantic import BaseModel, Field


class DriverBaseDTO(BaseModel):
    driver_ref: str
    number: str = Field(coerce_numbers_to_str=True, default="\\N")
    code: str
    forename: str
    surname: str
    dob: str
    nationality: str
    url: str


class DriverCreateDTO(DriverBaseDTO):
    pass


class DriverUpdateDTO(DriverBaseDTO):
    pass


class DriverDTO(DriverBaseDTO):
    id: int
