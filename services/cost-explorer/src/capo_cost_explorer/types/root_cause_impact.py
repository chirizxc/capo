"""Generated from Smithy shape ``com.amazonaws.costexplorer#RootCauseImpact``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_double


class RootCauseImpact(TypedDict, closed=True):
    contribution: "capo_cost_explorer.types.generic_double.GenericDouble"
    """<p>The dollar amount that this root cause contributed to the anomaly's TotalImpact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RootCauseImpact) -> dict:
    out: dict = {}
    out["Contribution"] = (
        "NaN"
        if value.get("contribution", 0) != value.get("contribution", 0)
        else "Infinity"
        if value.get("contribution", 0) == float("inf")
        else "-Infinity"
        if value.get("contribution", 0) == float("-inf")
        else value.get("contribution", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RootCauseImpact:
    out: RootCauseImpact = {}  # type: ignore[typeddict-item]
    if data.get("Contribution") is not None:
        out["contribution"] = float(data["Contribution"])
    else:
        out["contribution"] = 0
    return out
