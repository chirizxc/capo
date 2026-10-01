"""Generated from Smithy shape ``com.amazonaws.amp#Destination``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_amp.types.amp_configuration
    import capo_amp.types.cloud_watch_configuration


class _Destination_ampConfiguration(TypedDict, closed=True):
    ampConfiguration: "capo_amp.types.amp_configuration.AmpConfiguration"


class _Destination_cloudWatchConfiguration(TypedDict, closed=True):
    cloudWatchConfiguration: (
        "capo_amp.types.cloud_watch_configuration.CloudWatchConfiguration"
    )


Destination: TypeAlias = (
    _Destination_ampConfiguration | _Destination_cloudWatchConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    if "ampConfiguration" in value:
        import capo_amp.types.amp_configuration

        return {
            "ampConfiguration": capo_amp.types.amp_configuration.serialize_json(
                value["ampConfiguration"]
            )
        }
    elif "cloudWatchConfiguration" in value:
        import capo_amp.types.cloud_watch_configuration

        return {
            "cloudWatchConfiguration": capo_amp.types.cloud_watch_configuration.serialize_json(
                value["cloudWatchConfiguration"]
            )
        }
    else:
        raise SerializationError("Destination: no variant present")


def deserialize_json(data: dict) -> Destination:
    if data.get("ampConfiguration") is not None:
        import capo_amp.types.amp_configuration

        return {
            "ampConfiguration": capo_amp.types.amp_configuration.deserialize_json(
                data["ampConfiguration"]
            )
        }
    elif data.get("cloudWatchConfiguration") is not None:
        import capo_amp.types.cloud_watch_configuration

        return {
            "cloudWatchConfiguration": capo_amp.types.cloud_watch_configuration.deserialize_json(
                data["cloudWatchConfiguration"]
            )
        }
    else:
        raise DeserializationError("Destination: no recognized variant key")
