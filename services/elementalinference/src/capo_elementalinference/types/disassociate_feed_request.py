"""Generated from Smithy shape ``com.amazonaws.elementalinference#DisassociateFeedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elementalinference.types.associated_resource_name
    import capo_elementalinference.types.feed_id


class DisassociateFeedRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed where you want to release the resource.</p>"""
    associated_resource_name: (
        "capo_elementalinference.types.associated_resource_name.AssociatedResourceName"
    )
    """<p>The name of the resource currently associated with the feed.</p>"""
    dry_run: "bool"
    """<p>Set to true if you want to do a dry run of the disassociate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions. If the dry run fails, the action returns a 4xx error code. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateFeedRequest) -> dict:
    out: dict = {}
    out["associatedResourceName"] = value["associated_resource_name"]
    out["dryRun"] = value.get("dry_run", False)
    return out


def deserialize_json(data: dict) -> DisassociateFeedRequest:
    out: DisassociateFeedRequest = {}  # type: ignore[typeddict-item]
    if data.get("associatedResourceName") is not None:
        out["associated_resource_name"] = data["associatedResourceName"]
    else:
        raise DeserializationError(
            "DisassociateFeedRequest.associated_resource_name required"
        )
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out
