"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentConditionalField``."""

from typing_extensions import NotRequired, TypedDict


class DeploymentConditionalField(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the deployment condition.</p>"""
    value: NotRequired["str"]
    """<p>The value of the condition.</p>"""
    comparator: NotRequired["str"]
    """<p>The comparator of the condition.</p> <p>Valid values: <code>Equal | NotEqual</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentConditionalField) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    if "comparator" in value:
        out["comparator"] = value["comparator"]
    return out


def deserialize_json(data: dict) -> DeploymentConditionalField:
    out: DeploymentConditionalField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("comparator") is not None:
        out["comparator"] = data["comparator"]
    return out
