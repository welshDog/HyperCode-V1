# models/core.py
import enum

from sqlalchemy import JSON, Column, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base, BaseModel


class NodeType(str, enum.Enum):
    """Types of nodes in the knowledge graph."""

    CONCEPT = "concept"
    PERSON = "person"
    TOOL = "tool"
    INSTITUTION = "institution"
    PAPER = "paper"
    CODE = "code"


class KnowledgeNode(Base, BaseModel):
    """Core entity in the knowledge graph."""

    __tablename__ = "knowledge_nodes"

    node_type = Column(String(50), nullable=False, index=True)
    label = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    metadata_ = Column("metadata", JSON, default=dict)

    # Relationships
    source_relationships = relationship(
        "KnowledgeRelationship",
        foreign_keys="KnowledgeRelationship.source_id",
        back_populates="source_node",
    )
    target_relationships = relationship(
        "KnowledgeRelationship",
        foreign_keys="KnowledgeRelationship.target_id",
        back_populates="target_node",
    )

    __table_args__ = (
        Index("idx_node_label_ft", "label"),
        Index("idx_node_metadata", "metadata"),
    )

    def __repr__(self) -> str:
        return f"<KnowledgeNode {self.node_type}:{self.label}>"


class KnowledgeRelationship(Base, BaseModel):
    """Relationship between knowledge nodes."""

    __tablename__ = "knowledge_relationships"

    source_id = Column(Integer, ForeignKey("knowledge_nodes.id"), nullable=False)
    target_id = Column(Integer, ForeignKey("knowledge_nodes.id"), nullable=False)
    relationship_type = Column(String(100), nullable=False, index=True)
    weight = Column(JSON, default=dict)

    # Relationships
    source_node = relationship(
        "KnowledgeNode", foreign_keys=[source_id], back_populates="source_relationships"
    )
    target_node = relationship(
        "KnowledgeNode", foreign_keys=[target_id], back_populates="target_relationships"
    )

    __table_args__ = (
        Index(
            "idx_relationship",
            "source_id",
            "target_id",
            "relationship_type",
            unique=True,
        ),
    )

    def __repr__(self) -> str:
        return (
            f"<KnowledgeRelationship {self.source_id} "
            f"-[{self.relationship_type}]-> {self.target_id}>"
        )
