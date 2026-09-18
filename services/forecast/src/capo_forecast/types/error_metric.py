"""Generated from Smithy shape ``com.amazonaws.forecast#ErrorMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.double
    import capo_forecast.types.forecast_type


class ErrorMetric(TypedDict, closed=True):
    forecast_type: NotRequired["capo_forecast.types.forecast_type.ForecastType"]
    """<p> The Forecast type used to compute WAPE, MAPE, MASE, and RMSE. </p>"""
    wape: NotRequired["capo_forecast.types.double.Double"]
    """<p> The weighted absolute percentage error (WAPE). </p>"""
    rmse: NotRequired["capo_forecast.types.double.Double"]
    """<p> The root-mean-square error (RMSE). </p>"""
    mase: NotRequired["capo_forecast.types.double.Double"]
    """<p>The Mean Absolute Scaled Error (MASE)</p>"""
    mape: NotRequired["capo_forecast.types.double.Double"]
    """<p>The Mean Absolute Percentage Error (MAPE)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorMetric) -> dict:
    out: dict = {}
    if "forecast_type" in value:
        out["ForecastType"] = value["forecast_type"]
    if "wape" in value:
        out["WAPE"] = (
            "NaN"
            if value["wape"] != value["wape"]
            else "Infinity"
            if value["wape"] == float("inf")
            else "-Infinity"
            if value["wape"] == float("-inf")
            else value["wape"]
        )
    if "rmse" in value:
        out["RMSE"] = (
            "NaN"
            if value["rmse"] != value["rmse"]
            else "Infinity"
            if value["rmse"] == float("inf")
            else "-Infinity"
            if value["rmse"] == float("-inf")
            else value["rmse"]
        )
    if "mase" in value:
        out["MASE"] = (
            "NaN"
            if value["mase"] != value["mase"]
            else "Infinity"
            if value["mase"] == float("inf")
            else "-Infinity"
            if value["mase"] == float("-inf")
            else value["mase"]
        )
    if "mape" in value:
        out["MAPE"] = (
            "NaN"
            if value["mape"] != value["mape"]
            else "Infinity"
            if value["mape"] == float("inf")
            else "-Infinity"
            if value["mape"] == float("-inf")
            else value["mape"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorMetric:
    out: ErrorMetric = {}  # type: ignore[typeddict-item]
    if data.get("ForecastType") is not None:
        out["forecast_type"] = data["ForecastType"]
    if data.get("WAPE") is not None:
        out["wape"] = float(data["WAPE"])
    if data.get("RMSE") is not None:
        out["rmse"] = float(data["RMSE"])
    if data.get("MASE") is not None:
        out["mase"] = float(data["MASE"])
    if data.get("MAPE") is not None:
        out["mape"] = float(data["MAPE"])
    return out
