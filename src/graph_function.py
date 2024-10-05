from typing import List

from langchain_core.messages import BaseMessage, ToolMessage
from langgraph.graph import MessageGraph, END

from src.chains import revisor, first_responder
from src.tool_executor import execute_tools
from src.const import MAX_ITERATIONS


def event_loop(state: List[BaseMessage]) -> str:
    """
    :param state: A list containing instances of messages, where BaseMessage and its derived classes (such as ToolMessage) are expected.
    :return: A string indicating the next action. Returns 'execute_tools' if the number of ToolMessage instances is within the allowed iterations, otherwise returns END.
    """
    count_tool_visit = sum(isinstance(item, ToolMessage) for item in state)
    num_iterations = count_tool_visit
    if num_iterations > MAX_ITERATIONS:
        return END
    return "execute_tools"


def build_reflexion_agent():
    """
    Builds a reflexion agent by constructing a message graph with specified nodes and edges.

    :return: An instance of `MessageGraph` representing the reflexion agent.
    """
    builder = MessageGraph()
    builder.add_node("draft", first_responder)
    builder.add_node("execute_tools", execute_tools)
    builder.add_node("revise", revisor)
    builder.add_edge("draft", "execute_tools")
    builder.add_edge("execute_tools", "revise")

    builder.add_conditional_edges("revise", event_loop)
    builder.set_entry_point("draft")

    return builder


app = build_reflexion_agent()
app = app.compile()
