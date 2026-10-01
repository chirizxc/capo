"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateIntegrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.integration


class UpdateIntegrationOutput(TypedDict, closed=True):
    integration: NotRequired["capo_cloudwatchomni.types.integration.Integration"]
    """The details of the updated integration. This is the same object returned by GetIntegration and CreateIntegration. Populated on a successful update; absent only if the post-update read-back of the resource did not complete."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateIntegrationOutput) -> dict:
    out: dict = {}
    if "integration" in value:
        import capo_cloudwatchomni.types.integration

        out["integration"] = capo_cloudwatchomni.types.integration.serialize_cbor(
            value["integration"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdateIntegrationOutput:
    out: UpdateIntegrationOutput = {}  # type: ignore[typeddict-item]
    if data.get("integration") is not None:
        import capo_cloudwatchomni.types.integration

        out["integration"] = capo_cloudwatchomni.types.integration.deserialize_cbor(
            data["integration"]
        )
    return out
