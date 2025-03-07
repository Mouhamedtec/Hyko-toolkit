import httpx
from hyko_sdk.io import Audio
from hyko_sdk.models import CoreModel, Method
from pydantic import Field

from hyko_toolkit.exceptions import APICallError
from hyko_toolkit.registry import ToolkitAPI

func = ToolkitAPI(
    name="openai_speech_to_text",
    task="openai",
    description="Use openai api to turn audio into text.",
)


@func.set_input
class Inputs(CoreModel):
    audio: Audio = Field(..., description="Audio to convert to text.")


@func.set_param
class Params(CoreModel):
    api_key: str = Field(description="API key")


@func.set_output
class Outputs(CoreModel):
    text: str = Field(..., description="The extracted text.")


class Responce(CoreModel):
    text: str


@func.on_call
async def call(inputs: Inputs, params: Params):
    async with httpx.AsyncClient() as client:
        res = await client.request(
            method=Method.post,
            url="https://api.openai.com/v1/audio/transcriptions",
            headers={
                "Authorization": f"Bearer {params.api_key}",
            },
            files={
                "file": (inputs.audio.file_name, await inputs.audio.get_data(), None),
            },
            data={"model": "whisper-1"},
            timeout=60 * 5,
        )
    if res.is_success:
        response = Responce(**res.json())
    else:
        raise APICallError(status=res.status_code, detail=res.text)

    return Outputs(text=response.text)
