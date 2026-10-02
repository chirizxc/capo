"""Generated from Smithy shape ``com.amazonaws.wellarchitected#JiraConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_wellarchitected.types.jira_issue_url


class JiraConfiguration(TypedDict, closed=True):
    jira_issue_url: NotRequired[
        "capo_wellarchitected.types.jira_issue_url.JiraIssueUrl"
    ]
    """<p>The URL of the associated Jira issue.</p>"""
    last_synced_time: NotRequired["datetime.datetime"]
    """<p>The date and time when the Jira configuration was last synced.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JiraConfiguration) -> dict:
    out: dict = {}
    if "jira_issue_url" in value:
        out["JiraIssueUrl"] = value["jira_issue_url"]
    if "last_synced_time" in value:
        import capo_wellarchitected.types._prelude.timestamp

        out["LastSyncedTime"] = (
            capo_wellarchitected.types._prelude.timestamp.serialize_json(
                value["last_synced_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> JiraConfiguration:
    out: JiraConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("JiraIssueUrl") is not None:
        out["jira_issue_url"] = data["JiraIssueUrl"]
    if data.get("LastSyncedTime") is not None:
        import capo_wellarchitected.types._prelude.timestamp

        out["last_synced_time"] = (
            capo_wellarchitected.types._prelude.timestamp.deserialize_json(
                data["LastSyncedTime"]
            )
        )
    return out
