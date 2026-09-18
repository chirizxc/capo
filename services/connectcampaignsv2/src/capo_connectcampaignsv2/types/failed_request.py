"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#FailedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.client_token
    import capo_connectcampaignsv2.types.dial_request_id
    import capo_connectcampaignsv2.types.failure_code


class FailedRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_connectcampaignsv2.types.client_token.ClientToken"]
    id: NotRequired["capo_connectcampaignsv2.types.dial_request_id.DialRequestId"]
    failure_code: NotRequired["capo_connectcampaignsv2.types.failure_code.FailureCode"]


# --- restJson1 ser/de ---
def serialize_json(value: FailedRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "id" in value:
        out["id"] = value["id"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    return out


def deserialize_json(data: dict) -> FailedRequest:
    out: FailedRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("failureCode") is not None:
        out["failure_code"] = data["failureCode"]
    return out
