"""Generated from Smithy shape ``com.amazonaws.connect#RulesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.behavior


class RulesConfiguration(TypedDict, closed=True):
    behavior: NotRequired["capo_connect.types.behavior.Behavior"]
    """<p>Controls whether Contact Lens rules are evaluated for the contact. Valid values: <code>Enable</code> | <code>Disable</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RulesConfiguration) -> dict:
    out: dict = {}
    if "behavior" in value:
        import capo_connect.types.behavior

        out["Behavior"] = capo_connect.types.behavior.serialize_json(value["behavior"])
    return out


def deserialize_json(data: dict) -> RulesConfiguration:
    out: RulesConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Behavior") is not None:
        import capo_connect.types.behavior

        out["behavior"] = capo_connect.types.behavior.deserialize_json(data["Behavior"])
    return out
