"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_template_summary

TestTemplateSummaryList: TypeAlias = list[
    "capo_resiliencehubv2.types.test_template_summary.TestTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TestTemplateSummaryList) -> list:
    import capo_resiliencehubv2.types.test_template_summary

    out: list = []
    for item in value:
        out.append(
            capo_resiliencehubv2.types.test_template_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TestTemplateSummaryList:
    import capo_resiliencehubv2.types.test_template_summary

    out: TestTemplateSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resiliencehubv2.types.test_template_summary.deserialize_json(item)
        )
    return out
