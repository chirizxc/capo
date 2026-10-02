"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmConnectorSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.cspm_connector_summary

CspmConnectorSummaryList: TypeAlias = list[
    "capo_securityhub.types.cspm_connector_summary.CspmConnectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CspmConnectorSummaryList) -> list:
    import capo_securityhub.types.cspm_connector_summary

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.cspm_connector_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CspmConnectorSummaryList:
    import capo_securityhub.types.cspm_connector_summary

    out: CspmConnectorSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.cspm_connector_summary.deserialize_json(item))
    return out
