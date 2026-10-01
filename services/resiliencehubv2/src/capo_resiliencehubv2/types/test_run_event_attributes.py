"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunEventAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_run_event_attribute_key
    import capo_resiliencehubv2.types.test_run_event_attribute_value

TestRunEventAttributes: TypeAlias = dict[
    "capo_resiliencehubv2.types.test_run_event_attribute_key.TestRunEventAttributeKey",
    "capo_resiliencehubv2.types.test_run_event_attribute_value.TestRunEventAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TestRunEventAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TestRunEventAttributes:
    out: TestRunEventAttributes = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
