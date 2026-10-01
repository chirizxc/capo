"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#TermTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.term_template

TermTemplateList: TypeAlias = list[
    "capo_marketplace_discovery.types.term_template.TermTemplate"
]


# --- restJson1 ser/de ---
def serialize_json(value: TermTemplateList) -> list:
    import capo_marketplace_discovery.types.term_template

    out: list = []
    for item in value:
        out.append(capo_marketplace_discovery.types.term_template.serialize_json(item))
    return out


def deserialize_json(data: list) -> TermTemplateList:
    import capo_marketplace_discovery.types.term_template

    out: TermTemplateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_discovery.types.term_template.deserialize_json(item)
        )
    return out
