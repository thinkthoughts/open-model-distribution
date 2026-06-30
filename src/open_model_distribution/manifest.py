"""Manifest generation for reproducible model distribution."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import yaml

from .hashing import content_id


@dataclass(frozen=True)
class ArtifactManifest:
    name: str
    path: str
    size_bytes: int
    content_id: str

    @classmethod
    def from_file(cls, path: str | Path, name: str | None = None) -> "ArtifactManifest":
        p = Path(path)
        return cls(
            name=name or p.name,
            path=str(p),
            size_bytes=p.stat().st_size,
            content_id=content_id(p),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def write_yaml(self, output_path: str | Path) -> None:
        with Path(output_path).open("w", encoding="utf-8") as handle:
            yaml.safe_dump(self.to_dict(), handle, sort_keys=False)
