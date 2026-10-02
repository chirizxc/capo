"""Generated from Smithy shape ``com.amazonaws.autoscaling#Operator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.manager_identifier


class Operator(TypedDict, closed=True):
    principal: NotRequired[
        "capo_auto_scaling.types.manager_identifier.ManagerIdentifier"
    ]
    """<p>The service principal that is authorized to manage the Auto Scaling group. When an operator is specified, only the designated operator service principal can make mutating changes to the Auto Scaling group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Operator, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "principal" in value:
        pairs.append((f"{key_prefix}Principal", str(value["principal"])))


def deserialize_query(el: Element) -> Operator:
    out: Operator = {}  # type: ignore[typeddict-item]
    child_principal = el.find("Principal")
    if child_principal is not None:
        out["principal"] = str(child_principal.text or "")
    return out
