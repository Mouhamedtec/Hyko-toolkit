from pydantic import Field

from hyko_sdk.definitions import SDKFunction
from hyko_sdk.models import CoreModel

func = SDKFunction(
    description="Convert a given string to uppercase",
)


@func.set_input
class Inputs(CoreModel):
    text: str = Field(..., description="Input text")


@func.set_param
class Params(CoreModel):
    pass


@func.set_output
class Outputs(CoreModel):
    uppercase_string: str = Field(
        ..., description="Uppercase version of the input string"
    )
