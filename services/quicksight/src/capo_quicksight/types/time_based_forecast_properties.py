"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeBasedForecastProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.periods_backward
    import capo_quicksight.types.periods_forward
    import capo_quicksight.types.prediction_interval
    import capo_quicksight.types.seasonality


class TimeBasedForecastProperties(TypedDict, closed=True):
    periods_forward: NotRequired["capo_quicksight.types.periods_forward.PeriodsForward"]
    """<p>The periods forward setup of a forecast computation.</p>"""
    periods_backward: NotRequired[
        "capo_quicksight.types.periods_backward.PeriodsBackward"
    ]
    """<p>The periods backward setup of a forecast computation.</p>"""
    upper_boundary: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The upper boundary setup of a forecast computation.</p>"""
    lower_boundary: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The lower boundary setup of a forecast computation.</p>"""
    prediction_interval: NotRequired[
        "capo_quicksight.types.prediction_interval.PredictionInterval"
    ]
    """<p>The prediction interval setup of a forecast computation.</p>"""
    seasonality: NotRequired["capo_quicksight.types.seasonality.Seasonality"]
    """<p>The seasonality setup of a forecast computation. Choose one of the following options:</p> <ul> <li> <p> <code>NULL</code>: The input is set to <code>NULL</code>.</p> </li> <li> <p> <code>NON_NULL</code>: The input is set to a custom value.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeBasedForecastProperties) -> dict:
    out: dict = {}
    if "periods_forward" in value:
        out["PeriodsForward"] = value["periods_forward"]
    if "periods_backward" in value:
        out["PeriodsBackward"] = value["periods_backward"]
    if "upper_boundary" in value:
        out["UpperBoundary"] = (
            "NaN"
            if value["upper_boundary"] != value["upper_boundary"]
            else "Infinity"
            if value["upper_boundary"] == float("inf")
            else "-Infinity"
            if value["upper_boundary"] == float("-inf")
            else value["upper_boundary"]
        )
    if "lower_boundary" in value:
        out["LowerBoundary"] = (
            "NaN"
            if value["lower_boundary"] != value["lower_boundary"]
            else "Infinity"
            if value["lower_boundary"] == float("inf")
            else "-Infinity"
            if value["lower_boundary"] == float("-inf")
            else value["lower_boundary"]
        )
    if "prediction_interval" in value:
        out["PredictionInterval"] = value["prediction_interval"]
    if "seasonality" in value:
        out["Seasonality"] = value["seasonality"]
    return out


def deserialize_json(data: dict) -> TimeBasedForecastProperties:
    out: TimeBasedForecastProperties = {}  # type: ignore[typeddict-item]
    if data.get("PeriodsForward") is not None:
        out["periods_forward"] = data["PeriodsForward"]
    if data.get("PeriodsBackward") is not None:
        out["periods_backward"] = data["PeriodsBackward"]
    if data.get("UpperBoundary") is not None:
        out["upper_boundary"] = float(data["UpperBoundary"])
    if data.get("LowerBoundary") is not None:
        out["lower_boundary"] = float(data["LowerBoundary"])
    if data.get("PredictionInterval") is not None:
        out["prediction_interval"] = data["PredictionInterval"]
    if data.get("Seasonality") is not None:
        out["seasonality"] = data["Seasonality"]
    return out
