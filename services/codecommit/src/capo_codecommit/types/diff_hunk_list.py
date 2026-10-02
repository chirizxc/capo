"""Generated from Smithy shape ``com.amazonaws.codecommit#DiffHunkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.diff_hunk

DiffHunkList: TypeAlias = list["capo_codecommit.types.diff_hunk.DiffHunk"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiffHunkList) -> list:
    import capo_codecommit.types.diff_hunk

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.diff_hunk.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DiffHunkList:
    import capo_codecommit.types.diff_hunk

    out: DiffHunkList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codecommit.types.diff_hunk.deserialize_aws_json_1_1(item))
    return out
