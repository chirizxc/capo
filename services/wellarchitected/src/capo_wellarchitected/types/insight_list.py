"""Generated from Smithy shape ``com.amazonaws.wellarchitected#InsightList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.insight

InsightList: TypeAlias = list["capo_wellarchitected.types.insight.Insight"]


# --- restJson1 ser/de ---
def serialize_json(value: InsightList) -> list:
    import capo_wellarchitected.types.insight

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.insight.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightList:
    import capo_wellarchitected.types.insight

    out: InsightList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.insight.deserialize_json(item))
    return out
