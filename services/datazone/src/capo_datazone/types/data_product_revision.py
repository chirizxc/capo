"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.data_product_id
    import capo_datazone.types.domain_id
    import capo_datazone.types.revision


class DataProductRevision(TypedDict, closed=True):
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the domain where the data product revision lives.</p>"""
    id: NotRequired["capo_datazone.types.data_product_id.DataProductId"]
    """<p>The ID of the data product revision.</p>"""
    revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The data product revision.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data product revision was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the data product revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductRevision) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> DataProductRevision:
    out: DataProductRevision = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    return out
