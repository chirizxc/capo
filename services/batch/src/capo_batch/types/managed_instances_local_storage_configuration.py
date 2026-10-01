"""Generated from Smithy shape ``com.amazonaws.batch#ManagedInstancesLocalStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean


class ManagedInstancesLocalStorageConfiguration(TypedDict, closed=True):
    use_local_storage: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether instance store volumes (local NVMe SSDs) are available to containers. When enabled, containers can use the instance store for high-performance temporary storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedInstancesLocalStorageConfiguration) -> dict:
    out: dict = {}
    if "use_local_storage" in value:
        out["useLocalStorage"] = value["use_local_storage"]
    return out


def deserialize_json(data: dict) -> ManagedInstancesLocalStorageConfiguration:
    out: ManagedInstancesLocalStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("useLocalStorage") is not None:
        out["use_local_storage"] = data["useLocalStorage"]
    return out
