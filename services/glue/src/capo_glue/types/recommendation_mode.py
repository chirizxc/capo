"""Generated from Smithy shape ``com.amazonaws.glue#RecommendationMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the mode for how Glue Data Quality recommends rules.</p> <ul> <li> <p> <code>BASIC</code> uses an Glue job to analyze table data and recommend rules. This value is the default.</p> </li> <li> <p> <code>ADVANCED</code> uses Amazon Athena to analyze table data and Amazon Bedrock to recommend rules.</p> </li> </ul>"""
RecommendationMode: TypeAlias = Literal[
    "BASIC",
    "ADVANCED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationMode:
    return cast(RecommendationMode, data)
