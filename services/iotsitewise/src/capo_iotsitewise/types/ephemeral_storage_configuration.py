"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EphemeralStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.ephemeral_storage_configuration_storage_size_in_gi_b_integer
    import capo_iotsitewise.types.storage_class


class EphemeralStorageConfiguration(TypedDict, closed=True):
    storage_class: "capo_iotsitewise.types.storage_class.StorageClass"
    """<p>Storage type that determines I/O performance family and level.</p>"""
    storage_size_in_gi_b: "capo_iotsitewise.types.ephemeral_storage_configuration_storage_size_in_gi_b_integer.EphemeralStorageConfigurationStorageSizeInGiBInteger"
    """<p>Storage volume size in GiB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemeralStorageConfiguration) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.storage_class

    out["storageClass"] = capo_iotsitewise.types.storage_class.serialize_json(
        value["storage_class"]
    )
    out["storageSizeInGiB"] = value["storage_size_in_gi_b"]
    return out


def deserialize_json(data: dict) -> EphemeralStorageConfiguration:
    out: EphemeralStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageClass") is not None:
        import capo_iotsitewise.types.storage_class

        out["storage_class"] = capo_iotsitewise.types.storage_class.deserialize_json(
            data["storageClass"]
        )
    else:
        raise DeserializationError(
            "EphemeralStorageConfiguration.storage_class required"
        )
    if data.get("storageSizeInGiB") is not None:
        out["storage_size_in_gi_b"] = data["storageSizeInGiB"]
    else:
        raise DeserializationError(
            "EphemeralStorageConfiguration.storage_size_in_gi_b required"
        )
    return out
