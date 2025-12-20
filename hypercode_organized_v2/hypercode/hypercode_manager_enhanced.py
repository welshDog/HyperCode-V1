"""
Enhanced HyperCode Manager

This module provides enhanced management capabilities for HyperCode projects,
including version control, dependency management, and project configuration.
"""

from enum import Enum, auto
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field
import os
import json
import yaml
from pathlib import Path
import subprocess
from datetime import datetime


class VersionChangeType(Enum):
    """Types of version changes for semantic versioning."""

    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"
    PRERELEASE = "prerelease"
    BUILD = "build"


@dataclass
class ProjectDependency:
    """Represents a project dependency."""

    name: str
    version: str
    is_dev: bool = False
    optional: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """Convert to a dictionary for serialization."""
        return {
            "name": self.name,
            "version": self.version,
            "is_dev": self.is_dev,
            "optional": self.optional,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProjectDependency":
        """Create from a dictionary."""
        return cls(
            name=data["name"],
            version=data["version"],
            is_dev=data.get("is_dev", False),
            optional=data.get("optional", False),
        )


@dataclass
class ProjectConfig:
    """Configuration for a HyperCode project."""

    name: str
    version: str
    description: str = ""
    author: str = ""
    license: str = "MIT"
    python_version: str = "3.8+"
    dependencies: List[ProjectDependency] = field(default_factory=list)
    dev_dependencies: List[ProjectDependency] = field(default_factory=list)
    scripts: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to a dictionary for serialization."""
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "author": self.author,
            "license": self.license,
            "python_version": self.python_version,
            "dependencies": [dep.to_dict() for dep in self.dependencies],
            "dev_dependencies": [dep.to_dict() for dep in self.dev_dependencies],
            "scripts": self.scripts,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProjectConfig":
        """Create from a dictionary."""
        return cls(
            name=data["name"],
            version=data["version"],
            description=data.get("description", ""),
            author=data.get("author", ""),
            license=data.get("license", "MIT"),
            python_version=data.get("python_version", "3.8+"),
            dependencies=[
                ProjectDependency.from_dict(dep) for dep in data.get("dependencies", [])
            ],
            dev_dependencies=[
                ProjectDependency.from_dict(dep)
                for dep in data.get("dev_dependencies", [])
            ],
            scripts=data.get("scripts", {}),
        )


class HyperCodeDataManager:
    """Manages HyperCode project data, configuration, and versioning."""

    CONFIG_FILENAME = "hypercode.config.json"

    def __init__(self, project_root: Optional[Union[str, Path]] = None):
        """Initialize the HyperCode data manager.

        Args:
            project_root: Root directory of the project. If None, uses the current working directory.
        """
        if project_root is None:
            self.project_root = Path.cwd()
        else:
            self.project_root = Path(project_root)

        self.config_path = self.project_root / self.CONFIG_FILENAME
        self._config: Optional[ProjectConfig] = None

    @property
    def config(self) -> ProjectConfig:
        """Get the project configuration."""
        if self._config is None:
            self._load_config()
        return self._config or self._create_default_config()

    def _load_config(self) -> None:
        """Load the project configuration from disk."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    config_data = json.load(f)
                    self._config = ProjectConfig.from_dict(config_data)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading config file: {e}")
                self._config = self._create_default_config()
        else:
            self._config = self._create_default_config()

    def _create_default_config(self) -> ProjectConfig:
        """Create a default configuration for a new project."""
        return ProjectConfig(
            name=self.project_root.name,
            version="0.1.0",
            description="A HyperCode project",
            author="",
            license="MIT",
            python_version="3.8+",
            dependencies=[],
            dev_dependencies=[],
            scripts={},
        )

    def save_config(self) -> None:
        """Save the current configuration to disk."""
        if self._config is None:
            return

        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.config.to_dict(), f, indent=2)

    def update_version(self, change_type: VersionChangeType) -> str:
        """Update the project version according to semantic versioning.

        Args:
            change_type: Type of version change to apply

        Returns:
            The new version string
        """
        if self._config is None:
            self._load_config()

        major, minor, patch = map(int, self.config.version.split("."))

        if change_type == VersionChangeType.MAJOR:
            major += 1
            minor = 0
            patch = 0
        elif change_type == VersionChangeType.MINOR:
            minor += 1
            patch = 0
        elif change_type == VersionChangeType.PATCH:
            patch += 1
        # For prerelease and build, we'd append suffixes like -alpha.1 or +build.1

        new_version = f"{major}.{minor}.{patch}"
        self._config.version = new_version
        self.save_config()

        return new_version

    def add_dependency(
        self,
        name: str,
        version: str = "*",
        is_dev: bool = False,
        optional: bool = False,
    ) -> None:
        """Add a dependency to the project.

        Args:
            name: Name of the dependency
            version: Version specifier (default: "*" for any version)
            is_dev: Whether this is a development dependency
            optional: Whether this is an optional dependency
        """
        dep = ProjectDependency(
            name=name, version=version, is_dev=is_dev, optional=optional
        )

        if is_dev:
            self.config.dev_dependencies.append(dep)
        else:
            self.config.dependencies.append(dep)

        self.save_config()

    def remove_dependency(self, name: str, is_dev: bool = False) -> bool:
        """Remove a dependency from the project.

        Args:
            name: Name of the dependency to remove
            is_dev: Whether to look in dev dependencies

        Returns:
            True if the dependency was found and removed, False otherwise
        """
        if is_dev:
            deps = self.config.dev_dependencies
        else:
            deps = self.config.dependencies

        initial_length = len(deps)
        deps[:] = [d for d in deps if d.name.lower() != name.lower()]

        if len(deps) < initial_length:
            self.save_config()
            return True
        return False


# Example usage
if __name__ == "__main__":
    # Initialize the manager
    manager = HyperCodeDataManager()

    # Print current config
    print(f"Project: {manager.config.name} v{manager.config.version}")
    print(f"Description: {manager.config.description}")

    # Update version
    new_version = manager.update_version(VersionChangeType.PATCH)
    print(f"Updated version to: {new_version}")

    # Add a dependency
    manager.add_dependency("requests", "^2.28.0")
    print("Added 'requests' dependency")
