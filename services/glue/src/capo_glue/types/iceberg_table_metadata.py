"""Generated from Smithy shape ``com.amazonaws.glue#IcebergTableMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.iceberg_partition_spec_list
    import capo_glue.types.iceberg_schema_list
    import capo_glue.types.iceberg_sort_order_list
    import capo_glue.types.integer
    import capo_glue.types.location_string
    import capo_glue.types.string_to_string_map
    import capo_glue.types.table_id_string
    import capo_glue.types.version_string


class IcebergTableMetadata(TypedDict, closed=True):
    format_version: NotRequired["capo_glue.types.version_string.VersionString"]
    """<p>The Apache Iceberg table format version, such as <code>1</code> or <code>2</code>. Determines the set of features and on-disk layout supported by the table.</p>"""
    table_uuid: NotRequired["capo_glue.types.table_id_string.TableIdString"]
    """<p>The unique identifier (UUID) for the Iceberg table, assigned when the table is created and used to track the table across metadata updates.</p>"""
    location: NotRequired["capo_glue.types.location_string.LocationString"]
    """<p>The base S3 location where the Iceberg table's data and metadata files are stored.</p>"""
    properties: NotRequired["capo_glue.types.string_to_string_map.StringToStringMap"]
    """<p>A map of key-value pairs that define table-level properties and configuration settings for the Iceberg table.</p>"""
    schemas: NotRequired["capo_glue.types.iceberg_schema_list.IcebergSchemaList"]
    """<p>The list of schemas that have been associated with the Iceberg table over its history, supporting schema evolution.</p>"""
    current_schema_id: "capo_glue.types.integer.Integer"
    """<p>The identifier of the schema that is currently active for the Iceberg table. Matches an entry in <code>Schemas</code>.</p>"""
    last_column_id: "capo_glue.types.integer.Integer"
    """<p>The highest column identifier that has been assigned in the Iceberg table's schema, used to ensure unique IDs as new columns are added.</p>"""
    partition_specs: NotRequired[
        "capo_glue.types.iceberg_partition_spec_list.IcebergPartitionSpecList"
    ]
    """<p>The list of partition specifications that have been associated with the Iceberg table over its history, supporting partition evolution.</p>"""
    default_spec_id: "capo_glue.types.integer.Integer"
    """<p>The identifier of the partition specification that is currently used by default when writing new data to the Iceberg table.</p>"""
    last_partition_id: "capo_glue.types.integer.Integer"
    """<p>The highest partition field identifier that has been assigned across the table's partition specifications.</p>"""
    sort_orders: NotRequired[
        "capo_glue.types.iceberg_sort_order_list.IcebergSortOrderList"
    ]
    """<p>The list of sort order specifications that have been associated with the Iceberg table over its history.</p>"""
    default_sort_order_id: "capo_glue.types.integer.Integer"
    """<p>The identifier of the sort order that is currently used by default when writing new data to the Iceberg table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergTableMetadata) -> dict:
    out: dict = {}
    if "format_version" in value:
        out["FormatVersion"] = value["format_version"]
    if "table_uuid" in value:
        out["TableUuid"] = value["table_uuid"]
    if "location" in value:
        out["Location"] = value["location"]
    if "properties" in value:
        import capo_glue.types.string_to_string_map

        out["Properties"] = capo_glue.types.string_to_string_map.serialize_aws_json_1_1(
            value["properties"]
        )
    if "schemas" in value:
        import capo_glue.types.iceberg_schema_list

        out["Schemas"] = capo_glue.types.iceberg_schema_list.serialize_aws_json_1_1(
            value["schemas"]
        )
    out["CurrentSchemaId"] = value.get("current_schema_id", 0)
    out["LastColumnId"] = value.get("last_column_id", 0)
    if "partition_specs" in value:
        import capo_glue.types.iceberg_partition_spec_list

        out["PartitionSpecs"] = (
            capo_glue.types.iceberg_partition_spec_list.serialize_aws_json_1_1(
                value["partition_specs"]
            )
        )
    out["DefaultSpecId"] = value.get("default_spec_id", 0)
    out["LastPartitionId"] = value.get("last_partition_id", 0)
    if "sort_orders" in value:
        import capo_glue.types.iceberg_sort_order_list

        out["SortOrders"] = (
            capo_glue.types.iceberg_sort_order_list.serialize_aws_json_1_1(
                value["sort_orders"]
            )
        )
    out["DefaultSortOrderId"] = value.get("default_sort_order_id", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergTableMetadata:
    out: IcebergTableMetadata = {}  # type: ignore[typeddict-item]
    if data.get("FormatVersion") is not None:
        out["format_version"] = data["FormatVersion"]
    if data.get("TableUuid") is not None:
        out["table_uuid"] = data["TableUuid"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("Properties") is not None:
        import capo_glue.types.string_to_string_map

        out["properties"] = (
            capo_glue.types.string_to_string_map.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if data.get("Schemas") is not None:
        import capo_glue.types.iceberg_schema_list

        out["schemas"] = capo_glue.types.iceberg_schema_list.deserialize_aws_json_1_1(
            data["Schemas"]
        )
    if data.get("CurrentSchemaId") is not None:
        out["current_schema_id"] = data["CurrentSchemaId"]
    else:
        out["current_schema_id"] = 0
    if data.get("LastColumnId") is not None:
        out["last_column_id"] = data["LastColumnId"]
    else:
        out["last_column_id"] = 0
    if data.get("PartitionSpecs") is not None:
        import capo_glue.types.iceberg_partition_spec_list

        out["partition_specs"] = (
            capo_glue.types.iceberg_partition_spec_list.deserialize_aws_json_1_1(
                data["PartitionSpecs"]
            )
        )
    if data.get("DefaultSpecId") is not None:
        out["default_spec_id"] = data["DefaultSpecId"]
    else:
        out["default_spec_id"] = 0
    if data.get("LastPartitionId") is not None:
        out["last_partition_id"] = data["LastPartitionId"]
    else:
        out["last_partition_id"] = 0
    if data.get("SortOrders") is not None:
        import capo_glue.types.iceberg_sort_order_list

        out["sort_orders"] = (
            capo_glue.types.iceberg_sort_order_list.deserialize_aws_json_1_1(
                data["SortOrders"]
            )
        )
    if data.get("DefaultSortOrderId") is not None:
        out["default_sort_order_id"] = data["DefaultSortOrderId"]
    else:
        out["default_sort_order_id"] = 0
    return out
