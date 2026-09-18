"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalyScore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_double


class AnomalyScore(TypedDict, closed=True):
    max_score: "capo_cost_explorer.types.generic_double.GenericDouble"
    """<p>The maximum score that's observed during the <code>AnomalyDateInterval</code>. </p>"""
    current_score: "capo_cost_explorer.types.generic_double.GenericDouble"
    """<p>The last observed score. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalyScore) -> dict:
    out: dict = {}
    out["MaxScore"] = (
        "NaN"
        if value.get("max_score", 0) != value.get("max_score", 0)
        else "Infinity"
        if value.get("max_score", 0) == float("inf")
        else "-Infinity"
        if value.get("max_score", 0) == float("-inf")
        else value.get("max_score", 0)
    )
    out["CurrentScore"] = (
        "NaN"
        if value.get("current_score", 0) != value.get("current_score", 0)
        else "Infinity"
        if value.get("current_score", 0) == float("inf")
        else "-Infinity"
        if value.get("current_score", 0) == float("-inf")
        else value.get("current_score", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnomalyScore:
    out: AnomalyScore = {}  # type: ignore[typeddict-item]
    if data.get("MaxScore") is not None:
        out["max_score"] = float(data["MaxScore"])
    else:
        out["max_score"] = 0
    if data.get("CurrentScore") is not None:
        out["current_score"] = float(data["CurrentScore"])
    else:
        out["current_score"] = 0
    return out
