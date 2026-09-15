"""store/ — the intermediate artifacts.

Keeping documents, signals and reports on disk is what makes each stage
re-runnable in isolation: `edu compile` reads reports written weeks ago without
ingestion or enriching anything again.

Most of this directory is versioned, which is deliberate. `corpus/baseline.json`
is the novelty memory and `calibration/` is each source's track record; a run
that starts without them re-promotes what it already covered. Only the raw
per-run document dumps are heavy and genuinely regenerable, so those are the
part .gitignore excludes and `prune_corpus` deletes.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

from .models import CalibrationRecord, Document, Report, Signal

#: The novelty baseline is a rolling window: old centroids stop being a useful
#: definition of "already covered".
_BASELINE_CAP = 2000


class Store:
    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        for sub in ("corpus", "signals", "reports", "calibration"):
            (self.root / sub).mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------- corpus ---
    def save_documents(self, run_id: str, docs: list[Document]) -> None:
        payload = [d.model_dump(mode="json") for d in docs]
        (self.root / "corpus" / f"{run_id}.json").write_text(json.dumps(payload))

    def prune_corpus(self, keep_days: int = 30) -> int:
        """Delete raw per-run document dumps past their useful life.

        The baseline, signals, reports and calibration records all survive, so
        pruning never costs the pipeline its memory of what it already covered.
        Returns how many files were removed.
        """
        cutoff = time.time() - keep_days * 86_400
        removed = 0
        for path in (self.root / "corpus").glob("*.json"):
            if path.name == "baseline.json" or path.stat().st_mtime >= cutoff:
                continue
            path.unlink()
            removed += 1
        return removed

    def load_documents(self, run_id: str) -> list[Document]:
        path = self.root / "corpus" / f"{run_id}.json"
        if not path.exists():
            return []
        return [Document.model_validate(d) for d in json.loads(path.read_text())]

    # ---------------------------------------- baseline (novelty reference) ---
    def load_baseline(self) -> list[list[float]]:
        path = self.root / "corpus" / "baseline.json"
        return json.loads(path.read_text()) if path.exists() else []

    def append_baseline(self, centroids: list[list[float]]) -> None:
        if not centroids:
            return
        baseline = self.load_baseline()
        if baseline and len(baseline[0]) != len(centroids[0]):
            baseline = []  # the embedder changed; old vectors are incomparable
        baseline.extend(centroids)
        (self.root / "corpus" / "baseline.json").write_text(
            json.dumps(baseline[-_BASELINE_CAP:]))

    # ------------------------------------------------------------ signals ---
    def save_signal(self, signal: Signal) -> None:
        (self.root / "signals" / f"{signal.id}.json").write_text(
            signal.model_dump_json(indent=2))

    def load_signals(self) -> list[Signal]:
        return [Signal.model_validate_json(p.read_text())
                for p in sorted((self.root / "signals").glob("*.json"))]

    def get_signal(self, signal_id: str) -> Signal | None:
        path = self.root / "signals" / f"{signal_id}.json"
        return Signal.model_validate_json(path.read_text()) if path.exists() else None

    # ------------------------------------------------------------ reports ---
    def save_report(self, report: Report) -> None:
        (self.root / "reports" / f"{report.signal_id}.json").write_text(
            report.model_dump_json(indent=2))

    def load_reports(self) -> list[Report]:
        return [Report.model_validate_json(p.read_text())
                for p in sorted((self.root / "reports").glob("*.json"))]

    def get_report(self, signal_id: str) -> Report | None:
        path = self.root / "reports" / f"{signal_id}.json"
        return Report.model_validate_json(path.read_text()) if path.exists() else None

    # -------------------------------------------------------- calibration ---
    def save_calibration(self, record: CalibrationRecord) -> None:
        (self.root / "calibration" / f"{record.source}.json").write_text(
            record.model_dump_json(indent=2))

    def load_calibration(self) -> dict[str, CalibrationRecord]:
        out: dict[str, CalibrationRecord] = {}
        for path in sorted((self.root / "calibration").glob("*.json")):
            record = CalibrationRecord.model_validate_json(path.read_text())
            out[record.source] = record
        return out
