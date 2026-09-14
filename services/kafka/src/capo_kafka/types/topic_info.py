"""Generated from Smithy shape ``com.amazonaws.kafka#TopicInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__integer
    import capo_kafka.types.__string


class TopicInfo(TypedDict, closed=True):
    topic_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Name for a topic.</p>"""
    replication_factor: NotRequired["capo_kafka.types.__integer.__integer"]
    """<p>Replication factor for a topic.</p>"""
    partition_count: NotRequired["capo_kafka.types.__integer.__integer"]
    """<p>Partition count for a topic.</p>"""
    out_of_sync_replica_count: NotRequired["capo_kafka.types.__integer.__integer"]
    """<p>Number of out-of-sync replicas for a topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicInfo) -> dict:
    out: dict = {}
    if "topic_arn" in value:
        out["topicArn"] = value["topic_arn"]
    if "topic_name" in value:
        out["topicName"] = value["topic_name"]
    if "replication_factor" in value:
        out["replicationFactor"] = value["replication_factor"]
    if "partition_count" in value:
        out["partitionCount"] = value["partition_count"]
    if "out_of_sync_replica_count" in value:
        out["outOfSyncReplicaCount"] = value["out_of_sync_replica_count"]
    return out


def deserialize_json(data: dict) -> TopicInfo:
    out: TopicInfo = {}  # type: ignore[typeddict-item]
    if data.get("topicArn") is not None:
        out["topic_arn"] = data["topicArn"]
    if data.get("topicName") is not None:
        out["topic_name"] = data["topicName"]
    if data.get("replicationFactor") is not None:
        out["replication_factor"] = data["replicationFactor"]
    if data.get("partitionCount") is not None:
        out["partition_count"] = data["partitionCount"]
    if data.get("outOfSyncReplicaCount") is not None:
        out["out_of_sync_replica_count"] = data["outOfSyncReplicaCount"]
    return out
