"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#GetConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_quicksetup.types.configuration_parameters_map
    import capo_ssm_quicksetup.types.status_summaries_list


class GetConfigurationOutput(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>A service generated identifier for the configuration.</p>"""
    manager_arn: NotRequired["str"]
    """<p>The ARN of the configuration manager.</p>"""
    configuration_definition_id: NotRequired["str"]
    """<p>The ID of the configuration definition.</p>"""
    type: NotRequired["str"]
    """<p>The type of the Quick Setup configuration.</p>"""
    type_version: NotRequired["str"]
    """<p>The version of the Quick Setup type used.</p>"""
    account: NotRequired["str"]
    """<p>The ID of the Amazon Web Services account where the configuration was deployed.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region where the configuration was deployed.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The datetime stamp when the configuration manager was created.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The datetime stamp when the configuration manager was last updated.</p>"""
    status_summaries: NotRequired[
        "capo_ssm_quicksetup.types.status_summaries_list.StatusSummariesList"
    ]
    """<p>A summary of the state of the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.</p>"""
    parameters: NotRequired[
        "capo_ssm_quicksetup.types.configuration_parameters_map.ConfigurationParametersMap"
    ]
    """<p>The parameters for the configuration definition type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "manager_arn" in value:
        out["ManagerArn"] = value["manager_arn"]
    if "configuration_definition_id" in value:
        out["ConfigurationDefinitionId"] = value["configuration_definition_id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "type_version" in value:
        out["TypeVersion"] = value["type_version"]
    if "account" in value:
        out["Account"] = value["account"]
    if "region" in value:
        out["Region"] = value["region"]
    if "created_at" in value:
        import capo_ssm_quicksetup._protocol.serialize

        out["CreatedAt"] = capo_ssm_quicksetup._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "last_modified_at" in value:
        import capo_ssm_quicksetup._protocol.serialize

        out["LastModifiedAt"] = capo_ssm_quicksetup._protocol.serialize.fmt_date_time(
            value["last_modified_at"]
        )
    if "status_summaries" in value:
        import capo_ssm_quicksetup.types.status_summaries_list

        out["StatusSummaries"] = (
            capo_ssm_quicksetup.types.status_summaries_list.serialize_json(
                value["status_summaries"]
            )
        )
    if "parameters" in value:
        import capo_ssm_quicksetup.types.configuration_parameters_map

        out["Parameters"] = (
            capo_ssm_quicksetup.types.configuration_parameters_map.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationOutput:
    out: GetConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ManagerArn") is not None:
        out["manager_arn"] = data["ManagerArn"]
    if data.get("ConfigurationDefinitionId") is not None:
        out["configuration_definition_id"] = data["ConfigurationDefinitionId"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("TypeVersion") is not None:
        out["type_version"] = data["TypeVersion"]
    if data.get("Account") is not None:
        out["account"] = data["Account"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("CreatedAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["CreatedAt"].replace("Z", "+00:00")
        )
    if data.get("LastModifiedAt") is not None:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromisoformat(
            data["LastModifiedAt"].replace("Z", "+00:00")
        )
    if data.get("StatusSummaries") is not None:
        import capo_ssm_quicksetup.types.status_summaries_list

        out["status_summaries"] = (
            capo_ssm_quicksetup.types.status_summaries_list.deserialize_json(
                data["StatusSummaries"]
            )
        )
    if data.get("Parameters") is not None:
        import capo_ssm_quicksetup.types.configuration_parameters_map

        out["parameters"] = (
            capo_ssm_quicksetup.types.configuration_parameters_map.deserialize_json(
                data["Parameters"]
            )
        )
    return out
