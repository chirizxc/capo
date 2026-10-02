"""Generated from Smithy shape ``com.amazonaws.odb#GetExascaleDbStorageVaultOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_odb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_odb.types.exascale_db_storage_vault


class GetExascaleDbStorageVaultOutput(TypedDict, closed=True):
    exascale_db_storage_vault: (
        "capo_odb.types.exascale_db_storage_vault.ExascaleDbStorageVault"
    )
    """<p>The Exascale storage vault.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetExascaleDbStorageVaultOutput) -> dict:
    out: dict = {}
    import capo_odb.types.exascale_db_storage_vault

    out["exascaleDbStorageVault"] = (
        capo_odb.types.exascale_db_storage_vault.serialize_aws_json_1_0(
            value["exascale_db_storage_vault"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetExascaleDbStorageVaultOutput:
    out: GetExascaleDbStorageVaultOutput = {}  # type: ignore[typeddict-item]
    if data.get("exascaleDbStorageVault") is not None:
        import capo_odb.types.exascale_db_storage_vault

        out["exascale_db_storage_vault"] = (
            capo_odb.types.exascale_db_storage_vault.deserialize_aws_json_1_0(
                data["exascaleDbStorageVault"]
            )
        )
    else:
        raise DeserializationError(
            "GetExascaleDbStorageVaultOutput.exascale_db_storage_vault required"
        )
    return out
