"""Generated from Smithy shape ``com.amazonaws.odb#WalletPasswordSourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_odb.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_odb.types.customer_managed_aws_secret_configuration


class _WalletPasswordSourceConfiguration_customerManagedAwsSecret(
    TypedDict, closed=True
):
    customerManagedAwsSecret: "capo_odb.types.customer_managed_aws_secret_configuration.CustomerManagedAwsSecretConfiguration"


WalletPasswordSourceConfiguration: TypeAlias = (
    _WalletPasswordSourceConfiguration_customerManagedAwsSecret
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WalletPasswordSourceConfiguration) -> dict:
    if "customerManagedAwsSecret" in value:
        import capo_odb.types.customer_managed_aws_secret_configuration

        return {
            "customerManagedAwsSecret": capo_odb.types.customer_managed_aws_secret_configuration.serialize_aws_json_1_0(
                value["customerManagedAwsSecret"]
            )
        }
    else:
        raise SerializationError(
            "WalletPasswordSourceConfiguration: no variant present"
        )


def deserialize_aws_json_1_0(data: dict) -> WalletPasswordSourceConfiguration:
    if data.get("customerManagedAwsSecret") is not None:
        import capo_odb.types.customer_managed_aws_secret_configuration

        return {
            "customerManagedAwsSecret": capo_odb.types.customer_managed_aws_secret_configuration.deserialize_aws_json_1_0(
                data["customerManagedAwsSecret"]
            )
        }
    else:
        raise DeserializationError(
            "WalletPasswordSourceConfiguration: no recognized variant key"
        )
