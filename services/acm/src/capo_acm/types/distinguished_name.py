"""Generated from Smithy shape ``com.amazonaws.acm#DistinguishedName``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.custom_attribute_list
    import capo_acm.types.domain_component_list
    import capo_acm.types.string


class DistinguishedName(TypedDict, closed=True):
    common_name: NotRequired["capo_acm.types.string.String"]
    """<p>The common name (CN) attribute.</p>"""
    domain_components: NotRequired[
        "capo_acm.types.domain_component_list.DomainComponentList"
    ]
    """<p>The domain component attributes.</p>"""
    country: NotRequired["capo_acm.types.string.String"]
    """<p>The country (C) attribute.</p>"""
    custom_attributes: NotRequired[
        "capo_acm.types.custom_attribute_list.CustomAttributeList"
    ]
    """<p>A list of custom attributes in the distinguished name. Each custom attribute contains an object identifier (OID) and its corresponding value.</p>"""
    distinguished_name_qualifier: NotRequired["capo_acm.types.string.String"]
    """<p>The distinguished name qualifier attribute.</p>"""
    generation_qualifier: NotRequired["capo_acm.types.string.String"]
    """<p>The generation qualifier attribute.</p>"""
    given_name: NotRequired["capo_acm.types.string.String"]
    """<p>The given name attribute.</p>"""
    initials: NotRequired["capo_acm.types.string.String"]
    """<p>The initials attribute.</p>"""
    locality: NotRequired["capo_acm.types.string.String"]
    """<p>The locality (L) attribute.</p>"""
    organization: NotRequired["capo_acm.types.string.String"]
    """<p>The organization (O) attribute.</p>"""
    organizational_unit: NotRequired["capo_acm.types.string.String"]
    """<p>The organizational unit (OU) attribute.</p>"""
    pseudonym: NotRequired["capo_acm.types.string.String"]
    """<p>The pseudonym attribute.</p>"""
    serial_number: NotRequired["capo_acm.types.string.String"]
    """<p>The serial number attribute.</p>"""
    state: NotRequired["capo_acm.types.string.String"]
    """<p>The state or province (ST) attribute.</p>"""
    surname: NotRequired["capo_acm.types.string.String"]
    """<p>The surname attribute.</p>"""
    title: NotRequired["capo_acm.types.string.String"]
    """<p>The title attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistinguishedName) -> dict:
    out: dict = {}
    if "common_name" in value:
        out["CommonName"] = value["common_name"]
    if "domain_components" in value:
        import capo_acm.types.domain_component_list

        out["DomainComponents"] = (
            capo_acm.types.domain_component_list.serialize_aws_json_1_1(
                value["domain_components"]
            )
        )
    if "country" in value:
        out["Country"] = value["country"]
    if "custom_attributes" in value:
        import capo_acm.types.custom_attribute_list

        out["CustomAttributes"] = (
            capo_acm.types.custom_attribute_list.serialize_aws_json_1_1(
                value["custom_attributes"]
            )
        )
    if "distinguished_name_qualifier" in value:
        out["DistinguishedNameQualifier"] = value["distinguished_name_qualifier"]
    if "generation_qualifier" in value:
        out["GenerationQualifier"] = value["generation_qualifier"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "initials" in value:
        out["Initials"] = value["initials"]
    if "locality" in value:
        out["Locality"] = value["locality"]
    if "organization" in value:
        out["Organization"] = value["organization"]
    if "organizational_unit" in value:
        out["OrganizationalUnit"] = value["organizational_unit"]
    if "pseudonym" in value:
        out["Pseudonym"] = value["pseudonym"]
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "state" in value:
        out["State"] = value["state"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "title" in value:
        out["Title"] = value["title"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DistinguishedName:
    out: DistinguishedName = {}  # type: ignore[typeddict-item]
    if data.get("CommonName") is not None:
        out["common_name"] = data["CommonName"]
    if data.get("DomainComponents") is not None:
        import capo_acm.types.domain_component_list

        out["domain_components"] = (
            capo_acm.types.domain_component_list.deserialize_aws_json_1_1(
                data["DomainComponents"]
            )
        )
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("CustomAttributes") is not None:
        import capo_acm.types.custom_attribute_list

        out["custom_attributes"] = (
            capo_acm.types.custom_attribute_list.deserialize_aws_json_1_1(
                data["CustomAttributes"]
            )
        )
    if data.get("DistinguishedNameQualifier") is not None:
        out["distinguished_name_qualifier"] = data["DistinguishedNameQualifier"]
    if data.get("GenerationQualifier") is not None:
        out["generation_qualifier"] = data["GenerationQualifier"]
    if data.get("GivenName") is not None:
        out["given_name"] = data["GivenName"]
    if data.get("Initials") is not None:
        out["initials"] = data["Initials"]
    if data.get("Locality") is not None:
        out["locality"] = data["Locality"]
    if data.get("Organization") is not None:
        out["organization"] = data["Organization"]
    if data.get("OrganizationalUnit") is not None:
        out["organizational_unit"] = data["OrganizationalUnit"]
    if data.get("Pseudonym") is not None:
        out["pseudonym"] = data["Pseudonym"]
    if data.get("SerialNumber") is not None:
        out["serial_number"] = data["SerialNumber"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("Surname") is not None:
        out["surname"] = data["Surname"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    return out
