"""Generated from Smithy shape ``com.amazonaws.pcs#NodeLifecycleActions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.node_lifecycle_stages
    import capo_pcs.types.script_caching_policy


class NodeLifecycleActions(TypedDict, closed=True):
    stages: "capo_pcs.types.node_lifecycle_stages.NodeLifecycleStages"
    """<p>The lifecycle stages where you configure scripts to run.</p>"""
    script_caching_policy: "capo_pcs.types.script_caching_policy.ScriptCachingPolicy"
    """<p>The caching policy for node lifecycle scripts. The default value is <code>CACHE_ONCE</code>. Valid values:</p> <ul> <li> <p> <code>CACHE_ONCE</code> – Downloads each script once and reuses it on subsequent boots.</p> </li> <li> <p> <code>REFRESH_ON_REBOOT</code> – Downloads each script on every boot.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NodeLifecycleActions) -> dict:
    out: dict = {}
    import capo_pcs.types.node_lifecycle_stages

    out["stages"] = capo_pcs.types.node_lifecycle_stages.serialize_aws_json_1_0(
        value["stages"]
    )
    import capo_pcs.types.script_caching_policy

    out["scriptCachingPolicy"] = (
        capo_pcs.types.script_caching_policy.serialize_aws_json_1_0(
            value.get("script_caching_policy", "CACHE_ONCE")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NodeLifecycleActions:
    out: NodeLifecycleActions = {}  # type: ignore[typeddict-item]
    if data.get("stages") is not None:
        import capo_pcs.types.node_lifecycle_stages

        out["stages"] = capo_pcs.types.node_lifecycle_stages.deserialize_aws_json_1_0(
            data["stages"]
        )
    else:
        raise DeserializationError("NodeLifecycleActions.stages required")
    if data.get("scriptCachingPolicy") is not None:
        import capo_pcs.types.script_caching_policy

        out["script_caching_policy"] = (
            capo_pcs.types.script_caching_policy.deserialize_aws_json_1_0(
                data["scriptCachingPolicy"]
            )
        )
    else:
        out["script_caching_policy"] = "CACHE_ONCE"
    return out
