"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.arn
    import capo_cost_explorer.types.cost_category_name
    import capo_cost_explorer.types.cost_category_processing_status_list
    import capo_cost_explorer.types.cost_category_value
    import capo_cost_explorer.types.cost_category_values_list
    import capo_cost_explorer.types.non_negative_integer
    import capo_cost_explorer.types.resource_types
    import capo_cost_explorer.types.zoned_date_time


class CostCategoryReference(TypedDict, closed=True):
    cost_category_arn: NotRequired["capo_cost_explorer.types.arn.Arn"]
    """<p>The unique identifier for your cost category. </p>"""
    name: NotRequired["capo_cost_explorer.types.cost_category_name.CostCategoryName"]
    effective_start: NotRequired[
        "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The cost category's effective start date.</p>"""
    effective_end: NotRequired["capo_cost_explorer.types.zoned_date_time.ZonedDateTime"]
    """<p>The cost category's effective end date.</p>"""
    number_of_rules: "capo_cost_explorer.types.non_negative_integer.NonNegativeInteger"
    """<p>The number of rules that are associated with a specific cost category. </p>"""
    processing_status: NotRequired[
        "capo_cost_explorer.types.cost_category_processing_status_list.CostCategoryProcessingStatusList"
    ]
    """<p>The list of processing statuses for Cost Management products for a specific cost category. </p>"""
    values: NotRequired[
        "capo_cost_explorer.types.cost_category_values_list.CostCategoryValuesList"
    ]
    """<p>A list of unique cost category values in a specific cost category. </p>"""
    default_value: NotRequired[
        "capo_cost_explorer.types.cost_category_value.CostCategoryValue"
    ]
    supported_resource_types: NotRequired[
        "capo_cost_explorer.types.resource_types.ResourceTypes"
    ]
    """<p> The resource types supported by a specific cost category. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryReference) -> dict:
    out: dict = {}
    if "cost_category_arn" in value:
        out["CostCategoryArn"] = value["cost_category_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "effective_start" in value:
        out["EffectiveStart"] = value["effective_start"]
    if "effective_end" in value:
        out["EffectiveEnd"] = value["effective_end"]
    out["NumberOfRules"] = value.get("number_of_rules", 0)
    if "processing_status" in value:
        import capo_cost_explorer.types.cost_category_processing_status_list

        out["ProcessingStatus"] = (
            capo_cost_explorer.types.cost_category_processing_status_list.serialize_aws_json_1_1(
                value["processing_status"]
            )
        )
    if "values" in value:
        import capo_cost_explorer.types.cost_category_values_list

        out["Values"] = (
            capo_cost_explorer.types.cost_category_values_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "supported_resource_types" in value:
        import capo_cost_explorer.types.resource_types

        out["SupportedResourceTypes"] = (
            capo_cost_explorer.types.resource_types.serialize_aws_json_1_1(
                value["supported_resource_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategoryReference:
    out: CostCategoryReference = {}  # type: ignore[typeddict-item]
    if data.get("CostCategoryArn") is not None:
        out["cost_category_arn"] = data["CostCategoryArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EffectiveStart") is not None:
        out["effective_start"] = data["EffectiveStart"]
    if data.get("EffectiveEnd") is not None:
        out["effective_end"] = data["EffectiveEnd"]
    if data.get("NumberOfRules") is not None:
        out["number_of_rules"] = data["NumberOfRules"]
    else:
        out["number_of_rules"] = 0
    if data.get("ProcessingStatus") is not None:
        import capo_cost_explorer.types.cost_category_processing_status_list

        out["processing_status"] = (
            capo_cost_explorer.types.cost_category_processing_status_list.deserialize_aws_json_1_1(
                data["ProcessingStatus"]
            )
        )
    if data.get("Values") is not None:
        import capo_cost_explorer.types.cost_category_values_list

        out["values"] = (
            capo_cost_explorer.types.cost_category_values_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    if data.get("SupportedResourceTypes") is not None:
        import capo_cost_explorer.types.resource_types

        out["supported_resource_types"] = (
            capo_cost_explorer.types.resource_types.deserialize_aws_json_1_1(
                data["SupportedResourceTypes"]
            )
        )
    return out
