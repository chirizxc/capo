"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestionScoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.evaluation_form_score_threshold_list
    import capo_connect.types.question_points_configuration


class EvaluationFormQuestionScoringConfiguration(TypedDict, closed=True):
    points_configuration: NotRequired[
        "capo_connect.types.question_points_configuration.QuestionPointsConfiguration"
    ]
    """<p>The points configuration for point-based scoring.</p>"""
    is_excluded_from_scoring: "capo_connect.types.boolean.Boolean"
    """<p>The flag to exclude the question from scoring.</p>"""
    score_thresholds: NotRequired[
        "capo_connect.types.evaluation_form_score_threshold_list.EvaluationFormScoreThresholdList"
    ]
    """<p>The score thresholds for performance categories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormQuestionScoringConfiguration) -> dict:
    out: dict = {}
    if "points_configuration" in value:
        import capo_connect.types.question_points_configuration

        out["PointsConfiguration"] = (
            capo_connect.types.question_points_configuration.serialize_json(
                value["points_configuration"]
            )
        )
    out["IsExcludedFromScoring"] = value.get("is_excluded_from_scoring", False)
    if "score_thresholds" in value:
        import capo_connect.types.evaluation_form_score_threshold_list

        out["ScoreThresholds"] = (
            capo_connect.types.evaluation_form_score_threshold_list.serialize_json(
                value["score_thresholds"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormQuestionScoringConfiguration:
    out: EvaluationFormQuestionScoringConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PointsConfiguration") is not None:
        import capo_connect.types.question_points_configuration

        out["points_configuration"] = (
            capo_connect.types.question_points_configuration.deserialize_json(
                data["PointsConfiguration"]
            )
        )
    if data.get("IsExcludedFromScoring") is not None:
        out["is_excluded_from_scoring"] = data["IsExcludedFromScoring"]
    else:
        out["is_excluded_from_scoring"] = False
    if data.get("ScoreThresholds") is not None:
        import capo_connect.types.evaluation_form_score_threshold_list

        out["score_thresholds"] = (
            capo_connect.types.evaluation_form_score_threshold_list.deserialize_json(
                data["ScoreThresholds"]
            )
        )
    return out
