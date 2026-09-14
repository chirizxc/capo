"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.arn
    import capo_codeartifact.types.description
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.package_group_contact_info
    import capo_codeartifact.types.package_group_origin_configuration
    import capo_codeartifact.types.package_group_pattern
    import capo_codeartifact.types.package_group_reference
    import capo_codeartifact.types.timestamp


class PackageGroupSummary(TypedDict, closed=True):
    arn: NotRequired["capo_codeartifact.types.arn.Arn"]
    """<p> The ARN of the package group. </p>"""
    pattern: NotRequired[
        "capo_codeartifact.types.package_group_pattern.PackageGroupPattern"
    ]
    """<p> The pattern of the package group. The pattern determines which packages are associated with the package group. </p>"""
    domain_name: NotRequired["capo_codeartifact.types.domain_name.DomainName"]
    """<p> The domain that contains the package group. </p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    created_time: NotRequired["capo_codeartifact.types.timestamp.Timestamp"]
    """<p>A timestamp that represents the date and time the repository was created.</p>"""
    contact_info: NotRequired[
        "capo_codeartifact.types.package_group_contact_info.PackageGroupContactInfo"
    ]
    """<p> The contact information of the package group. </p>"""
    description: NotRequired["capo_codeartifact.types.description.Description"]
    """<p> The description of the package group. </p>"""
    origin_configuration: NotRequired[
        "capo_codeartifact.types.package_group_origin_configuration.PackageGroupOriginConfiguration"
    ]
    """<p>Details about the package origin configuration of a package group.</p>"""
    parent: NotRequired[
        "capo_codeartifact.types.package_group_reference.PackageGroupReference"
    ]
    """<p> The direct parent package group of the package group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "pattern" in value:
        out["pattern"] = value["pattern"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "domain_owner" in value:
        out["domainOwner"] = value["domain_owner"]
    if "created_time" in value:
        import capo_codeartifact.types.timestamp

        out["createdTime"] = capo_codeartifact.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "contact_info" in value:
        out["contactInfo"] = value["contact_info"]
    if "description" in value:
        out["description"] = value["description"]
    if "origin_configuration" in value:
        import capo_codeartifact.types.package_group_origin_configuration

        out["originConfiguration"] = (
            capo_codeartifact.types.package_group_origin_configuration.serialize_json(
                value["origin_configuration"]
            )
        )
    if "parent" in value:
        import capo_codeartifact.types.package_group_reference

        out["parent"] = capo_codeartifact.types.package_group_reference.serialize_json(
            value["parent"]
        )
    return out


def deserialize_json(data: dict) -> PackageGroupSummary:
    out: PackageGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("pattern") is not None:
        out["pattern"] = data["pattern"]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("domainOwner") is not None:
        out["domain_owner"] = data["domainOwner"]
    if data.get("createdTime") is not None:
        import capo_codeartifact.types.timestamp

        out["created_time"] = capo_codeartifact.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    if data.get("contactInfo") is not None:
        out["contact_info"] = data["contactInfo"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("originConfiguration") is not None:
        import capo_codeartifact.types.package_group_origin_configuration

        out["origin_configuration"] = (
            capo_codeartifact.types.package_group_origin_configuration.deserialize_json(
                data["originConfiguration"]
            )
        )
    if data.get("parent") is not None:
        import capo_codeartifact.types.package_group_reference

        out["parent"] = (
            capo_codeartifact.types.package_group_reference.deserialize_json(
                data["parent"]
            )
        )
    return out
