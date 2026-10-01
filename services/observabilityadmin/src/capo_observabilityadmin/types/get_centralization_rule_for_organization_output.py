"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetCentralizationRuleForOrganizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.centralization_failure_reason
    import capo_observabilityadmin.types.centralization_rule
    import capo_observabilityadmin.types.context_graph_status
    import capo_observabilityadmin.types.region
    import capo_observabilityadmin.types.resource_arn
    import capo_observabilityadmin.types.rule_health
    import capo_observabilityadmin.types.rule_name
    import capo_observabilityadmin.types.tag_propagation_failure_reason
    import capo_observabilityadmin.types.tag_propagation_status


class GetCentralizationRuleForOrganizationOutput(TypedDict, closed=True):
    rule_name: NotRequired["capo_observabilityadmin.types.rule_name.RuleName"]
    """<p>The name of the organization centralization rule.</p>"""
    rule_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the organization centralization rule.</p>"""
    creator_account_id: NotRequired["str"]
    """<p>The Amazon Web Services Account that created the organization centralization rule.</p>"""
    created_time_stamp: NotRequired["int"]
    """<p>The timestamp when the organization centralization rule was created.</p>"""
    created_region: NotRequired["capo_observabilityadmin.types.region.Region"]
    """<p>The Amazon Web Services region where the organization centralization rule was created.</p>"""
    last_update_time_stamp: NotRequired["int"]
    """<p>The timestamp when the organization centralization rule was last updated.</p>"""
    rule_health: NotRequired["capo_observabilityadmin.types.rule_health.RuleHealth"]
    """<p>The health status of the organization centralization rule.</p>"""
    failure_reason: NotRequired[
        "capo_observabilityadmin.types.centralization_failure_reason.CentralizationFailureReason"
    ]
    """<p>The reason why an organization centralization rule is marked UNHEALTHY.</p>"""
    tag_propagation_status: NotRequired[
        "capo_observabilityadmin.types.tag_propagation_status.TagPropagationStatus"
    ]
    """<p>The health status of tag propagation for this rule. This status is independent of the overall <code>RuleHealth</code> for log delivery. Returns <code>Healthy</code> when the most recent tag-propagation attempt succeeded, or <code>Unhealthy</code> when the most recent attempt failed.</p>"""
    tag_propagation_failure_reason: NotRequired[
        "capo_observabilityadmin.types.tag_propagation_failure_reason.TagPropagationFailureReason"
    ]
    """<p>The reason tag propagation is unhealthy for this rule. Only present when <code>TagPropagationStatus</code> is <code>Unhealthy</code>.</p>"""
    context_graph_status: NotRequired[
        "capo_observabilityadmin.types.context_graph_status.ContextGraphStatus"
    ]
    """<p>The status of context graph centralization for this rule. Returns <code>Provisioning</code> while the context graph is being set up, <code>Healthy</code> once it is active, or <code>Unhealthy</code> if provisioning failed. This status is independent of the overall <code>RuleHealth</code> for log delivery.</p>"""
    centralization_rule: NotRequired[
        "capo_observabilityadmin.types.centralization_rule.CentralizationRule"
    ]
    """<p>The configuration details for the organization centralization rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCentralizationRuleForOrganizationOutput) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "creator_account_id" in value:
        out["CreatorAccountId"] = value["creator_account_id"]
    if "created_time_stamp" in value:
        out["CreatedTimeStamp"] = value["created_time_stamp"]
    if "created_region" in value:
        out["CreatedRegion"] = value["created_region"]
    if "last_update_time_stamp" in value:
        out["LastUpdateTimeStamp"] = value["last_update_time_stamp"]
    if "rule_health" in value:
        import capo_observabilityadmin.types.rule_health

        out["RuleHealth"] = capo_observabilityadmin.types.rule_health.serialize_json(
            value["rule_health"]
        )
    if "failure_reason" in value:
        import capo_observabilityadmin.types.centralization_failure_reason

        out["FailureReason"] = (
            capo_observabilityadmin.types.centralization_failure_reason.serialize_json(
                value["failure_reason"]
            )
        )
    if "tag_propagation_status" in value:
        import capo_observabilityadmin.types.tag_propagation_status

        out["TagPropagationStatus"] = (
            capo_observabilityadmin.types.tag_propagation_status.serialize_json(
                value["tag_propagation_status"]
            )
        )
    if "tag_propagation_failure_reason" in value:
        import capo_observabilityadmin.types.tag_propagation_failure_reason

        out["TagPropagationFailureReason"] = (
            capo_observabilityadmin.types.tag_propagation_failure_reason.serialize_json(
                value["tag_propagation_failure_reason"]
            )
        )
    if "context_graph_status" in value:
        import capo_observabilityadmin.types.context_graph_status

        out["ContextGraphStatus"] = (
            capo_observabilityadmin.types.context_graph_status.serialize_json(
                value["context_graph_status"]
            )
        )
    if "centralization_rule" in value:
        import capo_observabilityadmin.types.centralization_rule

        out["CentralizationRule"] = (
            capo_observabilityadmin.types.centralization_rule.serialize_json(
                value["centralization_rule"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCentralizationRuleForOrganizationOutput:
    out: GetCentralizationRuleForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    if data.get("RuleArn") is not None:
        out["rule_arn"] = data["RuleArn"]
    if data.get("CreatorAccountId") is not None:
        out["creator_account_id"] = data["CreatorAccountId"]
    if data.get("CreatedTimeStamp") is not None:
        out["created_time_stamp"] = data["CreatedTimeStamp"]
    if data.get("CreatedRegion") is not None:
        out["created_region"] = data["CreatedRegion"]
    if data.get("LastUpdateTimeStamp") is not None:
        out["last_update_time_stamp"] = data["LastUpdateTimeStamp"]
    if data.get("RuleHealth") is not None:
        import capo_observabilityadmin.types.rule_health

        out["rule_health"] = capo_observabilityadmin.types.rule_health.deserialize_json(
            data["RuleHealth"]
        )
    if data.get("FailureReason") is not None:
        import capo_observabilityadmin.types.centralization_failure_reason

        out["failure_reason"] = (
            capo_observabilityadmin.types.centralization_failure_reason.deserialize_json(
                data["FailureReason"]
            )
        )
    if data.get("TagPropagationStatus") is not None:
        import capo_observabilityadmin.types.tag_propagation_status

        out["tag_propagation_status"] = (
            capo_observabilityadmin.types.tag_propagation_status.deserialize_json(
                data["TagPropagationStatus"]
            )
        )
    if data.get("TagPropagationFailureReason") is not None:
        import capo_observabilityadmin.types.tag_propagation_failure_reason

        out["tag_propagation_failure_reason"] = (
            capo_observabilityadmin.types.tag_propagation_failure_reason.deserialize_json(
                data["TagPropagationFailureReason"]
            )
        )
    if data.get("ContextGraphStatus") is not None:
        import capo_observabilityadmin.types.context_graph_status

        out["context_graph_status"] = (
            capo_observabilityadmin.types.context_graph_status.deserialize_json(
                data["ContextGraphStatus"]
            )
        )
    if data.get("CentralizationRule") is not None:
        import capo_observabilityadmin.types.centralization_rule

        out["centralization_rule"] = (
            capo_observabilityadmin.types.centralization_rule.deserialize_json(
                data["CentralizationRule"]
            )
        )
    return out
