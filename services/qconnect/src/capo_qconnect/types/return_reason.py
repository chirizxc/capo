"""Generated from Smithy shape ``com.amazonaws.qconnect#ReturnReason``."""

from typing import TypeAlias

"""<p>The reason a sub-agent returned control to the calling agent.</p> <ul> <li> <p> <code>COMPLETE</code> – the request was fulfilled.</p> </li> <li> <p> <code>COMPLETE_WITH_ERROR</code> – the sub-agent attempted the request but could not fully complete it.</p> </li> <li> <p> <code>ESCALATE</code> – the conversation should be transferred to a human agent.</p> </li> <li> <p> <code>OUT_OF_DOMAIN</code> – the request fell outside the sub-agent's domain of expertise.</p> </li> </ul>"""
ReturnReason: TypeAlias = str
