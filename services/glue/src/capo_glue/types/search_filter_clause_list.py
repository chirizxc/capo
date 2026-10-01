"""Generated from Smithy shape ``com.amazonaws.glue#SearchFilterClauseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.search_filter_clause

SearchFilterClauseList: TypeAlias = list[
    "capo_glue.types.search_filter_clause.SearchFilterClause"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFilterClauseList) -> list:
    import capo_glue.types.search_filter_clause

    out: list = []
    for item in value:
        out.append(capo_glue.types.search_filter_clause.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SearchFilterClauseList:
    import capo_glue.types.search_filter_clause

    out: SearchFilterClauseList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_glue.types.search_filter_clause.deserialize_aws_json_1_1(item))
    return out
