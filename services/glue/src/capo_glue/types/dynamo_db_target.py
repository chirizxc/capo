"""Generated from Smithy shape ``com.amazonaws.glue#DynamoDBTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.nullable_boolean
    import capo_glue.types.nullable_double
    import capo_glue.types.path


class DynamoDBTarget(TypedDict, closed=True):
    path: NotRequired["capo_glue.types.path.Path"]
    """<p>The name of the DynamoDB table to crawl.</p>"""
    scan_all: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates whether to scan all the records, or to sample rows from the table. Scanning all the records can take a long time when the table is not a high throughput table.</p> <p>A value of <code>true</code> means to scan all records, while a value of <code>false</code> means to sample the records. If no value is specified, the value defaults to <code>true</code>.</p>"""
    scan_rate: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The percentage of the configured read capacity units to use by the Glue crawler. Read capacity units is a term defined by DynamoDB, and is a numeric value that acts as rate limiter for the number of reads that can be performed on that table per second.</p> <p>The valid values are null or a value between 0.1 to 1.5. A null value is used when user does not provide a value, and defaults to 0.5 of the configured Read Capacity Unit (for provisioned tables), or 0.25 of the max configured Read Capacity Unit (for tables using on-demand mode).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamoDBTarget) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    if "scan_all" in value:
        out["scanAll"] = value["scan_all"]
    if "scan_rate" in value:
        out["scanRate"] = (
            "NaN"
            if value["scan_rate"] != value["scan_rate"]
            else "Infinity"
            if value["scan_rate"] == float("inf")
            else "-Infinity"
            if value["scan_rate"] == float("-inf")
            else value["scan_rate"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamoDBTarget:
    out: DynamoDBTarget = {}  # type: ignore[typeddict-item]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("scanAll") is not None:
        out["scan_all"] = data["scanAll"]
    if data.get("scanRate") is not None:
        out["scan_rate"] = float(data["scanRate"])
    return out
