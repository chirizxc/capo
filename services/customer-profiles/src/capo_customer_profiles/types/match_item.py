"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MatchItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.double
    import capo_customer_profiles.types.profile_id_list
    import capo_customer_profiles.types.string1_to255


class MatchItem(TypedDict, closed=True):
    match_id: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The unique identifiers for this group of profiles that match.</p>"""
    profile_ids: NotRequired[
        "capo_customer_profiles.types.profile_id_list.ProfileIdList"
    ]
    """<p>A list of identifiers for profiles that match.</p>"""
    confidence_score: NotRequired["capo_customer_profiles.types.double.Double"]
    """<p>A number between 0 and 1, where a higher score means higher similarity. Examining match confidence scores lets you distinguish between groups of similar records in which the system is highly confident (which you may decide to merge), groups of similar records about which the system is uncertain (which you may decide to have reviewed by a human), and groups of similar records that the system deems to be unlikely (which you may decide to reject). Given confidence scores vary as per the data input, it should not be used an absolute measure of matching quality.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchItem) -> dict:
    out: dict = {}
    if "match_id" in value:
        out["MatchId"] = value["match_id"]
    if "profile_ids" in value:
        import capo_customer_profiles.types.profile_id_list

        out["ProfileIds"] = capo_customer_profiles.types.profile_id_list.serialize_json(
            value["profile_ids"]
        )
    if "confidence_score" in value:
        out["ConfidenceScore"] = (
            "NaN"
            if value["confidence_score"] != value["confidence_score"]
            else "Infinity"
            if value["confidence_score"] == float("inf")
            else "-Infinity"
            if value["confidence_score"] == float("-inf")
            else value["confidence_score"]
        )
    return out


def deserialize_json(data: dict) -> MatchItem:
    out: MatchItem = {}  # type: ignore[typeddict-item]
    if data.get("MatchId") is not None:
        out["match_id"] = data["MatchId"]
    if data.get("ProfileIds") is not None:
        import capo_customer_profiles.types.profile_id_list

        out["profile_ids"] = (
            capo_customer_profiles.types.profile_id_list.deserialize_json(
                data["ProfileIds"]
            )
        )
    if data.get("ConfidenceScore") is not None:
        out["confidence_score"] = float(data["ConfidenceScore"])
    return out
