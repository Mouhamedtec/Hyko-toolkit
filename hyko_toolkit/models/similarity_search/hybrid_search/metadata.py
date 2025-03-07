from hyko_sdk.models import CoreModel
from pydantic import Field

from hyko_toolkit.registry import ToolkitModel

func = ToolkitModel(
    name="hybrid_search",
    task="similarity_search",
    description="Executes simultaneous BM25 keyword matching and document similarity searches on input documents.",
    absolute_dockerfile_path="./toolkit/hyko_toolkit/models/similarity_search/hybrid_search/Dockerfile",
    docker_context="./toolkit/hyko_toolkit/models/similarity_search/hybrid_search",
)


@func.set_input
class Inputs(CoreModel):
    docs: list[str] = Field(..., description="Input Documents.")
    query: str = Field(
        ..., description="Query or the Question to compare against the input text."
    )


@func.set_param
class Params(CoreModel):
    bm25_k: int = Field(
        default=3,
        description="Number of top results to consider in Best Matching Algorithm (BM25) (default=3).",
    )
    faiss_k: int = Field(
        default=3,
        description="Number of top results to consider in Similarity Search Algorithm (default=3).",
    )


@func.set_output
class Outputs(CoreModel):
    result: list[str] = Field(..., description="Top K results.")
