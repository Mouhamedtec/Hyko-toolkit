import os
from enum import Enum

from hyko_sdk.io import Image
from hyko_sdk.models import CoreModel, Ext
from pydantic import Field

from hyko_toolkit.registry import ToolkitUtils

func = ToolkitUtils(
    name="image_converter",
    task="image_utils",
    description="Convert an input image to a specified target image type.",
)


class SupportedTypes(Enum):
    png = Ext.PNG
    jpeg = Ext.JPEG
    bmp = Ext.BMP
    webp = Ext.WEBP


@func.set_input
class Inputs(CoreModel):
    original_image: Image = Field(
        ...,
        description="The original image.",
    )


@func.set_param
class Params(CoreModel):
    target_type: SupportedTypes = Field(
        ...,
        description="The Target Type.",
    )


@func.set_output
class Outputs(CoreModel):
    output: Image = Field(
        ...,
        description="Converted image.",
    )


@func.on_call
async def call(inputs: Inputs, params: Params) -> Outputs:
    img = await inputs.original_image.to_pil()
    img.save(f"converted-image.{params.target_type.name}")
    with open(f"converted-image.{params.target_type.name}", "rb") as file:
        val = file.read()
    os.remove(f"converted-image.{params.target_type.name}")
    return Outputs(
        output=await Image(
            obj_ext=params.target_type.value,
        ).init_from_val(
            val=val,
        )
    )
