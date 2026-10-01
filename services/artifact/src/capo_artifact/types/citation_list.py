"""Generated from Smithy shape ``com.amazonaws.artifact#CitationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_artifact.types.citation

CitationList: TypeAlias = list["capo_artifact.types.citation.Citation"]


# --- restJson1 ser/de ---
def serialize_json(value: CitationList) -> list:
    import capo_artifact.types.citation

    out: list = []
    for item in value:
        out.append(capo_artifact.types.citation.serialize_json(item))
    return out


def deserialize_json(data: list) -> CitationList:
    import capo_artifact.types.citation

    out: CitationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_artifact.types.citation.deserialize_json(item))
    return out
