"""Generated from Smithy shape ``com.amazonaws.odb#WalletPasswordSourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.wallet_password_source
    import capo_odb.types.wallet_password_source_configuration


class WalletPasswordSourceSummary(TypedDict, closed=True):
    password_source: NotRequired[
        "capo_odb.types.wallet_password_source.WalletPasswordSource"
    ]
    """<p>The source of the password for the Autonomous Database wallet.</p>"""
    password_source_configuration: NotRequired[
        "capo_odb.types.wallet_password_source_configuration.WalletPasswordSourceConfiguration"
    ]
    """<p>The configuration of the password source for the Autonomous Database wallet.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WalletPasswordSourceSummary) -> dict:
    out: dict = {}
    if "password_source" in value:
        import capo_odb.types.wallet_password_source

        out["passwordSource"] = (
            capo_odb.types.wallet_password_source.serialize_aws_json_1_0(
                value["password_source"]
            )
        )
    if "password_source_configuration" in value:
        import capo_odb.types.wallet_password_source_configuration

        out["passwordSourceConfiguration"] = (
            capo_odb.types.wallet_password_source_configuration.serialize_aws_json_1_0(
                value["password_source_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WalletPasswordSourceSummary:
    out: WalletPasswordSourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("passwordSource") is not None:
        import capo_odb.types.wallet_password_source

        out["password_source"] = (
            capo_odb.types.wallet_password_source.deserialize_aws_json_1_0(
                data["passwordSource"]
            )
        )
    if data.get("passwordSourceConfiguration") is not None:
        import capo_odb.types.wallet_password_source_configuration

        out["password_source_configuration"] = (
            capo_odb.types.wallet_password_source_configuration.deserialize_aws_json_1_0(
                data["passwordSourceConfiguration"]
            )
        )
    return out
