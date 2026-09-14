"""Generated from Smithy shape ``com.amazonaws.omics#AnnotationImportItemDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.job_status
    import capo_omics.types.s3_uri


class AnnotationImportItemDetail(TypedDict, closed=True):
    source: "capo_omics.types.s3_uri.S3Uri"
    """<p>The source file's location in Amazon S3.</p>"""
    job_status: "capo_omics.types.job_status.JobStatus"
    """<p>The item's job status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationImportItemDetail) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["jobStatus"] = value["job_status"]
    return out


def deserialize_json(data: dict) -> AnnotationImportItemDetail:
    out: AnnotationImportItemDetail = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        raise DeserializationError("AnnotationImportItemDetail.source required")
    if data.get("jobStatus") is not None:
        out["job_status"] = data["jobStatus"]
    else:
        raise DeserializationError("AnnotationImportItemDetail.job_status required")
    return out
