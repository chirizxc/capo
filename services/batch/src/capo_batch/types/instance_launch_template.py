"""Generated from Smithy shape ``com.amazonaws.batch#InstanceLaunchTemplate``."""

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


class InstanceLaunchTemplate(TypedDict, closed=True):
    ec2_instance_profile_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon EC2 instance profile for the managed instances. The instance profile must use the <code>AmazonECSInstanceRolePolicyForManagedInstances</code> managed policy with a trust policy for <code>ec2.amazonaws.com</code>.</p>"""
    network_configuration: NotRequired[
        "capo_batch.types.managed_instances_network_configuration.ManagedInstancesNetworkConfiguration"
    ]
    """<p>The network configuration for the managed instances. Specifies the VPC subnets and security groups where instances are launched.</p>"""
    instance_requirements: NotRequired[
        "capo_batch.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The instance type requirements for the capacity provider. Use this to constrain which Amazon EC2 instance types Amazon ECS can launch. If not specified, all available instance types are eligible.</p>"""
    capacity_option_type: NotRequired["capo_batch.types.string.String"]
    """<p>The capacity pricing model for the managed instances. Valid values:</p> <ul> <li> <p> <code>ON_DEMAND</code> (default) — On-Demand pricing.</p> </li> <li> <p> <code>SPOT</code> — Spot Instances, which can provide significant cost savings for fault-tolerant workloads.</p> </li> </ul>"""
    storage_configuration: NotRequired[
        "capo_batch.types.managed_instances_storage_configuration.ManagedInstancesStorageConfiguration"
    ]
    """<p>The storage configuration for the managed instances. Configures the root EBS volume size. If not specified, the service uses the default EBS volume size for the instance type.</p>"""
    monitoring: NotRequired["capo_batch.types.string.String"]
    """<p>The level of CloudWatch monitoring for the managed instances. Valid values are <code>BASIC</code> and <code>DETAILED</code>.</p>"""
    fips_enabled: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether FIPS 140-2 validated cryptographic modules are enabled on the managed instances. Not available in all Regions.</p>"""
    capacity_reservations: NotRequired[
        "capo_batch.types.capacity_reservation_request.CapacityReservationRequest"
    ]
    """<p>The capacity reservation configuration for the managed instances. Use this to target On-Demand Capacity Reservations or Reserved Instances for predictable capacity and cost optimization.</p>"""
    instance_metadata_tags_propagation: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether instance tags are accessible from the instance metadata service (IMDS). If not specified, instance tags are not accessible from IMDS.</p>"""
    local_storage_configuration: NotRequired[
        "capo_batch.types.managed_instances_local_storage_configuration.ManagedInstancesLocalStorageConfiguration"
    ]
    """<p>The local storage configuration for the managed instances. If not specified, instance store volumes are not available to containers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceLaunchTemplate) -> dict:
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
    if "capacity_option_type" in value:
        out["capacityOptionType"] = value["capacity_option_type"]
    if "storage_configuration" in value:
        import capo_batch.types.managed_instances_storage_configuration

        out["storageConfiguration"] = (
            capo_batch.types.managed_instances_storage_configuration.serialize_json(
                value["storage_configuration"]
            )
        )
    if "monitoring" in value:
        out["monitoring"] = value["monitoring"]
    if "fips_enabled" in value:
        out["fipsEnabled"] = value["fips_enabled"]
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


def deserialize_json(data: dict) -> InstanceLaunchTemplate:
    out: InstanceLaunchTemplate = {}  # type: ignore[typeddict-item]
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
    if data.get("capacityOptionType") is not None:
        out["capacity_option_type"] = data["capacityOptionType"]
    if data.get("storageConfiguration") is not None:
        import capo_batch.types.managed_instances_storage_configuration

        out["storage_configuration"] = (
            capo_batch.types.managed_instances_storage_configuration.deserialize_json(
                data["storageConfiguration"]
            )
        )
    if data.get("monitoring") is not None:
        out["monitoring"] = data["monitoring"]
    if data.get("fipsEnabled") is not None:
        out["fips_enabled"] = data["fipsEnabled"]
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
