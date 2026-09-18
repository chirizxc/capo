"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAmazonMqBrokerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_amazon_mq_broker_encryption_options_details
    import capo_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details
    import capo_securityhub.types.aws_amazon_mq_broker_logs_details
    import capo_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details
    import capo_securityhub.types.aws_amazon_mq_broker_users_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class AwsAmazonMqBrokerDetails(TypedDict, closed=True):
    authentication_strategy: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The authentication strategy used to secure the broker. The default is <code>SIMPLE</code>. </p>"""
    auto_minor_version_upgrade: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Whether automatically upgrade new minor versions for brokers, as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window of the broker or after a manual broker reboot. </p>"""
    broker_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the broker. </p>"""
    broker_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The broker's name. </p>"""
    deployment_mode: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The broker's deployment mode. </p>"""
    encryption_options: NotRequired[
        "capo_securityhub.types.aws_amazon_mq_broker_encryption_options_details.AwsAmazonMqBrokerEncryptionOptionsDetails"
    ]
    """<p> Encryption options for the broker. Doesn’t apply to RabbitMQ brokers. </p>"""
    engine_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The type of broker engine. </p>"""
    engine_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The version of the broker engine. </p>"""
    host_instance_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The broker's instance type. </p>"""
    broker_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The unique ID that Amazon MQ generates for the broker. </p>"""
    ldap_server_metadata: NotRequired[
        "capo_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details.AwsAmazonMqBrokerLdapServerMetadataDetails"
    ]
    """<p> The metadata of the Lightweight Directory Access Protocol (LDAP) server used to authenticate and authorize connections to the broker. This is an optional failover server. </p>"""
    logs: NotRequired[
        "capo_securityhub.types.aws_amazon_mq_broker_logs_details.AwsAmazonMqBrokerLogsDetails"
    ]
    """<p> Turns on Amazon CloudWatch logging for brokers. </p>"""
    maintenance_window_start_time: NotRequired[
        "capo_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details.AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails"
    ]
    """<p> The scheduled time period (UTC) during which Amazon MQ begins to apply pending updates or patches to the broker. </p>"""
    publicly_accessible: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Permits connections from applications outside of the VPC that hosts the broker's subnets. </p>"""
    security_groups: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p> The list of rules (one minimum, 125 maximum) that authorize connections to brokers. </p>"""
    storage_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The broker's storage type. </p>"""
    subnet_ids: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p> The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. </p>"""
    users: NotRequired[
        "capo_securityhub.types.aws_amazon_mq_broker_users_list.AwsAmazonMqBrokerUsersList"
    ]
    """<p> The list of all broker usernames for the specified broker. Doesn't apply to RabbitMQ brokers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAmazonMqBrokerDetails) -> dict:
    out: dict = {}
    if "authentication_strategy" in value:
        out["AuthenticationStrategy"] = value["authentication_strategy"]
    if "auto_minor_version_upgrade" in value:
        out["AutoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "broker_arn" in value:
        out["BrokerArn"] = value["broker_arn"]
    if "broker_name" in value:
        out["BrokerName"] = value["broker_name"]
    if "deployment_mode" in value:
        out["DeploymentMode"] = value["deployment_mode"]
    if "encryption_options" in value:
        import capo_securityhub.types.aws_amazon_mq_broker_encryption_options_details

        out["EncryptionOptions"] = (
            capo_securityhub.types.aws_amazon_mq_broker_encryption_options_details.serialize_json(
                value["encryption_options"]
            )
        )
    if "engine_type" in value:
        out["EngineType"] = value["engine_type"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "host_instance_type" in value:
        out["HostInstanceType"] = value["host_instance_type"]
    if "broker_id" in value:
        out["BrokerId"] = value["broker_id"]
    if "ldap_server_metadata" in value:
        import capo_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details

        out["LdapServerMetadata"] = (
            capo_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details.serialize_json(
                value["ldap_server_metadata"]
            )
        )
    if "logs" in value:
        import capo_securityhub.types.aws_amazon_mq_broker_logs_details

        out["Logs"] = (
            capo_securityhub.types.aws_amazon_mq_broker_logs_details.serialize_json(
                value["logs"]
            )
        )
    if "maintenance_window_start_time" in value:
        import capo_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details

        out["MaintenanceWindowStartTime"] = (
            capo_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details.serialize_json(
                value["maintenance_window_start_time"]
            )
        )
    if "publicly_accessible" in value:
        out["PubliclyAccessible"] = value["publicly_accessible"]
    if "security_groups" in value:
        import capo_securityhub.types.string_list

        out["SecurityGroups"] = capo_securityhub.types.string_list.serialize_json(
            value["security_groups"]
        )
    if "storage_type" in value:
        out["StorageType"] = value["storage_type"]
    if "subnet_ids" in value:
        import capo_securityhub.types.string_list

        out["SubnetIds"] = capo_securityhub.types.string_list.serialize_json(
            value["subnet_ids"]
        )
    if "users" in value:
        import capo_securityhub.types.aws_amazon_mq_broker_users_list

        out["Users"] = (
            capo_securityhub.types.aws_amazon_mq_broker_users_list.serialize_json(
                value["users"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsAmazonMqBrokerDetails:
    out: AwsAmazonMqBrokerDetails = {}  # type: ignore[typeddict-item]
    if data.get("AuthenticationStrategy") is not None:
        out["authentication_strategy"] = data["AuthenticationStrategy"]
    if data.get("AutoMinorVersionUpgrade") is not None:
        out["auto_minor_version_upgrade"] = data["AutoMinorVersionUpgrade"]
    if data.get("BrokerArn") is not None:
        out["broker_arn"] = data["BrokerArn"]
    if data.get("BrokerName") is not None:
        out["broker_name"] = data["BrokerName"]
    if data.get("DeploymentMode") is not None:
        out["deployment_mode"] = data["DeploymentMode"]
    if data.get("EncryptionOptions") is not None:
        import capo_securityhub.types.aws_amazon_mq_broker_encryption_options_details

        out["encryption_options"] = (
            capo_securityhub.types.aws_amazon_mq_broker_encryption_options_details.deserialize_json(
                data["EncryptionOptions"]
            )
        )
    if data.get("EngineType") is not None:
        out["engine_type"] = data["EngineType"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("HostInstanceType") is not None:
        out["host_instance_type"] = data["HostInstanceType"]
    if data.get("BrokerId") is not None:
        out["broker_id"] = data["BrokerId"]
    if data.get("LdapServerMetadata") is not None:
        import capo_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details

        out["ldap_server_metadata"] = (
            capo_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details.deserialize_json(
                data["LdapServerMetadata"]
            )
        )
    if data.get("Logs") is not None:
        import capo_securityhub.types.aws_amazon_mq_broker_logs_details

        out["logs"] = (
            capo_securityhub.types.aws_amazon_mq_broker_logs_details.deserialize_json(
                data["Logs"]
            )
        )
    if data.get("MaintenanceWindowStartTime") is not None:
        import capo_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details

        out["maintenance_window_start_time"] = (
            capo_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details.deserialize_json(
                data["MaintenanceWindowStartTime"]
            )
        )
    if data.get("PubliclyAccessible") is not None:
        out["publicly_accessible"] = data["PubliclyAccessible"]
    if data.get("SecurityGroups") is not None:
        import capo_securityhub.types.string_list

        out["security_groups"] = capo_securityhub.types.string_list.deserialize_json(
            data["SecurityGroups"]
        )
    if data.get("StorageType") is not None:
        out["storage_type"] = data["StorageType"]
    if data.get("SubnetIds") is not None:
        import capo_securityhub.types.string_list

        out["subnet_ids"] = capo_securityhub.types.string_list.deserialize_json(
            data["SubnetIds"]
        )
    if data.get("Users") is not None:
        import capo_securityhub.types.aws_amazon_mq_broker_users_list

        out["users"] = (
            capo_securityhub.types.aws_amazon_mq_broker_users_list.deserialize_json(
                data["Users"]
            )
        )
    return out
