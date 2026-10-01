"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ListRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.list_records_next_token
    import capo_sagemaker_featurestore_runtime.types.record_identifier_list


class ListRecordsResponse(TypedDict, closed=True):
    record_identifiers: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.record_identifier_list.RecordIdentifierList"
    ]
    """<p>A list of record identifier values for the records stored in the <code>OnlineStore</code>.</p>"""
    next_token: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.list_records_next_token.ListRecordsNextToken"
    ]
    """<p>A token to resume pagination if the response includes more record identifiers than <code>MaxResults</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecordsResponse) -> dict:
    out: dict = {}
    if "record_identifiers" in value:
        import capo_sagemaker_featurestore_runtime.types.record_identifier_list

        out["RecordIdentifiers"] = (
            capo_sagemaker_featurestore_runtime.types.record_identifier_list.serialize_json(
                value["record_identifiers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecordsResponse:
    out: ListRecordsResponse = {}  # type: ignore[typeddict-item]
    if data.get("RecordIdentifiers") is not None:
        import capo_sagemaker_featurestore_runtime.types.record_identifier_list

        out["record_identifiers"] = (
            capo_sagemaker_featurestore_runtime.types.record_identifier_list.deserialize_json(
                data["RecordIdentifiers"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
