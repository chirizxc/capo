"""Generated from Smithy shape ``com.amazonaws.appconfig#FlagValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.attribute_value_map
    import capo_appconfig.types.boolean


class FlagValue(TypedDict, closed=True):
    enabled: "capo_appconfig.types.boolean.Boolean"
    """<p>Specifies whether the feature flag is enabled for this treatment.</p>"""
    attribute_values: NotRequired[
        "capo_appconfig.types.attribute_value_map.AttributeValueMap"
    ]
    """<p>The attribute values associated with this flag value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlagValue) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    if "attribute_values" in value:
        import capo_appconfig.types.attribute_value_map

        out["AttributeValues"] = (
            capo_appconfig.types.attribute_value_map.serialize_json(
                value["attribute_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlagValue:
    out: FlagValue = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("AttributeValues") is not None:
        import capo_appconfig.types.attribute_value_map

        out["attribute_values"] = (
            capo_appconfig.types.attribute_value_map.deserialize_json(
                data["AttributeValues"]
            )
        )
    return out
