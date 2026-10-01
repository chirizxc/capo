"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableComputeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.worker_compute_configuration


class _IntermediateTableComputeConfiguration_queryComputeConfiguration(
    TypedDict, closed=True
):
    queryComputeConfiguration: (
        "capo_cleanrooms.types.worker_compute_configuration.WorkerComputeConfiguration"
    )


IntermediateTableComputeConfiguration: TypeAlias = (
    _IntermediateTableComputeConfiguration_queryComputeConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableComputeConfiguration) -> dict:
    if "queryComputeConfiguration" in value:
        import capo_cleanrooms.types.worker_compute_configuration

        return {
            "queryComputeConfiguration": capo_cleanrooms.types.worker_compute_configuration.serialize_json(
                value["queryComputeConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "IntermediateTableComputeConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> IntermediateTableComputeConfiguration:
    if data.get("queryComputeConfiguration") is not None:
        import capo_cleanrooms.types.worker_compute_configuration

        return {
            "queryComputeConfiguration": capo_cleanrooms.types.worker_compute_configuration.deserialize_json(
                data["queryComputeConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "IntermediateTableComputeConfiguration: no recognized variant key"
        )
