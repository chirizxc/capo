"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisExtractedInformationValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_extracted_information_value

RealTimeContactAnalysisExtractedInformationValues: TypeAlias = list[
    "capo_connect.types.real_time_contact_analysis_extracted_information_value.RealTimeContactAnalysisExtractedInformationValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisExtractedInformationValues) -> list:
    import capo_connect.types.real_time_contact_analysis_extracted_information_value

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.real_time_contact_analysis_extracted_information_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RealTimeContactAnalysisExtractedInformationValues:
    import capo_connect.types.real_time_contact_analysis_extracted_information_value

    out: RealTimeContactAnalysisExtractedInformationValues = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.real_time_contact_analysis_extracted_information_value.deserialize_json(
                item
            )
        )
    return out
