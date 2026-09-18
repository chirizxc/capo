"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateCredentialLockerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.credential_locker_arn
    import capo_iot_managed_integrations.types.credential_locker_created_at
    import capo_iot_managed_integrations.types.credential_locker_id


class CreateCredentialLockerResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential locker creation request.</p>"""
    arn: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_arn.CredentialLockerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the credential locker.</p>"""
    created_at: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_created_at.CredentialLockerCreatedAt"
    ]
    """<p>The timestamp value of when the credential locker request occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCredentialLockerResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_at" in value:
        import capo_iot_managed_integrations.types.credential_locker_created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.credential_locker_created_at.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateCredentialLockerResponse:
    out: CreateCredentialLockerResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreatedAt") is not None:
        import capo_iot_managed_integrations.types.credential_locker_created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.credential_locker_created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    return out
