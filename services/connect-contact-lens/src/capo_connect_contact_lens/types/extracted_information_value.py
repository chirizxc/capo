"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#ExtractedInformationValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.extracted_information_content
    import capo_connect_contact_lens.types.points_of_interest


class ExtractedInformationValue(TypedDict, closed=True):
    content: NotRequired[
        "capo_connect_contact_lens.types.extracted_information_content.ExtractedInformationContent"
    ]
    """<p>The text content of the extracted value.</p>"""
    points_of_interest: NotRequired[
        "capo_connect_contact_lens.types.points_of_interest.PointsOfInterest"
    ]
    """<p>The sections in the conversation that indicate where the extracted value was found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractedInformationValue) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    if "points_of_interest" in value:
        import capo_connect_contact_lens.types.points_of_interest

        out["PointsOfInterest"] = (
            capo_connect_contact_lens.types.points_of_interest.serialize_json(
                value["points_of_interest"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExtractedInformationValue:
    out: ExtractedInformationValue = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("PointsOfInterest") is not None:
        import capo_connect_contact_lens.types.points_of_interest

        out["points_of_interest"] = (
            capo_connect_contact_lens.types.points_of_interest.deserialize_json(
                data["PointsOfInterest"]
            )
        )
    return out
