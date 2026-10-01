"""Generated from Smithy shape ``com.amazonaws.signin#RevokeOAuth2TokenWithIAMResponse``."""

from typing_extensions import TypedDict


class RevokeOAuth2TokenWithIAMResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RevokeOAuth2TokenWithIAMResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RevokeOAuth2TokenWithIAMResponse:
    out: RevokeOAuth2TokenWithIAMResponse = {}  # type: ignore[typeddict-item]
    return out
