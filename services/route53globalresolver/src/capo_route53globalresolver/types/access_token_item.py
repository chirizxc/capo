"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#AccessTokenItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name_short
    import capo_route53globalresolver.types.token_status


class AccessTokenItem(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the token.</p>"""
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the token.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the token was created.</p>"""
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view associated with the token.</p>"""
    expires_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the token expires.</p>"""
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the global resolver associated with the token.</p>"""
    name: NotRequired[
        "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>The name of the token.</p>"""
    status: "capo_route53globalresolver.types.token_status.TokenStatus"
    """<p>The current status of the token.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the token was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessTokenItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    out["dnsViewId"] = value["dns_view_id"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["expiresAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["expires_at"]
        )
    )
    out["globalResolverId"] = value["global_resolver_id"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_route53globalresolver.types.token_status

    out["status"] = capo_route53globalresolver.types.token_status.serialize_json(
        value["status"]
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> AccessTokenItem:
    out: AccessTokenItem = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AccessTokenItem.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AccessTokenItem.arn required")
    if data.get("createdAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("AccessTokenItem.created_at required")
    if data.get("dnsViewId") is not None:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("AccessTokenItem.dns_view_id required")
    if data.get("expiresAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["expires_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["expiresAt"]
            )
        )
    else:
        raise DeserializationError("AccessTokenItem.expires_at required")
    if data.get("globalResolverId") is not None:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        raise DeserializationError("AccessTokenItem.global_resolver_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_route53globalresolver.types.token_status

        out["status"] = capo_route53globalresolver.types.token_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("AccessTokenItem.status required")
    if data.get("updatedAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("AccessTokenItem.updated_at required")
    return out
