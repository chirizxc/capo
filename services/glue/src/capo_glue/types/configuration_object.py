"""Generated from Smithy shape ``com.amazonaws.glue#ConfigurationObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.allowed_values_string_list
    import capo_glue.types.config_value_string


class ConfigurationObject(TypedDict, closed=True):
    default_value: NotRequired["capo_glue.types.config_value_string.ConfigValueString"]
    """<p>A default value for the parameter.</p>"""
    allowed_values: NotRequired[
        "capo_glue.types.allowed_values_string_list.AllowedValuesStringList"
    ]
    """<p>A list of allowed values for the parameter.</p>"""
    min_value: NotRequired["capo_glue.types.config_value_string.ConfigValueString"]
    """<p>A minimum allowed value for the parameter.</p>"""
    max_value: NotRequired["capo_glue.types.config_value_string.ConfigValueString"]
    """<p>A maximum allowed value for the parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationObject) -> dict:
    out: dict = {}
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "allowed_values" in value:
        import capo_glue.types.allowed_values_string_list

        out["AllowedValues"] = (
            capo_glue.types.allowed_values_string_list.serialize_aws_json_1_1(
                value["allowed_values"]
            )
        )
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationObject:
    out: ConfigurationObject = {}  # type: ignore[typeddict-item]
    if data.get("DefaultValue") is not None:
        out["default_value"] = data["DefaultValue"]
    if data.get("AllowedValues") is not None:
        import capo_glue.types.allowed_values_string_list

        out["allowed_values"] = (
            capo_glue.types.allowed_values_string_list.deserialize_aws_json_1_1(
                data["AllowedValues"]
            )
        )
    if data.get("MinValue") is not None:
        out["min_value"] = data["MinValue"]
    if data.get("MaxValue") is not None:
        out["max_value"] = data["MaxValue"]
    return out
