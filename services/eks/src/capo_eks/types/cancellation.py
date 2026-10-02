"""Generated from Smithy shape ``com.amazonaws.eks#Cancellation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.cancellation_status
    import capo_eks.types.string


class Cancellation(TypedDict, closed=True):
    status: NotRequired["capo_eks.types.cancellation_status.CancellationStatus"]
    """<p>The current status of the cancellation. Valid values are <code>InProgress</code>, <code>Failed</code>, and <code>Successful</code>.</p>"""
    reason: NotRequired["capo_eks.types.string.String"]
    """<p>A message providing additional details about the cancellation, such as the reason for the cancellation or failure details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cancellation) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_eks.types.cancellation_status

        out["status"] = capo_eks.types.cancellation_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> Cancellation:
    out: Cancellation = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_eks.types.cancellation_status

        out["status"] = capo_eks.types.cancellation_status.deserialize_json(
            data["status"]
        )
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
