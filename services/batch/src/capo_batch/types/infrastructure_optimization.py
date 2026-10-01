"""Generated from Smithy shape ``com.amazonaws.batch#InfrastructureOptimization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer


class InfrastructureOptimization(TypedDict, closed=True):
    scale_in_after: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The number of seconds an instance can remain idle before it is terminated. Valid values are <code>-1</code> or <code>0</code> to <code>3600</code>. Use <code>-1</code> as a special value to disable scale-in (instances are never terminated for being idle). If not specified, a default value applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InfrastructureOptimization) -> dict:
    out: dict = {}
    if "scale_in_after" in value:
        out["scaleInAfter"] = value["scale_in_after"]
    return out


def deserialize_json(data: dict) -> InfrastructureOptimization:
    out: InfrastructureOptimization = {}  # type: ignore[typeddict-item]
    if data.get("scaleInAfter") is not None:
        out["scale_in_after"] = data["scaleInAfter"]
    return out
