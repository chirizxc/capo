"""Generated from Smithy shape ``com.amazonaws.securityagent#StrideCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.stride_category

StrideCategoryList: TypeAlias = list[
    "capo_securityagent.types.stride_category.StrideCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: StrideCategoryList) -> list:
    import capo_securityagent.types.stride_category

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.stride_category.serialize_json(item))
    return out


def deserialize_json(data: list) -> StrideCategoryList:
    import capo_securityagent.types.stride_category

    out: StrideCategoryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.stride_category.deserialize_json(item))
    return out
