"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StaticQueryParameterValue``."""

from typing import TypeAlias

"""<p>The value of a static query parameter. Control characters (ASCII <code>0x00</code>-<code>0x1F</code> and <code>0x7F</code>) are not permitted. URI-reserved characters are allowed and are percent-encoded by the gateway. Empty values are allowed.</p>"""
StaticQueryParameterValue: TypeAlias = str
