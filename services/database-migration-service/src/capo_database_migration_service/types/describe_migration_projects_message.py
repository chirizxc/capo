"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeMigrationProjectsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.filter_list
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class DescribeMigrationProjectsMessage(TypedDict, closed=True):
    filters: NotRequired["capo_database_migration_service.types.filter_list.FilterList"]
    """<p>The filters to apply to the migration projects.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>migration-project-identifier</code> – The migration project name or ARN.</p> </li> <li> <p> <code>instance-profile-identifier</code> – The instance profile name or ARN.</p> </li> <li> <p> <code>data-provider-identifier</code> – The source or target data provider name or ARN.</p> </li> <li> <p> <code>source-data-provider-identifier</code> – The source data provider name or ARN.</p> </li> <li> <p> <code>target-data-provider-identifier</code> – The target data provider name or ARN.</p> </li> </ul>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMigrationProjectsMessage) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_database_migration_service.types.filter_list

        out["Filters"] = (
            capo_database_migration_service.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMigrationProjectsMessage:
    out: DescribeMigrationProjectsMessage = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_database_migration_service.types.filter_list

        out["filters"] = (
            capo_database_migration_service.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    return out
