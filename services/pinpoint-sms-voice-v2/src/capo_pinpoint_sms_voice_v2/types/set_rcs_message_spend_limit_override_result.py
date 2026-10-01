"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SetRcsMessageSpendLimitOverrideResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.monthly_limit


class SetRcsMessageSpendLimitOverrideResult(TypedDict, closed=True):
    monthly_limit: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit"
    ]
    """<p>The current monthly limit to enforce on RCS message spending.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetRcsMessageSpendLimitOverrideResult) -> dict:
    out: dict = {}
    if "monthly_limit" in value:
        out["MonthlyLimit"] = value["monthly_limit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SetRcsMessageSpendLimitOverrideResult:
    out: SetRcsMessageSpendLimitOverrideResult = {}  # type: ignore[typeddict-item]
    if data.get("MonthlyLimit") is not None:
        out["monthly_limit"] = data["MonthlyLimit"]
    return out
