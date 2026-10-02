"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.einvoice_delivery_attachment_types
    import capo_invoicing.types.einvoice_delivery_document_types


class InvoiceConfiguration(TypedDict, closed=True):
    document_types: NotRequired[
        "capo_invoicing.types.einvoice_delivery_document_types.EinvoiceDeliveryDocumentTypes"
    ]
    """<p>The e-invoice document types supported by the procurement portal.</p>"""
    attachment_types: NotRequired[
        "capo_invoicing.types.einvoice_delivery_attachment_types.EinvoiceDeliveryAttachmentTypes"
    ]
    """<p>The attachment types supported by the procurement portal for e-invoice delivery.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceConfiguration) -> dict:
    out: dict = {}
    if "document_types" in value:
        import capo_invoicing.types.einvoice_delivery_document_types

        out["DocumentTypes"] = (
            capo_invoicing.types.einvoice_delivery_document_types.serialize_aws_json_1_0(
                value["document_types"]
            )
        )
    if "attachment_types" in value:
        import capo_invoicing.types.einvoice_delivery_attachment_types

        out["AttachmentTypes"] = (
            capo_invoicing.types.einvoice_delivery_attachment_types.serialize_aws_json_1_0(
                value["attachment_types"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceConfiguration:
    out: InvoiceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DocumentTypes") is not None:
        import capo_invoicing.types.einvoice_delivery_document_types

        out["document_types"] = (
            capo_invoicing.types.einvoice_delivery_document_types.deserialize_aws_json_1_0(
                data["DocumentTypes"]
            )
        )
    if data.get("AttachmentTypes") is not None:
        import capo_invoicing.types.einvoice_delivery_attachment_types

        out["attachment_types"] = (
            capo_invoicing.types.einvoice_delivery_attachment_types.deserialize_aws_json_1_0(
                data["AttachmentTypes"]
            )
        )
    return out
