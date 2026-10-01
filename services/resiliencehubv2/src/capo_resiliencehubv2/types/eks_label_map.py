"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EksLabelMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.eks_label_key
    import capo_resiliencehubv2.types.eks_label_value

EksLabelMap: TypeAlias = dict[
    "capo_resiliencehubv2.types.eks_label_key.EksLabelKey",
    "capo_resiliencehubv2.types.eks_label_value.EksLabelValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EksLabelMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EksLabelMap:
    out: EksLabelMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
