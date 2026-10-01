"""Generated from Smithy shape ``com.amazonaws.qconnect#InteractionMode``."""

from typing import TypeAlias

"""<p>How an orchestrator agent engaged a collaborator agent.</p> <ul> <li> <p> <code>DELEGATE</code> indicates that the orchestrator invoked the collaborator agent and retained control of the conversation, resuming when the collaborator returns.</p> </li> <li> <p> <code>HANDOFF</code> indicates that the orchestrator transferred control of the conversation to the collaborator agent.</p> </li> </ul>"""
InteractionMode: TypeAlias = str
