"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InspectorScoreDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.cvss_score_details


class InspectorScoreDetails(TypedDict, closed=True):
    adjusted_cvss: NotRequired[
        "capo_imagebuilder.types.cvss_score_details.CvssScoreDetails"
    ]
    """<p>The CVSS score that Amazon Inspector assigned to the finding after applying its adjustments. It includes the score source, CVSS version, scoring vector, and the adjustments applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InspectorScoreDetails) -> dict:
    out: dict = {}
    if "adjusted_cvss" in value:
        import capo_imagebuilder.types.cvss_score_details

        out["adjustedCvss"] = capo_imagebuilder.types.cvss_score_details.serialize_json(
            value["adjusted_cvss"]
        )
    return out


def deserialize_json(data: dict) -> InspectorScoreDetails:
    out: InspectorScoreDetails = {}  # type: ignore[typeddict-item]
    if data.get("adjustedCvss") is not None:
        import capo_imagebuilder.types.cvss_score_details

        out["adjusted_cvss"] = (
            capo_imagebuilder.types.cvss_score_details.deserialize_json(
                data["adjustedCvss"]
            )
        )
    return out
