"""Generated from Smithy shape ``com.amazonaws.elementalinference#FixtureSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.fixture_summary

FixtureSummaryList: TypeAlias = list[
    "capo_elementalinference.types.fixture_summary.FixtureSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FixtureSummaryList) -> list:
    import capo_elementalinference.types.fixture_summary

    out: list = []
    for item in value:
        out.append(capo_elementalinference.types.fixture_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FixtureSummaryList:
    import capo_elementalinference.types.fixture_summary

    out: FixtureSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_elementalinference.types.fixture_summary.deserialize_json(item))
    return out
