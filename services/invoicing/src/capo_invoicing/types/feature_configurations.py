"""Generated from Smithy shape ``com.amazonaws.invoicing#FeatureConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.invoice_configuration


class FeatureConfigurations(TypedDict, closed=True):
    invoice_configuration: NotRequired[
        "capo_invoicing.types.invoice_configuration.InvoiceConfiguration"
    ]
    """<p>The invoice configuration settings for the procurement portal.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FeatureConfigurations) -> dict:
    out: dict = {}
    if "invoice_configuration" in value:
        import capo_invoicing.types.invoice_configuration

        out["InvoiceConfiguration"] = (
            capo_invoicing.types.invoice_configuration.serialize_aws_json_1_0(
                value["invoice_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FeatureConfigurations:
    out: FeatureConfigurations = {}  # type: ignore[typeddict-item]
    if data.get("InvoiceConfiguration") is not None:
        import capo_invoicing.types.invoice_configuration

        out["invoice_configuration"] = (
            capo_invoicing.types.invoice_configuration.deserialize_aws_json_1_0(
                data["InvoiceConfiguration"]
            )
        )
    return out
