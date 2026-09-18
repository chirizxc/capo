"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.aws_region
    import capo_config_service.types.resource_id
    import capo_config_service.types.resource_name


class ResourceFilters(TypedDict, closed=True):
    account_id: NotRequired["capo_config_service.types.account_id.AccountId"]
    """<p>The 12-digit source account ID.</p>"""
    resource_id: NotRequired["capo_config_service.types.resource_id.ResourceId"]
    """<p>The ID of the resource.</p>"""
    resource_name: NotRequired["capo_config_service.types.resource_name.ResourceName"]
    """<p>The name of the resource.</p>"""
    region: NotRequired["capo_config_service.types.aws_region.AwsRegion"]
    """<p>The source region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceFilters) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceFilters:
    out: ResourceFilters = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    return out
