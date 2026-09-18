"""Generated from Smithy shape ``com.amazonaws.datazone#ConfigurableActionParameter``."""

from typing_extensions import NotRequired, TypedDict


class ConfigurableActionParameter(TypedDict, closed=True):
    key: NotRequired["str"]
    """<p>The key of the configurable action parameter.</p>"""
    value: NotRequired["str"]
    """<p>The value of the configurable action parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableActionParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ConfigurableActionParameter:
    out: ConfigurableActionParameter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
