"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableAnalysisRuleType``."""

from typing import Literal, TypeAlias, cast

IntermediateTableAnalysisRuleType: TypeAlias = Literal["CUSTOM",]


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableAnalysisRuleType) -> str:
    return value


def deserialize_json(data: str) -> IntermediateTableAnalysisRuleType:
    return cast(IntermediateTableAnalysisRuleType, data)
