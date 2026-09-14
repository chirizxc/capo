"""Generated from Smithy shape ``com.amazonaws.securityhub#IntegerListConfigurationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.integer_list


class IntegerListConfigurationOptions(TypedDict, closed=True):
    default_value: NotRequired["capo_securityhub.types.integer_list.IntegerList"]
    """<p> The Security Hub CSPM default value for a control parameter that is a list of integers. </p>"""
    min: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The minimum valid value for a control parameter that is a list of integers. </p>"""
    max: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The maximum valid value for a control parameter that is a list of integers. </p>"""
    max_items: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The maximum number of list items that an interger list control parameter can accept. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerListConfigurationOptions) -> dict:
    out: dict = {}
    if "default_value" in value:
        import capo_securityhub.types.integer_list

        out["DefaultValue"] = capo_securityhub.types.integer_list.serialize_json(
            value["default_value"]
        )
    if "min" in value:
        out["Min"] = value["min"]
    if "max" in value:
        out["Max"] = value["max"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    return out


def deserialize_json(data: dict) -> IntegerListConfigurationOptions:
    out: IntegerListConfigurationOptions = {}  # type: ignore[typeddict-item]
    if data.get("DefaultValue") is not None:
        import capo_securityhub.types.integer_list

        out["default_value"] = capo_securityhub.types.integer_list.deserialize_json(
            data["DefaultValue"]
        )
    if data.get("Min") is not None:
        out["min"] = data["Min"]
    if data.get("Max") is not None:
        out["max"] = data["Max"]
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    return out
