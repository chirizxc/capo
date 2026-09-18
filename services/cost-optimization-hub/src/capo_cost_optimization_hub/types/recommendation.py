"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Recommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.datetime
    import capo_cost_optimization_hub.types.source
    import capo_cost_optimization_hub.types.tag_list


class Recommendation(TypedDict, closed=True):
    recommendation_id: NotRequired["str"]
    """<p>The ID for the recommendation.</p>"""
    account_id: NotRequired["str"]
    """<p>The account to which the recommendation applies.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region of the resource.</p>"""
    resource_id: NotRequired["str"]
    """<p>The resource ID for the recommendation.</p>"""
    resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the recommendation.</p>"""
    current_resource_type: NotRequired["str"]
    """<p>The current resource type.</p>"""
    recommended_resource_type: NotRequired["str"]
    """<p>The recommended resource type.</p>"""
    estimated_monthly_savings: NotRequired["float"]
    """<p>The estimated monthly savings amount for the recommendation.</p>"""
    estimated_savings_percentage: NotRequired["float"]
    """<p>The estimated savings percentage relative to the total cost over the cost calculation lookback period.</p>"""
    estimated_monthly_cost: NotRequired["float"]
    """<p>The estimated monthly cost of the current resource. For Reserved Instances and Savings Plans, it refers to the cost for eligible usage.</p>"""
    currency_code: NotRequired["str"]
    """<p>The currency code used for the recommendation.</p>"""
    implementation_effort: NotRequired["str"]
    """<p>The effort required to implement the recommendation.</p>"""
    restart_needed: NotRequired["bool"]
    """<p>Whether or not implementing the recommendation requires a restart.</p>"""
    action_type: NotRequired["str"]
    """<p>The type of tasks that can be carried out by this action.</p>"""
    rollback_possible: NotRequired["bool"]
    """<p>Whether or not implementing the recommendation can be rolled back.</p>"""
    current_resource_summary: NotRequired["str"]
    """<p>Describes the current resource.</p>"""
    recommended_resource_summary: NotRequired["str"]
    """<p>Describes the recommended resource.</p>"""
    last_refresh_timestamp: NotRequired[
        "capo_cost_optimization_hub.types.datetime.Datetime"
    ]
    """<p>The time when the recommendation was last generated.</p>"""
    recommendation_lookback_period_in_days: NotRequired["int"]
    """<p>The lookback period that's used to generate the recommendation.</p>"""
    source: NotRequired["capo_cost_optimization_hub.types.source.Source"]
    """<p>The source of the recommendation.</p>"""
    tags: NotRequired["capo_cost_optimization_hub.types.tag_list.TagList"]
    """<p>A list of tags assigned to the recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Recommendation) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "current_resource_type" in value:
        out["currentResourceType"] = value["current_resource_type"]
    if "recommended_resource_type" in value:
        out["recommendedResourceType"] = value["recommended_resource_type"]
    if "estimated_monthly_savings" in value:
        out["estimatedMonthlySavings"] = (
            "NaN"
            if value["estimated_monthly_savings"] != value["estimated_monthly_savings"]
            else "Infinity"
            if value["estimated_monthly_savings"] == float("inf")
            else "-Infinity"
            if value["estimated_monthly_savings"] == float("-inf")
            else value["estimated_monthly_savings"]
        )
    if "estimated_savings_percentage" in value:
        out["estimatedSavingsPercentage"] = (
            "NaN"
            if value["estimated_savings_percentage"]
            != value["estimated_savings_percentage"]
            else "Infinity"
            if value["estimated_savings_percentage"] == float("inf")
            else "-Infinity"
            if value["estimated_savings_percentage"] == float("-inf")
            else value["estimated_savings_percentage"]
        )
    if "estimated_monthly_cost" in value:
        out["estimatedMonthlyCost"] = (
            "NaN"
            if value["estimated_monthly_cost"] != value["estimated_monthly_cost"]
            else "Infinity"
            if value["estimated_monthly_cost"] == float("inf")
            else "-Infinity"
            if value["estimated_monthly_cost"] == float("-inf")
            else value["estimated_monthly_cost"]
        )
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "implementation_effort" in value:
        out["implementationEffort"] = value["implementation_effort"]
    if "restart_needed" in value:
        out["restartNeeded"] = value["restart_needed"]
    if "action_type" in value:
        out["actionType"] = value["action_type"]
    if "rollback_possible" in value:
        out["rollbackPossible"] = value["rollback_possible"]
    if "current_resource_summary" in value:
        out["currentResourceSummary"] = value["current_resource_summary"]
    if "recommended_resource_summary" in value:
        out["recommendedResourceSummary"] = value["recommended_resource_summary"]
    if "last_refresh_timestamp" in value:
        import capo_cost_optimization_hub.types.datetime

        out["lastRefreshTimestamp"] = (
            capo_cost_optimization_hub.types.datetime.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "recommendation_lookback_period_in_days" in value:
        out["recommendationLookbackPeriodInDays"] = value[
            "recommendation_lookback_period_in_days"
        ]
    if "source" in value:
        import capo_cost_optimization_hub.types.source

        out["source"] = capo_cost_optimization_hub.types.source.serialize_aws_json_1_0(
            value["source"]
        )
    if "tags" in value:
        import capo_cost_optimization_hub.types.tag_list

        out["tags"] = capo_cost_optimization_hub.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("currentResourceType") is not None:
        out["current_resource_type"] = data["currentResourceType"]
    if data.get("recommendedResourceType") is not None:
        out["recommended_resource_type"] = data["recommendedResourceType"]
    if data.get("estimatedMonthlySavings") is not None:
        out["estimated_monthly_savings"] = float(data["estimatedMonthlySavings"])
    if data.get("estimatedSavingsPercentage") is not None:
        out["estimated_savings_percentage"] = float(data["estimatedSavingsPercentage"])
    if data.get("estimatedMonthlyCost") is not None:
        out["estimated_monthly_cost"] = float(data["estimatedMonthlyCost"])
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("implementationEffort") is not None:
        out["implementation_effort"] = data["implementationEffort"]
    if data.get("restartNeeded") is not None:
        out["restart_needed"] = data["restartNeeded"]
    if data.get("actionType") is not None:
        out["action_type"] = data["actionType"]
    if data.get("rollbackPossible") is not None:
        out["rollback_possible"] = data["rollbackPossible"]
    if data.get("currentResourceSummary") is not None:
        out["current_resource_summary"] = data["currentResourceSummary"]
    if data.get("recommendedResourceSummary") is not None:
        out["recommended_resource_summary"] = data["recommendedResourceSummary"]
    if data.get("lastRefreshTimestamp") is not None:
        import capo_cost_optimization_hub.types.datetime

        out["last_refresh_timestamp"] = (
            capo_cost_optimization_hub.types.datetime.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("recommendationLookbackPeriodInDays") is not None:
        out["recommendation_lookback_period_in_days"] = data[
            "recommendationLookbackPeriodInDays"
        ]
    if data.get("source") is not None:
        import capo_cost_optimization_hub.types.source

        out["source"] = (
            capo_cost_optimization_hub.types.source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    if data.get("tags") is not None:
        import capo_cost_optimization_hub.types.tag_list

        out["tags"] = (
            capo_cost_optimization_hub.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
