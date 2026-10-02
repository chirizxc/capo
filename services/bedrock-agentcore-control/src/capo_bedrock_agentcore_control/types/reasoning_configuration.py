"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ReasoningConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class ReasoningConfiguration(TypedDict, closed=True):
    effort: NotRequired["str"]
    """<p> The level of reasoning effort the model applies when generating a response. For supported values, see the model provider's documentation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReasoningConfiguration) -> dict:
    out: dict = {}
    if "effort" in value:
        out["effort"] = value["effort"]
    return out


def deserialize_json(data: dict) -> ReasoningConfiguration:
    out: ReasoningConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("effort") is not None:
        out["effort"] = data["effort"]
    return out
