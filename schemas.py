from typing import List

from langchain_core.pydantic_v1 import BaseModel, Field


class Reflection(BaseModel):
    missing: str = Field(description="Critique of what is missing.")
    superfluos: str = Field(description="Critique of what is superfluos.")


class AnswerQuestion(BaseModel):
    """Answer the question."""

    search_queries: List[str] = Field(
        description="1-3 search queries for researching improvements to address the critique of your current answer."
    )
    answer: str = Field("~250 words detailed answer to the question.")
    reflection: Reflection = Field(description="Your reflection on the initial answer.")


class ReviseAnswer(AnswerQuestion):
    """Revise your original answer to your question."""

    reference: List[str] = Field(
        description="Citations motivating your updated answer."
    )
