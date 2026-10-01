"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EksLabelValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.eks_label_value

EksLabelValueList: TypeAlias = list[
    "capo_resiliencehubv2.types.eks_label_value.EksLabelValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksLabelValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> EksLabelValueList:
    return [item for item in data if item is not None]
