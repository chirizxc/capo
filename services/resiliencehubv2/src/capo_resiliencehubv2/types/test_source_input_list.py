"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSourceInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_source_input

TestSourceInputList: TypeAlias = list[
    "capo_resiliencehubv2.types.test_source_input.TestSourceInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSourceInputList) -> list:
    import capo_resiliencehubv2.types.test_source_input

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.test_source_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestSourceInputList:
    import capo_resiliencehubv2.types.test_source_input

    out: TestSourceInputList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resiliencehubv2.types.test_source_input.deserialize_json(item))
    return out
