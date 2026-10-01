"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchWriteRecordEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn
    import capo_sagemaker_featurestore_runtime.types.record
    import capo_sagemaker_featurestore_runtime.types.target_stores
    import capo_sagemaker_featurestore_runtime.types.ttl_duration


class BatchWriteRecordEntry(TypedDict, closed=True):
    feature_group_name: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the <code>FeatureGroup</code> to write the record to.</p>"""
    record: NotRequired["capo_sagemaker_featurestore_runtime.types.record.Record"]
    """<p>List of FeatureValues to be inserted. This will be a full over-write.</p>"""
    target_stores: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.target_stores.TargetStores"
    ]
    """<p>A list of stores to which you're adding the record. By default, Feature Store adds the record to all of the stores that you're using for the <code>FeatureGroup</code>.</p>"""
    ttl_duration: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.ttl_duration.TtlDuration"
    ]
    """<p>Time to live duration for this entry, where the record is hard deleted after the expiration time is reached; <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>. This overrides the request level <code>TtlDuration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteRecordEntry) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "record" in value:
        import capo_sagemaker_featurestore_runtime.types.record

        out["Record"] = capo_sagemaker_featurestore_runtime.types.record.serialize_json(
            value["record"]
        )
    if "target_stores" in value:
        import capo_sagemaker_featurestore_runtime.types.target_stores

        out["TargetStores"] = (
            capo_sagemaker_featurestore_runtime.types.target_stores.serialize_json(
                value["target_stores"]
            )
        )
    if "ttl_duration" in value:
        import capo_sagemaker_featurestore_runtime.types.ttl_duration

        out["TtlDuration"] = (
            capo_sagemaker_featurestore_runtime.types.ttl_duration.serialize_json(
                value["ttl_duration"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchWriteRecordEntry:
    out: BatchWriteRecordEntry = {}  # type: ignore[typeddict-item]
    if data.get("FeatureGroupName") is not None:
        out["feature_group_name"] = data["FeatureGroupName"]
    if data.get("Record") is not None:
        import capo_sagemaker_featurestore_runtime.types.record

        out["record"] = (
            capo_sagemaker_featurestore_runtime.types.record.deserialize_json(
                data["Record"]
            )
        )
    if data.get("TargetStores") is not None:
        import capo_sagemaker_featurestore_runtime.types.target_stores

        out["target_stores"] = (
            capo_sagemaker_featurestore_runtime.types.target_stores.deserialize_json(
                data["TargetStores"]
            )
        )
    if data.get("TtlDuration") is not None:
        import capo_sagemaker_featurestore_runtime.types.ttl_duration

        out["ttl_duration"] = (
            capo_sagemaker_featurestore_runtime.types.ttl_duration.deserialize_json(
                data["TtlDuration"]
            )
        )
    return out
