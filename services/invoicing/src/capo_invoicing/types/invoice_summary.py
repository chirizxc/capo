"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_invoicing.types.account_id_string
    import capo_invoicing.types.basic_string
    import capo_invoicing.types.bill_source_account_list
    import capo_invoicing.types.bill_type
    import capo_invoicing.types.billing_period
    import capo_invoicing.types.einvoice_delivery_status
    import capo_invoicing.types.entity
    import capo_invoicing.types.invoice_currency_amount
    import capo_invoicing.types.invoice_frequency
    import capo_invoicing.types.invoice_type
    import capo_invoicing.types.receiver_role
    import capo_invoicing.types.tax_authority_status


class InvoiceSummary(TypedDict, closed=True):
    account_id: NotRequired["capo_invoicing.types.account_id_string.AccountIdString"]
    """<p> The Amazon Web Services account ID. </p>"""
    invoice_id: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> The invoice ID. </p>"""
    issued_date: NotRequired["datetime.datetime"]
    """<p> The issued date of the invoice. </p>"""
    due_date: NotRequired["datetime.datetime"]
    """<p> The invoice due date. </p>"""
    bill_source_accounts: NotRequired[
        "capo_invoicing.types.bill_source_account_list.BillSourceAccountList"
    ]
    """<p> The list of Amazon Web Services account IDs that are the bill source of the invoice. Currently, only a single bill source account is returned.</p>"""
    bill_source_accounts_total_count: NotRequired["int"]
    """<p> The total number of accounts that are the bill source of the invoice. </p>"""
    receiver_role: NotRequired["capo_invoicing.types.receiver_role.ReceiverRole"]
    """<p>The role of the invoice receiver.</p>"""
    entity: NotRequired["capo_invoicing.types.entity.Entity"]
    """<p>The organization name providing Amazon Web Services services.</p>"""
    billing_period: NotRequired["capo_invoicing.types.billing_period.BillingPeriod"]
    """<p> The billing period of the invoice-related document. </p>"""
    invoice_frequency: NotRequired[
        "capo_invoicing.types.invoice_frequency.InvoiceFrequency"
    ]
    """<p> The frequency of the invoice. </p>"""
    bill_type: NotRequired["capo_invoicing.types.bill_type.BillType"]
    """<p> The type of the bill. </p>"""
    invoice_type: NotRequired["capo_invoicing.types.invoice_type.InvoiceType"]
    """<p> The type of invoice. </p>"""
    commercial_invoice_id: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> The commercial invoice ID. This is only applicable for tax invoices and identifies the associated commercial invoice. </p>"""
    original_invoice_id: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p>The initial or original invoice ID. </p>"""
    purchase_order_number: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> The purchase order number associated to the invoice.</p>"""
    einvoice_delivery_status: NotRequired[
        "capo_invoicing.types.einvoice_delivery_status.EinvoiceDeliveryStatus"
    ]
    """<p> The e-invoice delivery status. </p>"""
    tax_authority_status: NotRequired[
        "capo_invoicing.types.tax_authority_status.TaxAuthorityStatus"
    ]
    """<p> The current status of an invoice as reported to the tax authority. This captures scenarios where an invoice may be cancelled after issuance. </p>"""
    base_currency_amount: NotRequired[
        "capo_invoicing.types.invoice_currency_amount.InvoiceCurrencyAmount"
    ]
    """<p> The summary with the product and service currency. </p>"""
    tax_currency_amount: NotRequired[
        "capo_invoicing.types.invoice_currency_amount.InvoiceCurrencyAmount"
    ]
    """<p> The summary with the tax currency. </p>"""
    payment_currency_amount: NotRequired[
        "capo_invoicing.types.invoice_currency_amount.InvoiceCurrencyAmount"
    ]
    """<p> The summary with the customer configured currency. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceSummary) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "invoice_id" in value:
        out["InvoiceId"] = value["invoice_id"]
    if "issued_date" in value:
        import capo_invoicing.types._prelude.timestamp

        out["IssuedDate"] = (
            capo_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["issued_date"]
            )
        )
    if "due_date" in value:
        import capo_invoicing.types._prelude.timestamp

        out["DueDate"] = capo_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["due_date"]
        )
    if "bill_source_accounts" in value:
        import capo_invoicing.types.bill_source_account_list

        out["BillSourceAccounts"] = (
            capo_invoicing.types.bill_source_account_list.serialize_aws_json_1_0(
                value["bill_source_accounts"]
            )
        )
    if "bill_source_accounts_total_count" in value:
        out["BillSourceAccountsTotalCount"] = value["bill_source_accounts_total_count"]
    if "receiver_role" in value:
        import capo_invoicing.types.receiver_role

        out["ReceiverRole"] = capo_invoicing.types.receiver_role.serialize_aws_json_1_0(
            value["receiver_role"]
        )
    if "entity" in value:
        import capo_invoicing.types.entity

        out["Entity"] = capo_invoicing.types.entity.serialize_aws_json_1_0(
            value["entity"]
        )
    if "billing_period" in value:
        import capo_invoicing.types.billing_period

        out["BillingPeriod"] = (
            capo_invoicing.types.billing_period.serialize_aws_json_1_0(
                value["billing_period"]
            )
        )
    if "invoice_frequency" in value:
        import capo_invoicing.types.invoice_frequency

        out["InvoiceFrequency"] = (
            capo_invoicing.types.invoice_frequency.serialize_aws_json_1_0(
                value["invoice_frequency"]
            )
        )
    if "bill_type" in value:
        import capo_invoicing.types.bill_type

        out["BillType"] = capo_invoicing.types.bill_type.serialize_aws_json_1_0(
            value["bill_type"]
        )
    if "invoice_type" in value:
        import capo_invoicing.types.invoice_type

        out["InvoiceType"] = capo_invoicing.types.invoice_type.serialize_aws_json_1_0(
            value["invoice_type"]
        )
    if "commercial_invoice_id" in value:
        out["CommercialInvoiceId"] = value["commercial_invoice_id"]
    if "original_invoice_id" in value:
        out["OriginalInvoiceId"] = value["original_invoice_id"]
    if "purchase_order_number" in value:
        out["PurchaseOrderNumber"] = value["purchase_order_number"]
    if "einvoice_delivery_status" in value:
        import capo_invoicing.types.einvoice_delivery_status

        out["EinvoiceDeliveryStatus"] = (
            capo_invoicing.types.einvoice_delivery_status.serialize_aws_json_1_0(
                value["einvoice_delivery_status"]
            )
        )
    if "tax_authority_status" in value:
        import capo_invoicing.types.tax_authority_status

        out["TaxAuthorityStatus"] = (
            capo_invoicing.types.tax_authority_status.serialize_aws_json_1_0(
                value["tax_authority_status"]
            )
        )
    if "base_currency_amount" in value:
        import capo_invoicing.types.invoice_currency_amount

        out["BaseCurrencyAmount"] = (
            capo_invoicing.types.invoice_currency_amount.serialize_aws_json_1_0(
                value["base_currency_amount"]
            )
        )
    if "tax_currency_amount" in value:
        import capo_invoicing.types.invoice_currency_amount

        out["TaxCurrencyAmount"] = (
            capo_invoicing.types.invoice_currency_amount.serialize_aws_json_1_0(
                value["tax_currency_amount"]
            )
        )
    if "payment_currency_amount" in value:
        import capo_invoicing.types.invoice_currency_amount

        out["PaymentCurrencyAmount"] = (
            capo_invoicing.types.invoice_currency_amount.serialize_aws_json_1_0(
                value["payment_currency_amount"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceSummary:
    out: InvoiceSummary = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("InvoiceId") is not None:
        out["invoice_id"] = data["InvoiceId"]
    if data.get("IssuedDate") is not None:
        import capo_invoicing.types._prelude.timestamp

        out["issued_date"] = (
            capo_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["IssuedDate"]
            )
        )
    if data.get("DueDate") is not None:
        import capo_invoicing.types._prelude.timestamp

        out["due_date"] = (
            capo_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["DueDate"]
            )
        )
    if data.get("BillSourceAccounts") is not None:
        import capo_invoicing.types.bill_source_account_list

        out["bill_source_accounts"] = (
            capo_invoicing.types.bill_source_account_list.deserialize_aws_json_1_0(
                data["BillSourceAccounts"]
            )
        )
    if data.get("BillSourceAccountsTotalCount") is not None:
        out["bill_source_accounts_total_count"] = data["BillSourceAccountsTotalCount"]
    if data.get("ReceiverRole") is not None:
        import capo_invoicing.types.receiver_role

        out["receiver_role"] = (
            capo_invoicing.types.receiver_role.deserialize_aws_json_1_0(
                data["ReceiverRole"]
            )
        )
    if data.get("Entity") is not None:
        import capo_invoicing.types.entity

        out["entity"] = capo_invoicing.types.entity.deserialize_aws_json_1_0(
            data["Entity"]
        )
    if data.get("BillingPeriod") is not None:
        import capo_invoicing.types.billing_period

        out["billing_period"] = (
            capo_invoicing.types.billing_period.deserialize_aws_json_1_0(
                data["BillingPeriod"]
            )
        )
    if data.get("InvoiceFrequency") is not None:
        import capo_invoicing.types.invoice_frequency

        out["invoice_frequency"] = (
            capo_invoicing.types.invoice_frequency.deserialize_aws_json_1_0(
                data["InvoiceFrequency"]
            )
        )
    if data.get("BillType") is not None:
        import capo_invoicing.types.bill_type

        out["bill_type"] = capo_invoicing.types.bill_type.deserialize_aws_json_1_0(
            data["BillType"]
        )
    if data.get("InvoiceType") is not None:
        import capo_invoicing.types.invoice_type

        out["invoice_type"] = (
            capo_invoicing.types.invoice_type.deserialize_aws_json_1_0(
                data["InvoiceType"]
            )
        )
    if data.get("CommercialInvoiceId") is not None:
        out["commercial_invoice_id"] = data["CommercialInvoiceId"]
    if data.get("OriginalInvoiceId") is not None:
        out["original_invoice_id"] = data["OriginalInvoiceId"]
    if data.get("PurchaseOrderNumber") is not None:
        out["purchase_order_number"] = data["PurchaseOrderNumber"]
    if data.get("EinvoiceDeliveryStatus") is not None:
        import capo_invoicing.types.einvoice_delivery_status

        out["einvoice_delivery_status"] = (
            capo_invoicing.types.einvoice_delivery_status.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryStatus"]
            )
        )
    if data.get("TaxAuthorityStatus") is not None:
        import capo_invoicing.types.tax_authority_status

        out["tax_authority_status"] = (
            capo_invoicing.types.tax_authority_status.deserialize_aws_json_1_0(
                data["TaxAuthorityStatus"]
            )
        )
    if data.get("BaseCurrencyAmount") is not None:
        import capo_invoicing.types.invoice_currency_amount

        out["base_currency_amount"] = (
            capo_invoicing.types.invoice_currency_amount.deserialize_aws_json_1_0(
                data["BaseCurrencyAmount"]
            )
        )
    if data.get("TaxCurrencyAmount") is not None:
        import capo_invoicing.types.invoice_currency_amount

        out["tax_currency_amount"] = (
            capo_invoicing.types.invoice_currency_amount.deserialize_aws_json_1_0(
                data["TaxCurrencyAmount"]
            )
        )
    if data.get("PaymentCurrencyAmount") is not None:
        import capo_invoicing.types.invoice_currency_amount

        out["payment_currency_amount"] = (
            capo_invoicing.types.invoice_currency_amount.deserialize_aws_json_1_0(
                data["PaymentCurrencyAmount"]
            )
        )
    return out
