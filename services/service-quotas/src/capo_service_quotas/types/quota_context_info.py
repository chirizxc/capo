"""Generated from Smithy shape ``com.amazonaws.servicequotas#QuotaContextInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.adjustable_at_level_enum
    import capo_service_quotas.types.quota_context_id
    import capo_service_quotas.types.quota_context_scope
    import capo_service_quotas.types.quota_context_scope_type


class QuotaContextInfo(TypedDict, closed=True):
    context_scope: NotRequired[
        "capo_service_quotas.types.quota_context_scope.QuotaContextScope"
    ]
    """<p>Specifies the scope to which the quota value is applied. If the scope is <code>RESOURCE</code>, the quota value is applied to each resource in the Amazon Web Services account. If the scope is <code>ACCOUNT</code>, the quota value is applied to the Amazon Web Services account.</p>"""
    context_scope_type: NotRequired[
        "capo_service_quotas.types.quota_context_scope_type.QuotaContextScopeType"
    ]
    """<p>Specifies the resource type to which the quota can be applied.</p>"""
    context_id: NotRequired["capo_service_quotas.types.quota_context_id.QuotaContextId"]
    """<p>Specifies the resource, or resources, to which the quota applies. The value for this field is either an Amazon Resource Name (ARN) or *. If the value is an ARN, the quota value applies to that resource. If the value is *, then the quota value applies to all resources listed in the <code>ContextScopeType</code> field. The quota value applies to all resources for which you haven’t previously applied a quota value, and any new resources you create in your Amazon Web Services account.</p>"""
    adjustable_at_level: NotRequired[
        "capo_service_quotas.types.adjustable_at_level_enum.AdjustableAtLevelEnum"
    ]
    """<p>Specifies the level at which you can request an increase for this quota:</p> <ul> <li> <p> <code>ACCOUNT</code> – You can request an increase only at the account level.</p> </li> <li> <p> <code>PER_RESOURCE</code> – You can request an increase only for an individual resource.</p> </li> <li> <p> <code>ALL</code> – You can request an increase at either the account level or for an individual resource.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuotaContextInfo) -> dict:
    out: dict = {}
    if "context_scope" in value:
        import capo_service_quotas.types.quota_context_scope

        out["ContextScope"] = (
            capo_service_quotas.types.quota_context_scope.serialize_aws_json_1_1(
                value["context_scope"]
            )
        )
    if "context_scope_type" in value:
        out["ContextScopeType"] = value["context_scope_type"]
    if "context_id" in value:
        out["ContextId"] = value["context_id"]
    if "adjustable_at_level" in value:
        import capo_service_quotas.types.adjustable_at_level_enum

        out["AdjustableAtLevel"] = (
            capo_service_quotas.types.adjustable_at_level_enum.serialize_aws_json_1_1(
                value["adjustable_at_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QuotaContextInfo:
    out: QuotaContextInfo = {}  # type: ignore[typeddict-item]
    if data.get("ContextScope") is not None:
        import capo_service_quotas.types.quota_context_scope

        out["context_scope"] = (
            capo_service_quotas.types.quota_context_scope.deserialize_aws_json_1_1(
                data["ContextScope"]
            )
        )
    if data.get("ContextScopeType") is not None:
        out["context_scope_type"] = data["ContextScopeType"]
    if data.get("ContextId") is not None:
        out["context_id"] = data["ContextId"]
    if data.get("AdjustableAtLevel") is not None:
        import capo_service_quotas.types.adjustable_at_level_enum

        out["adjustable_at_level"] = (
            capo_service_quotas.types.adjustable_at_level_enum.deserialize_aws_json_1_1(
                data["AdjustableAtLevel"]
            )
        )
    return out
