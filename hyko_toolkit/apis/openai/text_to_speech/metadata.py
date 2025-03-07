from enum import Enum

import httpx
from hyko_sdk.io import Audio
from hyko_sdk.models import CoreModel, Ext, Method
from pydantic import Field

from hyko_toolkit.exceptions import APICallError
from hyko_toolkit.registry import ToolkitAPI

func = ToolkitAPI(
    name="openai_text_to_speech",
    task="openai",
    description="Use openai api to turn text into lifelike spoken audio.",
)


class Model(str, Enum):
    tts1 = "tts-1"
    tts1hd = "tts-1-hd"


class VoiceNames(str, Enum):
    alloy = "alloy"
    echo = "echo"
    fable = "fable"
    onyx = "onyx"
    nova = "nova"
    shimmer = "shimmer"


@func.set_input
class Inputs(CoreModel):
    text: str = Field(..., description="Text to convert to speech.")


@func.set_param
class Params(CoreModel):
    api_key: str = Field(description="API key")
    model: Model = Field(
        default=Model.tts1,
        description="Openai model to use.",
    )
    voice: VoiceNames = Field(
        default=VoiceNames.alloy,
        description="Voice to use.",
    )


@func.set_output
class Outputs(CoreModel):
    voice: Audio = Field(..., description="Generated Audio.")


class Voice(CoreModel):
    voice: bytes


@func.on_call
async def call(inputs: Inputs, params: Params):
    async with httpx.AsyncClient() as client:
        res = await client.request(
            method=Method.post,
            url="https://api.openai.com/v1/audio/speech",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {params.api_key}",
            },
            json={
                "input": inputs.text,
                "model": params.model.value,
                "voice": params.voice.name,
            },
            timeout=60 * 5,
        )
    if res.is_success:
        response = Voice(voice=res.content)
    else:
        raise APICallError(status=res.status_code, detail=res.text)

    return Outputs(voice=await Audio(obj_ext=Ext.MP3).init_from_val(val=response.voice))
