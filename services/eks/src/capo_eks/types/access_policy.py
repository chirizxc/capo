"""Generated from Smithy shape ``com.amazonaws.eks#AccessPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class AccessPolicy(TypedDict, closed=True):
    name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the access policy.</p>"""
    arn: NotRequired["capo_eks.types.string.String"]
    """<p>The ARN of the access policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessPolicy) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AccessPolicy:
    out: AccessPolicy = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
