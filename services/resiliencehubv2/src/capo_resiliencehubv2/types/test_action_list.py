"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_action

TestActionList: TypeAlias = list["capo_resiliencehubv2.types.test_action.TestAction"]


# --- restJson1 ser/de ---
def serialize_json(value: TestActionList) -> list:
    import capo_resiliencehubv2.types.test_action

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.test_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestActionList:
    import capo_resiliencehubv2.types.test_action

    out: TestActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resiliencehubv2.types.test_action.deserialize_json(item))
    return out
