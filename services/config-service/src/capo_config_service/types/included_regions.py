"""Generated from Smithy shape ``com.amazonaws.configservice#IncludedRegions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.third_party_cloud_region

IncludedRegions: TypeAlias = list[
    "capo_config_service.types.third_party_cloud_region.ThirdPartyCloudRegion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncludedRegions) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IncludedRegions:
    return [item for item in data if item is not None]
