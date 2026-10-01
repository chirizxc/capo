"""Generated from Smithy shape ``com.amazonaws.kafka#DestinationTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.partition_spec


class DestinationTable(TypedDict, closed=True):
    destination_database_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the destination namespace (database) in the AWS Glue Data Catalog.</p>"""
    destination_table_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the destination Apache Iceberg table.</p>"""
    partition_spec: NotRequired["capo_kafka.types.partition_spec.PartitionSpec"]
    """<p>The partition specification for the destination table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationTable) -> dict:
    out: dict = {}
    if "destination_database_name" in value:
        out["destinationDatabaseName"] = value["destination_database_name"]
    if "destination_table_name" in value:
        out["destinationTableName"] = value["destination_table_name"]
    if "partition_spec" in value:
        import capo_kafka.types.partition_spec

        out["partitionSpec"] = capo_kafka.types.partition_spec.serialize_json(
            value["partition_spec"]
        )
    return out


def deserialize_json(data: dict) -> DestinationTable:
    out: DestinationTable = {}  # type: ignore[typeddict-item]
    if data.get("destinationDatabaseName") is not None:
        out["destination_database_name"] = data["destinationDatabaseName"]
    if data.get("destinationTableName") is not None:
        out["destination_table_name"] = data["destinationTableName"]
    if data.get("partitionSpec") is not None:
        import capo_kafka.types.partition_spec

        out["partition_spec"] = capo_kafka.types.partition_spec.deserialize_json(
            data["partitionSpec"]
        )
    return out
