"""Generated from Smithy shape ``com.amazonaws.odb#ExascaleDbStorageVaultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.exascale_db_storage_vault_summary

ExascaleDbStorageVaultList: TypeAlias = list[
    "capo_odb.types.exascale_db_storage_vault_summary.ExascaleDbStorageVaultSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExascaleDbStorageVaultList) -> list:
    import capo_odb.types.exascale_db_storage_vault_summary

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.exascale_db_storage_vault_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExascaleDbStorageVaultList:
    import capo_odb.types.exascale_db_storage_vault_summary

    out: ExascaleDbStorageVaultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_odb.types.exascale_db_storage_vault_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
