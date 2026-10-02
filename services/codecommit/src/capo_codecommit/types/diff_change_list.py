"""Generated from Smithy shape ``com.amazonaws.codecommit#DiffChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.diff_change

DiffChangeList: TypeAlias = list["capo_codecommit.types.diff_change.DiffChange"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiffChangeList) -> list:
    import capo_codecommit.types.diff_change

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.diff_change.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DiffChangeList:
    import capo_codecommit.types.diff_change

    out: DiffChangeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codecommit.types.diff_change.deserialize_aws_json_1_1(item))
    return out
