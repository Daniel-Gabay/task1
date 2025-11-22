from pydantic import BaseModel, Field, field_validator

class Machine(BaseModel):
    name: str = Field(..., min_length=1, max_length=10)
    os: str
    cpu: int = Field(..., gt=0)
    ram: int = Field(..., gt=0)

    @field_validator("os")
    def validate_os(cls, v):
        allowed = ["ubuntu", "centos", "windows"]
        if v.lower() not in allowed:
            raise ValueError("OS must be ubuntu, centos, or windows")
        return v.lower()
