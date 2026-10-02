"""Generated from Smithy shape ``com.amazonaws.batch#ManagedInstancesStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer


class ManagedInstancesStorageConfiguration(TypedDict, closed=True):
    storage_size_gi_b: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The size of the root EBS volume in GiB for the managed instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedInstancesStorageConfiguration) -> dict:
    out: dict = {}
    if "storage_size_gi_b" in value:
        out["storageSizeGiB"] = value["storage_size_gi_b"]
    return out


def deserialize_json(data: dict) -> ManagedInstancesStorageConfiguration:
    out: ManagedInstancesStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageSizeGiB") is not None:
        out["storage_size_gi_b"] = data["storageSizeGiB"]
    return out
