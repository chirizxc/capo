"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobTopicV2OverridePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_permissions

AssetBundleImportJobTopicV2OverridePermissionsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_topic_v2_override_permissions.AssetBundleImportJobTopicV2OverridePermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobTopicV2OverridePermissionsList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_permissions

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_topic_v2_override_permissions.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobTopicV2OverridePermissionsList:
    import capo_quicksight.types.asset_bundle_import_job_topic_v2_override_permissions

    out: AssetBundleImportJobTopicV2OverridePermissionsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.asset_bundle_import_job_topic_v2_override_permissions.deserialize_json(
                item
            )
        )
    return out
