"""Generated from Smithy shape ``com.amazonaws.glue#CatalogTableConfigOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.uri_string


class CatalogTableConfigOptions(TypedDict, closed=True):
    database_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the database in the Glue Data Catalog.</p>"""
    table_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the table in the Glue Data Catalog.</p>"""
    s3_location: NotRequired["capo_glue.types.uri_string.UriString"]
    """<p>The Amazon S3 location for storing the results.</p>"""
    catalog_id: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>A unique identifier for the Glue Data Catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogTableConfigOptions) -> dict:
    out: dict = {}
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "s3_location" in value:
        out["S3Location"] = value["s3_location"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogTableConfigOptions:
    out: CatalogTableConfigOptions = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("S3Location") is not None:
        out["s3_location"] = data["S3Location"]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    return out
