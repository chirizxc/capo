"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PromotionalEmbeddedVideo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.nullable_string
    import capo_marketplace_discovery.types.url


class PromotionalEmbeddedVideo(TypedDict, closed=True):
    title: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The title displayed when hovering over the video.</p>"""
    url: "capo_marketplace_discovery.types.url.URL"
    """<p>The URL of the video file.</p>"""
    preview: "capo_marketplace_discovery.types.url.URL"
    """<p>The URL of the high-resolution preview image for the video.</p>"""
    thumbnail: "capo_marketplace_discovery.types.url.URL"
    """<p>The URL of the thumbnail image for the video.</p>"""
    description: NotRequired[
        "capo_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>An optional description of the video.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromotionalEmbeddedVideo) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["url"] = value["url"]
    out["preview"] = value["preview"]
    out["thumbnail"] = value["thumbnail"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PromotionalEmbeddedVideo:
    out: PromotionalEmbeddedVideo = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        raise DeserializationError("PromotionalEmbeddedVideo.title required")
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        raise DeserializationError("PromotionalEmbeddedVideo.url required")
    if data.get("preview") is not None:
        out["preview"] = data["preview"]
    else:
        raise DeserializationError("PromotionalEmbeddedVideo.preview required")
    if data.get("thumbnail") is not None:
        out["thumbnail"] = data["thumbnail"]
    else:
        raise DeserializationError("PromotionalEmbeddedVideo.thumbnail required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
