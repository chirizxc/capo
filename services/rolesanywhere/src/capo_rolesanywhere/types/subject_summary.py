"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#SubjectSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rolesanywhere.types.uuid


class SubjectSummary(TypedDict, closed=True):
    subject_arn: NotRequired["str"]
    """<p>The ARN of the resource.</p>"""
    subject_id: NotRequired["capo_rolesanywhere.types.uuid.Uuid"]
    """<p>The id of the resource.</p>"""
    enabled: NotRequired["bool"]
    """<p>The enabled status of the subject. </p>"""
    x509_subject: NotRequired["str"]
    """<p>The x509 principal identifier of the authenticating certificate.</p>"""
    last_seen_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 time stamp of when the certificate was last used in a temporary credential request.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 time stamp of when the certificate was first used in a temporary credential request.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the subject was last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubjectSummary) -> dict:
    out: dict = {}
    if "subject_arn" in value:
        out["subjectArn"] = value["subject_arn"]
    if "subject_id" in value:
        out["subjectId"] = value["subject_id"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "x509_subject" in value:
        out["x509Subject"] = value["x509_subject"]
    if "last_seen_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["lastSeenAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["last_seen_at"]
        )
    if "created_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["createdAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["updatedAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> SubjectSummary:
    out: SubjectSummary = {}  # type: ignore[typeddict-item]
    if data.get("subjectArn") is not None:
        out["subject_arn"] = data["subjectArn"]
    if data.get("subjectId") is not None:
        out["subject_id"] = data["subjectId"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("x509Subject") is not None:
        out["x509_subject"] = data["x509Subject"]
    if data.get("lastSeenAt") is not None:
        import datetime

        out["last_seen_at"] = datetime.datetime.fromisoformat(
            data["lastSeenAt"].replace("Z", "+00:00")
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out
