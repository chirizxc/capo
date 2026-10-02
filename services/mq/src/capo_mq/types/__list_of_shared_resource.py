"""Generated from Smithy shape ``com.amazonaws.mq#__listOfSharedResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mq.types.shared_resource

__listOfSharedResource: TypeAlias = list["capo_mq.types.shared_resource.SharedResource"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSharedResource) -> list:
    import capo_mq.types.shared_resource

    out: list = []
    for item in value:
        out.append(capo_mq.types.shared_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSharedResource:
    import capo_mq.types.shared_resource

    out: __listOfSharedResource = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mq.types.shared_resource.deserialize_json(item))
    return out
