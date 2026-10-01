"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteLineageEventOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.lineage_event_identifier
    import capo_datazone.types.lineage_event_processing_status


class DeleteLineageEventOutput(TypedDict, closed=True):
    id: NotRequired[
        "capo_datazone.types.lineage_event_identifier.LineageEventIdentifier"
    ]
    """<p>The ID of the lineage event.</p>"""
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the domain.</p>"""
    processing_status: NotRequired[
        "capo_datazone.types.lineage_event_processing_status.LineageEventProcessingStatus"
    ]
    """<p>The progressing status of the lineage event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLineageEventOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "processing_status" in value:
        import capo_datazone.types.lineage_event_processing_status

        out["processingStatus"] = (
            capo_datazone.types.lineage_event_processing_status.serialize_json(
                value["processing_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteLineageEventOutput:
    out: DeleteLineageEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("processingStatus") is not None:
        import capo_datazone.types.lineage_event_processing_status

        out["processing_status"] = (
            capo_datazone.types.lineage_event_processing_status.deserialize_json(
                data["processingStatus"]
            )
        )
    return out
