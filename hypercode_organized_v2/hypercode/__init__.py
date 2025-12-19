"""
HyperCode - A programming language designed for neurodivergent developers.

This package contains the core implementation of the HyperCode language,
including the lexer, parser, and interpreter components, as well as
additional modules for knowledge management and AI integration.
"""

__version__ = "0.1.0"

# Core components
from .core.lexer import Lexer, LexerError
from .core.parser import Parser
from .core.tokens import Token, TokenType

# Knowledge management
from .knowledge_base import HyperCodeKnowledgeBase, ResearchDocument

# AI Integration
from .perplexity_client import PerplexityClient
from .enhanced_perplexity_client import EnhancedPerplexityClient

# Project management
from .hypercode_manager_enhanced import HyperCodeDataManager, VersionChangeType, ProjectConfig, ProjectDependency

__all__ = [
    # Core components
    'Lexer', 'LexerError', 'Parser', 'Token', 'TokenType',
    
    # Knowledge management
    'HyperCodeKnowledgeBase', 'ResearchDocument',
    
    # AI Integration
    'PerplexityClient', 'EnhancedPerplexityClient',
    
    # Project management
    'HyperCodeDataManager', 'VersionChangeType', 'ProjectConfig', 'ProjectDependency',
]
