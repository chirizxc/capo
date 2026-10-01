"""Generated from Smithy shape ``com.amazonaws.quicksight#UserLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.effective_limit_list


class UserLimits(TypedDict, closed=True):
    user_name: "str"
    """<p>The name of the user.</p>"""
    namespace: "str"
    """<p>The namespace of the user.</p>"""
    effective_limits: "capo_quicksight.types.effective_limit_list.EffectiveLimitList"
    """<p>A list of effective limits for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserLimits) -> dict:
    out: dict = {}
    out["userName"] = value["user_name"]
    out["namespace"] = value["namespace"]
    import capo_quicksight.types.effective_limit_list

    out["effectiveLimits"] = capo_quicksight.types.effective_limit_list.serialize_json(
        value["effective_limits"]
    )
    return out


def deserialize_json(data: dict) -> UserLimits:
    out: UserLimits = {}  # type: ignore[typeddict-item]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    else:
        raise DeserializationError("UserLimits.user_name required")
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("UserLimits.namespace required")
    if data.get("effectiveLimits") is not None:
        import capo_quicksight.types.effective_limit_list

        out["effective_limits"] = (
            capo_quicksight.types.effective_limit_list.deserialize_json(
                data["effectiveLimits"]
            )
        )
    else:
        raise DeserializationError("UserLimits.effective_limits required")
    return out
