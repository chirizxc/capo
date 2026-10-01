"""Generated from Smithy shape ``com.amazonaws.mq#__listOfResourceShareError``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mq.types.resource_share_error

__listOfResourceShareError: TypeAlias = list[
    "capo_mq.types.resource_share_error.ResourceShareError"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfResourceShareError) -> list:
    import capo_mq.types.resource_share_error

    out: list = []
    for item in value:
        out.append(capo_mq.types.resource_share_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfResourceShareError:
    import capo_mq.types.resource_share_error

    out: __listOfResourceShareError = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mq.types.resource_share_error.deserialize_json(item))
    return out
