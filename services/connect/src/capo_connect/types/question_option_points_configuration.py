"""Generated from Smithy shape ``com.amazonaws.connect#QuestionOptionPointsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.point_value


class QuestionOptionPointsConfiguration(TypedDict, closed=True):
    point_value: "capo_connect.types.point_value.PointValue"
    """<p>The point value assigned to the answer option.</p>"""
    is_bonus: "capo_connect.types.boolean.Boolean"
    """<p>The flag to mark the option as a bonus option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuestionOptionPointsConfiguration) -> dict:
    out: dict = {}
    out["PointValue"] = value.get("point_value", 0)
    out["IsBonus"] = value.get("is_bonus", False)
    return out


def deserialize_json(data: dict) -> QuestionOptionPointsConfiguration:
    out: QuestionOptionPointsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PointValue") is not None:
        out["point_value"] = data["PointValue"]
    else:
        out["point_value"] = 0
    if data.get("IsBonus") is not None:
        out["is_bonus"] = data["IsBonus"]
    else:
        out["is_bonus"] = False
    return out
