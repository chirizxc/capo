"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AssociatedSegmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.associated_segment

AssociatedSegmentsList: TypeAlias = list[
    "capo_customer_profiles.types.associated_segment.AssociatedSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedSegmentsList) -> list:
    import capo_customer_profiles.types.associated_segment

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.associated_segment.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedSegmentsList:
    import capo_customer_profiles.types.associated_segment

    out: AssociatedSegmentsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_customer_profiles.types.associated_segment.deserialize_json(item)
        )
    return out
