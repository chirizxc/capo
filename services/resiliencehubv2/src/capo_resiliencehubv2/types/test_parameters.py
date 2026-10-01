"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.parameter_key
    import capo_resiliencehubv2.types.string_list

TestParameters: TypeAlias = dict[
    "capo_resiliencehubv2.types.parameter_key.ParameterKey",
    "capo_resiliencehubv2.types.string_list.StringList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TestParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_resiliencehubv2.types.string_list

        out[key] = capo_resiliencehubv2.types.string_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TestParameters:
    out: TestParameters = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_resiliencehubv2.types.string_list

        out[key] = capo_resiliencehubv2.types.string_list.deserialize_json(value)
    return out
