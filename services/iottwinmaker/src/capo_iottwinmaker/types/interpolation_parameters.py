"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#InterpolationParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.interpolation_type
    import capo_iottwinmaker.types.interval_in_seconds


class InterpolationParameters(TypedDict, closed=True):
    interpolation_type: NotRequired[
        "capo_iottwinmaker.types.interpolation_type.InterpolationType"
    ]
    """<p>The interpolation type.</p>"""
    interval_in_seconds: NotRequired[
        "capo_iottwinmaker.types.interval_in_seconds.IntervalInSeconds"
    ]
    """<p>The interpolation time interval in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InterpolationParameters) -> dict:
    out: dict = {}
    if "interpolation_type" in value:
        out["interpolationType"] = value["interpolation_type"]
    if "interval_in_seconds" in value:
        out["intervalInSeconds"] = value["interval_in_seconds"]
    return out


def deserialize_json(data: dict) -> InterpolationParameters:
    out: InterpolationParameters = {}  # type: ignore[typeddict-item]
    if data.get("interpolationType") is not None:
        out["interpolation_type"] = data["interpolationType"]
    if data.get("intervalInSeconds") is not None:
        out["interval_in_seconds"] = data["intervalInSeconds"]
    return out
