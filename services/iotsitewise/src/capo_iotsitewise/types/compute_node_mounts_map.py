"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNodeMountsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.mount_list
    import capo_iotsitewise.types.resource_name

ComputeNodeMountsMap: TypeAlias = dict[
    "capo_iotsitewise.types.resource_name.ResourceName",
    "capo_iotsitewise.types.mount_list.MountList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComputeNodeMountsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iotsitewise.types.mount_list

        out[key] = capo_iotsitewise.types.mount_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ComputeNodeMountsMap:
    out: ComputeNodeMountsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_iotsitewise.types.mount_list

        out[key] = capo_iotsitewise.types.mount_list.deserialize_json(value)
    return out
