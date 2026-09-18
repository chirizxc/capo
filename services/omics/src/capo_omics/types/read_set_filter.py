"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.creation_type
    import capo_omics.types.generated_from
    import capo_omics.types.read_set_name
    import capo_omics.types.read_set_status
    import capo_omics.types.reference_arn_filter
    import capo_omics.types.sample_id
    import capo_omics.types.subject_id


class ReadSetFilter(TypedDict, closed=True):
    name: NotRequired["capo_omics.types.read_set_name.ReadSetName"]
    """<p>A name to filter on.</p>"""
    status: NotRequired["capo_omics.types.read_set_status.ReadSetStatus"]
    """<p>A status to filter on.</p>"""
    reference_arn: NotRequired[
        "capo_omics.types.reference_arn_filter.ReferenceArnFilter"
    ]
    """<p>A genome reference ARN to filter on.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>The filter's start date.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>The filter's end date.</p>"""
    sample_id: NotRequired["capo_omics.types.sample_id.SampleId"]
    """<p> The read set source's sample ID. </p>"""
    subject_id: NotRequired["capo_omics.types.subject_id.SubjectId"]
    """<p> The read set source's subject ID. </p>"""
    generated_from: NotRequired["capo_omics.types.generated_from.GeneratedFrom"]
    """<p> Where the source originated. </p>"""
    creation_type: NotRequired["capo_omics.types.creation_type.CreationType"]
    """<p> The creation type of the read set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "reference_arn" in value:
        out["referenceArn"] = value["reference_arn"]
    if "created_after" in value:
        import capo_omics._protocol.serialize

        out["createdAfter"] = capo_omics._protocol.serialize.fmt_date_time(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_omics._protocol.serialize

        out["createdBefore"] = capo_omics._protocol.serialize.fmt_date_time(
            value["created_before"]
        )
    if "sample_id" in value:
        out["sampleId"] = value["sample_id"]
    if "subject_id" in value:
        out["subjectId"] = value["subject_id"]
    if "generated_from" in value:
        out["generatedFrom"] = value["generated_from"]
    if "creation_type" in value:
        out["creationType"] = value["creation_type"]
    return out


def deserialize_json(data: dict) -> ReadSetFilter:
    out: ReadSetFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("referenceArn") is not None:
        out["reference_arn"] = data["referenceArn"]
    if data.get("createdAfter") is not None:
        import datetime

        out["created_after"] = datetime.datetime.fromisoformat(
            data["createdAfter"].replace("Z", "+00:00")
        )
    if data.get("createdBefore") is not None:
        import datetime

        out["created_before"] = datetime.datetime.fromisoformat(
            data["createdBefore"].replace("Z", "+00:00")
        )
    if data.get("sampleId") is not None:
        out["sample_id"] = data["sampleId"]
    if data.get("subjectId") is not None:
        out["subject_id"] = data["subjectId"]
    if data.get("generatedFrom") is not None:
        out["generated_from"] = data["generatedFrom"]
    if data.get("creationType") is not None:
        out["creation_type"] = data["creationType"]
    return out
