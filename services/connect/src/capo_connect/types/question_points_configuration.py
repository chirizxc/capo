"""Generated from Smithy shape ``com.amazonaws.connect#QuestionPointsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.point_value


class QuestionPointsConfiguration(TypedDict, closed=True):
    max_point_value: "capo_connect.types.point_value.PointValue"
    """<p>The maximum point value.</p>"""
    min_point_value: "capo_connect.types.point_value.PointValue"
    """<p>The minimum point value.</p>"""
    is_bonus: "capo_connect.types.boolean.Boolean"
    """<p>The flag to mark the question as a bonus question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuestionPointsConfiguration) -> dict:
    out: dict = {}
    out["MaxPointValue"] = value.get("max_point_value", 0)
    out["MinPointValue"] = value.get("min_point_value", 0)
    out["IsBonus"] = value.get("is_bonus", False)
    return out


def deserialize_json(data: dict) -> QuestionPointsConfiguration:
    out: QuestionPointsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MaxPointValue") is not None:
        out["max_point_value"] = data["MaxPointValue"]
    else:
        out["max_point_value"] = 0
    if data.get("MinPointValue") is not None:
        out["min_point_value"] = data["MinPointValue"]
    else:
        out["min_point_value"] = 0
    if data.get("IsBonus") is not None:
        out["is_bonus"] = data["IsBonus"]
    else:
        out["is_bonus"] = False
    return out
