"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DiversityColumnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.diversity_column

DiversityColumnsList: TypeAlias = list[
    "capo_customer_profiles.types.diversity_column.DiversityColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: DiversityColumnsList) -> list:
    import capo_customer_profiles.types.diversity_column

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.diversity_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> DiversityColumnsList:
    import capo_customer_profiles.types.diversity_column

    out: DiversityColumnsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_customer_profiles.types.diversity_column.deserialize_json(item))
    return out
