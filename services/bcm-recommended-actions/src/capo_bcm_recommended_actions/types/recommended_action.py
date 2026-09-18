"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#RecommendedAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_recommended_actions.types.account_id
    import capo_bcm_recommended_actions.types.action_type
    import capo_bcm_recommended_actions.types.context
    import capo_bcm_recommended_actions.types.feature
    import capo_bcm_recommended_actions.types.next_steps
    import capo_bcm_recommended_actions.types.severity


class RecommendedAction(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID for the recommended action.</p>"""
    type: NotRequired["capo_bcm_recommended_actions.types.action_type.ActionType"]
    """<p>The type of action you can take by adopting the recommended action.</p>"""
    account_id: NotRequired["capo_bcm_recommended_actions.types.account_id.AccountId"]
    """<p>The account that the recommended action is for.</p>"""
    severity: NotRequired["capo_bcm_recommended_actions.types.severity.Severity"]
    """<p>The severity associated with the recommended action.</p>"""
    feature: NotRequired["capo_bcm_recommended_actions.types.feature.Feature"]
    """<p>The feature associated with the recommended action.</p>"""
    context: NotRequired["capo_bcm_recommended_actions.types.context.Context"]
    """<p>Context that applies to the recommended action.</p>"""
    next_steps: NotRequired["capo_bcm_recommended_actions.types.next_steps.NextSteps"]
    """<p>The possible next steps to execute the recommended action.</p>"""
    last_updated_time_stamp: NotRequired["str"]
    """<p>The time when the recommended action status was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedAction) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import capo_bcm_recommended_actions.types.action_type

        out["type"] = (
            capo_bcm_recommended_actions.types.action_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity" in value:
        import capo_bcm_recommended_actions.types.severity

        out["severity"] = (
            capo_bcm_recommended_actions.types.severity.serialize_aws_json_1_0(
                value["severity"]
            )
        )
    if "feature" in value:
        import capo_bcm_recommended_actions.types.feature

        out["feature"] = (
            capo_bcm_recommended_actions.types.feature.serialize_aws_json_1_0(
                value["feature"]
            )
        )
    if "context" in value:
        import capo_bcm_recommended_actions.types.context

        out["context"] = (
            capo_bcm_recommended_actions.types.context.serialize_aws_json_1_0(
                value["context"]
            )
        )
    if "next_steps" in value:
        import capo_bcm_recommended_actions.types.next_steps

        out["nextSteps"] = (
            capo_bcm_recommended_actions.types.next_steps.serialize_aws_json_1_0(
                value["next_steps"]
            )
        )
    if "last_updated_time_stamp" in value:
        out["lastUpdatedTimeStamp"] = value["last_updated_time_stamp"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendedAction:
    out: RecommendedAction = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("type") is not None:
        import capo_bcm_recommended_actions.types.action_type

        out["type"] = (
            capo_bcm_recommended_actions.types.action_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("severity") is not None:
        import capo_bcm_recommended_actions.types.severity

        out["severity"] = (
            capo_bcm_recommended_actions.types.severity.deserialize_aws_json_1_0(
                data["severity"]
            )
        )
    if data.get("feature") is not None:
        import capo_bcm_recommended_actions.types.feature

        out["feature"] = (
            capo_bcm_recommended_actions.types.feature.deserialize_aws_json_1_0(
                data["feature"]
            )
        )
    if data.get("context") is not None:
        import capo_bcm_recommended_actions.types.context

        out["context"] = (
            capo_bcm_recommended_actions.types.context.deserialize_aws_json_1_0(
                data["context"]
            )
        )
    if data.get("nextSteps") is not None:
        import capo_bcm_recommended_actions.types.next_steps

        out["next_steps"] = (
            capo_bcm_recommended_actions.types.next_steps.deserialize_aws_json_1_0(
                data["nextSteps"]
            )
        )
    if data.get("lastUpdatedTimeStamp") is not None:
        out["last_updated_time_stamp"] = data["lastUpdatedTimeStamp"]
    return out
