"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyDetachedFromServiceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.account_id
    import capo_resiliencehubv2.types.arn


class PolicyDetachedFromServiceMetadata(TypedDict, closed=True):
    service_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    account_id: NotRequired["capo_resiliencehubv2.types.account_id.AccountId"]
    """<p>The account that owns the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyDetachedFromServiceMetadata) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> PolicyDetachedFromServiceMetadata:
    out: PolicyDetachedFromServiceMetadata = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    return out
