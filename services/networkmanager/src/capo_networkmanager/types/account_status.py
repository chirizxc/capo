"""Generated from Smithy shape ``com.amazonaws.networkmanager#AccountStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.account_id
    import capo_networkmanager.types.slr_deployment_status


class AccountStatus(TypedDict, closed=True):
    account_id: NotRequired["capo_networkmanager.types.account_id.AccountId"]
    """<p>The ID of an account within the Amazon Web Services Organization.</p>"""
    slr_deployment_status: NotRequired[
        "capo_networkmanager.types.slr_deployment_status.SLRDeploymentStatus"
    ]
    """<p>The status of SLR deployment for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountStatus) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "slr_deployment_status" in value:
        out["SLRDeploymentStatus"] = value["slr_deployment_status"]
    return out


def deserialize_json(data: dict) -> AccountStatus:
    out: AccountStatus = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("SLRDeploymentStatus") is not None:
        out["slr_deployment_status"] = data["SLRDeploymentStatus"]
    return out
