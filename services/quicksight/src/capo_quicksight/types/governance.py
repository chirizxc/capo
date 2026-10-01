"""Generated from Smithy shape ``com.amazonaws.quicksight#Governance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.default_category_effects_map


class Governance(TypedDict, closed=True):
    default_category_effects: NotRequired[
        "capo_quicksight.types.default_category_effects_map.DefaultCategoryEffectsMap"
    ]
    """<p>A map of <code>DefaultCategoryEffects</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Governance) -> dict:
    out: dict = {}
    if "default_category_effects" in value:
        import capo_quicksight.types.default_category_effects_map

        out["DefaultCategoryEffects"] = (
            capo_quicksight.types.default_category_effects_map.serialize_json(
                value["default_category_effects"]
            )
        )
    return out


def deserialize_json(data: dict) -> Governance:
    out: Governance = {}  # type: ignore[typeddict-item]
    if data.get("DefaultCategoryEffects") is not None:
        import capo_quicksight.types.default_category_effects_map

        out["default_category_effects"] = (
            capo_quicksight.types.default_category_effects_map.deserialize_json(
                data["DefaultCategoryEffects"]
            )
        )
    return out
