"""Generated from Smithy shape ``com.amazonaws.billingconductor#AssociateResourceError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.associate_resource_error_reason
    import capo_billingconductor.types.string


class AssociateResourceError(TypedDict, closed=True):
    message: NotRequired["capo_billingconductor.types.string.String"]
    """<p>The reason why the resource association failed.</p>"""
    reason: NotRequired[
        "capo_billingconductor.types.associate_resource_error_reason.AssociateResourceErrorReason"
    ]
    """<p>A static error code that's used to classify the type of failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateResourceError) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_billingconductor.types.associate_resource_error_reason

        out["Reason"] = (
            capo_billingconductor.types.associate_resource_error_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateResourceError:
    out: AssociateResourceError = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_billingconductor.types.associate_resource_error_reason

        out["reason"] = (
            capo_billingconductor.types.associate_resource_error_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out
