"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_run_summary

TestRunSummaryList: TypeAlias = list[
    "capo_resiliencehubv2.types.test_run_summary.TestRunSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSummaryList) -> list:
    import capo_resiliencehubv2.types.test_run_summary

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.test_run_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestRunSummaryList:
    import capo_resiliencehubv2.types.test_run_summary

    out: TestRunSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resiliencehubv2.types.test_run_summary.deserialize_json(item))
    return out
