"""Generated from Smithy shape ``com.amazonaws.devicefarm#InsightsType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of insights to generate.</p>"""
InsightsType: TypeAlias = Literal["TEST_REPORT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsightsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InsightsType:
    return cast(InsightsType, data)
