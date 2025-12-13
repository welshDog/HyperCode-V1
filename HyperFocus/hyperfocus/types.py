from typing import TYPE_CHECKING, List, Optional, Protocol

# Use string literals to avoid circular imports
if TYPE_CHECKING:
    from .session import HyperFocusSession


class Task(Protocol):
    """Protocol defining the Task interface."""

    def execute(self) -> None:
        """Execute the task."""
        ...


class CognitiveProfile:
    """Manages cognitive profile for the user."""

    def __init__(self) -> None:
        self.peak_hours: List[int] = [9, 10, 11, 14, 15]  # Default peak hours
        self.cognitive_load: float = 0.0

    def calculate_cognitive_load(self) -> float:
        """Calculate current cognitive load (0-10 scale)."""
        # TODO: Implement actual calculation
        return self.cognitive_load


class NotificationFilter:
    """Manages notification filtering based on focus mode."""

    pass


class VisualProgressTracker:
    """Tracks and displays progress visually."""

    def update(self, session: "HyperFocusSession") -> None:
        """Update the visual feedback."""
        pass


class TaskQueue:
    """Manages the queue of tasks."""

    def get_next_task(self) -> Optional["Task"]:
        """Get the next task in the queue."""
        return None

    def get_easy_task(self) -> Optional["Task"]:
        """Get an easy task (low cognitive load)."""
        return None

    def get_important_task(self) -> Optional["Task"]:
        """Get an important task (for deep work)."""
        return None
