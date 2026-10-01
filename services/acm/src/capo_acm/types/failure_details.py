"""Generated from Smithy shape ``com.amazonaws.acm#FailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_domain_validation_failure_reason


class FailureDetails(TypedDict, closed=True):
    reason: NotRequired[
        "capo_acm.types.acme_domain_validation_failure_reason.AcmeDomainValidationFailureReason"
    ]
    """<p>The reason for the failure.</p>"""
    message: NotRequired["str"]
    """<p>A message describing the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureDetails) -> dict:
    out: dict = {}
    if "reason" in value:
        import capo_acm.types.acme_domain_validation_failure_reason

        out["Reason"] = (
            capo_acm.types.acme_domain_validation_failure_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailureDetails:
    out: FailureDetails = {}  # type: ignore[typeddict-item]
    if data.get("Reason") is not None:
        import capo_acm.types.acme_domain_validation_failure_reason

        out["reason"] = (
            capo_acm.types.acme_domain_validation_failure_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
