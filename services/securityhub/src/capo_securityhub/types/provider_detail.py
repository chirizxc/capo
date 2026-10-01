"""Generated from Smithy shape ``com.amazonaws.securityhub#ProviderDetail``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityhub.types.azure_detail
    import capo_securityhub.types.jira_cloud_detail
    import capo_securityhub.types.service_now_detail


class _ProviderDetail_JiraCloud(TypedDict, closed=True):
    JiraCloud: "capo_securityhub.types.jira_cloud_detail.JiraCloudDetail"


class _ProviderDetail_ServiceNow(TypedDict, closed=True):
    ServiceNow: "capo_securityhub.types.service_now_detail.ServiceNowDetail"


class _ProviderDetail_Azure(TypedDict, closed=True):
    Azure: "capo_securityhub.types.azure_detail.AzureDetail"


ProviderDetail: TypeAlias = (
    _ProviderDetail_JiraCloud | _ProviderDetail_ServiceNow | _ProviderDetail_Azure
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderDetail) -> dict:
    if "JiraCloud" in value:
        import capo_securityhub.types.jira_cloud_detail

        return {
            "JiraCloud": capo_securityhub.types.jira_cloud_detail.serialize_json(
                value["JiraCloud"]
            )
        }
    elif "ServiceNow" in value:
        import capo_securityhub.types.service_now_detail

        return {
            "ServiceNow": capo_securityhub.types.service_now_detail.serialize_json(
                value["ServiceNow"]
            )
        }
    elif "Azure" in value:
        import capo_securityhub.types.azure_detail

        return {
            "Azure": capo_securityhub.types.azure_detail.serialize_json(value["Azure"])
        }
    else:
        raise SerializationError("ProviderDetail: no variant present")


def deserialize_json(data: dict) -> ProviderDetail:
    if data.get("JiraCloud") is not None:
        import capo_securityhub.types.jira_cloud_detail

        return {
            "JiraCloud": capo_securityhub.types.jira_cloud_detail.deserialize_json(
                data["JiraCloud"]
            )
        }
    elif data.get("ServiceNow") is not None:
        import capo_securityhub.types.service_now_detail

        return {
            "ServiceNow": capo_securityhub.types.service_now_detail.deserialize_json(
                data["ServiceNow"]
            )
        }
    elif data.get("Azure") is not None:
        import capo_securityhub.types.azure_detail

        return {
            "Azure": capo_securityhub.types.azure_detail.deserialize_json(data["Azure"])
        }
    else:
        raise DeserializationError("ProviderDetail: no recognized variant key")
