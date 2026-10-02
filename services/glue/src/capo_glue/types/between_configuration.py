"""Generated from Smithy shape ``com.amazonaws.glue#BetweenConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class BetweenConfiguration(TypedDict, closed=True):
    low_bound_key: NotRequired["str"]
    """<p>The parameter name used for the lower bound value in a BETWEEN filter operation.</p>"""
    high_bound_key: NotRequired["str"]
    """<p>The parameter name used for the upper bound value in a BETWEEN filter operation.</p>"""
    template: NotRequired["str"]
    """<p>A template string for constructing the BETWEEN filter expression.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BetweenConfiguration) -> dict:
    out: dict = {}
    if "low_bound_key" in value:
        out["LowBoundKey"] = value["low_bound_key"]
    if "high_bound_key" in value:
        out["HighBoundKey"] = value["high_bound_key"]
    if "template" in value:
        out["Template"] = value["template"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BetweenConfiguration:
    out: BetweenConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LowBoundKey") is not None:
        out["low_bound_key"] = data["LowBoundKey"]
    if data.get("HighBoundKey") is not None:
        out["high_bound_key"] = data["HighBoundKey"]
    if data.get("Template") is not None:
        out["template"] = data["Template"]
    return out
