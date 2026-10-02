"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateOmniDashboardOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.omni_dashboard


class UpdateOmniDashboardOutput(TypedDict, closed=True):
    omni_dashboard: "capo_cloudwatchomni.types.omni_dashboard.OmniDashboard"
    """The dashboard."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateOmniDashboardOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.omni_dashboard

    out["omniDashboard"] = capo_cloudwatchomni.types.omni_dashboard.serialize_cbor(
        value["omni_dashboard"]
    )
    return out


def deserialize_cbor(data: dict) -> UpdateOmniDashboardOutput:
    out: UpdateOmniDashboardOutput = {}  # type: ignore[typeddict-item]
    if data.get("omniDashboard") is not None:
        import capo_cloudwatchomni.types.omni_dashboard

        out["omni_dashboard"] = (
            capo_cloudwatchomni.types.omni_dashboard.deserialize_cbor(
                data["omniDashboard"]
            )
        )
    else:
        raise DeserializationError("UpdateOmniDashboardOutput.omni_dashboard required")
    return out
