"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmHealthCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cspm_connector_status
    import capo_securityhub.types.health_issue_list
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.timestamp


class CspmHealthCheck(TypedDict, closed=True):
    connector_status: NotRequired[
        "capo_securityhub.types.cspm_connector_status.CspmConnectorStatus"
    ]
    """<p>The connectivity status of the connector.</p>"""
    message: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A message describing the reason for the current connector status.</p>"""
    last_checked_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The ISO 8601 UTC timestamp indicating when the health status was last checked.</p>"""
    issues: NotRequired["capo_securityhub.types.health_issue_list.HealthIssueList"]
    """<p>A list of health issues associated with the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CspmHealthCheck) -> dict:
    out: dict = {}
    if "connector_status" in value:
        import capo_securityhub.types.cspm_connector_status

        out["ConnectorStatus"] = (
            capo_securityhub.types.cspm_connector_status.serialize_json(
                value["connector_status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "last_checked_at" in value:
        import capo_securityhub.types.timestamp

        out["LastCheckedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["last_checked_at"]
        )
    if "issues" in value:
        import capo_securityhub.types.health_issue_list

        out["Issues"] = capo_securityhub.types.health_issue_list.serialize_json(
            value["issues"]
        )
    return out


def deserialize_json(data: dict) -> CspmHealthCheck:
    out: CspmHealthCheck = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorStatus") is not None:
        import capo_securityhub.types.cspm_connector_status

        out["connector_status"] = (
            capo_securityhub.types.cspm_connector_status.deserialize_json(
                data["ConnectorStatus"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("LastCheckedAt") is not None:
        import capo_securityhub.types.timestamp

        out["last_checked_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["LastCheckedAt"]
        )
    if data.get("Issues") is not None:
        import capo_securityhub.types.health_issue_list

        out["issues"] = capo_securityhub.types.health_issue_list.deserialize_json(
            data["Issues"]
        )
    return out
