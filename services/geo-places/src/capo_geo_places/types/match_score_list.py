"""Generated from Smithy shape ``com.amazonaws.geoplaces#MatchScoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.match_score

MatchScoreList: TypeAlias = list["capo_geo_places.types.match_score.MatchScore"]


# --- restJson1 ser/de ---
def serialize_json(value: MatchScoreList) -> list:
    return [
        (
            "NaN"
            if item != item
            else "Infinity"
            if item == float("inf")
            else "-Infinity"
            if item == float("-inf")
            else item
        )
        for item in value
    ]


def deserialize_json(data: list) -> MatchScoreList:
    return [float(item) for item in data if item is not None]
