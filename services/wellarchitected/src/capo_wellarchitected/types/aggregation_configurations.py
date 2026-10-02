"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AggregationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.aggregation_configuration

AggregationConfigurations: TypeAlias = list[
    "capo_wellarchitected.types.aggregation_configuration.AggregationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationConfigurations) -> list:
    import capo_wellarchitected.types.aggregation_configuration

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.aggregation_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AggregationConfigurations:
    import capo_wellarchitected.types.aggregation_configuration

    out: AggregationConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.aggregation_configuration.deserialize_json(item)
        )
    return out
