"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.resource_id


class Cluster(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_elastic_beanstalk.types.resource_id.ResourceId"]
    """<p>The Amazon Resource Name (ARN) of the Amazon EKS cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Cluster, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_arn" in value:
        pairs.append((f"{key_prefix}ClusterArn", str(value["cluster_arn"])))


def deserialize_query(el: Element) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    child_cluster_arn = el.find("ClusterArn")
    if child_cluster_arn is not None:
        out["cluster_arn"] = str(child_cluster_arn.text or "")
    return out
