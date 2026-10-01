"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssessmentSortField``."""

from typing import Literal, TypeAlias, cast

"""<p>The field by which to sort failure mode assessment results.</p>"""
AssessmentSortField: TypeAlias = Literal["STARTED_AT",]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentSortField) -> str:
    return value


def deserialize_json(data: str) -> AssessmentSortField:
    return cast(AssessmentSortField, data)
