"""Generated from Smithy shape ``com.amazonaws.qbusiness#Retriever``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.retriever_id
    import capo_qbusiness.types.retriever_name
    import capo_qbusiness.types.retriever_status
    import capo_qbusiness.types.retriever_type


class Retriever(TypedDict, closed=True):
    application_id: NotRequired["capo_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier of the Amazon Q Business application using the retriever.</p>"""
    retriever_id: NotRequired["capo_qbusiness.types.retriever_id.RetrieverId"]
    """<p>The identifier of the retriever used by your Amazon Q Business application.</p>"""
    type: NotRequired["capo_qbusiness.types.retriever_type.RetrieverType"]
    """<p>The type of your retriever.</p>"""
    status: NotRequired["capo_qbusiness.types.retriever_status.RetrieverStatus"]
    """<p>The status of your retriever.</p>"""
    display_name: NotRequired["capo_qbusiness.types.retriever_name.RetrieverName"]
    """<p>The name of your retriever.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Retriever) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "retriever_id" in value:
        out["retrieverId"] = value["retriever_id"]
    if "type" in value:
        import capo_qbusiness.types.retriever_type

        out["type"] = capo_qbusiness.types.retriever_type.serialize_json(value["type"])
    if "status" in value:
        import capo_qbusiness.types.retriever_status

        out["status"] = capo_qbusiness.types.retriever_status.serialize_json(
            value["status"]
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> Retriever:
    out: Retriever = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("retrieverId") is not None:
        out["retriever_id"] = data["retrieverId"]
    if data.get("type") is not None:
        import capo_qbusiness.types.retriever_type

        out["type"] = capo_qbusiness.types.retriever_type.deserialize_json(data["type"])
    if data.get("status") is not None:
        import capo_qbusiness.types.retriever_status

        out["status"] = capo_qbusiness.types.retriever_status.deserialize_json(
            data["status"]
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    return out
