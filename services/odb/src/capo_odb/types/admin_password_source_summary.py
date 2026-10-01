"""Generated from Smithy shape ``com.amazonaws.odb#AdminPasswordSourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.admin_password_source
    import capo_odb.types.admin_password_source_configuration


class AdminPasswordSourceSummary(TypedDict, closed=True):
    admin_password_source: NotRequired[
        "capo_odb.types.admin_password_source.AdminPasswordSource"
    ]
    """<p>The source of the admin password for the Autonomous Database.</p>"""
    admin_password_source_configuration: NotRequired[
        "capo_odb.types.admin_password_source_configuration.AdminPasswordSourceConfiguration"
    ]
    """<p>The configuration of the admin password source for the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AdminPasswordSourceSummary) -> dict:
    out: dict = {}
    if "admin_password_source" in value:
        import capo_odb.types.admin_password_source

        out["adminPasswordSource"] = (
            capo_odb.types.admin_password_source.serialize_aws_json_1_0(
                value["admin_password_source"]
            )
        )
    if "admin_password_source_configuration" in value:
        import capo_odb.types.admin_password_source_configuration

        out["adminPasswordSourceConfiguration"] = (
            capo_odb.types.admin_password_source_configuration.serialize_aws_json_1_0(
                value["admin_password_source_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AdminPasswordSourceSummary:
    out: AdminPasswordSourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("adminPasswordSource") is not None:
        import capo_odb.types.admin_password_source

        out["admin_password_source"] = (
            capo_odb.types.admin_password_source.deserialize_aws_json_1_0(
                data["adminPasswordSource"]
            )
        )
    if data.get("adminPasswordSourceConfiguration") is not None:
        import capo_odb.types.admin_password_source_configuration

        out["admin_password_source_configuration"] = (
            capo_odb.types.admin_password_source_configuration.deserialize_aws_json_1_0(
                data["adminPasswordSourceConfiguration"]
            )
        )
    return out
