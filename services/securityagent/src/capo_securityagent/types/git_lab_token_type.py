"""Generated from Smithy shape ``com.amazonaws.securityagent#GitLabTokenType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of GitLab access token.</p>"""
GitLabTokenType: TypeAlias = Literal[
    "PERSONAL",
    "GROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: GitLabTokenType) -> str:
    return value


def deserialize_json(data: str) -> GitLabTokenType:
    return cast(GitLabTokenType, data)
