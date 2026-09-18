"""Generated from Smithy shape ``com.amazonaws.oam#ListSinksItem``."""

from typing_extensions import NotRequired, TypedDict


class ListSinksItem(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The ARN of the sink.</p>"""
    id: NotRequired["str"]
    """<p>The random ID string that Amazon Web Services generated as part of the sink ARN.</p>"""
    name: NotRequired["str"]
    """<p>The name of the sink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSinksItem) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ListSinksItem:
    out: ListSinksItem = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
