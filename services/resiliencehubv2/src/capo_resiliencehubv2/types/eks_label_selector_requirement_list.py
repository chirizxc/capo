"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EksLabelSelectorRequirementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.eks_label_selector_requirement

EksLabelSelectorRequirementList: TypeAlias = list[
    "capo_resiliencehubv2.types.eks_label_selector_requirement.EksLabelSelectorRequirement"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksLabelSelectorRequirementList) -> list:
    import capo_resiliencehubv2.types.eks_label_selector_requirement

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehubv2.types.eks_label_selector_requirement.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EksLabelSelectorRequirementList:
    import capo_resiliencehubv2.types.eks_label_selector_requirement

    out: EksLabelSelectorRequirementList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resiliencehubv2.types.eks_label_selector_requirement.deserialize_json(
                item
            )
        )
    return out
