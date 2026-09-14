"""Generated from Smithy shape ``com.amazonaws.securityhub#ActorSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.actor_session_mfa_status
    import capo_securityhub.types.long
    import capo_securityhub.types.non_empty_string


class ActorSession(TypedDict, closed=True):
    uid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Unique identifier of the session. </p>"""
    mfa_status: NotRequired[
        "capo_securityhub.types.actor_session_mfa_status.ActorSessionMfaStatus"
    ]
    """<p> Indicates whether multi-factor authentication (MFA) was used for authentication during the session.</p> <p>In CloudTrail, you can find this value as <code>userIdentity.sessionContext.attributes.mfaAuthenticated</code>.</p>"""
    created_time: NotRequired["capo_securityhub.types.long.Long"]
    """<p>The timestamp for when the session was created. </p> <p>In CloudTrail, you can find this value as <code>userIdentity.sessionContext.attributes.creationDate</code>.</p>"""
    issuer: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The issuer of the session. </p> <p>In CloudTrail, you can find this value as <code>userIdentity.sessionContext.sessionIssuer.arn</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActorSession) -> dict:
    out: dict = {}
    if "uid" in value:
        out["Uid"] = value["uid"]
    if "mfa_status" in value:
        import capo_securityhub.types.actor_session_mfa_status

        out["MfaStatus"] = (
            capo_securityhub.types.actor_session_mfa_status.serialize_json(
                value["mfa_status"]
            )
        )
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
    return out


def deserialize_json(data: dict) -> ActorSession:
    out: ActorSession = {}  # type: ignore[typeddict-item]
    if data.get("Uid") is not None:
        out["uid"] = data["Uid"]
    if data.get("MfaStatus") is not None:
        import capo_securityhub.types.actor_session_mfa_status

        out["mfa_status"] = (
            capo_securityhub.types.actor_session_mfa_status.deserialize_json(
                data["MfaStatus"]
            )
        )
    if data.get("CreatedTime") is not None:
        out["created_time"] = data["CreatedTime"]
    if data.get("Issuer") is not None:
        out["issuer"] = data["Issuer"]
    return out
