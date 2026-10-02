"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_source_summary

TestSourceSummaryList: TypeAlias = list[
    "capo_resiliencehubv2.types.test_source_summary.TestSourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSourceSummaryList) -> list:
    import capo_resiliencehubv2.types.test_source_summary

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.test_source_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestSourceSummaryList:
    import capo_resiliencehubv2.types.test_source_summary

    out: TestSourceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resiliencehubv2.types.test_source_summary.deserialize_json(item)
        )
    return out
