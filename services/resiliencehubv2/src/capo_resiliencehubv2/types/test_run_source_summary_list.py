"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_run_source_summary

TestRunSourceSummaryList: TypeAlias = list[
    "capo_resiliencehubv2.types.test_run_source_summary.TestRunSourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSourceSummaryList) -> list:
    import capo_resiliencehubv2.types.test_run_source_summary

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehubv2.types.test_run_source_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TestRunSourceSummaryList:
    import capo_resiliencehubv2.types.test_run_source_summary

    out: TestRunSourceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resiliencehubv2.types.test_run_source_summary.deserialize_json(item)
        )
    return out
