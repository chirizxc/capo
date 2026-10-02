"""Generated from Smithy shape ``com.amazonaws.glue#FilterOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.between_configuration
    import capo_glue.types.connection_string_to_string_map


class FilterOverrides(TypedDict, closed=True):
    field_name: NotRequired["str"]
    """<p>An override for the field name to use in filter expressions, if different from the schema field name.</p>"""
    operator_mappings: NotRequired[
        "capo_glue.types.connection_string_to_string_map.ConnectionStringToStringMap"
    ]
    """<p>A map of logical filter operators to their field-specific API representations, overriding the global operator mappings. Supported operator keys are: <code>EQUAL_TO</code>, <code>NOT_EQUAL_TO</code>, <code>LESS_THAN</code>, <code>GREATER_THAN</code>, <code>LESS_THAN_OR_EQUAL_TO</code>, <code>GREATER_THAN_OR_EQUAL_TO</code>, <code>CONTAINS</code>, <code>BETWEEN</code>, <code>AND</code>, and <code>OR</code>.</p>"""
    between_configuration: NotRequired[
        "capo_glue.types.between_configuration.BetweenConfiguration"
    ]
    """<p>Field-specific configuration for handling BETWEEN range filter operations.</p>"""
    date_time_format: NotRequired["str"]
    """<p>The date and time format for filter expressions on this field, overriding the global <code>DateTimeFormat</code>. Accepts Java <code>DateTimeFormatter</code> patterns (for example, <code>EEE, d MMM yyyy HH:mm:ss Z</code>), <code>EPOCH_SECONDS</code> for Unix epoch seconds, or <code>EPOCH_MILLIS</code> for Unix epoch milliseconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterOverrides) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "operator_mappings" in value:
        import capo_glue.types.connection_string_to_string_map

        out["OperatorMappings"] = (
            capo_glue.types.connection_string_to_string_map.serialize_aws_json_1_1(
                value["operator_mappings"]
            )
        )
    if "between_configuration" in value:
        import capo_glue.types.between_configuration

        out["BetweenConfiguration"] = (
            capo_glue.types.between_configuration.serialize_aws_json_1_1(
                value["between_configuration"]
            )
        )
    if "date_time_format" in value:
        out["DateTimeFormat"] = value["date_time_format"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterOverrides:
    out: FilterOverrides = {}  # type: ignore[typeddict-item]
    if data.get("FieldName") is not None:
        out["field_name"] = data["FieldName"]
    if data.get("OperatorMappings") is not None:
        import capo_glue.types.connection_string_to_string_map

        out["operator_mappings"] = (
            capo_glue.types.connection_string_to_string_map.deserialize_aws_json_1_1(
                data["OperatorMappings"]
            )
        )
    if data.get("BetweenConfiguration") is not None:
        import capo_glue.types.between_configuration

        out["between_configuration"] = (
            capo_glue.types.between_configuration.deserialize_aws_json_1_1(
                data["BetweenConfiguration"]
            )
        )
    if data.get("DateTimeFormat") is not None:
        out["date_time_format"] = data["DateTimeFormat"]
    return out
