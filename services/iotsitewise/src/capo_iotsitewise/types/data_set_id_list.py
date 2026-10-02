"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DataSetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_id

DataSetIdList: TypeAlias = list["capo_iotsitewise.types.dataset_id.DatasetId"]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> DataSetIdList:
    return [item for item in data if item is not None]
