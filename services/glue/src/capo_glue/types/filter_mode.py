"""Generated from Smithy shape ``com.amazonaws.glue#FilterMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The strategy used to apply filter predicates to REST API requests.</p>"""
FilterMode: TypeAlias = Literal[
    "QUERY_PARAMS",
    "FILTER_STRING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterMode:
    return cast(FilterMode, data)
