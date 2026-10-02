"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_summary

TestSummaryList: TypeAlias = list["capo_resiliencehubv2.types.test_summary.TestSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: TestSummaryList) -> list:
    import capo_resiliencehubv2.types.test_summary

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.test_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TestSummaryList:
    import capo_resiliencehubv2.types.test_summary

    out: TestSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resiliencehubv2.types.test_summary.deserialize_json(item))
    return out
