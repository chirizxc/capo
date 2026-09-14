"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ViewOffNadirInput``."""

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError


class ViewOffNadirInput(TypedDict, closed=True):
    lower_bound: "float"
    """<p>The minimum value for ViewOffNadir property filter. This filters items having ViewOffNadir greater than or equal to this value. </p>"""
    upper_bound: "float"
    """<p>The maximum value for ViewOffNadir property filter. This filters items having ViewOffNadir lesser than or equal to this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewOffNadirInput) -> dict:
    out: dict = {}
    out["LowerBound"] = (
        "NaN"
        if value["lower_bound"] != value["lower_bound"]
        else "Infinity"
        if value["lower_bound"] == float("inf")
        else "-Infinity"
        if value["lower_bound"] == float("-inf")
        else value["lower_bound"]
    )
    out["UpperBound"] = (
        "NaN"
        if value["upper_bound"] != value["upper_bound"]
        else "Infinity"
        if value["upper_bound"] == float("inf")
        else "-Infinity"
        if value["upper_bound"] == float("-inf")
        else value["upper_bound"]
    )
    return out


def deserialize_json(data: dict) -> ViewOffNadirInput:
    out: ViewOffNadirInput = {}  # type: ignore[typeddict-item]
    if data.get("LowerBound") is not None:
        out["lower_bound"] = float(data["LowerBound"])
    else:
        raise DeserializationError("ViewOffNadirInput.lower_bound required")
    if data.get("UpperBound") is not None:
        out["upper_bound"] = float(data["UpperBound"])
    else:
        raise DeserializationError("ViewOffNadirInput.upper_bound required")
    return out
