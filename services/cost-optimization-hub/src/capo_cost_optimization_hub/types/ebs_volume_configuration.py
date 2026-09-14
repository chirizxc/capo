"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#EbsVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.block_storage_performance_configuration
    import capo_cost_optimization_hub.types.storage_configuration


class EbsVolumeConfiguration(TypedDict, closed=True):
    storage: NotRequired[
        "capo_cost_optimization_hub.types.storage_configuration.StorageConfiguration"
    ]
    """<p>The disk storage of the Amazon Elastic Block Store volume.</p>"""
    performance: NotRequired[
        "capo_cost_optimization_hub.types.block_storage_performance_configuration.BlockStoragePerformanceConfiguration"
    ]
    """<p>The Amazon Elastic Block Store performance configuration.</p>"""
    attachment_state: NotRequired["str"]
    """<p>The Amazon Elastic Block Store attachment state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EbsVolumeConfiguration) -> dict:
    out: dict = {}
    if "storage" in value:
        import capo_cost_optimization_hub.types.storage_configuration

        out["storage"] = (
            capo_cost_optimization_hub.types.storage_configuration.serialize_aws_json_1_0(
                value["storage"]
            )
        )
    if "performance" in value:
        import capo_cost_optimization_hub.types.block_storage_performance_configuration

        out["performance"] = (
            capo_cost_optimization_hub.types.block_storage_performance_configuration.serialize_aws_json_1_0(
                value["performance"]
            )
        )
    if "attachment_state" in value:
        out["attachmentState"] = value["attachment_state"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EbsVolumeConfiguration:
    out: EbsVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storage") is not None:
        import capo_cost_optimization_hub.types.storage_configuration

        out["storage"] = (
            capo_cost_optimization_hub.types.storage_configuration.deserialize_aws_json_1_0(
                data["storage"]
            )
        )
    if data.get("performance") is not None:
        import capo_cost_optimization_hub.types.block_storage_performance_configuration

        out["performance"] = (
            capo_cost_optimization_hub.types.block_storage_performance_configuration.deserialize_aws_json_1_0(
                data["performance"]
            )
        )
    if data.get("attachmentState") is not None:
        out["attachment_state"] = data["attachmentState"]
    return out
