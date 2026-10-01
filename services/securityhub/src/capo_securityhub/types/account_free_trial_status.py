"""Generated from Smithy shape ``com.amazonaws.securityhub#AccountFreeTrialStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.free_trial_account_id
    import capo_securityhub.types.free_trial_status_list
    import capo_securityhub.types.timestamp


class AccountFreeTrialStatus(TypedDict, closed=True):
    account_id: NotRequired[
        "capo_securityhub.types.free_trial_account_id.FreeTrialAccountId"
    ]
    """<p>The Amazon Web Services account identifier that the free trial statuses apply to.</p>"""
    evaluated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The date and time at which Security Hub evaluated the free trial statuses for this account. Every status in <code>FreeTrialStatuses</code> reflects this point in time.</p>"""
    free_trial_statuses: NotRequired[
        "capo_securityhub.types.free_trial_status_list.FreeTrialStatusList"
    ]
    """<p>An array of free trial statuses, one for each feature that has a free trial period for the account. The array is empty if the account has no free trial to report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountFreeTrialStatus) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "evaluated_at" in value:
        import capo_securityhub.types.timestamp

        out["EvaluatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["evaluated_at"]
        )
    if "free_trial_statuses" in value:
        import capo_securityhub.types.free_trial_status_list

        out["FreeTrialStatuses"] = (
            capo_securityhub.types.free_trial_status_list.serialize_json(
                value["free_trial_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountFreeTrialStatus:
    out: AccountFreeTrialStatus = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("EvaluatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["evaluated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["EvaluatedAt"]
        )
    if data.get("FreeTrialStatuses") is not None:
        import capo_securityhub.types.free_trial_status_list

        out["free_trial_statuses"] = (
            capo_securityhub.types.free_trial_status_list.deserialize_json(
                data["FreeTrialStatuses"]
            )
        )
    return out
