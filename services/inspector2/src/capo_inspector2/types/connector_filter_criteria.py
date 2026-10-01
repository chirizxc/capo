"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.aws_config_connector_arn_filter_list
    import capo_inspector2.types.connector_arn_filter_list
    import capo_inspector2.types.connector_type_filter_list
    import capo_inspector2.types.provider_filter_list
    import capo_inspector2.types.string_filter_list


class ConnectorFilterCriteria(TypedDict, closed=True):
    connector_arns: NotRequired[
        "capo_inspector2.types.connector_arn_filter_list.ConnectorArnFilterList"
    ]
    """<p>Filter by connector ARNs.</p>"""
    accounts: NotRequired["capo_inspector2.types.string_filter_list.StringFilterList"]
    """<p>Filter by Amazon Web Services account IDs.</p>"""
    aws_config_connector_arns: NotRequired[
        "capo_inspector2.types.aws_config_connector_arn_filter_list.AwsConfigConnectorArnFilterList"
    ]
    """<p>Filter by Amazon Web Services Config connector ARNs.</p>"""
    connector_type: NotRequired[
        "capo_inspector2.types.connector_type_filter_list.ConnectorTypeFilterList"
    ]
    """<p>Filter by connector type.</p>"""
    provider: NotRequired[
        "capo_inspector2.types.provider_filter_list.ProviderFilterList"
    ]
    """<p>Filter by cloud provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorFilterCriteria) -> dict:
    out: dict = {}
    if "connector_arns" in value:
        import capo_inspector2.types.connector_arn_filter_list

        out["connectorArns"] = (
            capo_inspector2.types.connector_arn_filter_list.serialize_json(
                value["connector_arns"]
            )
        )
    if "accounts" in value:
        import capo_inspector2.types.string_filter_list

        out["accounts"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["accounts"]
        )
    if "aws_config_connector_arns" in value:
        import capo_inspector2.types.aws_config_connector_arn_filter_list

        out["awsConfigConnectorArns"] = (
            capo_inspector2.types.aws_config_connector_arn_filter_list.serialize_json(
                value["aws_config_connector_arns"]
            )
        )
    if "connector_type" in value:
        import capo_inspector2.types.connector_type_filter_list

        out["connectorType"] = (
            capo_inspector2.types.connector_type_filter_list.serialize_json(
                value["connector_type"]
            )
        )
    if "provider" in value:
        import capo_inspector2.types.provider_filter_list

        out["provider"] = capo_inspector2.types.provider_filter_list.serialize_json(
            value["provider"]
        )
    return out


def deserialize_json(data: dict) -> ConnectorFilterCriteria:
    out: ConnectorFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("connectorArns") is not None:
        import capo_inspector2.types.connector_arn_filter_list

        out["connector_arns"] = (
            capo_inspector2.types.connector_arn_filter_list.deserialize_json(
                data["connectorArns"]
            )
        )
    if data.get("accounts") is not None:
        import capo_inspector2.types.string_filter_list

        out["accounts"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["accounts"]
        )
    if data.get("awsConfigConnectorArns") is not None:
        import capo_inspector2.types.aws_config_connector_arn_filter_list

        out["aws_config_connector_arns"] = (
            capo_inspector2.types.aws_config_connector_arn_filter_list.deserialize_json(
                data["awsConfigConnectorArns"]
            )
        )
    if data.get("connectorType") is not None:
        import capo_inspector2.types.connector_type_filter_list

        out["connector_type"] = (
            capo_inspector2.types.connector_type_filter_list.deserialize_json(
                data["connectorType"]
            )
        )
    if data.get("provider") is not None:
        import capo_inspector2.types.provider_filter_list

        out["provider"] = capo_inspector2.types.provider_filter_list.deserialize_json(
            data["provider"]
        )
    return out
