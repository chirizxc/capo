"""Generated from Smithy shape ``com.amazonaws.acm#AcmeExternalAccountBindingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_acm.types.acme_endpoint_arn
    import capo_acm.types.acme_external_account_binding_arn
    import capo_acm.types.role_arn


class AcmeExternalAccountBindingSummary(TypedDict, closed=True):
    acme_external_account_binding_arn: NotRequired[
        "capo_acm.types.acme_external_account_binding_arn.AcmeExternalAccountBindingArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the ACME external account binding.</p>"""
    acme_endpoint_arn: NotRequired["capo_acm.types.acme_endpoint_arn.AcmeEndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>"""
    role_arn: NotRequired["capo_acm.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the external account binding.</p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p>The time at which the external account binding expires.</p>"""
    revoked_at: NotRequired["datetime.datetime"]
    """<p>The time at which the external account binding was revoked.</p>"""
    last_used_at: NotRequired["datetime.datetime"]
    """<p>The time at which the external account binding was last used.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time at which the external account binding was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The time at which the external account binding was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeExternalAccountBindingSummary) -> dict:
    out: dict = {}
    if "acme_external_account_binding_arn" in value:
        out["AcmeExternalAccountBindingArn"] = value[
            "acme_external_account_binding_arn"
        ]
    if "acme_endpoint_arn" in value:
        out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "expires_at" in value:
        import capo_acm.types._prelude.timestamp

        out["ExpiresAt"] = capo_acm.types._prelude.timestamp.serialize_aws_json_1_1(
            value["expires_at"]
        )
    if "revoked_at" in value:
        import capo_acm.types._prelude.timestamp

        out["RevokedAt"] = capo_acm.types._prelude.timestamp.serialize_aws_json_1_1(
            value["revoked_at"]
        )
    if "last_used_at" in value:
        import capo_acm.types._prelude.timestamp

        out["LastUsedAt"] = capo_acm.types._prelude.timestamp.serialize_aws_json_1_1(
            value["last_used_at"]
        )
    if "created_at" in value:
        import capo_acm.types._prelude.timestamp

        out["CreatedAt"] = capo_acm.types._prelude.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_acm.types._prelude.timestamp

        out["UpdatedAt"] = capo_acm.types._prelude.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcmeExternalAccountBindingSummary:
    out: AcmeExternalAccountBindingSummary = {}  # type: ignore[typeddict-item]
    if data.get("AcmeExternalAccountBindingArn") is not None:
        out["acme_external_account_binding_arn"] = data["AcmeExternalAccountBindingArn"]
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ExpiresAt") is not None:
        import capo_acm.types._prelude.timestamp

        out["expires_at"] = capo_acm.types._prelude.timestamp.deserialize_aws_json_1_1(
            data["ExpiresAt"]
        )
    if data.get("RevokedAt") is not None:
        import capo_acm.types._prelude.timestamp

        out["revoked_at"] = capo_acm.types._prelude.timestamp.deserialize_aws_json_1_1(
            data["RevokedAt"]
        )
    if data.get("LastUsedAt") is not None:
        import capo_acm.types._prelude.timestamp

        out["last_used_at"] = (
            capo_acm.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["LastUsedAt"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_acm.types._prelude.timestamp

        out["created_at"] = capo_acm.types._prelude.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_acm.types._prelude.timestamp

        out["updated_at"] = capo_acm.types._prelude.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    return out
