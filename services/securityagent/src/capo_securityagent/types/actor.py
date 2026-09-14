"""Generated from Smithy shape ``com.amazonaws.securityagent#Actor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.authentication
    import capo_securityagent.types.uri_list


class Actor(TypedDict, closed=True):
    identifier: NotRequired["str"]
    """<p>The unique identifier for the actor.</p>"""
    uris: NotRequired["capo_securityagent.types.uri_list.UriList"]
    """<p>The list of URIs that the actor targets during testing.</p>"""
    authentication: NotRequired[
        "capo_securityagent.types.authentication.Authentication"
    ]
    """<p>The authentication configuration for the actor.</p>"""
    description: NotRequired["str"]
    """<p>A description of the actor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Actor) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "uris" in value:
        import capo_securityagent.types.uri_list

        out["uris"] = capo_securityagent.types.uri_list.serialize_json(value["uris"])
    if "authentication" in value:
        import capo_securityagent.types.authentication

        out["authentication"] = capo_securityagent.types.authentication.serialize_json(
            value["authentication"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> Actor:
    out: Actor = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("uris") is not None:
        import capo_securityagent.types.uri_list

        out["uris"] = capo_securityagent.types.uri_list.deserialize_json(data["uris"])
    if data.get("authentication") is not None:
        import capo_securityagent.types.authentication

        out["authentication"] = (
            capo_securityagent.types.authentication.deserialize_json(
                data["authentication"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
