from hyko_sdk.io import Image
from hyko_sdk.models import CoreModel
from pydantic import Field

from hyko_toolkit.registry import ToolkitModel

func = ToolkitModel(
    name="background_image_removal",
    task="computer_vision",
    description="This function removes the background from the original input image.",
    absolute_dockerfile_path="./toolkit/hyko_toolkit/models/computer_vision/background_image_removal/Dockerfile",
    docker_context="./toolkit/hyko_toolkit/models/computer_vision/background_image_removal",
)


@func.set_input
class Inputs(CoreModel):
    input_image: Image = Field(..., description="Original image")


@func.set_output
class Outputs(CoreModel):
    image: Image = Field(..., description="Image without background")
