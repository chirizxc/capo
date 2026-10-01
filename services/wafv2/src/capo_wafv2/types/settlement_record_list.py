"""Generated from Smithy shape ``com.amazonaws.wafv2#SettlementRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.settlement_record

SettlementRecordList: TypeAlias = list[
    "capo_wafv2.types.settlement_record.SettlementRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SettlementRecordList) -> list:
    import capo_wafv2.types.settlement_record

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.settlement_record.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SettlementRecordList:
    import capo_wafv2.types.settlement_record

    out: SettlementRecordList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wafv2.types.settlement_record.deserialize_aws_json_1_1(item))
    return out
