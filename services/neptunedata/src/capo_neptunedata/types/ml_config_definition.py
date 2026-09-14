"""Generated from Smithy shape ``com.amazonaws.neptunedata#MlConfigDefinition``."""

from typing_extensions import NotRequired, TypedDict


class MlConfigDefinition(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The configuration name.</p>"""
    arn: NotRequired["str"]
    """<p>The ARN for the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MlConfigDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> MlConfigDefinition:
    out: MlConfigDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
