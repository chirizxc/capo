"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ControlAssessmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.control_assessment

ControlAssessmentList: TypeAlias = list[
    "capo_marketplace_catalog.types.control_assessment.ControlAssessment"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlAssessmentList) -> list:
    import capo_marketplace_catalog.types.control_assessment

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.control_assessment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ControlAssessmentList:
    import capo_marketplace_catalog.types.control_assessment

    out: ControlAssessmentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_catalog.types.control_assessment.deserialize_json(item)
        )
    return out
