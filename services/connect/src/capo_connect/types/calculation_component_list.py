"""Generated from Smithy shape ``com.amazonaws.connect#CalculationComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.calculation_component

CalculationComponentList: TypeAlias = list[
    "capo_connect.types.calculation_component.CalculationComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculationComponentList) -> list:
    import capo_connect.types.calculation_component

    out: list = []
    for item in value:
        out.append(capo_connect.types.calculation_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> CalculationComponentList:
    import capo_connect.types.calculation_component

    out: CalculationComponentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.calculation_component.deserialize_json(item))
    return out
