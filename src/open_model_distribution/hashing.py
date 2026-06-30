"""Content identity utilities for open model distribution."""

from __future__ import annotations

import hashlib
from pathlib import Path


def sha256_file(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    """Return the SHA-256 digest for a file."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def content_id(path: str | Path, algorithm: str = "sha256") -> str:
    """Return a simple content-addressed identifier."""
    if algorithm != "sha256":
        raise ValueError("Only sha256 is currently supported.")
    return f"sha256:{sha256_file(path)}"
