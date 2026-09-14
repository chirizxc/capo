"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ImprovementSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.choice_improvement_plans
    import capo_wellarchitected.types.improvement_plan_url
    import capo_wellarchitected.types.jira_configuration
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.question_title
    import capo_wellarchitected.types.risk


class ImprovementSummary(TypedDict, closed=True):
    question_id: NotRequired["capo_wellarchitected.types.question_id.QuestionId"]
    pillar_id: NotRequired["capo_wellarchitected.types.pillar_id.PillarId"]
    question_title: NotRequired[
        "capo_wellarchitected.types.question_title.QuestionTitle"
    ]
    risk: NotRequired["capo_wellarchitected.types.risk.Risk"]
    improvement_plan_url: NotRequired[
        "capo_wellarchitected.types.improvement_plan_url.ImprovementPlanUrl"
    ]
    improvement_plans: NotRequired[
        "capo_wellarchitected.types.choice_improvement_plans.ChoiceImprovementPlans"
    ]
    """<p>The improvement plan details.</p>"""
    jira_configuration: NotRequired[
        "capo_wellarchitected.types.jira_configuration.JiraConfiguration"
    ]
    """<p>Configuration of the Jira integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImprovementSummary) -> dict:
    out: dict = {}
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "question_title" in value:
        out["QuestionTitle"] = value["question_title"]
    if "risk" in value:
        import capo_wellarchitected.types.risk

        out["Risk"] = capo_wellarchitected.types.risk.serialize_json(value["risk"])
    if "improvement_plan_url" in value:
        out["ImprovementPlanUrl"] = value["improvement_plan_url"]
    if "improvement_plans" in value:
        import capo_wellarchitected.types.choice_improvement_plans

        out["ImprovementPlans"] = (
            capo_wellarchitected.types.choice_improvement_plans.serialize_json(
                value["improvement_plans"]
            )
        )
    if "jira_configuration" in value:
        import capo_wellarchitected.types.jira_configuration

        out["JiraConfiguration"] = (
            capo_wellarchitected.types.jira_configuration.serialize_json(
                value["jira_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImprovementSummary:
    out: ImprovementSummary = {}  # type: ignore[typeddict-item]
    if data.get("QuestionId") is not None:
        out["question_id"] = data["QuestionId"]
    if data.get("PillarId") is not None:
        out["pillar_id"] = data["PillarId"]
    if data.get("QuestionTitle") is not None:
        out["question_title"] = data["QuestionTitle"]
    if data.get("Risk") is not None:
        import capo_wellarchitected.types.risk

        out["risk"] = capo_wellarchitected.types.risk.deserialize_json(data["Risk"])
    if data.get("ImprovementPlanUrl") is not None:
        out["improvement_plan_url"] = data["ImprovementPlanUrl"]
    if data.get("ImprovementPlans") is not None:
        import capo_wellarchitected.types.choice_improvement_plans

        out["improvement_plans"] = (
            capo_wellarchitected.types.choice_improvement_plans.deserialize_json(
                data["ImprovementPlans"]
            )
        )
    if data.get("JiraConfiguration") is not None:
        import capo_wellarchitected.types.jira_configuration

        out["jira_configuration"] = (
            capo_wellarchitected.types.jira_configuration.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    return out
