"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DomainPackageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.domain_package_status
    import capo_elasticsearch_service.types.error_details
    import capo_elasticsearch_service.types.last_updated
    import capo_elasticsearch_service.types.package_id
    import capo_elasticsearch_service.types.package_name
    import capo_elasticsearch_service.types.package_type
    import capo_elasticsearch_service.types.package_version
    import capo_elasticsearch_service.types.reference_path


class DomainPackageDetails(TypedDict, closed=True):
    package_id: NotRequired["capo_elasticsearch_service.types.package_id.PackageID"]
    """<p>Internal ID of the package.</p>"""
    package_name: NotRequired[
        "capo_elasticsearch_service.types.package_name.PackageName"
    ]
    """<p>User specified name of the package.</p>"""
    package_type: NotRequired[
        "capo_elasticsearch_service.types.package_type.PackageType"
    ]
    """<p>Currently supports only TXT-DICTIONARY.</p>"""
    last_updated: NotRequired[
        "capo_elasticsearch_service.types.last_updated.LastUpdated"
    ]
    """<p>Timestamp of the most-recent update to the association status.</p>"""
    domain_name: NotRequired["capo_elasticsearch_service.types.domain_name.DomainName"]
    """<p>Name of the domain you've associated a package with.</p>"""
    domain_package_status: NotRequired[
        "capo_elasticsearch_service.types.domain_package_status.DomainPackageStatus"
    ]
    """<p>State of the association. Values are ASSOCIATING/ASSOCIATION_FAILED/ACTIVE/DISSOCIATING/DISSOCIATION_FAILED.</p>"""
    package_version: NotRequired[
        "capo_elasticsearch_service.types.package_version.PackageVersion"
    ]
    reference_path: NotRequired[
        "capo_elasticsearch_service.types.reference_path.ReferencePath"
    ]
    """<p>The relative path on Amazon ES nodes, which can be used as synonym_path when the package is synonym file.</p>"""
    error_details: NotRequired[
        "capo_elasticsearch_service.types.error_details.ErrorDetails"
    ]
    """<p>Additional information if the package is in an error state. Null otherwise.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainPackageDetails) -> dict:
    out: dict = {}
    if "package_id" in value:
        out["PackageID"] = value["package_id"]
    if "package_name" in value:
        out["PackageName"] = value["package_name"]
    if "package_type" in value:
        import capo_elasticsearch_service.types.package_type

        out["PackageType"] = (
            capo_elasticsearch_service.types.package_type.serialize_json(
                value["package_type"]
            )
        )
    if "last_updated" in value:
        import capo_elasticsearch_service.types.last_updated

        out["LastUpdated"] = (
            capo_elasticsearch_service.types.last_updated.serialize_json(
                value["last_updated"]
            )
        )
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "domain_package_status" in value:
        import capo_elasticsearch_service.types.domain_package_status

        out["DomainPackageStatus"] = (
            capo_elasticsearch_service.types.domain_package_status.serialize_json(
                value["domain_package_status"]
            )
        )
    if "package_version" in value:
        out["PackageVersion"] = value["package_version"]
    if "reference_path" in value:
        out["ReferencePath"] = value["reference_path"]
    if "error_details" in value:
        import capo_elasticsearch_service.types.error_details

        out["ErrorDetails"] = (
            capo_elasticsearch_service.types.error_details.serialize_json(
                value["error_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> DomainPackageDetails:
    out: DomainPackageDetails = {}  # type: ignore[typeddict-item]
    if data.get("PackageID") is not None:
        out["package_id"] = data["PackageID"]
    if data.get("PackageName") is not None:
        out["package_name"] = data["PackageName"]
    if data.get("PackageType") is not None:
        import capo_elasticsearch_service.types.package_type

        out["package_type"] = (
            capo_elasticsearch_service.types.package_type.deserialize_json(
                data["PackageType"]
            )
        )
    if data.get("LastUpdated") is not None:
        import capo_elasticsearch_service.types.last_updated

        out["last_updated"] = (
            capo_elasticsearch_service.types.last_updated.deserialize_json(
                data["LastUpdated"]
            )
        )
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("DomainPackageStatus") is not None:
        import capo_elasticsearch_service.types.domain_package_status

        out["domain_package_status"] = (
            capo_elasticsearch_service.types.domain_package_status.deserialize_json(
                data["DomainPackageStatus"]
            )
        )
    if data.get("PackageVersion") is not None:
        out["package_version"] = data["PackageVersion"]
    if data.get("ReferencePath") is not None:
        out["reference_path"] = data["ReferencePath"]
    if data.get("ErrorDetails") is not None:
        import capo_elasticsearch_service.types.error_details

        out["error_details"] = (
            capo_elasticsearch_service.types.error_details.deserialize_json(
                data["ErrorDetails"]
            )
        )
    return out
