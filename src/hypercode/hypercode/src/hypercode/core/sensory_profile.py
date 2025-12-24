"""
Sensory Profile System for HyperCode

This module handles the configuration of sensory profiles that customize the
coding environment for different neurodivergent needs.
"""

import json
from dataclasses import asdict, dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Type, TypeVar


class VisualNoiseLevel(str, Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class AnimationSpeed(float, Enum):
    SLOW = 0.5
    NORMAL = 1.0
    FAST = 1.5


@dataclass
class VisualSettings:
    """Configuration for visual aspects of the editor."""

    theme: str = "dark"
    font_family: str = "Fira Code"
    font_size: int = 14
    line_height: float = 1.5
    visual_noise: VisualNoiseLevel = VisualNoiseLevel.LOW
    show_line_numbers: bool = True
    show_minimap: bool = False
    show_gutter_icons: bool = True


@dataclass
class AudioSettings:
    """Configuration for audio feedback."""

    enabled: bool = False
    volume: float = 0.5  # 0.0 to 1.0
    sound_effects: Dict[str, str] = field(
        default_factory=lambda: {
            "error": "soft_beep",
            "completion": "none",
            "notification": "none",
        }
    )


@dataclass
class AnimationSettings:
    """Configuration for animations and transitions."""

    enabled: bool = True
    speed: AnimationSpeed = AnimationSpeed.NORMAL
    cursor_style: str = "block"
    smooth_scrolling: bool = True


@dataclass
class SensoryProfile:
    """A complete sensory profile configuration."""

    name: str
    description: str = ""
    visual: VisualSettings = field(default_factory=VisualSettings)
    audio: AudioSettings = field(default_factory=AudioSettings)
    animation: AnimationSettings = field(default_factory=AnimationSettings)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the profile to a dictionary."""
        data = asdict(self)
        data["visual"]["visual_noise"] = self.visual.visual_noise.value
        data["animation"]["speed"] = self.animation.speed.value
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SensoryProfile":
        """Create a profile from a dictionary."""
        visual_data = data.get("visual", {})
        audio_data = data.get("audio", {})
        animation_data = data.get("animation", {})

        profile = cls(
            name=data["name"],
            description=data.get("description", ""),
            visual=VisualSettings(**visual_data),
            audio=AudioSettings(**audio_data),
            animation=AnimationSettings(**animation_data),
        )

        # Handle enums
        if "visual_noise" in visual_data:
            profile.visual.visual_noise = VisualNoiseLevel(visual_data["visual_noise"])
        if "speed" in animation_data:
            profile.animation.speed = AnimationSpeed(animation_data["speed"])

        return profile

    def save(self, path: Path):
        """Save the profile to a file."""
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load(cls, path: Path) -> "SensoryProfile":
        """Load a profile from a file."""
        with open(path, "r") as f:
            data = json.load(f)
        return cls.from_dict(data)


class ProfileManager:
    """Manages loading and saving of sensory profiles."""

    def __init__(self, profiles_dir: Optional[Path] = None):
        """Initialize with optional custom profiles directory."""
        if profiles_dir is None:
            self.profiles_dir = Path.home() / ".hypercode" / "profiles"
        else:
            self.profiles_dir = profiles_dir

        self.profiles_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_default_profiles()

    def _ensure_default_profiles(self):
        """Ensure default profiles exist."""
        default_profiles = [
            self._create_minimal_profile(),
            self._create_enhanced_profile(),
            self._create_high_contrast_profile(),
        ]

        for profile in default_profiles:
            path = self.profiles_dir / f"{profile.name.lower().replace(' ', '_')}.json"
            if not path.exists():
                profile.save(path)

    def _create_minimal_profile(self) -> SensoryProfile:
        """Create a minimal distraction-free profile."""
        return SensoryProfile(
            name="Minimal",
            description="A distraction-free profile with minimal visual noise and animations.",
            visual=VisualSettings(
                theme="monochrome",
                font_family="Courier New",
                font_size=14,
                visual_noise=VisualNoiseLevel.NONE,
                show_minimap=False,
                show_gutter_icons=False,
            ),
            audio=AudioSettings(enabled=False, volume=0.0),
            animation=AnimationSettings(enabled=False, cursor_style="block"),
        )

    def _create_enhanced_profile(self) -> SensoryProfile:
        """Create an enhanced profile with helpful visual cues."""
        return SensoryProfile(
            name="Enhanced",
            description="A balanced profile with helpful visual cues and moderate animations.",
            visual=VisualSettings(
                theme="solarized-light",
                font_family="Fira Code",
                font_size=15,
                line_height=1.6,
                visual_noise=VisualNoiseLevel.LOW,
                show_minimap=True,
            ),
            audio=AudioSettings(
                enabled=True,
                volume=0.5,
                sound_effects={
                    "error": "soft_chime",
                    "completion": "soft_click",
                    "notification": "gentle_bell",
                },
            ),
            animation=AnimationSettings(
                enabled=True, speed=AnimationSpeed.NORMAL, cursor_style="underline"
            ),
        )

    def _create_high_contrast_profile(self) -> SensoryProfile:
        """Create a high-contrast profile for better readability."""
        return SensoryProfile(
            name="High Contrast",
            description="High contrast theme for better readability and reduced eye strain.",
            visual=VisualSettings(
                theme="high-contrast",
                font_family="Consolas",
                font_size=16,
                line_height=1.8,
                visual_noise=VisualNoiseLevel.LOW,
            ),
            audio=AudioSettings(
                enabled=True,
                volume=0.7,
                sound_effects={
                    "error": "distinct_chime",
                    "completion": "soft_chime",
                    "notification": "gentle_click",
                },
            ),
            animation=AnimationSettings(
                enabled=True, speed=AnimationSpeed.SLOW, cursor_style="block"
            ),
        )

    def list_profiles(self) -> List[str]:
        """List all available profile names."""
        return [p.stem for p in self.profiles_dir.glob("*.json")]

    def get_profile(self, name: str) -> Optional[SensoryProfile]:
        """Get a profile by name."""
        path = self.profiles_dir / f"{name}.json"
        if path.exists():
            return SensoryProfile.load(path)
        return None

    def save_profile(self, profile: SensoryProfile):
        """Save a profile."""
        path = self.profiles_dir / f"{profile.name.lower().replace(' ', '_')}.json"
        profile.save(path)

    def delete_profile(self, name: str):
        """Delete a profile by name."""
        path = self.profiles_dir / f"{name}.json"
        if path.exists():
            path.unlink()


# Default profile manager instance
profile_manager = ProfileManager()


def get_profile(name: str) -> Optional[SensoryProfile]:
    """Helper function to get a profile by name."""
    return profile_manager.get_profile(name)


def list_profiles() -> List[str]:
    """Helper function to list all available profiles."""
    return profile_manager.list_profiles()
