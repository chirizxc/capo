"""Generated from Smithy shape ``com.amazonaws.eks#Taint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.taint_effect
    import capo_eks.types.taint_key
    import capo_eks.types.taint_value


class Taint(TypedDict, closed=True):
    key: NotRequired["capo_eks.types.taint_key.taintKey"]
    """<p>The key of the taint.</p>"""
    value: NotRequired["capo_eks.types.taint_value.taintValue"]
    """<p>The value of the taint.</p>"""
    effect: NotRequired["capo_eks.types.taint_effect.TaintEffect"]
    """<p>The effect of the taint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Taint) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    if "effect" in value:
        import capo_eks.types.taint_effect

        out["effect"] = capo_eks.types.taint_effect.serialize_json(value["effect"])
    return out


def deserialize_json(data: dict) -> Taint:
    out: Taint = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("effect") is not None:
        import capo_eks.types.taint_effect

        out["effect"] = capo_eks.types.taint_effect.deserialize_json(data["effect"])
    return out
