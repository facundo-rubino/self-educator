"""Smoke tests for the commands that cost nothing to run."""
from __future__ import annotations

import shutil
from pathlib import Path

import yaml
from typer.testing import CliRunner

from self_educator.cli import app

runner = CliRunner()
REPO_ROOT = Path(__file__).resolve().parent.parent


def _project(tmp_path: Path) -> Path:
    shutil.copy(REPO_ROOT / "config.yaml", tmp_path / "config.yaml")
    (tmp_path / "kb").mkdir()
    shutil.copy(REPO_ROOT / "kb" / "SCHEMA.md", tmp_path / "kb" / "SCHEMA.md")
    return tmp_path


def test_init_creates_a_directory_per_configured_note_type(tmp_path: Path):
    root = _project(tmp_path)
    (root / "config.yaml").write_text(yaml.safe_dump({
        "topic": "mycology",
        "kb": {"note_types": [{"name": "species", "dir": "species",
                               "half_life_days": 3650}]},
    }))
    result = runner.invoke(app, ["init", "--root", str(root)])
    assert result.exit_code == 0
    assert (root / "kb" / "species").is_dir()
    assert not (root / "kb" / "concepts").exists()


def test_sources_shows_what_will_run(tmp_path: Path):
    result = runner.invoke(app, ["sources", "--root", str(_project(tmp_path))])
    assert result.exit_code == 0
    assert "files" in result.stdout


def test_lint_is_clean_on_an_empty_kb(tmp_path: Path):
    root = _project(tmp_path)
    runner.invoke(app, ["init", "--root", str(root)])
    result = runner.invoke(app, ["lint", "--root", str(root)])
    assert result.exit_code == 0
    assert "clean" in result.stdout


def test_status_tells_you_what_to_do_next(tmp_path: Path):
    root = _project(tmp_path)
    runner.invoke(app, ["init", "--root", str(root)])
    result = runner.invoke(app, ["status", "--root", str(root)])
    assert result.exit_code == 0
    assert "edu run" in result.stdout


def test_gaps_is_empty_on_a_fresh_kb(tmp_path: Path):
    root = _project(tmp_path)
    runner.invoke(app, ["init", "--root", str(root)])
    result = runner.invoke(app, ["gaps", "--root", str(root)])
    assert result.exit_code == 0
    assert "No open gaps" in result.stdout
