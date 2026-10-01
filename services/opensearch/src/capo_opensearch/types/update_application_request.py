"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.app_configs
    import capo_opensearch.types.data_sources
    import capo_opensearch.types.iam_identity_center_options_input
    import capo_opensearch.types.id


class UpdateApplicationRequest(TypedDict, closed=True):
    id: "capo_opensearch.types.id.Id"
    """<p>The unique identifier for the OpenSearch application to be updated.</p>"""
    data_sources: NotRequired["capo_opensearch.types.data_sources.DataSources"]
    """<p>The data sources to associate with the OpenSearch application.</p>"""
    app_configs: NotRequired["capo_opensearch.types.app_configs.AppConfigs"]
    """<p>The configuration settings to modify for the OpenSearch application.</p>"""
    iam_identity_center_options: NotRequired[
        "capo_opensearch.types.iam_identity_center_options_input.IamIdentityCenterOptionsInput"
    ]
    """<p>Configuration settings for integrating IAM Identity Center with the OpenSearch application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "data_sources" in value:
        import capo_opensearch.types.data_sources

        out["dataSources"] = capo_opensearch.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "app_configs" in value:
        import capo_opensearch.types.app_configs

        out["appConfigs"] = capo_opensearch.types.app_configs.serialize_json(
            value["app_configs"]
        )
    if "iam_identity_center_options" in value:
        import capo_opensearch.types.iam_identity_center_options_input

        out["iamIdentityCenterOptions"] = (
            capo_opensearch.types.iam_identity_center_options_input.serialize_json(
                value["iam_identity_center_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("dataSources") is not None:
        import capo_opensearch.types.data_sources

        out["data_sources"] = capo_opensearch.types.data_sources.deserialize_json(
            data["dataSources"]
        )
    if data.get("appConfigs") is not None:
        import capo_opensearch.types.app_configs

        out["app_configs"] = capo_opensearch.types.app_configs.deserialize_json(
            data["appConfigs"]
        )
    if data.get("iamIdentityCenterOptions") is not None:
        import capo_opensearch.types.iam_identity_center_options_input

        out["iam_identity_center_options"] = (
            capo_opensearch.types.iam_identity_center_options_input.deserialize_json(
                data["iamIdentityCenterOptions"]
            )
        )
    return out
