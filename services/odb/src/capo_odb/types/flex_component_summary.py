"""Generated from Smithy shape ``com.amazonaws.odb#FlexComponentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.compute_model
    import capo_odb.types.hardware_type


class FlexComponentSummary(TypedDict, closed=True):
    available_core_count: NotRequired["int"]
    """<p>The maximum number of CPU cores that can be enabled for the flex component.</p>"""
    available_db_storage_in_g_bs: NotRequired["int"]
    """<p>The maximum amount of database storage, in gigabytes (GB), that can be enabled for the flex component.</p>"""
    available_local_storage_in_g_bs: NotRequired["int"]
    """<p>The maximum amount of local storage, in gigabytes (GB), that can be enabled for the flex component.</p>"""
    available_memory_in_g_bs: NotRequired["int"]
    """<p>The maximum amount of memory, in gigabytes (GB), that can be enabled for the flex component.</p>"""
    compute_model: NotRequired["capo_odb.types.compute_model.ComputeModel"]
    """<p>The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled. </p>"""
    description_summary: NotRequired["str"]
    """<p>A summary description of the flex component.</p>"""
    hardware_type: NotRequired["capo_odb.types.hardware_type.HardwareType"]
    """<p>The type of hardware for the flex component. Valid values are <code>COMPUTE</code> for compute servers and <code>CELL</code> for storage servers.</p>"""
    minimum_core_count: NotRequired["int"]
    """<p>The minimum number of CPU cores that can be enabled for the flex component.</p>"""
    name: NotRequired["str"]
    """<p>The name of the flex component.</p>"""
    runtime_minimum_core_count: NotRequired["int"]
    """<p>The runtime minimum number of CPU cores that can be enabled for the flex component.</p>"""
    shape: NotRequired["str"]
    """<p>The shape that uses the flex component.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlexComponentSummary) -> dict:
    out: dict = {}
    if "available_core_count" in value:
        out["availableCoreCount"] = value["available_core_count"]
    if "available_db_storage_in_g_bs" in value:
        out["availableDbStorageInGBs"] = value["available_db_storage_in_g_bs"]
    if "available_local_storage_in_g_bs" in value:
        out["availableLocalStorageInGBs"] = value["available_local_storage_in_g_bs"]
    if "available_memory_in_g_bs" in value:
        out["availableMemoryInGBs"] = value["available_memory_in_g_bs"]
    if "compute_model" in value:
        import capo_odb.types.compute_model

        out["computeModel"] = capo_odb.types.compute_model.serialize_aws_json_1_0(
            value["compute_model"]
        )
    if "description_summary" in value:
        out["descriptionSummary"] = value["description_summary"]
    if "hardware_type" in value:
        import capo_odb.types.hardware_type

        out["hardwareType"] = capo_odb.types.hardware_type.serialize_aws_json_1_0(
            value["hardware_type"]
        )
    if "minimum_core_count" in value:
        out["minimumCoreCount"] = value["minimum_core_count"]
    if "name" in value:
        out["name"] = value["name"]
    if "runtime_minimum_core_count" in value:
        out["runtimeMinimumCoreCount"] = value["runtime_minimum_core_count"]
    if "shape" in value:
        out["shape"] = value["shape"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FlexComponentSummary:
    out: FlexComponentSummary = {}  # type: ignore[typeddict-item]
    if data.get("availableCoreCount") is not None:
        out["available_core_count"] = data["availableCoreCount"]
    if data.get("availableDbStorageInGBs") is not None:
        out["available_db_storage_in_g_bs"] = data["availableDbStorageInGBs"]
    if data.get("availableLocalStorageInGBs") is not None:
        out["available_local_storage_in_g_bs"] = data["availableLocalStorageInGBs"]
    if data.get("availableMemoryInGBs") is not None:
        out["available_memory_in_g_bs"] = data["availableMemoryInGBs"]
    if data.get("computeModel") is not None:
        import capo_odb.types.compute_model

        out["compute_model"] = capo_odb.types.compute_model.deserialize_aws_json_1_0(
            data["computeModel"]
        )
    if data.get("descriptionSummary") is not None:
        out["description_summary"] = data["descriptionSummary"]
    if data.get("hardwareType") is not None:
        import capo_odb.types.hardware_type

        out["hardware_type"] = capo_odb.types.hardware_type.deserialize_aws_json_1_0(
            data["hardwareType"]
        )
    if data.get("minimumCoreCount") is not None:
        out["minimum_core_count"] = data["minimumCoreCount"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("runtimeMinimumCoreCount") is not None:
        out["runtime_minimum_core_count"] = data["runtimeMinimumCoreCount"]
    if data.get("shape") is not None:
        out["shape"] = data["shape"]
    return out
