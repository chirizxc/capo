"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AppflowIntegrationWorkflowMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.long


class AppflowIntegrationWorkflowMetrics(TypedDict, closed=True):
    records_processed: "capo_customer_profiles.types.long.long"
    """<p>Number of records processed in <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    steps_completed: "capo_customer_profiles.types.long.long"
    """<p>Total steps completed in <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    total_steps: "capo_customer_profiles.types.long.long"
    """<p>Total steps in <code>APPFLOW_INTEGRATION</code> workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppflowIntegrationWorkflowMetrics) -> dict:
    out: dict = {}
    out["RecordsProcessed"] = value.get("records_processed", 0)
    out["StepsCompleted"] = value.get("steps_completed", 0)
    out["TotalSteps"] = value.get("total_steps", 0)
    return out


def deserialize_json(data: dict) -> AppflowIntegrationWorkflowMetrics:
    out: AppflowIntegrationWorkflowMetrics = {}  # type: ignore[typeddict-item]
    if data.get("RecordsProcessed") is not None:
        out["records_processed"] = data["RecordsProcessed"]
    else:
        out["records_processed"] = 0
    if data.get("StepsCompleted") is not None:
        out["steps_completed"] = data["StepsCompleted"]
    else:
        out["steps_completed"] = 0
    if data.get("TotalSteps") is not None:
        out["total_steps"] = data["TotalSteps"]
    else:
        out["total_steps"] = 0
    return out
