"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_run_event

TestRunEventList: TypeAlias = list[
    "capo_resiliencehubv2.types.test_run_event.TestRunEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRunEventList) -> list:
    import capo_resiliencehubv2.types.test_run_event

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.test_run_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestRunEventList:
    import capo_resiliencehubv2.types.test_run_event

    out: TestRunEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resiliencehubv2.types.test_run_event.deserialize_json(item))
    return out
