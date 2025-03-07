from enum import Enum

from hyko_sdk.io import Image as HykoImage
from hyko_sdk.models import CoreModel
from PIL import Image
from pydantic import Field, PositiveFloat

from hyko_toolkit.registry import ToolkitUtils

func = ToolkitUtils(
    name="resize_factor",
    task="image_utils",
    description="Resize an image by a factor",
)


class InterpolationMethod(str, Enum):
    Area = "area"
    Linear = "linear"
    Lanczos = "lanczos"
    NearestNeighbor = "nearest-neighbor"
    Cubic = "cubic"


@func.set_input
class Inputs(CoreModel):
    image: HykoImage = Field(..., description="Input image to resize")


@func.set_param
class Params(CoreModel):
    scale_factor: PositiveFloat = Field(
        default=0, description="Scaling factor for resizing"
    )
    interpolation: InterpolationMethod = Field(
        InterpolationMethod.Lanczos, description="Interpolation method for resizing"
    )


@func.set_output
class Outputs(CoreModel):
    resized_image: HykoImage = Field(..., description="Resized image")


@func.on_call
async def call(inputs: Inputs, params: Params) -> Outputs:
    pil_image = await inputs.image.to_pil()
    original_width, original_height = pil_image.size

    new_width = max(round(original_width * (params.scale_factor / 100)), 1)
    new_height = max(round(original_height * (params.scale_factor / 100)), 1)

    interpolation_methods = {
        "area": Image.Resampling.BOX,
        "linear": Image.Resampling.BILINEAR,
        "lanczos": Image.Resampling.LANCZOS,
        "nearest-neighbor": Image.Resampling.NEAREST,
        "cubic": Image.Resampling.BICUBIC,
    }
    interpolation = interpolation_methods.get(
        params.interpolation, Image.Resampling.BOX
    )
    resized_pil_image = pil_image.resize((new_width, new_height), interpolation)
    resized_image = await HykoImage.from_pil(resized_pil_image)

    return Outputs(resized_image=resized_image)
