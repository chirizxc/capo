"""Generated from Smithy shape ``com.amazonaws.elementalinference#Competitor``."""

from typing_extensions import NotRequired, TypedDict


class Competitor(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the competitor, as provided by the data source.</p>"""
    is_home: NotRequired["bool"]
    """<p>Specifies whether this competitor is the home side in the fixture. If true, this competitor is the home side. If false, this competitor is the away side. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Competitor) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "is_home" in value:
        out["isHome"] = value["is_home"]
    return out


def deserialize_json(data: dict) -> Competitor:
    out: Competitor = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("isHome") is not None:
        out["is_home"] = data["isHome"]
    return out
