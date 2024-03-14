from pydantic import Field

from hyko_sdk.function import SDKFunction
from hyko_sdk.metadata import CoreModel

func = SDKFunction(
    description="Tool for computing similarity scores based on a given threshold."
)


@func.set_input
class Inputs(CoreModel):
    docs: list[str] = Field(
        ...,
        description="Text Input.",
    )
    query: str = Field(
        ...,
        description="Query or the Question to compare against the input text.",
    )


@func.set_startup_params
class StartupParams(CoreModel):
    pass


@func.set_param
class Params(CoreModel):
    top_k: int = Field(
        default=3,
        description="Number of top results to consider (default=3).",
    )
    score_threshold: float = Field(
        default=0.4,
        description="Threshold score to filter similarity results (default=0.4).",
    )


@func.set_output
class Outputs(CoreModel):
    result: list[str] = Field(..., description="Top K results. ")
