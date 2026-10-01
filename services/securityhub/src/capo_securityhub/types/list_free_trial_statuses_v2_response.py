"""Generated from Smithy shape ``com.amazonaws.securityhub#ListFreeTrialStatusesV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.account_free_trial_status_list
    import capo_securityhub.types.next_token


class ListFreeTrialStatusesV2Response(TypedDict, closed=True):
    account_free_trial_statuses: NotRequired[
        "capo_securityhub.types.account_free_trial_status_list.AccountFreeTrialStatusList"
    ]
    """<p>An array of free trial statuses, one for each account in scope.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. If there are no additional results, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFreeTrialStatusesV2Response) -> dict:
    out: dict = {}
    if "account_free_trial_statuses" in value:
        import capo_securityhub.types.account_free_trial_status_list

        out["AccountFreeTrialStatuses"] = (
            capo_securityhub.types.account_free_trial_status_list.serialize_json(
                value["account_free_trial_statuses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFreeTrialStatusesV2Response:
    out: ListFreeTrialStatusesV2Response = {}  # type: ignore[typeddict-item]
    if data.get("AccountFreeTrialStatuses") is not None:
        import capo_securityhub.types.account_free_trial_status_list

        out["account_free_trial_statuses"] = (
            capo_securityhub.types.account_free_trial_status_list.deserialize_json(
                data["AccountFreeTrialStatuses"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
