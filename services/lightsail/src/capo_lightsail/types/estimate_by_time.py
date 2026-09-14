"""Generated from Smithy shape ``com.amazonaws.lightsail#EstimateByTime``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.currency
    import capo_lightsail.types.double
    import capo_lightsail.types.pricing_unit
    import capo_lightsail.types.time_period


class EstimateByTime(TypedDict, closed=True):
    usage_cost: NotRequired["capo_lightsail.types.double.double"]
    """<p>The amount of cost or usage that's measured for the cost estimate.</p>"""
    pricing_unit: NotRequired["capo_lightsail.types.pricing_unit.PricingUnit"]
    """<p>The unit of measurement that's used for the cost estimate.</p>"""
    unit: NotRequired["capo_lightsail.types.double.double"]
    """<p>The number of pricing units used to calculate the total number of hours. For example, 1 unit equals 1 hour.</p>"""
    currency: NotRequired["capo_lightsail.types.currency.Currency"]
    """<p>The currency of the estimate in USD.</p>"""
    time_period: NotRequired["capo_lightsail.types.time_period.TimePeriod"]
    """<p>The period of time, in days, that an estimate covers. The period has a start date and an end date. The start date must come before the end date.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EstimateByTime) -> dict:
    out: dict = {}
    if "usage_cost" in value:
        out["usageCost"] = (
            "NaN"
            if value["usage_cost"] != value["usage_cost"]
            else "Infinity"
            if value["usage_cost"] == float("inf")
            else "-Infinity"
            if value["usage_cost"] == float("-inf")
            else value["usage_cost"]
        )
    if "pricing_unit" in value:
        import capo_lightsail.types.pricing_unit

        out["pricingUnit"] = capo_lightsail.types.pricing_unit.serialize_aws_json_1_1(
            value["pricing_unit"]
        )
    if "unit" in value:
        out["unit"] = (
            "NaN"
            if value["unit"] != value["unit"]
            else "Infinity"
            if value["unit"] == float("inf")
            else "-Infinity"
            if value["unit"] == float("-inf")
            else value["unit"]
        )
    if "currency" in value:
        import capo_lightsail.types.currency

        out["currency"] = capo_lightsail.types.currency.serialize_aws_json_1_1(
            value["currency"]
        )
    if "time_period" in value:
        import capo_lightsail.types.time_period

        out["timePeriod"] = capo_lightsail.types.time_period.serialize_aws_json_1_1(
            value["time_period"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EstimateByTime:
    out: EstimateByTime = {}  # type: ignore[typeddict-item]
    if data.get("usageCost") is not None:
        out["usage_cost"] = float(data["usageCost"])
    if data.get("pricingUnit") is not None:
        import capo_lightsail.types.pricing_unit

        out["pricing_unit"] = (
            capo_lightsail.types.pricing_unit.deserialize_aws_json_1_1(
                data["pricingUnit"]
            )
        )
    if data.get("unit") is not None:
        out["unit"] = float(data["unit"])
    if data.get("currency") is not None:
        import capo_lightsail.types.currency

        out["currency"] = capo_lightsail.types.currency.deserialize_aws_json_1_1(
            data["currency"]
        )
    if data.get("timePeriod") is not None:
        import capo_lightsail.types.time_period

        out["time_period"] = capo_lightsail.types.time_period.deserialize_aws_json_1_1(
            data["timePeriod"]
        )
    return out
