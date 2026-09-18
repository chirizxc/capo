"""Generated from Smithy shape ``com.amazonaws.entityresolution#JobMetrics``."""

from typing_extensions import NotRequired, TypedDict


class JobMetrics(TypedDict, closed=True):
    input_records: NotRequired["int"]
    """<p>The total number of input records.</p>"""
    total_records_processed: NotRequired["int"]
    """<p>The total number of records processed.</p>"""
    records_not_processed: NotRequired["int"]
    """<p>The total number of records that did not get processed.</p>"""
    delete_records_processed: NotRequired["int"]
    """<p>The number of records processed that were marked for deletion (<code>DELETE</code> = True) in the input file. This metric tracks records flagged for removal during the job execution.</p>"""
    match_i_ds: NotRequired["int"]
    """<p>The total number of <code>matchID</code>s generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobMetrics) -> dict:
    out: dict = {}
    if "input_records" in value:
        out["inputRecords"] = value["input_records"]
    if "total_records_processed" in value:
        out["totalRecordsProcessed"] = value["total_records_processed"]
    if "records_not_processed" in value:
        out["recordsNotProcessed"] = value["records_not_processed"]
    if "delete_records_processed" in value:
        out["deleteRecordsProcessed"] = value["delete_records_processed"]
    if "match_i_ds" in value:
        out["matchIDs"] = value["match_i_ds"]
    return out


def deserialize_json(data: dict) -> JobMetrics:
    out: JobMetrics = {}  # type: ignore[typeddict-item]
    if data.get("inputRecords") is not None:
        out["input_records"] = data["inputRecords"]
    if data.get("totalRecordsProcessed") is not None:
        out["total_records_processed"] = data["totalRecordsProcessed"]
    if data.get("recordsNotProcessed") is not None:
        out["records_not_processed"] = data["recordsNotProcessed"]
    if data.get("deleteRecordsProcessed") is not None:
        out["delete_records_processed"] = data["deleteRecordsProcessed"]
    if data.get("matchIDs") is not None:
        out["match_i_ds"] = data["matchIDs"]
    return out
