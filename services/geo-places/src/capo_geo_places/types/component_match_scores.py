"""Generated from Smithy shape ``com.amazonaws.geoplaces#ComponentMatchScores``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.address_component_match_scores
    import capo_geo_places.types.match_score


class ComponentMatchScores(TypedDict, closed=True):
    title: "capo_geo_places.types.match_score.MatchScore"
    """<p>Indicates the match score of the title in the text query that match the found title. </p>"""
    address: NotRequired[
        "capo_geo_places.types.address_component_match_scores.AddressComponentMatchScores"
    ]
    """<p>The place's address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentMatchScores) -> dict:
    out: dict = {}
    out["Title"] = (
        "NaN"
        if value.get("title", 0) != value.get("title", 0)
        else "Infinity"
        if value.get("title", 0) == float("inf")
        else "-Infinity"
        if value.get("title", 0) == float("-inf")
        else value.get("title", 0)
    )
    if "address" in value:
        import capo_geo_places.types.address_component_match_scores

        out["Address"] = (
            capo_geo_places.types.address_component_match_scores.serialize_json(
                value["address"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentMatchScores:
    out: ComponentMatchScores = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = float(data["Title"])
    else:
        out["title"] = 0
    if data.get("Address") is not None:
        import capo_geo_places.types.address_component_match_scores

        out["address"] = (
            capo_geo_places.types.address_component_match_scores.deserialize_json(
                data["Address"]
            )
        )
    return out
