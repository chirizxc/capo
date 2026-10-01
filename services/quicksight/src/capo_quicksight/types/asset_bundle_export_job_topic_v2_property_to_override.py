"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobTopicV2PropertyToOverride``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportJobTopicV2PropertyToOverride: TypeAlias = Literal[
    "Name",
    "Description",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobTopicV2PropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobTopicV2PropertyToOverride:
    return cast(AssetBundleExportJobTopicV2PropertyToOverride, data)
