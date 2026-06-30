"""Chunking primitives for large model artifacts."""

from __future__ import annotations

from pathlib import Path
from typing import Iterator


def iter_chunks(path: str | Path, chunk_size: int = 1024 * 1024) -> Iterator[bytes]:
    """Yield file chunks from a path."""
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            yield chunk
