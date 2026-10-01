"""Generated from Smithy shape ``com.amazonaws.securityagent#ReportFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.report_filter_value

ReportFilterList: TypeAlias = list[
    "capo_securityagent.types.report_filter_value.ReportFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> ReportFilterList:
    return [item for item in data if item is not None]
