"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDescribeUserLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.batch_describe_user_limits_request_users_list
    import capo_quicksight.types.resource_type_list


class BatchDescribeUserLimitsRequest(TypedDict, closed=True):
    account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the users.</p>"""
    users: NotRequired[
        "capo_quicksight.types.batch_describe_user_limits_request_users_list.BatchDescribeUserLimitsRequestUsersList"
    ]
    """<p>A list of users to describe limits for. Each entry contains a user name and namespace.</p>"""
    resource_types: NotRequired[
        "capo_quicksight.types.resource_type_list.ResourceTypeList"
    ]
    """<p>An optional filter that limits the results to specific resource types. If you don't specify a value, the operation returns limits for all resource types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDescribeUserLimitsRequest) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_quicksight.types.batch_describe_user_limits_request_users_list

        out["users"] = (
            capo_quicksight.types.batch_describe_user_limits_request_users_list.serialize_json(
                value["users"]
            )
        )
    if "resource_types" in value:
        import capo_quicksight.types.resource_type_list

        out["resourceTypes"] = capo_quicksight.types.resource_type_list.serialize_json(
            value["resource_types"]
        )
    return out


def deserialize_json(data: dict) -> BatchDescribeUserLimitsRequest:
    out: BatchDescribeUserLimitsRequest = {}  # type: ignore[typeddict-item]
    if data.get("users") is not None:
        import capo_quicksight.types.batch_describe_user_limits_request_users_list

        out["users"] = (
            capo_quicksight.types.batch_describe_user_limits_request_users_list.deserialize_json(
                data["users"]
            )
        )
    if data.get("resourceTypes") is not None:
        import capo_quicksight.types.resource_type_list

        out["resource_types"] = (
            capo_quicksight.types.resource_type_list.deserialize_json(
                data["resourceTypes"]
            )
        )
    return out
