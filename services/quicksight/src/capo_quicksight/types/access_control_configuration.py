"""Generated from Smithy shape ``com.amazonaws.quicksight#AccessControlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean


class AccessControlConfiguration(TypedDict, closed=True):
    is_acl_enabled: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>Specifies whether ACLs are enabled for the knowledge base.</p> <p>This setting works together with the data source connector's ACL crawling. To enforce document-level access control end to end, set <code>isACLEnabled</code> to <code>true</code> and enable ACL crawling on the connector. For example, for an Amazon S3 data source, set <code>accessControlConfiguration.crawlAcl</code> to <code>true</code> in the connector template. For more information, see <code>KbTemplateConfiguration</code>. Enabling only one of the two settings does not produce a fully ACL-enforced knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessControlConfiguration) -> dict:
    out: dict = {}
    if "is_acl_enabled" in value:
        out["isACLEnabled"] = value["is_acl_enabled"]
    return out


def deserialize_json(data: dict) -> AccessControlConfiguration:
    out: AccessControlConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("isACLEnabled") is not None:
        out["is_acl_enabled"] = data["isACLEnabled"]
    return out
