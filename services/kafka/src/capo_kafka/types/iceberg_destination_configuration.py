"""Generated from Smithy shape ``com.amazonaws.kafka#IcebergDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean
    import capo_kafka.types.__integer
    import capo_kafka.types.__list_of_destination_table
    import capo_kafka.types.__string
    import capo_kafka.types.catalog
    import capo_kafka.types.dead_letter_queue_s3
    import capo_kafka.types.iceberg_compression_type
    import capo_kafka.types.schema_evolution
    import capo_kafka.types.table_creation


class IcebergDestinationConfiguration(TypedDict, closed=True):
    append_only: NotRequired["capo_kafka.types.__boolean.__boolean"]
    """<p>Whether the destination is append-only. Must be true; updates and deletes are not supported.</p>"""
    catalog: NotRequired["capo_kafka.types.catalog.Catalog"]
    """<p>The AWS Glue Data Catalog and S3 Tables warehouse used by the destination.</p>"""
    data_freshness_in_seconds: NotRequired["capo_kafka.types.__integer.__integer"]
    """<p>The maximum time, in seconds, that records buffer in MSK before being flushed to the destination. Allowed range: 300 to 900. Default: 600.</p>"""
    dead_letter_queue_s3: NotRequired[
        "capo_kafka.types.dead_letter_queue_s3.DeadLetterQueueS3"
    ]
    """<p>The Amazon S3 bucket and prefix where MSK writes records that fail to deliver.</p>"""
    destination_table_list: NotRequired[
        "capo_kafka.types.__list_of_destination_table.__listOfDestinationTable"
    ]
    """<p>The destination Iceberg tables. Currently exactly one table must be specified.</p>"""
    schema_evolution: NotRequired["capo_kafka.types.schema_evolution.SchemaEvolution"]
    """<p>Configuration controlling whether the destination table's schema is evolved to match incoming records.</p>"""
    service_execution_role_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that MSK assumes to access the destination table, the AWS Glue Data Catalog, and the dead-letter Amazon S3 bucket.</p>"""
    table_creation: NotRequired["capo_kafka.types.table_creation.TableCreation"]
    """<p>Configuration controlling whether MSK creates the destination table if it does not already exist.</p>"""
    compression_type: NotRequired[
        "capo_kafka.types.iceberg_compression_type.IcebergCompressionType"
    ]
    """<p>The compression codec for Iceberg table data files. Defaults to ZSTD.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergDestinationConfiguration) -> dict:
    out: dict = {}
    if "append_only" in value:
        out["appendOnly"] = value["append_only"]
    if "catalog" in value:
        import capo_kafka.types.catalog

        out["catalog"] = capo_kafka.types.catalog.serialize_json(value["catalog"])
    if "data_freshness_in_seconds" in value:
        out["dataFreshnessInSeconds"] = value["data_freshness_in_seconds"]
    if "dead_letter_queue_s3" in value:
        import capo_kafka.types.dead_letter_queue_s3

        out["deadLetterQueueS3"] = capo_kafka.types.dead_letter_queue_s3.serialize_json(
            value["dead_letter_queue_s3"]
        )
    if "destination_table_list" in value:
        import capo_kafka.types.__list_of_destination_table

        out["destinationTableList"] = (
            capo_kafka.types.__list_of_destination_table.serialize_json(
                value["destination_table_list"]
            )
        )
    if "schema_evolution" in value:
        import capo_kafka.types.schema_evolution

        out["schemaEvolution"] = capo_kafka.types.schema_evolution.serialize_json(
            value["schema_evolution"]
        )
    if "service_execution_role_arn" in value:
        out["serviceExecutionRoleArn"] = value["service_execution_role_arn"]
    if "table_creation" in value:
        import capo_kafka.types.table_creation

        out["tableCreation"] = capo_kafka.types.table_creation.serialize_json(
            value["table_creation"]
        )
    if "compression_type" in value:
        import capo_kafka.types.iceberg_compression_type

        out["compressionType"] = (
            capo_kafka.types.iceberg_compression_type.serialize_json(
                value["compression_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> IcebergDestinationConfiguration:
    out: IcebergDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("appendOnly") is not None:
        out["append_only"] = data["appendOnly"]
    if data.get("catalog") is not None:
        import capo_kafka.types.catalog

        out["catalog"] = capo_kafka.types.catalog.deserialize_json(data["catalog"])
    if data.get("dataFreshnessInSeconds") is not None:
        out["data_freshness_in_seconds"] = data["dataFreshnessInSeconds"]
    if data.get("deadLetterQueueS3") is not None:
        import capo_kafka.types.dead_letter_queue_s3

        out["dead_letter_queue_s3"] = (
            capo_kafka.types.dead_letter_queue_s3.deserialize_json(
                data["deadLetterQueueS3"]
            )
        )
    if data.get("destinationTableList") is not None:
        import capo_kafka.types.__list_of_destination_table

        out["destination_table_list"] = (
            capo_kafka.types.__list_of_destination_table.deserialize_json(
                data["destinationTableList"]
            )
        )
    if data.get("schemaEvolution") is not None:
        import capo_kafka.types.schema_evolution

        out["schema_evolution"] = capo_kafka.types.schema_evolution.deserialize_json(
            data["schemaEvolution"]
        )
    if data.get("serviceExecutionRoleArn") is not None:
        out["service_execution_role_arn"] = data["serviceExecutionRoleArn"]
    if data.get("tableCreation") is not None:
        import capo_kafka.types.table_creation

        out["table_creation"] = capo_kafka.types.table_creation.deserialize_json(
            data["tableCreation"]
        )
    if data.get("compressionType") is not None:
        import capo_kafka.types.iceberg_compression_type

        out["compression_type"] = (
            capo_kafka.types.iceberg_compression_type.deserialize_json(
                data["compressionType"]
            )
        )
    return out
