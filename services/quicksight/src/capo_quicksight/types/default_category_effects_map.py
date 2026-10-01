"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultCategoryEffectsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.default_category_effect
    import capo_quicksight.types.governance_category_name

DefaultCategoryEffectsMap: TypeAlias = dict[
    "capo_quicksight.types.governance_category_name.GovernanceCategoryName",
    "capo_quicksight.types.default_category_effect.DefaultCategoryEffect",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DefaultCategoryEffectsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.default_category_effect

        out[key] = capo_quicksight.types.default_category_effect.serialize_json(value)
    return out


def deserialize_json(data: dict) -> DefaultCategoryEffectsMap:
    out: DefaultCategoryEffectsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_quicksight.types.default_category_effect

        out[key] = capo_quicksight.types.default_category_effect.deserialize_json(value)
    return out
