"""Generated from Smithy shape ``com.amazonaws.odb#GiMinorVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.gi_minor_version_summary

GiMinorVersionList: TypeAlias = list[
    "capo_odb.types.gi_minor_version_summary.GiMinorVersionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GiMinorVersionList) -> list:
    import capo_odb.types.gi_minor_version_summary

    out: list = []
    for item in value:
        out.append(capo_odb.types.gi_minor_version_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> GiMinorVersionList:
    import capo_odb.types.gi_minor_version_summary

    out: GiMinorVersionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_odb.types.gi_minor_version_summary.deserialize_aws_json_1_0(item)
        )
    return out
