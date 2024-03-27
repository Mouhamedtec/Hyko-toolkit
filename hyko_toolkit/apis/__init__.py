"""register all apis"""

### Openai API
from .openai.text_completion.metadata import func as func
from .openai.text_embedding.metadata import func as func  # noqa: F811
from .stability_ai.image_to_image_with_prompt.metadata import func as func  # noqa: F811
from .stability_ai.image_upscaler.metadata import func as func  # noqa: F811
from .stability_ai.text_to_image.metadata import func as func  # noqa: F811
