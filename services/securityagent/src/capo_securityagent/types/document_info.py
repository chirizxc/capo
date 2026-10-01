"""Generated from Smithy shape ``com.amazonaws.securityagent#DocumentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.integrated_document


class DocumentInfo(TypedDict, closed=True):
    s3_location: NotRequired["str"]
    """<p>The Amazon S3 location of the document.</p>"""
    artifact_id: NotRequired["str"]
    """<p>The unique identifier of the artifact associated with the document.</p>"""
    integrated_document: NotRequired[
        "capo_securityagent.types.integrated_document.IntegratedDocument"
    ]
    """<p>A reference to a document in an integrated third-party provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentInfo) -> dict:
    out: dict = {}
    if "s3_location" in value:
        out["s3Location"] = value["s3_location"]
    if "artifact_id" in value:
        out["artifactId"] = value["artifact_id"]
    if "integrated_document" in value:
        import capo_securityagent.types.integrated_document

        out["integratedDocument"] = (
            capo_securityagent.types.integrated_document.serialize_json(
                value["integrated_document"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentInfo:
    out: DocumentInfo = {}  # type: ignore[typeddict-item]
    if data.get("s3Location") is not None:
        out["s3_location"] = data["s3Location"]
    if data.get("artifactId") is not None:
        out["artifact_id"] = data["artifactId"]
    if data.get("integratedDocument") is not None:
        import capo_securityagent.types.integrated_document

        out["integrated_document"] = (
            capo_securityagent.types.integrated_document.deserialize_json(
                data["integratedDocument"]
            )
        )
    return out
