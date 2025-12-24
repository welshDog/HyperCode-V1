"""Utilities for canonicalizing node/relationship identifiers."""

import re
from typing import Tuple


def slugify_label(label: str) -> str:
    """Lowercase, trim, and slugify a label for canonical_form."""
    slug = label.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "unknown"


def entity_key(node_type: str, label: str) -> Tuple[str, str]:
    """Stable key used for deduping entities before insert."""
    return (node_type.lower(), slugify_label(label))

