# hyperfocus/config.py
from pathlib import Path
from typing import Any, Dict

import yaml
from pydantic import BaseModel


class AIConfig(BaseModel):
    provider: str = "anthropic"
    model: str = "claude-3-opus"


class FocusModeConfig(BaseModel):
    duration: int
    break_duration: int
    allowed_notifications: list[str]


class DatabaseConfig(BaseModel):
    url: str = f"sqlite:///{Path.home() / '.hyperfocus' / 'hyperfocus.db'}"
    echo: bool = False
    pool_pre_ping: bool = True


class Config(BaseModel):
    focus: Dict[str, FocusModeConfig]
    cognitive: Dict[str, Any]
    ai: AIConfig
    database: DatabaseConfig = DatabaseConfig()


def load_config(path: str = "config.yaml") -> Config:
    config_path = Path(path)
    if not config_path.exists():
        return get_default_config()

    with open(config_path) as f:
        config_data = yaml.safe_load(f)
        return Config(**config_data)


def get_default_config() -> Config:
    """Return default configuration."""
    return Config(
        focus={
            "deep_work": FocusModeConfig(
                duration=50, break_duration=10, allowed_notifications=["critical"]
            ),
            "creative_flow": FocusModeConfig(
                duration=90, break_duration=15, allowed_notifications=[]
            ),
        },
        cognitive={"load_threshold": 7.5, "recovery_time": 5},
        ai=AIConfig(),
    )
