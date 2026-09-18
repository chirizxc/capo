"""Generated from Smithy shape ``com.amazonaws.appintegrations#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.application_config
    import capo_appintegrations.types.application_name
    import capo_appintegrations.types.application_source_config
    import capo_appintegrations.types.application_type
    import capo_appintegrations.types.arn_or_uuid
    import capo_appintegrations.types.boolean
    import capo_appintegrations.types.description
    import capo_appintegrations.types.iframe_config
    import capo_appintegrations.types.initialization_timeout
    import capo_appintegrations.types.permission_list
    import capo_appintegrations.types.publication_list
    import capo_appintegrations.types.subscription_list


class UpdateApplicationRequest(TypedDict, closed=True):
    arn: "capo_appintegrations.types.arn_or_uuid.ArnOrUUID"
    """<p>The Amazon Resource Name (ARN) of the Application.</p>"""
    name: NotRequired["capo_appintegrations.types.application_name.ApplicationName"]
    """<p>The name of the application.</p>"""
    description: NotRequired["capo_appintegrations.types.description.Description"]
    """<p>The description of the application.</p>"""
    application_source_config: NotRequired[
        "capo_appintegrations.types.application_source_config.ApplicationSourceConfig"
    ]
    """<p>The configuration for where the application should be loaded from.</p>"""
    subscriptions: NotRequired[
        "capo_appintegrations.types.subscription_list.SubscriptionList"
    ]
    """<p>The events that the application subscribes.</p>"""
    publications: NotRequired[
        "capo_appintegrations.types.publication_list.PublicationList"
    ]
    """<p>The events that the application publishes.</p>"""
    permissions: NotRequired[
        "capo_appintegrations.types.permission_list.PermissionList"
    ]
    """<p>The configuration of events or requests that the application has access to.</p>"""
    is_service: NotRequired["capo_appintegrations.types.boolean.Boolean"]
    """<p>Indicates whether the application is a service.</p>"""
    initialization_timeout: NotRequired[
        "capo_appintegrations.types.initialization_timeout.InitializationTimeout"
    ]
    """<p>The maximum time in milliseconds allowed to establish a connection with the workspace.</p>"""
    application_config: NotRequired[
        "capo_appintegrations.types.application_config.ApplicationConfig"
    ]
    """<p>The configuration settings for the application.</p>"""
    iframe_config: NotRequired["capo_appintegrations.types.iframe_config.IframeConfig"]
    """<p>The iframe configuration for the application.</p>"""
    application_type: NotRequired[
        "capo_appintegrations.types.application_type.ApplicationType"
    ]
    """<p>The type of application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "application_source_config" in value:
        import capo_appintegrations.types.application_source_config

        out["ApplicationSourceConfig"] = (
            capo_appintegrations.types.application_source_config.serialize_json(
                value["application_source_config"]
            )
        )
    if "subscriptions" in value:
        import capo_appintegrations.types.subscription_list

        out["Subscriptions"] = (
            capo_appintegrations.types.subscription_list.serialize_json(
                value["subscriptions"]
            )
        )
    if "publications" in value:
        import capo_appintegrations.types.publication_list

        out["Publications"] = (
            capo_appintegrations.types.publication_list.serialize_json(
                value["publications"]
            )
        )
    if "permissions" in value:
        import capo_appintegrations.types.permission_list

        out["Permissions"] = capo_appintegrations.types.permission_list.serialize_json(
            value["permissions"]
        )
    if "is_service" in value:
        out["IsService"] = value["is_service"]
    if "initialization_timeout" in value:
        out["InitializationTimeout"] = value["initialization_timeout"]
    if "application_config" in value:
        import capo_appintegrations.types.application_config

        out["ApplicationConfig"] = (
            capo_appintegrations.types.application_config.serialize_json(
                value["application_config"]
            )
        )
    if "iframe_config" in value:
        import capo_appintegrations.types.iframe_config

        out["IframeConfig"] = capo_appintegrations.types.iframe_config.serialize_json(
            value["iframe_config"]
        )
    if "application_type" in value:
        import capo_appintegrations.types.application_type

        out["ApplicationType"] = (
            capo_appintegrations.types.application_type.serialize_json(
                value["application_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ApplicationSourceConfig") is not None:
        import capo_appintegrations.types.application_source_config

        out["application_source_config"] = (
            capo_appintegrations.types.application_source_config.deserialize_json(
                data["ApplicationSourceConfig"]
            )
        )
    if data.get("Subscriptions") is not None:
        import capo_appintegrations.types.subscription_list

        out["subscriptions"] = (
            capo_appintegrations.types.subscription_list.deserialize_json(
                data["Subscriptions"]
            )
        )
    if data.get("Publications") is not None:
        import capo_appintegrations.types.publication_list

        out["publications"] = (
            capo_appintegrations.types.publication_list.deserialize_json(
                data["Publications"]
            )
        )
    if data.get("Permissions") is not None:
        import capo_appintegrations.types.permission_list

        out["permissions"] = (
            capo_appintegrations.types.permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if data.get("IsService") is not None:
        out["is_service"] = data["IsService"]
    if data.get("InitializationTimeout") is not None:
        out["initialization_timeout"] = data["InitializationTimeout"]
    if data.get("ApplicationConfig") is not None:
        import capo_appintegrations.types.application_config

        out["application_config"] = (
            capo_appintegrations.types.application_config.deserialize_json(
                data["ApplicationConfig"]
            )
        )
    if data.get("IframeConfig") is not None:
        import capo_appintegrations.types.iframe_config

        out["iframe_config"] = (
            capo_appintegrations.types.iframe_config.deserialize_json(
                data["IframeConfig"]
            )
        )
    if data.get("ApplicationType") is not None:
        import capo_appintegrations.types.application_type

        out["application_type"] = (
            capo_appintegrations.types.application_type.deserialize_json(
                data["ApplicationType"]
            )
        )
    return out
