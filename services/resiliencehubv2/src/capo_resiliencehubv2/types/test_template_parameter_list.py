"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestTemplateParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_template_parameter

TestTemplateParameterList: TypeAlias = list[
    "capo_resiliencehubv2.types.test_template_parameter.TestTemplateParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestTemplateParameterList) -> list:
    import capo_resiliencehubv2.types.test_template_parameter

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehubv2.types.test_template_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TestTemplateParameterList:
    import capo_resiliencehubv2.types.test_template_parameter

    out: TestTemplateParameterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resiliencehubv2.types.test_template_parameter.deserialize_json(item)
        )
    return out
