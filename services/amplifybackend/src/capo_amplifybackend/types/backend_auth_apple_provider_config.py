"""Generated from Smithy shape ``com.amazonaws.amplifybackend#BackendAuthAppleProviderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string


class BackendAuthAppleProviderConfig(TypedDict, closed=True):
    client_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>Describes the client_id (also called Services ID) that comes from Apple.</p>"""
    key_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>Describes the key_id that comes from Apple.</p>"""
    private_key: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>Describes the private_key that comes from Apple.</p>"""
    team_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>Describes the team_id that comes from Apple.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackendAuthAppleProviderConfig) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["client_id"] = value["client_id"]
    if "key_id" in value:
        out["key_id"] = value["key_id"]
    if "private_key" in value:
        out["private_key"] = value["private_key"]
    if "team_id" in value:
        out["team_id"] = value["team_id"]
    return out


def deserialize_json(data: dict) -> BackendAuthAppleProviderConfig:
    out: BackendAuthAppleProviderConfig = {}  # type: ignore[typeddict-item]
    if data.get("client_id") is not None:
        out["client_id"] = data["client_id"]
    if data.get("key_id") is not None:
        out["key_id"] = data["key_id"]
    if data.get("private_key") is not None:
        out["private_key"] = data["private_key"]
    if data.get("team_id") is not None:
        out["team_id"] = data["team_id"]
    return out
