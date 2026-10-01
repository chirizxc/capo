"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementProspectingResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_prospecting_result

EngagementProspectingResultList: TypeAlias = list[
    "capo_partnercentral_selling.types.engagement_prospecting_result.EngagementProspectingResult"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementProspectingResultList) -> list:
    import capo_partnercentral_selling.types.engagement_prospecting_result

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.engagement_prospecting_result.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EngagementProspectingResultList:
    import capo_partnercentral_selling.types.engagement_prospecting_result

    out: EngagementProspectingResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.engagement_prospecting_result.deserialize_aws_json_1_0(
                item
            )
        )
    return out
