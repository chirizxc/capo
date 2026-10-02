"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteSegmentSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to1000


class DeleteSegmentSubscriptionResponse(TypedDict, closed=True):
    message: NotRequired["capo_customer_profiles.types.string1_to1000.string1To1000"]
    """<p>A confirmation message indicating the subscription was deleted successfully. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSegmentSubscriptionResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteSegmentSubscriptionResponse:
    out: DeleteSegmentSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
