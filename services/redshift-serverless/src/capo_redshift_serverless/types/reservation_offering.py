"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ReservationOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.charge
    import capo_redshift_serverless.types.currency_code
    import capo_redshift_serverless.types.duration
    import capo_redshift_serverless.types.offering_id
    import capo_redshift_serverless.types.offering_type


class ReservationOffering(TypedDict, closed=True):
    offering_id: NotRequired["capo_redshift_serverless.types.offering_id.OfferingId"]
    """<p>The offering identifier.</p>"""
    duration: "capo_redshift_serverless.types.duration.Duration"
    """<p>The duration, in seconds, for which the reservation reserves the RPUs.</p>"""
    upfront_charge: "capo_redshift_serverless.types.charge.Charge"
    """<p>The up-front price you are charged for the reservation.</p>"""
    hourly_charge: "capo_redshift_serverless.types.charge.Charge"
    """<p>The rate you are charged for each hour the reservation is active.</p>"""
    currency_code: NotRequired[
        "capo_redshift_serverless.types.currency_code.CurrencyCode"
    ]
    """<p>The currency code for the offering.</p>"""
    offering_type: NotRequired[
        "capo_redshift_serverless.types.offering_type.OfferingType"
    ]
    """<p>Determines the payment schedule for the reservation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationOffering) -> dict:
    out: dict = {}
    if "offering_id" in value:
        out["offeringId"] = value["offering_id"]
    out["duration"] = value.get("duration", 0)
    out["upfrontCharge"] = (
        "NaN"
        if value.get("upfront_charge", 0) != value.get("upfront_charge", 0)
        else "Infinity"
        if value.get("upfront_charge", 0) == float("inf")
        else "-Infinity"
        if value.get("upfront_charge", 0) == float("-inf")
        else value.get("upfront_charge", 0)
    )
    out["hourlyCharge"] = (
        "NaN"
        if value.get("hourly_charge", 0) != value.get("hourly_charge", 0)
        else "Infinity"
        if value.get("hourly_charge", 0) == float("inf")
        else "-Infinity"
        if value.get("hourly_charge", 0) == float("-inf")
        else value.get("hourly_charge", 0)
    )
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "offering_type" in value:
        out["offeringType"] = value["offering_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservationOffering:
    out: ReservationOffering = {}  # type: ignore[typeddict-item]
    if data.get("offeringId") is not None:
        out["offering_id"] = data["offeringId"]
    if data.get("duration") is not None:
        out["duration"] = data["duration"]
    else:
        out["duration"] = 0
    if data.get("upfrontCharge") is not None:
        out["upfront_charge"] = float(data["upfrontCharge"])
    else:
        out["upfront_charge"] = 0
    if data.get("hourlyCharge") is not None:
        out["hourly_charge"] = float(data["hourlyCharge"])
    else:
        out["hourly_charge"] = 0
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("offeringType") is not None:
        out["offering_type"] = data["offeringType"]
    return out
