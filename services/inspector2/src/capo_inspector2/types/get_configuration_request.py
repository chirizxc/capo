"""Generated from Smithy shape ``com.amazonaws.inspector2#GetConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id


class GetConfigurationRequest(TypedDict, closed=True):
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The 12-digit Amazon Web Services account ID of the member account whose scan configuration you want to retrieve. When specified, you must be the delegated administrator for this member account. If not specified, the operation returns your own configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> GetConfigurationRequest:
    out: GetConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    return out
