"""Generated from Smithy shape ``com.amazonaws.eks#KubeSchedulerVersionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.node_resources_fit_version_config


class KubeSchedulerVersionConfig(TypedDict, closed=True):
    node_resources_fit: NotRequired[
        "capo_eks.types.node_resources_fit_version_config.NodeResourcesFitVersionConfig"
    ]
    """<p>The NodeResourcesFit configuration with default value and constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubeSchedulerVersionConfig) -> dict:
    out: dict = {}
    if "node_resources_fit" in value:
        import capo_eks.types.node_resources_fit_version_config

        out["nodeResourcesFit"] = (
            capo_eks.types.node_resources_fit_version_config.serialize_json(
                value["node_resources_fit"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubeSchedulerVersionConfig:
    out: KubeSchedulerVersionConfig = {}  # type: ignore[typeddict-item]
    if data.get("nodeResourcesFit") is not None:
        import capo_eks.types.node_resources_fit_version_config

        out["node_resources_fit"] = (
            capo_eks.types.node_resources_fit_version_config.deserialize_json(
                data["nodeResourcesFit"]
            )
        )
    return out
