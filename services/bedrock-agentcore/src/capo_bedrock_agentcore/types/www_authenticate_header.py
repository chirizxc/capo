"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#WwwAuthenticateHeader``."""

from typing import TypeAlias

"""<p>A raw <code>WWW-Authenticate: Payment</code> header value from a 402 response, containing RFC 9110 auth-params such as <code>id</code>, <code>realm</code>, <code>method</code>, <code>intent</code>, and <code>request</code>. Pass this value in the request body, not as an HTTP header.</p>"""
WwwAuthenticateHeader: TypeAlias = str
