"""
Tests for the sensory profile system.
"""

import json
import tempfile
from pathlib import Path

import pytest

from hypercode.core.sensory_profile import (
    AnimationSettings,
    AnimationSpeed,
    AudioSettings,
    ProfileManager,
    SensoryProfile,
    VisualNoiseLevel,
    VisualSettings,
)


def test_visual_settings_creation():
    """Test creating visual settings."""
    visual = VisualSettings(
        theme="dark",
        font_family="Fira Code",
        font_size=14,
        visual_noise=VisualNoiseLevel.LOW,
    )

    assert visual.theme == "dark"
    assert visual.font_family == "Fira Code"
    assert visual.visual_noise == VisualNoiseLevel.LOW


def test_audio_settings_creation():
    """Test creating audio settings."""
    audio = AudioSettings(enabled=True, volume=0.7, sound_effects={"error": "beep"})

    assert audio.enabled is True
    assert audio.volume == 0.7
    assert "error" in audio.sound_effects


def test_animation_settings_creation():
    """Test creating animation settings."""
    animation = AnimationSettings(
        enabled=True, speed=AnimationSpeed.SLOW, cursor_style="block"
    )

    assert animation.enabled is True
    assert animation.speed == AnimationSpeed.SLOW
    assert animation.cursor_style == "block"


def test_sensory_profile_creation():
    """Test creating a complete sensory profile."""
    profile = SensoryProfile(
        name="Test Profile",
        description="A test profile",
        visual=VisualSettings(),
        audio=AudioSettings(),
        animation=AnimationSettings(),
    )

    assert profile.name == "Test Profile"
    assert isinstance(profile.visual, VisualSettings)
    assert isinstance(profile.audio, AudioSettings)
    assert isinstance(profile.animation, AnimationSettings)


def test_profile_serialization():
    """Test serializing AND deserializing a profile."""
    original = SensoryProfile(
        name="Serialization Test",
        visual=VisualSettings(theme="dark", visual_noise=VisualNoiseLevel.MEDIUM),
        audio=AudioSettings(volume=0.8),
        animation=AnimationSettings(speed=AnimationSpeed.FAST),
    )

    # Convert to dict and back
    data = original.to_dict()
    restored = SensoryProfile.from_dict(data)

    # Check if restored profile matches original
    assert restored.name == original.name
    assert restored.visual.theme == original.visual.theme
    assert restored.visual.visual_noise == original.visual.visual_noise
    assert restored.audio.volume == original.audio.volume
    assert restored.animation.speed == original.animation.speed


def test_profile_file_io(tmp_path):
    """Test saving and loading a profile to/from a file."""
    profile = SensoryProfile(
        name="File I/O Test",
        visual=VisualSettings(theme="light"),
        audio=AudioSettings(enabled=True),
        animation=AnimationSettings(enabled=True),
    )

    # Save to file
    file_path = tmp_path / "test_profile.json"
    profile.save(file_path)

    # Load from file
    loaded = SensoryProfile.load(file_path)

    # Verify
    assert loaded.name == profile.name
    assert loaded.visual.theme == profile.visual.theme
    assert loaded.audio.enabled == profile.audio.enabled
    assert loaded.animation.enabled == profile.animation.enabled


def test_profile_manager_initialization(tmp_path):
    """Test initializing the profile manager and checking default profiles."""
    # Create a temporary directory for profiles
    profiles_dir = tmp_path / "profiles"
    manager = ProfileManager(profiles_dir)

    # Check if default profiles were created
    profiles = manager.list_profiles()
    assert len(profiles) >= 3  # Should have at least 3 default profiles
    assert "minimal" in profiles
    assert "enhanced" in profiles
    assert "high_contrast" in profiles


def test_profile_manager_get_profile(tmp_path):
    """Test getting a profile by name."""
    profiles_dir = tmp_path / "profiles"
    manager = ProfileManager(profiles_dir)

    # Get the minimal profile
    profile = manager.get_profile("minimal")
    assert profile is not None
    assert profile.name.lower() == "minimal"
    assert not profile.audio.enabled
    assert not profile.animation.enabled


def test_profile_manager_save_custom_profile(tmp_path):
    """Test saving a custom profile."""
    profiles_dir = tmp_path / "profiles"
    manager = ProfileManager(profiles_dir)

    # Create a custom profile
    custom = SensoryProfile(
        name="Custom Profile",
        visual=VisualSettings(theme="solarized"),
        audio=AudioSettings(volume=0.9),
    )

    # Save the custom profile
    manager.save_profile(custom)

    # Check if it was saved
    profiles = manager.list_profiles()
    assert "custom_profile" in profiles

    # Load it back and verify
    loaded = manager.get_profile("custom_profile")
    assert loaded is not None
    assert loaded.name == "Custom Profile"
    assert loaded.visual.theme == "solarized"
    assert loaded.audio.volume == 0.9


def test_profile_manager_delete_profile(tmp_path):
    """Test deleting a profile."""
    profiles_dir = tmp_path / "profiles"
    manager = ProfileManager(profiles_dir)

    # Create and save a test profile
    test_profile = SensoryProfile(name="Test Delete")
    manager.save_profile(test_profile)
    assert "test_delete" in manager.list_profiles()

    # Delete the profile
    manager.delete_profile("test_delete")
    assert "test_delete" not in manager.list_profiles()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
