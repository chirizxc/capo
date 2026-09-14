"""Generated from Smithy shape ``com.amazonaws.workmail#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.email_address
    import capo_workmail.types.entity_state
    import capo_workmail.types.identity_provider_identity_store_id
    import capo_workmail.types.identity_provider_user_id
    import capo_workmail.types.string
    import capo_workmail.types.timestamp
    import capo_workmail.types.user_name
    import capo_workmail.types.user_role
    import capo_workmail.types.work_mail_identifier


class User(TypedDict, closed=True):
    id: NotRequired["capo_workmail.types.work_mail_identifier.WorkMailIdentifier"]
    """<p>The identifier of the user.</p>"""
    email: NotRequired["capo_workmail.types.email_address.EmailAddress"]
    """<p>The email of the user.</p>"""
    name: NotRequired["capo_workmail.types.user_name.UserName"]
    """<p>The name of the user.</p>"""
    display_name: NotRequired["capo_workmail.types.string.String"]
    """<p>The display name of the user.</p>"""
    state: NotRequired["capo_workmail.types.entity_state.EntityState"]
    """<p>The state of the user, which can be ENABLED, DISABLED, or DELETED.</p>"""
    user_role: NotRequired["capo_workmail.types.user_role.UserRole"]
    """<p>The role of the user.</p>"""
    enabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the user was enabled for WorkMail use.</p>"""
    disabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date indicating when the user was disabled from WorkMail use.</p>"""
    identity_provider_user_id: NotRequired[
        "capo_workmail.types.identity_provider_user_id.IdentityProviderUserId"
    ]
    """<p>User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.</p>"""
    identity_provider_identity_store_id: NotRequired[
        "capo_workmail.types.identity_provider_identity_store_id.IdentityProviderIdentityStoreId"
    ]
    """<p>Identity store ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: User) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "email" in value:
        out["Email"] = value["email"]
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "state" in value:
        import capo_workmail.types.entity_state

        out["State"] = capo_workmail.types.entity_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "user_role" in value:
        import capo_workmail.types.user_role

        out["UserRole"] = capo_workmail.types.user_role.serialize_aws_json_1_1(
            value["user_role"]
        )
    if "enabled_date" in value:
        import capo_workmail.types.timestamp

        out["EnabledDate"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["enabled_date"]
        )
    if "disabled_date" in value:
        import capo_workmail.types.timestamp

        out["DisabledDate"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["disabled_date"]
        )
    if "identity_provider_user_id" in value:
        out["IdentityProviderUserId"] = value["identity_provider_user_id"]
    if "identity_provider_identity_store_id" in value:
        out["IdentityProviderIdentityStoreId"] = value[
            "identity_provider_identity_store_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("State") is not None:
        import capo_workmail.types.entity_state

        out["state"] = capo_workmail.types.entity_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("UserRole") is not None:
        import capo_workmail.types.user_role

        out["user_role"] = capo_workmail.types.user_role.deserialize_aws_json_1_1(
            data["UserRole"]
        )
    if data.get("EnabledDate") is not None:
        import capo_workmail.types.timestamp

        out["enabled_date"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["EnabledDate"]
        )
    if data.get("DisabledDate") is not None:
        import capo_workmail.types.timestamp

        out["disabled_date"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DisabledDate"]
        )
    if data.get("IdentityProviderUserId") is not None:
        out["identity_provider_user_id"] = data["IdentityProviderUserId"]
    if data.get("IdentityProviderIdentityStoreId") is not None:
        out["identity_provider_identity_store_id"] = data[
            "IdentityProviderIdentityStoreId"
        ]
    return out
