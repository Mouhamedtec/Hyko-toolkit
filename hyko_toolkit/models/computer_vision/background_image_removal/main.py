from hyko_sdk.io import Image
from hyko_sdk.models import CoreModel, Ext
from metadata import Inputs, Outputs, func
from rembg import remove


@func.on_execute
async def main(inputs: Inputs, params: CoreModel) -> Outputs:
    """
    This function removes the background from the original input image .

    Args:
        inputs (Inputs): An object containing the original input image data.
    Returns:
        Outputs: An object containing the processed image data without the background.
    """
    image_buffer = await inputs.input_image.get_data()
    output = remove(image_buffer)
    return Outputs(
        image=await Image(
            obj_ext=Ext.PNG,
        ).init_from_val(
            val=output,
        )
    )
