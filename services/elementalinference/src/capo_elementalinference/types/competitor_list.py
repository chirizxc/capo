"""Generated from Smithy shape ``com.amazonaws.elementalinference#CompetitorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.competitor

CompetitorList: TypeAlias = list["capo_elementalinference.types.competitor.Competitor"]


# --- restJson1 ser/de ---
def serialize_json(value: CompetitorList) -> list:
    import capo_elementalinference.types.competitor

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.competitor.serialize_json(item))
    return out


def deserialize_json(data: list) -> CompetitorList:
    import capo_elementalinference.types.competitor

    out: CompetitorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_elementalinference.types.competitor.deserialize_json(item))
    return out
