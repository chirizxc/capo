"""Generated from Smithy shape ``com.amazonaws.glue#EvaluatedDistributionsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.distribution_data
    import capo_glue.types.name_string

EvaluatedDistributionsMap: TypeAlias = dict[
    "capo_glue.types.name_string.NameString",
    "capo_glue.types.distribution_data.DistributionData",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: EvaluatedDistributionsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.distribution_data

        out[key] = capo_glue.types.distribution_data.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluatedDistributionsMap:
    out: EvaluatedDistributionsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_glue.types.distribution_data

        out[key] = capo_glue.types.distribution_data.deserialize_aws_json_1_1(value)
    return out
