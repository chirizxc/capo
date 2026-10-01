"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MppPaymentCredential``."""

from typing import TypeAlias

"""<p>Ready-to-send <code>Authorization: Payment &lt;base64url-token&gt;</code> value. This is a bearer-like payment credential and must not appear in logs, traces, or error messages.</p>"""
MppPaymentCredential: TypeAlias = str
