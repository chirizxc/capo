"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeploymentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.deployment_config_mode
    import capo_cloudformation.types.disable_rollback


class DeploymentConfig(TypedDict, closed=True):
    mode: NotRequired[
        "capo_cloudformation.types.deployment_config_mode.DeploymentConfigMode"
    ]
    """<p>Specifies the deployment mode for the stack operation. Possible values are:</p> <ul> <li> <p> <code>STANDARD</code> - Use the standard deployment behavior, ensuring resources are ready to serve traffic before completing the operation. This is the default. You do not need to specify this value explicitly.</p> </li> <li> <p> <code>EXPRESS</code> - Complete the stack operation when resource configuration is applied, without waiting for resources to become ready to serve traffic. Resources continue becoming ready in the background.</p> </li> </ul>"""
    disable_rollback: NotRequired[
        "capo_cloudformation.types.disable_rollback.DisableRollback"
    ]
    """<p>Specifies whether to disable rollback of the stack if the stack operation fails.</p> <p>Default: <code>false</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeploymentConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "mode" in value:
        import capo_cloudformation.types.deployment_config_mode

        capo_cloudformation.types.deployment_config_mode.serialize_query(
            value["mode"], pairs, f"{key_prefix}Mode"
        )
    if "disable_rollback" in value:
        pairs.append(
            (
                f"{key_prefix}DisableRollback",
                "true" if value["disable_rollback"] else "false",
            )
        )


def deserialize_query(el: Element) -> DeploymentConfig:
    out: DeploymentConfig = {}  # type: ignore[typeddict-item]
    child_mode = el.find("Mode")
    if child_mode is not None:
        import capo_cloudformation.types.deployment_config_mode

        out["mode"] = (
            capo_cloudformation.types.deployment_config_mode.deserialize_query(
                child_mode
            )
        )
    child_disable_rollback = el.find("DisableRollback")
    if child_disable_rollback is not None:
        out["disable_rollback"] = (child_disable_rollback.text or "").lower() == "true"
    return out
