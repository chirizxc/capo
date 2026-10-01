"""Generated from Smithy shape ``com.amazonaws.lightsail#DistributionCustomErrorResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.distribution_custom_error_response

DistributionCustomErrorResponseList: TypeAlias = list[
    "capo_lightsail.types.distribution_custom_error_response.DistributionCustomErrorResponse"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributionCustomErrorResponseList) -> list:
    import capo_lightsail.types.distribution_custom_error_response

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.distribution_custom_error_response.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DistributionCustomErrorResponseList:
    import capo_lightsail.types.distribution_custom_error_response

    out: DistributionCustomErrorResponseList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lightsail.types.distribution_custom_error_response.deserialize_aws_json_1_1(
                item
            )
        )
    return out
