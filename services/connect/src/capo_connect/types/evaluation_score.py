"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.double
    import capo_connect.types.evaluation_score_percentage


class EvaluationScore(TypedDict, closed=True):
    percentage: (
        "capo_connect.types.evaluation_score_percentage.EvaluationScorePercentage"
    )
    """<p>The score percentage for an item in a contact evaluation.</p>"""
    not_applicable: "capo_connect.types.boolean.Boolean"
    """<p>The flag to mark the item as not applicable for scoring.</p>"""
    automatic_fail: "capo_connect.types.boolean.Boolean"
    """<p>The flag that marks the item as automatic fail. If the item or a child item gets an automatic fail answer, this flag will be true.</p>"""
    applied_weight: NotRequired["capo_connect.types.double.Double"]
    """<p>Weight applied to this evaluation score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationScore) -> dict:
    out: dict = {}
    out["Percentage"] = (
        "NaN"
        if value.get("percentage", 0) != value.get("percentage", 0)
        else "Infinity"
        if value.get("percentage", 0) == float("inf")
        else "-Infinity"
        if value.get("percentage", 0) == float("-inf")
        else value.get("percentage", 0)
    )
    out["NotApplicable"] = value.get("not_applicable", False)
    out["AutomaticFail"] = value.get("automatic_fail", False)
    if "applied_weight" in value:
        out["AppliedWeight"] = (
            "NaN"
            if value["applied_weight"] != value["applied_weight"]
            else "Infinity"
            if value["applied_weight"] == float("inf")
            else "-Infinity"
            if value["applied_weight"] == float("-inf")
            else value["applied_weight"]
        )
    return out


def deserialize_json(data: dict) -> EvaluationScore:
    out: EvaluationScore = {}  # type: ignore[typeddict-item]
    if data.get("Percentage") is not None:
        out["percentage"] = float(data["Percentage"])
    else:
        out["percentage"] = 0
    if data.get("NotApplicable") is not None:
        out["not_applicable"] = data["NotApplicable"]
    else:
        out["not_applicable"] = False
    if data.get("AutomaticFail") is not None:
        out["automatic_fail"] = data["AutomaticFail"]
    else:
        out["automatic_fail"] = False
    if data.get("AppliedWeight") is not None:
        out["applied_weight"] = float(data["AppliedWeight"])
    return out
