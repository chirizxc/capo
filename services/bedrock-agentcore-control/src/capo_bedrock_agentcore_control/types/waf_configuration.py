"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WafConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.waf_failure_mode


class WafConfiguration(TypedDict, closed=True):
    failure_mode: NotRequired[
        "capo_bedrock_agentcore_control.types.waf_failure_mode.WafFailureMode"
    ]
    """<p>The failure mode that determines how the gateway handles requests when Amazon Web Services WAF is unreachable or times out. Valid values include:</p> <ul> <li> <p> <code>FAIL_CLOSE</code> - The gateway blocks requests when Amazon Web Services WAF cannot be evaluated.</p> </li> <li> <p> <code>FAIL_OPEN</code> - The gateway allows requests when Amazon Web Services WAF cannot be evaluated.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: WafConfiguration) -> dict:
    out: dict = {}
    if "failure_mode" in value:
        import capo_bedrock_agentcore_control.types.waf_failure_mode

        out["failureMode"] = (
            capo_bedrock_agentcore_control.types.waf_failure_mode.serialize_json(
                value["failure_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> WafConfiguration:
    out: WafConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("failureMode") is not None:
        import capo_bedrock_agentcore_control.types.waf_failure_mode

        out["failure_mode"] = (
            capo_bedrock_agentcore_control.types.waf_failure_mode.deserialize_json(
                data["failureMode"]
            )
        )
    return out
