"""Generated from Smithy shape ``com.amazonaws.glue#SearchMapFilterValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_glue.types.search_filter_string_value


class _SearchMapFilterValue_StringValue(TypedDict, closed=True):
    StringValue: "capo_glue.types.search_filter_string_value.SearchFilterStringValue"


SearchMapFilterValue: TypeAlias = _SearchMapFilterValue_StringValue


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchMapFilterValue) -> dict:
    if "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    else:
        raise SerializationError("SearchMapFilterValue: no variant present")


def deserialize_aws_json_1_1(data: dict) -> SearchMapFilterValue:
    if data.get("StringValue") is not None:
        return {"StringValue": data["StringValue"]}
    else:
        raise DeserializationError("SearchMapFilterValue: no recognized variant key")
