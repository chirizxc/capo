"""Generated from Smithy shape ``com.amazonaws.iot#AuthorizerDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.authorizer_arn
    import capo_iot.types.authorizer_function_arn
    import capo_iot.types.authorizer_name
    import capo_iot.types.authorizer_status
    import capo_iot.types.boolean_key
    import capo_iot.types.date_type
    import capo_iot.types.enable_caching_for_http
    import capo_iot.types.public_key_map
    import capo_iot.types.token_key_name


class AuthorizerDescription(TypedDict, closed=True):
    authorizer_name: NotRequired["capo_iot.types.authorizer_name.AuthorizerName"]
    """<p>The authorizer name.</p>"""
    authorizer_arn: NotRequired["capo_iot.types.authorizer_arn.AuthorizerArn"]
    """<p>The authorizer ARN.</p>"""
    authorizer_function_arn: NotRequired[
        "capo_iot.types.authorizer_function_arn.AuthorizerFunctionArn"
    ]
    """<p>The authorizer's Lambda function ARN.</p>"""
    token_key_name: NotRequired["capo_iot.types.token_key_name.TokenKeyName"]
    """<p>The key used to extract the token from the HTTP headers.</p>"""
    token_signing_public_keys: NotRequired["capo_iot.types.public_key_map.PublicKeyMap"]
    """<p>The public keys used to validate the token signature returned by your custom authentication service.</p>"""
    status: NotRequired["capo_iot.types.authorizer_status.AuthorizerStatus"]
    """<p>The status of the authorizer.</p>"""
    creation_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The UNIX timestamp of when the authorizer was created.</p>"""
    last_modified_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The UNIX timestamp of when the authorizer was last updated.</p>"""
    signing_disabled: NotRequired["capo_iot.types.boolean_key.BooleanKey"]
    """<p>Specifies whether IoT validates the token signature in an authorization request.</p>"""
    enable_caching_for_http: NotRequired[
        "capo_iot.types.enable_caching_for_http.EnableCachingForHttp"
    ]
    """<p>When <code>true</code>, the result from the authorizer’s Lambda function is cached for the time specified in <code>refreshAfterInSeconds</code>. The cached result is used while the device reuses the same HTTP connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizerDescription) -> dict:
    out: dict = {}
    if "authorizer_name" in value:
        out["authorizerName"] = value["authorizer_name"]
    if "authorizer_arn" in value:
        out["authorizerArn"] = value["authorizer_arn"]
    if "authorizer_function_arn" in value:
        out["authorizerFunctionArn"] = value["authorizer_function_arn"]
    if "token_key_name" in value:
        out["tokenKeyName"] = value["token_key_name"]
    if "token_signing_public_keys" in value:
        import capo_iot.types.public_key_map

        out["tokenSigningPublicKeys"] = capo_iot.types.public_key_map.serialize_json(
            value["token_signing_public_keys"]
        )
    if "status" in value:
        import capo_iot.types.authorizer_status

        out["status"] = capo_iot.types.authorizer_status.serialize_json(value["status"])
    if "creation_date" in value:
        import capo_iot.types.date_type

        out["creationDate"] = capo_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import capo_iot.types.date_type

        out["lastModifiedDate"] = capo_iot.types.date_type.serialize_json(
            value["last_modified_date"]
        )
    if "signing_disabled" in value:
        out["signingDisabled"] = value["signing_disabled"]
    if "enable_caching_for_http" in value:
        out["enableCachingForHttp"] = value["enable_caching_for_http"]
    return out


def deserialize_json(data: dict) -> AuthorizerDescription:
    out: AuthorizerDescription = {}  # type: ignore[typeddict-item]
    if data.get("authorizerName") is not None:
        out["authorizer_name"] = data["authorizerName"]
    if data.get("authorizerArn") is not None:
        out["authorizer_arn"] = data["authorizerArn"]
    if data.get("authorizerFunctionArn") is not None:
        out["authorizer_function_arn"] = data["authorizerFunctionArn"]
    if data.get("tokenKeyName") is not None:
        out["token_key_name"] = data["tokenKeyName"]
    if data.get("tokenSigningPublicKeys") is not None:
        import capo_iot.types.public_key_map

        out["token_signing_public_keys"] = (
            capo_iot.types.public_key_map.deserialize_json(
                data["tokenSigningPublicKeys"]
            )
        )
    if data.get("status") is not None:
        import capo_iot.types.authorizer_status

        out["status"] = capo_iot.types.authorizer_status.deserialize_json(
            data["status"]
        )
    if data.get("creationDate") is not None:
        import capo_iot.types.date_type

        out["creation_date"] = capo_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    if data.get("lastModifiedDate") is not None:
        import capo_iot.types.date_type

        out["last_modified_date"] = capo_iot.types.date_type.deserialize_json(
            data["lastModifiedDate"]
        )
    if data.get("signingDisabled") is not None:
        out["signing_disabled"] = data["signingDisabled"]
    if data.get("enableCachingForHttp") is not None:
        out["enable_caching_for_http"] = data["enableCachingForHttp"]
    return out
