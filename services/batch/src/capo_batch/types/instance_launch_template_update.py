"""Generated from Smithy shape ``com.amazonaws.batch#InstanceLaunchTemplateUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.capacity_reservation_request
    import capo_batch.types.instance_requirements_request
    import capo_batch.types.managed_instances_local_storage_configuration
    import capo_batch.types.managed_instances_network_configuration
    import capo_batch.types.managed_instances_storage_configuration
    import capo_batch.types.string


class InstanceLaunchTemplateUpdate(TypedDict, closed=True):
    ec2_instance_profile_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The updated Amazon Resource Name (ARN) of the Amazon EC2 instance profile for the managed instances.</p>"""
    network_configuration: NotRequired[
        "capo_batch.types.managed_instances_network_configuration.ManagedInstancesNetworkConfiguration"
    ]
    """<p>The updated network configuration for the managed instances.</p>"""
    instance_requirements: NotRequired[
        "capo_batch.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The updated instance type requirements for the capacity provider.</p>"""
    storage_configuration: NotRequired[
        "capo_batch.types.managed_instances_storage_configuration.ManagedInstancesStorageConfiguration"
    ]
    """<p>The updated storage configuration for the managed instances.</p>"""
    monitoring: NotRequired["capo_batch.types.string.String"]
    """<p>The updated monitoring level. Valid values are <code>BASIC</code> and <code>DETAILED</code>.</p>"""
    capacity_reservations: NotRequired[
        "capo_batch.types.capacity_reservation_request.CapacityReservationRequest"
    ]
    """<p>The updated capacity reservation configuration.</p>"""
    instance_metadata_tags_propagation: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether instance tags are accessible from the instance metadata service (IMDS).</p>"""
    local_storage_configuration: NotRequired[
        "capo_batch.types.managed_instances_local_storage_configuration.ManagedInstancesLocalStorageConfiguration"
    ]
    """<p>The updated local storage configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceLaunchTemplateUpdate) -> dict:
    out: dict = {}
    if "ec2_instance_profile_arn" in value:
        out["ec2InstanceProfileArn"] = value["ec2_instance_profile_arn"]
    if "network_configuration" in value:
        import capo_batch.types.managed_instances_network_configuration

        out["networkConfiguration"] = (
            capo_batch.types.managed_instances_network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "instance_requirements" in value:
        import capo_batch.types.instance_requirements_request

        out["instanceRequirements"] = (
            capo_batch.types.instance_requirements_request.serialize_json(
                value["instance_requirements"]
            )
        )
    if "storage_configuration" in value:
        import capo_batch.types.managed_instances_storage_configuration

        out["storageConfiguration"] = (
            capo_batch.types.managed_instances_storage_configuration.serialize_json(
                value["storage_configuration"]
            )
        )
    if "monitoring" in value:
        out["monitoring"] = value["monitoring"]
    if "capacity_reservations" in value:
        import capo_batch.types.capacity_reservation_request

        out["capacityReservations"] = (
            capo_batch.types.capacity_reservation_request.serialize_json(
                value["capacity_reservations"]
            )
        )
    if "instance_metadata_tags_propagation" in value:
        out["instanceMetadataTagsPropagation"] = value[
            "instance_metadata_tags_propagation"
        ]
    if "local_storage_configuration" in value:
        import capo_batch.types.managed_instances_local_storage_configuration

        out["localStorageConfiguration"] = (
            capo_batch.types.managed_instances_local_storage_configuration.serialize_json(
                value["local_storage_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceLaunchTemplateUpdate:
    out: InstanceLaunchTemplateUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ec2InstanceProfileArn") is not None:
        out["ec2_instance_profile_arn"] = data["ec2InstanceProfileArn"]
    if data.get("networkConfiguration") is not None:
        import capo_batch.types.managed_instances_network_configuration

        out["network_configuration"] = (
            capo_batch.types.managed_instances_network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if data.get("instanceRequirements") is not None:
        import capo_batch.types.instance_requirements_request

        out["instance_requirements"] = (
            capo_batch.types.instance_requirements_request.deserialize_json(
                data["instanceRequirements"]
            )
        )
    if data.get("storageConfiguration") is not None:
        import capo_batch.types.managed_instances_storage_configuration

        out["storage_configuration"] = (
            capo_batch.types.managed_instances_storage_configuration.deserialize_json(
                data["storageConfiguration"]
            )
        )
    if data.get("monitoring") is not None:
        out["monitoring"] = data["monitoring"]
    if data.get("capacityReservations") is not None:
        import capo_batch.types.capacity_reservation_request

        out["capacity_reservations"] = (
            capo_batch.types.capacity_reservation_request.deserialize_json(
                data["capacityReservations"]
            )
        )
    if data.get("instanceMetadataTagsPropagation") is not None:
        out["instance_metadata_tags_propagation"] = data[
            "instanceMetadataTagsPropagation"
        ]
    if data.get("localStorageConfiguration") is not None:
        import capo_batch.types.managed_instances_local_storage_configuration

        out["local_storage_configuration"] = (
            capo_batch.types.managed_instances_local_storage_configuration.deserialize_json(
                data["localStorageConfiguration"]
            )
        )
    return out
