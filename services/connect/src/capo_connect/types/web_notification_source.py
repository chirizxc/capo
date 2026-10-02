"""Generated from Smithy shape ``com.amazonaws.connect#WebNotificationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.source_campaign


class WebNotificationSource(TypedDict, closed=True):
    source_campaign: "capo_connect.types.source_campaign.SourceCampaign"
    """<p>Information about the campaign that triggered the web notification, including the campaign identifier and outbound request identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebNotificationSource) -> dict:
    out: dict = {}
    import capo_connect.types.source_campaign

    out["SourceCampaign"] = capo_connect.types.source_campaign.serialize_json(
        value["source_campaign"]
    )
    return out


def deserialize_json(data: dict) -> WebNotificationSource:
    out: WebNotificationSource = {}  # type: ignore[typeddict-item]
    if data.get("SourceCampaign") is not None:
        import capo_connect.types.source_campaign

        out["source_campaign"] = capo_connect.types.source_campaign.deserialize_json(
            data["SourceCampaign"]
        )
    else:
        raise DeserializationError("WebNotificationSource.source_campaign required")
    return out
