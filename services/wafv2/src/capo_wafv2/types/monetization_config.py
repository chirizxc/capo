"""Generated from Smithy shape ``com.amazonaws.wafv2#MonetizationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.crypto_config
    import capo_wafv2.types.currency_mode


class MonetizationConfig(TypedDict, closed=True):
    crypto_config: NotRequired["capo_wafv2.types.crypto_config.CryptoConfig"]
    """<p>The cryptocurrency payment configuration, including the blockchain networks and wallet addresses where you receive payments.</p>"""
    currency_mode: NotRequired["capo_wafv2.types.currency_mode.CurrencyMode"]
    """<p>Specifies whether the configuration uses real or test currency. Set to <code>REAL</code> to settle payments in USDC on production blockchain networks (Base, Solana). Set to <code>TEST</code> to settle on testnet networks (Base Sepolia, Solana Devnet) with tokens that have no monetary value. If not specified, defaults to <code>REAL</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonetizationConfig) -> dict:
    out: dict = {}
    if "crypto_config" in value:
        import capo_wafv2.types.crypto_config

        out["CryptoConfig"] = capo_wafv2.types.crypto_config.serialize_aws_json_1_1(
            value["crypto_config"]
        )
    if "currency_mode" in value:
        import capo_wafv2.types.currency_mode

        out["CurrencyMode"] = capo_wafv2.types.currency_mode.serialize_aws_json_1_1(
            value["currency_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonetizationConfig:
    out: MonetizationConfig = {}  # type: ignore[typeddict-item]
    if data.get("CryptoConfig") is not None:
        import capo_wafv2.types.crypto_config

        out["crypto_config"] = capo_wafv2.types.crypto_config.deserialize_aws_json_1_1(
            data["CryptoConfig"]
        )
    if data.get("CurrencyMode") is not None:
        import capo_wafv2.types.currency_mode

        out["currency_mode"] = capo_wafv2.types.currency_mode.deserialize_aws_json_1_1(
            data["CurrencyMode"]
        )
    return out
