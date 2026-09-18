"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ThemeValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.theme_value


class ThemeValues(TypedDict, closed=True):
    key: NotRequired["str"]
    """<p>The name of the property.</p>"""
    value: NotRequired["capo_amplifyuibuilder.types.theme_value.ThemeValue"]
    """<p>The value of the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThemeValues) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        import capo_amplifyuibuilder.types.theme_value

        out["value"] = capo_amplifyuibuilder.types.theme_value.serialize_json(
            value["value"]
        )
    return out


def deserialize_json(data: dict) -> ThemeValues:
    out: ThemeValues = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("value") is not None:
        import capo_amplifyuibuilder.types.theme_value

        out["value"] = capo_amplifyuibuilder.types.theme_value.deserialize_json(
            data["value"]
        )
    return out
