"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.lookup_table_configuration
    import capo_cloudwatch_logs.types.s3_configuration


class DestinationConfiguration(TypedDict, closed=True):
    s3_configuration: NotRequired[
        "capo_cloudwatch_logs.types.s3_configuration.S3Configuration"
    ]
    """<p>Configuration for delivering query results to Amazon S3.</p>"""
    lookup_table_configuration: NotRequired[
        "capo_cloudwatch_logs.types.lookup_table_configuration.LookupTableConfiguration"
    ]
    """<p>Configuration for delivering query results to a lookup table. The query results automatically populate or refresh the specified lookup table on each scheduled execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationConfiguration) -> dict:
    out: dict = {}
    if "s3_configuration" in value:
        import capo_cloudwatch_logs.types.s3_configuration

        out["s3Configuration"] = (
            capo_cloudwatch_logs.types.s3_configuration.serialize_aws_json_1_1(
                value["s3_configuration"]
            )
        )
    if "lookup_table_configuration" in value:
        import capo_cloudwatch_logs.types.lookup_table_configuration

        out["lookupTableConfiguration"] = (
            capo_cloudwatch_logs.types.lookup_table_configuration.serialize_aws_json_1_1(
                value["lookup_table_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationConfiguration:
    out: DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("s3Configuration") is not None:
        import capo_cloudwatch_logs.types.s3_configuration

        out["s3_configuration"] = (
            capo_cloudwatch_logs.types.s3_configuration.deserialize_aws_json_1_1(
                data["s3Configuration"]
            )
        )
    if data.get("lookupTableConfiguration") is not None:
        import capo_cloudwatch_logs.types.lookup_table_configuration

        out["lookup_table_configuration"] = (
            capo_cloudwatch_logs.types.lookup_table_configuration.deserialize_aws_json_1_1(
                data["lookupTableConfiguration"]
            )
        )
    return out
