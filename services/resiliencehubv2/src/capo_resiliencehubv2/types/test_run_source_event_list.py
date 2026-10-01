"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSourceEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_run_source_event

TestRunSourceEventList: TypeAlias = list[
    "capo_resiliencehubv2.types.test_run_source_event.TestRunSourceEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSourceEventList) -> list:
    import capo_resiliencehubv2.types.test_run_source_event

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehubv2.types.test_run_source_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TestRunSourceEventList:
    import capo_resiliencehubv2.types.test_run_source_event

    out: TestRunSourceEventList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resiliencehubv2.types.test_run_source_event.deserialize_json(item)
        )
    return out
