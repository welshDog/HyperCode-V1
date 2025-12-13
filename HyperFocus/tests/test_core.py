# tests/test_core.py
import pytest

from hyperfocus.core import CognitiveState


def test_cognitive_state_initialization():
    cs = CognitiveState()
    assert cs.metrics["keystroke_intervals"] == []
    assert cs.metrics["error_rate"] == []
