"""Generated from Smithy shape ``com.amazonaws.elementalinference#TemplateGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.template_group

TemplateGroupList: TypeAlias = list[
    "capo_elementalinference.types.template_group.TemplateGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateGroupList) -> list:
    import capo_elementalinference.types.template_group

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.template_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> TemplateGroupList:
    import capo_elementalinference.types.template_group

    out: TemplateGroupList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_elementalinference.types.template_group.deserialize_json(item))
    return out
