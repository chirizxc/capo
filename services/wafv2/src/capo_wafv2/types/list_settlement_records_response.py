"""Generated from Smithy shape ``com.amazonaws.wafv2#ListSettlementRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.settlement_record_list


class ListSettlementRecordsResponse(TypedDict, closed=True):
    settlements: NotRequired[
        "capo_wafv2.types.settlement_record_list.SettlementRecordList"
    ]
    """<p>The list of settlement records.</p>"""
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you get a paginated response, this marker indicates that additional results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSettlementRecordsResponse) -> dict:
    out: dict = {}
    if "settlements" in value:
        import capo_wafv2.types.settlement_record_list

        out["Settlements"] = (
            capo_wafv2.types.settlement_record_list.serialize_aws_json_1_1(
                value["settlements"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSettlementRecordsResponse:
    out: ListSettlementRecordsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Settlements") is not None:
        import capo_wafv2.types.settlement_record_list

        out["settlements"] = (
            capo_wafv2.types.settlement_record_list.deserialize_aws_json_1_1(
                data["Settlements"]
            )
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
