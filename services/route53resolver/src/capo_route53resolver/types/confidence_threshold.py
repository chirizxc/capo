"""Generated from Smithy shape ``com.amazonaws.route53resolver#ConfidenceThreshold``."""

from typing import Literal, TypeAlias, cast

"""<p>The confidence threshold for a DNS Firewall Advanced rule. One of:</p> <ul> <li> <p> <code>LOW</code> — Provides the highest detection rate for threats, but also increases false positives.</p> </li> <li> <p> <code>MEDIUM</code> — Provides a balance between detecting threats and false positives.</p> </li> <li> <p> <code>HIGH</code> — Detects only the most well-corroborated threats with a low rate of false positives.</p> </li> </ul>"""
ConfidenceThreshold: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfidenceThreshold) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfidenceThreshold:
    return cast(ConfidenceThreshold, data)
