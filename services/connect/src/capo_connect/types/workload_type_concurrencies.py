"""Generated from Smithy shape ``com.amazonaws.connect#WorkloadTypeConcurrencies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.workload_type_concurrency

WorkloadTypeConcurrencies: TypeAlias = list[
    "capo_connect.types.workload_type_concurrency.WorkloadTypeConcurrency"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadTypeConcurrencies) -> list:
    import capo_connect.types.workload_type_concurrency

    out: list = []
    for item in value:
        out.append(capo_connect.types.workload_type_concurrency.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkloadTypeConcurrencies:
    import capo_connect.types.workload_type_concurrency

    out: WorkloadTypeConcurrencies = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.workload_type_concurrency.deserialize_json(item))
    return out
