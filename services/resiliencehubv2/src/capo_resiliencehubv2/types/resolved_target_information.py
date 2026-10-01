"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResolvedTargetInformation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.resolved_target_information_key
    import capo_resiliencehubv2.types.resolved_target_information_value

ResolvedTargetInformation: TypeAlias = dict[
    "capo_resiliencehubv2.types.resolved_target_information_key.ResolvedTargetInformationKey",
    "capo_resiliencehubv2.types.resolved_target_information_value.ResolvedTargetInformationValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResolvedTargetInformation) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ResolvedTargetInformation:
    out: ResolvedTargetInformation = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
