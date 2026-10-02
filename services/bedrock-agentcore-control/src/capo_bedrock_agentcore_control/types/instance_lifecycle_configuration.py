"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InstanceLifecycleConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class InstanceLifecycleConfiguration(TypedDict, closed=True):
    idle_instance_timeout: NotRequired["int"]
    """<p>The number of seconds an instance can remain idle before it is stopped. An instance is considered idle when all of its agents are idle. The default is 900 seconds (15 minutes).</p>"""
    max_lifetime: NotRequired["int"]
    """<p>The maximum lifetime of an instance, in seconds. When an instance reaches this limit, the service terminates it regardless of activity. The default is 28800 seconds (8 hours). The maximum is 1209600 seconds (14 days).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceLifecycleConfiguration) -> dict:
    out: dict = {}
    if "idle_instance_timeout" in value:
        out["idleInstanceTimeout"] = value["idle_instance_timeout"]
    if "max_lifetime" in value:
        out["maxLifetime"] = value["max_lifetime"]
    return out


def deserialize_json(data: dict) -> InstanceLifecycleConfiguration:
    out: InstanceLifecycleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("idleInstanceTimeout") is not None:
        out["idle_instance_timeout"] = data["idleInstanceTimeout"]
    if data.get("maxLifetime") is not None:
        out["max_lifetime"] = data["maxLifetime"]
    return out
