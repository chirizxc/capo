"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#ExtractedInformationValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.extracted_information_value

ExtractedInformationValues: TypeAlias = list[
    "capo_connect_contact_lens.types.extracted_information_value.ExtractedInformationValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtractedInformationValues) -> list:
    import capo_connect_contact_lens.types.extracted_information_value

    out: list = []
    for item in value:
        out.append(
            capo_connect_contact_lens.types.extracted_information_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ExtractedInformationValues:
    import capo_connect_contact_lens.types.extracted_information_value

    out: ExtractedInformationValues = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect_contact_lens.types.extracted_information_value.deserialize_json(
                item
            )
        )
    return out
