"""Generated from Smithy shape ``com.amazonaws.kafka#Catalog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class Catalog(TypedDict, closed=True):
    catalog_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the federated AWS Glue Data Catalog that projects the S3 Tables bucket. If omitted, MSK derives the catalog ARN from warehouseLocation.</p>"""
    warehouse_location: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the S3 Tables bucket that backs the Apache Iceberg warehouse.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Catalog) -> dict:
    out: dict = {}
    if "catalog_arn" in value:
        out["catalogArn"] = value["catalog_arn"]
    if "warehouse_location" in value:
        out["warehouseLocation"] = value["warehouse_location"]
    return out


def deserialize_json(data: dict) -> Catalog:
    out: Catalog = {}  # type: ignore[typeddict-item]
    if data.get("catalogArn") is not None:
        out["catalog_arn"] = data["catalogArn"]
    if data.get("warehouseLocation") is not None:
        out["warehouse_location"] = data["warehouseLocation"]
    return out
