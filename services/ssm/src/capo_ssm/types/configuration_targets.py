"""Generated from Smithy shape ``com.amazonaws.ssm#ConfigurationTargets``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_ssm.types.azure_subscription_list


class _ConfigurationTargets_Subscriptions(TypedDict, closed=True):
    Subscriptions: "capo_ssm.types.azure_subscription_list.AzureSubscriptionList"


ConfigurationTargets: TypeAlias = _ConfigurationTargets_Subscriptions


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationTargets) -> dict:
    if "Subscriptions" in value:
        import capo_ssm.types.azure_subscription_list

        return {
            "Subscriptions": capo_ssm.types.azure_subscription_list.serialize_aws_json_1_1(
                value["Subscriptions"]
            )
        }
    else:
        raise SerializationError("ConfigurationTargets: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ConfigurationTargets:
    if data.get("Subscriptions") is not None:
        import capo_ssm.types.azure_subscription_list

        return {
            "Subscriptions": capo_ssm.types.azure_subscription_list.deserialize_aws_json_1_1(
                data["Subscriptions"]
            )
        }
    else:
        raise DeserializationError("ConfigurationTargets: no recognized variant key")
