"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#QueryLanguage``."""

from typing import Literal, TypeAlias, cast

"""Query language for an alert rule expression."""
QueryLanguage: TypeAlias = Literal[
    "SQL",
    "PROMQL",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: QueryLanguage) -> str:
    return value


def deserialize_cbor(data: str) -> QueryLanguage:
    return cast(QueryLanguage, data)
