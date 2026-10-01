"""Generated from Smithy shape ``com.amazonaws.glue#SearchFilterValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_glue.types.search_filter_long_value
    import capo_glue.types.search_filter_string_value


class _SearchFilterValue_StringValue(TypedDict, closed=True):
    StringValue: "capo_glue.types.search_filter_string_value.SearchFilterStringValue"


class _SearchFilterValue_LongValue(TypedDict, closed=True):
    LongValue: "capo_glue.types.search_filter_long_value.SearchFilterLongValue"


SearchFilterValue: TypeAlias = (
    _SearchFilterValue_StringValue | _SearchFilterValue_LongValue
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFilterValue) -> dict:
    if "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    elif "LongValue" in value:
        return {"LongValue": value["LongValue"]}
    else:
        raise SerializationError("SearchFilterValue: no variant present")


def deserialize_aws_json_1_1(data: dict) -> SearchFilterValue:
    if data.get("StringValue") is not None:
        return {"StringValue": data["StringValue"]}
    elif data.get("LongValue") is not None:
        return {"LongValue": data["LongValue"]}
    else:
        raise DeserializationError("SearchFilterValue: no recognized variant key")
