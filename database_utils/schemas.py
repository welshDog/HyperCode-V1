"""Pydantic schemas for agent payloads/results to improve validation."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class DocumentRetrievalPayload(BaseModel):
    task_id: int
    query: str
    sources: List[str] = Field(default_factory=lambda: ["arxiv", "pubmed"])
    limit: int = 10


class FilterPayload(BaseModel):
    task_id: int
    content: str
    threshold: float = 0.5


class SummarizePayload(BaseModel):
    task_id: int
    content: str
    length: str = "medium"


class Entity(BaseModel):
    node_type: str
    label: str
    canonical_form: Optional[str] = None
    description: Optional[str] = None
    confidence_score: Optional[float] = None
    properties: Dict[str, Any] = Field(default_factory=dict)


class Relationship(BaseModel):
    relationship_type: str
    source_label: str
    target_label: str
    confidence_score: Optional[float] = None
    properties: Dict[str, Any] = Field(default_factory=dict)


class ExtractionResult(BaseModel):
    task_id: int
    entities: List[Entity] = Field(default_factory=list)
    relationships: List[Relationship] = Field(default_factory=list)

