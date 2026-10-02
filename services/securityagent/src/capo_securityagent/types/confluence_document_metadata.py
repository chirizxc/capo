"""Generated from Smithy shape ``com.amazonaws.securityagent#ConfluenceDocumentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.provider_resource_id
    import capo_securityagent.types.provider_resource_name


class ConfluenceDocumentMetadata(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    provider_resource_id: (
        "capo_securityagent.types.provider_resource_id.ProviderResourceId"
    )
    space_key: "str"
    """<p>The Confluence space key containing the document.</p>"""
    page_id: "str"
    """<p>The Confluence page identifier.</p>"""
    title: NotRequired["str"]
    """<p>The display title of the Confluence page.</p>"""
    space_title: NotRequired["str"]
    """<p>The display title of the Confluence space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceDocumentMetadata) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["providerResourceId"] = value["provider_resource_id"]
    out["spaceKey"] = value["space_key"]
    out["pageId"] = value["page_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "space_title" in value:
        out["spaceTitle"] = value["space_title"]
    return out


def deserialize_json(data: dict) -> ConfluenceDocumentMetadata:
    out: ConfluenceDocumentMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfluenceDocumentMetadata.name required")
    if data.get("providerResourceId") is not None:
        out["provider_resource_id"] = data["providerResourceId"]
    else:
        raise DeserializationError(
            "ConfluenceDocumentMetadata.provider_resource_id required"
        )
    if data.get("spaceKey") is not None:
        out["space_key"] = data["spaceKey"]
    else:
        raise DeserializationError("ConfluenceDocumentMetadata.space_key required")
    if data.get("pageId") is not None:
        out["page_id"] = data["pageId"]
    else:
        raise DeserializationError("ConfluenceDocumentMetadata.page_id required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("spaceTitle") is not None:
        out["space_title"] = data["spaceTitle"]
    return out
