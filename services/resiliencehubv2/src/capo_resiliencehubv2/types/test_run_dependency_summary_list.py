"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunDependencySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_run_dependency_summary

TestRunDependencySummaryList: TypeAlias = list[
    "capo_resiliencehubv2.types.test_run_dependency_summary.TestRunDependencySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRunDependencySummaryList) -> list:
    import capo_resiliencehubv2.types.test_run_dependency_summary

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehubv2.types.test_run_dependency_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TestRunDependencySummaryList:
    import capo_resiliencehubv2.types.test_run_dependency_summary

    out: TestRunDependencySummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resiliencehubv2.types.test_run_dependency_summary.deserialize_json(
                item
            )
        )
    return out
