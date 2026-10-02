"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id


class DeleteDomainInput(TypedDict, closed=True):
    identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon Web Services domain that is to be deleted.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""
    skip_deletion_check: NotRequired["bool"]
    """<p>Specifies whether to skip the check that prevents deletion of a domain that still contains resources. When you use this parameter, Amazon DataZone deletes the domain but might not remove its associated resources, which can leave orphaned resources behind. To delete a domain and fully clean up its associated resources, use <code>cascadeDelete</code> instead. You can't use this parameter together with <code>cascadeDelete</code>.</p>"""
    cascade_delete: NotRequired["bool"]
    """<p>Specifies whether to delete the domain along with all of its associated resources. When you use this parameter, Amazon DataZone deletes the domain and cleanly removes its associated resources without leaving orphaned resources behind. Amazon DataZone reports deletion progress in the <code>deleteProgress</code> field. Amazon DataZone reports any resources that it can't delete in the <code>failureReasons</code> field of the <code>GetDomain</code> response. You can't use this parameter together with <code>skipDeletionCheck</code>. If you don't specify a value, the default is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainInput:
    out: DeleteDomainInput = {}  # type: ignore[typeddict-item]
    return out
