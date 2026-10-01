"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#ExtractedInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.extracted_information_failure_code
    import capo_connect_contact_lens.types.extracted_information_values
    import capo_connect_contact_lens.types.extraction_definition_display_label
    import capo_connect_contact_lens.types.extraction_definition_id
    import capo_connect_contact_lens.types.extraction_definition_name


class ExtractedInformation(TypedDict, closed=True):
    extraction_definition_id: NotRequired[
        "capo_connect_contact_lens.types.extraction_definition_id.ExtractionDefinitionId"
    ]
    """<p>The identifier of the extraction definition that produced this result.</p>"""
    extraction_definition_name: NotRequired[
        "capo_connect_contact_lens.types.extraction_definition_name.ExtractionDefinitionName"
    ]
    """<p>The name of the extraction definition that produced this result.</p>"""
    extraction_definition_display_label: NotRequired[
        "capo_connect_contact_lens.types.extraction_definition_display_label.ExtractionDefinitionDisplayLabel"
    ]
    """<p>The display label of the extraction definition that produced this result.</p>"""
    extracted_values: NotRequired[
        "capo_connect_contact_lens.types.extracted_information_values.ExtractedInformationValues"
    ]
    """<p>The list of values extracted from the conversation for this extraction definition. This field is empty when a <code>FailureCode</code> is present.</p>"""
    failure_code: NotRequired[
        "capo_connect_contact_lens.types.extracted_information_failure_code.ExtractedInformationFailureCode"
    ]
    """<p>If the information failed to be extracted, one of the following failure codes occurs:</p> <ul> <li> <p> <code>QUOTA_EXCEEDED</code>: The number of concurrent analytics jobs reached your service quota.</p> </li> <li> <p> <code>INSUFFICIENT_CONVERSATION_CONTENT</code>: Information extraction requires a conversation with at least one turn from each participant.</p> </li> <li> <p> <code>FAILED_SAFETY_GUIDELINES</code>: The extracted information cannot be provided because it failed to meet system safety guidelines.</p> </li> <li> <p> <code>INTERNAL_ERROR</code>: Internal system error.</p> </li> <li> <p> <code>MAX_PACKAGE_FEATURE_ONLY</code>: Information extraction is only available in Amazon Connect Customer instances.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractedInformation) -> dict:
    out: dict = {}
    if "extraction_definition_id" in value:
        out["ExtractionDefinitionId"] = value["extraction_definition_id"]
    if "extraction_definition_name" in value:
        out["ExtractionDefinitionName"] = value["extraction_definition_name"]
    if "extraction_definition_display_label" in value:
        out["ExtractionDefinitionDisplayLabel"] = value[
            "extraction_definition_display_label"
        ]
    if "extracted_values" in value:
        import capo_connect_contact_lens.types.extracted_information_values

        out["ExtractedValues"] = (
            capo_connect_contact_lens.types.extracted_information_values.serialize_json(
                value["extracted_values"]
            )
        )
    if "failure_code" in value:
        import capo_connect_contact_lens.types.extracted_information_failure_code

        out["FailureCode"] = (
            capo_connect_contact_lens.types.extracted_information_failure_code.serialize_json(
                value["failure_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExtractedInformation:
    out: ExtractedInformation = {}  # type: ignore[typeddict-item]
    if data.get("ExtractionDefinitionId") is not None:
        out["extraction_definition_id"] = data["ExtractionDefinitionId"]
    if data.get("ExtractionDefinitionName") is not None:
        out["extraction_definition_name"] = data["ExtractionDefinitionName"]
    if data.get("ExtractionDefinitionDisplayLabel") is not None:
        out["extraction_definition_display_label"] = data[
            "ExtractionDefinitionDisplayLabel"
        ]
    if data.get("ExtractedValues") is not None:
        import capo_connect_contact_lens.types.extracted_information_values

        out["extracted_values"] = (
            capo_connect_contact_lens.types.extracted_information_values.deserialize_json(
                data["ExtractedValues"]
            )
        )
    if data.get("FailureCode") is not None:
        import capo_connect_contact_lens.types.extracted_information_failure_code

        out["failure_code"] = (
            capo_connect_contact_lens.types.extracted_information_failure_code.deserialize_json(
                data["FailureCode"]
            )
        )
    return out
