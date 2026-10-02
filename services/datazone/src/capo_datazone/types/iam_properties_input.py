"""Generated from Smithy shape ``com.amazonaws.datazone#IamPropertiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.role_arn


class IamPropertiesInput(TypedDict, closed=True):
    glue_lineage_sync_enabled: NotRequired["bool"]
    """<p>Specifies whether Amazon Web Services Glue lineage sync is enabled for a connection.</p>"""
    role_arn: NotRequired["capo_datazone.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role to associate with the connection as the project user role. To use this operation, you must have <code>iam:PassRole</code> permission for this role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamPropertiesInput) -> dict:
    out: dict = {}
    if "glue_lineage_sync_enabled" in value:
        out["glueLineageSyncEnabled"] = value["glue_lineage_sync_enabled"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> IamPropertiesInput:
    out: IamPropertiesInput = {}  # type: ignore[typeddict-item]
    if data.get("glueLineageSyncEnabled") is not None:
        out["glue_lineage_sync_enabled"] = data["glueLineageSyncEnabled"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out
