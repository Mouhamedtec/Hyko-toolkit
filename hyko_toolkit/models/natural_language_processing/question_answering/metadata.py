from hyko_sdk.models import CoreModel
from pydantic import Field

from hyko_toolkit.registry import ToolkitModel

func = ToolkitModel(
    name="question_answering",
    task="natural_language_processing",
    description="Hugging Face Question Answering task",
    absolute_dockerfile_path="./toolkit/hyko_toolkit/models/natural_language_processing/Dockerfile",
    docker_context="./toolkit/hyko_toolkit/models/natural_language_processing/question_answering",
)


@func.set_startup_params
class StartupParams(CoreModel):
    hugging_face_model: str = Field(..., description="Model")
    device_map: str = Field(..., description="Device map (Auto, CPU or GPU)")


@func.set_input
class Inputs(CoreModel):
    question: str = Field(..., description="Input question")
    context: str = Field(..., description="Context from which to answer the question")


@func.set_param
class Params(CoreModel):
    top_k: int = Field(default=1, description="Keep best k options (default:1).")
    doc_stride: int = Field(
        default=1,
        description="The stride of the splitting sliding window (default:128).",
    )


@func.set_output
class Outputs(CoreModel):
    answer: str = Field(..., description="Answer to the question")
    start: int = Field(..., description="Start index")
    end: int = Field(..., description="End index")
    score: float = Field(..., description="Score of the answer")
