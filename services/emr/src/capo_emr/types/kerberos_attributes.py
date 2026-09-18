"""Generated from Smithy shape ``com.amazonaws.emr#KerberosAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.xml_string_max_len256


class KerberosAttributes(TypedDict, closed=True):
    realm: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the Kerberos realm to which all nodes in a cluster belong. For example, <code>EC2.INTERNAL</code>. </p>"""
    kdc_admin_password: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster.</p>"""
    cross_realm_trust_principal_password: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms.</p>"""
    ad_domain_join_user: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain.</p>"""
    ad_domain_join_password: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The Active Directory password for <code>ADDomainJoinUser</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KerberosAttributes) -> dict:
    out: dict = {}
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "kdc_admin_password" in value:
        out["KdcAdminPassword"] = value["kdc_admin_password"]
    if "cross_realm_trust_principal_password" in value:
        out["CrossRealmTrustPrincipalPassword"] = value[
            "cross_realm_trust_principal_password"
        ]
    if "ad_domain_join_user" in value:
        out["ADDomainJoinUser"] = value["ad_domain_join_user"]
    if "ad_domain_join_password" in value:
        out["ADDomainJoinPassword"] = value["ad_domain_join_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KerberosAttributes:
    out: KerberosAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Realm") is not None:
        out["realm"] = data["Realm"]
    if data.get("KdcAdminPassword") is not None:
        out["kdc_admin_password"] = data["KdcAdminPassword"]
    if data.get("CrossRealmTrustPrincipalPassword") is not None:
        out["cross_realm_trust_principal_password"] = data[
            "CrossRealmTrustPrincipalPassword"
        ]
    if data.get("ADDomainJoinUser") is not None:
        out["ad_domain_join_user"] = data["ADDomainJoinUser"]
    if data.get("ADDomainJoinPassword") is not None:
        out["ad_domain_join_password"] = data["ADDomainJoinPassword"]
    return out
