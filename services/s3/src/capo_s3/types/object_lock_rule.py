"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.default_retention


class ObjectLockRule(TypedDict, closed=True):
    default_retention: NotRequired["capo_s3.types.default_retention.DefaultRetention"]
    """<p>The default Object Lock retention settings for new objects in this bucket. You can specify:</p> <ul> <li> <p>A default retention period, by using <code>Days</code> or <code>Years</code>.</p> </li> <li> <p>A default event hold duration, by using <code>DefaultEventHold</code>. This setting also uses days or years.</p> </li> </ul> <p>You can set one or both. You cannot use days and years in the same setting.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ObjectLockRule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "default_retention" in value:
        import capo_s3.types.default_retention

        capo_s3.types.default_retention.serialize_xml(
            value["default_retention"], el, "DefaultRetention"
        )


def deserialize_xml(el: Element) -> ObjectLockRule:
    out: ObjectLockRule = {}  # type: ignore[typeddict-item]
    child_default_retention = el.find("DefaultRetention")
    if child_default_retention is not None:
        import capo_s3.types.default_retention

        out["default_retention"] = capo_s3.types.default_retention.deserialize_xml(
            child_default_retention
        )
    return out
