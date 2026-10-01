"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightFeedbackEntityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of entity for which to submit insight feedback. Possible values are <code>DomainName</code>.</p>"""
InsightFeedbackEntityType: TypeAlias = Literal["DomainName",]


# --- restJson1 ser/de ---
def serialize_json(value: InsightFeedbackEntityType) -> str:
    return value


def deserialize_json(data: str) -> InsightFeedbackEntityType:
    return cast(InsightFeedbackEntityType, data)
