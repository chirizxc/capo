"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerConnectionDraining``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer


class AwsElbLoadBalancerConnectionDraining(TypedDict, closed=True):
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether connection draining is enabled for the load balancer.</p>"""
    timeout: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The maximum time, in seconds, to keep the existing connections open before deregistering the instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerConnectionDraining) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerConnectionDraining:
    out: AwsElbLoadBalancerConnectionDraining = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    return out
