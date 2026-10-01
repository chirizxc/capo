"""Generated from Smithy shape ``com.amazonaws.glue#IterableFormMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.iterable_form_entry
    import capo_glue.types.iterable_form_key

IterableFormMap: TypeAlias = dict[
    "capo_glue.types.iterable_form_key.IterableFormKey",
    "capo_glue.types.iterable_form_entry.IterableFormEntry",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: IterableFormMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.iterable_form_entry

        out[key] = capo_glue.types.iterable_form_entry.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> IterableFormMap:
    out: IterableFormMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_glue.types.iterable_form_entry

        out[key] = capo_glue.types.iterable_form_entry.deserialize_aws_json_1_1(value)
    return out
