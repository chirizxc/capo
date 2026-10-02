"""Generated from Smithy shape ``com.amazonaws.securityhub#ListFreeTrialStatusesV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.free_trial_account_id_list
    import capo_securityhub.types.free_trial_status_value_list
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token


class ListFreeTrialStatusesV2Request(TypedDict, closed=True):
    account_ids: NotRequired[
        "capo_securityhub.types.free_trial_account_id_list.FreeTrialAccountIdList"
    ]
    """<p>The Amazon Web Services account identifiers to list free trial status for. You can specify accounts other than your own only if you are a delegated Security Hub administrator.</p>"""
    statuses: NotRequired[
        "capo_securityhub.types.free_trial_status_value_list.FreeTrialStatusValueList"
    ]
    """<p>The free trial statuses to filter the results by. Valid values:</p> <ul> <li> <p> <code>ACTIVE</code> returns only features with an ongoing free trial period.</p> </li> <li> <p> <code>INACTIVE</code> returns only features whose free trial period has ended, or that never started.</p> </li> </ul>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. If you don't specify a value, Security Hub returns up to 100 results.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFreeTrialStatusesV2Request) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_securityhub.types.free_trial_account_id_list

        out["AccountIds"] = (
            capo_securityhub.types.free_trial_account_id_list.serialize_json(
                value["account_ids"]
            )
        )
    if "statuses" in value:
        import capo_securityhub.types.free_trial_status_value_list

        out["Statuses"] = (
            capo_securityhub.types.free_trial_status_value_list.serialize_json(
                value["statuses"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFreeTrialStatusesV2Request:
    out: ListFreeTrialStatusesV2Request = {}  # type: ignore[typeddict-item]
    if data.get("AccountIds") is not None:
        import capo_securityhub.types.free_trial_account_id_list

        out["account_ids"] = (
            capo_securityhub.types.free_trial_account_id_list.deserialize_json(
                data["AccountIds"]
            )
        )
    if data.get("Statuses") is not None:
        import capo_securityhub.types.free_trial_status_value_list

        out["statuses"] = (
            capo_securityhub.types.free_trial_status_value_list.deserialize_json(
                data["Statuses"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
