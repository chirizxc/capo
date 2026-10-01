"""Generated from Smithy shape ``com.amazonaws.securityagent#ConfluenceResourceCapabilities``."""

from typing_extensions import NotRequired, TypedDict


class ConfluenceResourceCapabilities(TypedDict, closed=True):
    fetch_document: NotRequired["bool"]
    """<p>Whether to fetch documents from this space.</p>"""
    create_document: NotRequired["bool"]
    """<p>Whether to create documents in this space.</p>"""
    update_document: NotRequired["bool"]
    """<p>Whether to update documents in this space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceResourceCapabilities) -> dict:
    out: dict = {}
    if "fetch_document" in value:
        out["fetchDocument"] = value["fetch_document"]
    if "create_document" in value:
        out["createDocument"] = value["create_document"]
    if "update_document" in value:
        out["updateDocument"] = value["update_document"]
    return out


def deserialize_json(data: dict) -> ConfluenceResourceCapabilities:
    out: ConfluenceResourceCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("fetchDocument") is not None:
        out["fetch_document"] = data["fetchDocument"]
    if data.get("createDocument") is not None:
        out["create_document"] = data["createDocument"]
    if data.get("updateDocument") is not None:
        out["update_document"] = data["updateDocument"]
    return out
