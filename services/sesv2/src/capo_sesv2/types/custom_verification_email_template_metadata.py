"""Generated from Smithy shape ``com.amazonaws.sesv2#CustomVerificationEmailTemplateMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address
    import capo_sesv2.types.email_template_name
    import capo_sesv2.types.email_template_subject
    import capo_sesv2.types.failure_redirection_url
    import capo_sesv2.types.success_redirection_url


class CustomVerificationEmailTemplateMetadata(TypedDict, closed=True):
    template_name: NotRequired["capo_sesv2.types.email_template_name.EmailTemplateName"]
    """<p>The name of the custom verification email template.</p>"""
    from_email_address: NotRequired["capo_sesv2.types.email_address.EmailAddress"]
    """<p>The email address that the custom verification email is sent from.</p>"""
    template_subject: NotRequired[
        "capo_sesv2.types.email_template_subject.EmailTemplateSubject"
    ]
    """<p>The subject line of the custom verification email.</p>"""
    success_redirection_url: NotRequired[
        "capo_sesv2.types.success_redirection_url.SuccessRedirectionURL"
    ]
    """<p>The URL that the recipient of the verification email is sent to if his or her address is successfully verified.</p>"""
    failure_redirection_url: NotRequired[
        "capo_sesv2.types.failure_redirection_url.FailureRedirectionURL"
    ]
    """<p>The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomVerificationEmailTemplateMetadata) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "from_email_address" in value:
        out["FromEmailAddress"] = value["from_email_address"]
    if "template_subject" in value:
        out["TemplateSubject"] = value["template_subject"]
    if "success_redirection_url" in value:
        out["SuccessRedirectionURL"] = value["success_redirection_url"]
    if "failure_redirection_url" in value:
        out["FailureRedirectionURL"] = value["failure_redirection_url"]
    return out


def deserialize_json(data: dict) -> CustomVerificationEmailTemplateMetadata:
    out: CustomVerificationEmailTemplateMetadata = {}  # type: ignore[typeddict-item]
    if data.get("TemplateName") is not None:
        out["template_name"] = data["TemplateName"]
    if data.get("FromEmailAddress") is not None:
        out["from_email_address"] = data["FromEmailAddress"]
    if data.get("TemplateSubject") is not None:
        out["template_subject"] = data["TemplateSubject"]
    if data.get("SuccessRedirectionURL") is not None:
        out["success_redirection_url"] = data["SuccessRedirectionURL"]
    if data.get("FailureRedirectionURL") is not None:
        out["failure_redirection_url"] = data["FailureRedirectionURL"]
    return out
