"""Generated from Smithy shape ``com.amazonaws.xray#SamplingStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.nullable_double
    import capo_xray.types.sampling_strategy_name


class SamplingStrategy(TypedDict, closed=True):
    name: NotRequired["capo_xray.types.sampling_strategy_name.SamplingStrategyName"]
    """<p>The name of a sampling rule.</p>"""
    value: NotRequired["capo_xray.types.nullable_double.NullableDouble"]
    """<p>The value of a sampling rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingStrategy) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_xray.types.sampling_strategy_name

        out["Name"] = capo_xray.types.sampling_strategy_name.serialize_json(
            value["name"]
        )
    if "value" in value:
        out["Value"] = (
            "NaN"
            if value["value"] != value["value"]
            else "Infinity"
            if value["value"] == float("inf")
            else "-Infinity"
            if value["value"] == float("-inf")
            else value["value"]
        )
    return out


def deserialize_json(data: dict) -> SamplingStrategy:
    out: SamplingStrategy = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_xray.types.sampling_strategy_name

        out["name"] = capo_xray.types.sampling_strategy_name.deserialize_json(
            data["Name"]
        )
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    return out
