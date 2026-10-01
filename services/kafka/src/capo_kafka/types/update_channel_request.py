"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.iceberg_destination_update
    import capo_kafka.types.s3_destination_update


class UpdateChannelRequest(TypedDict, closed=True):
    channel_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the channel.</p>"""
    cluster_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    iceberg_destination_update: NotRequired[
        "capo_kafka.types.iceberg_destination_update.IcebergDestinationUpdate"
    ]
    """<p>Updates fields on an Apache Iceberg destination. Use only when the channel was created with an Iceberg destination.</p>"""
    s3_destination_update: NotRequired[
        "capo_kafka.types.s3_destination_update.S3DestinationUpdate"
    ]
    """<p>Updates fields on an Amazon S3 destination. Use only when the channel was created with an Amazon S3 destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelRequest) -> dict:
    out: dict = {}
    if "iceberg_destination_update" in value:
        import capo_kafka.types.iceberg_destination_update

        out["icebergDestinationUpdate"] = (
            capo_kafka.types.iceberg_destination_update.serialize_json(
                value["iceberg_destination_update"]
            )
        )
    if "s3_destination_update" in value:
        import capo_kafka.types.s3_destination_update

        out["s3DestinationUpdate"] = (
            capo_kafka.types.s3_destination_update.serialize_json(
                value["s3_destination_update"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("icebergDestinationUpdate") is not None:
        import capo_kafka.types.iceberg_destination_update

        out["iceberg_destination_update"] = (
            capo_kafka.types.iceberg_destination_update.deserialize_json(
                data["icebergDestinationUpdate"]
            )
        )
    if data.get("s3DestinationUpdate") is not None:
        import capo_kafka.types.s3_destination_update

        out["s3_destination_update"] = (
            capo_kafka.types.s3_destination_update.deserialize_json(
                data["s3DestinationUpdate"]
            )
        )
    return out
