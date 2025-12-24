"""
Initialization for the research module.

This module contains all of the database plumbing and models
required to persist research‑related information for HyperCode.

The top level symbols exported here are the SQLAlchemy ``Base``
class and the ``SessionLocal`` factory.  Importing these from
``hypercode.backend.research`` will ensure the engine is set up
before the models are defined.

"""

from .db import Base, SessionLocal  # noqa: F401
