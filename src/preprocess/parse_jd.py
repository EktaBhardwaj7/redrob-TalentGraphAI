"""Parse a job-description file into a lightweight dictionary."""

from __future__ import annotations

import json
from pathlib import Path


def parse_jd(path: str | Path) -> dict[str, object]:
    jd_path = Path(path)
    if not jd_path.exists():
        return {"text": "", "source_exists": False}

    if jd_path.suffix.lower() == ".json":
        try:
            data = json.loads(jd_path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data.setdefault("text", json.dumps(data, sort_keys=True))
                data["source_exists"] = True
                return data
        except json.JSONDecodeError:
            pass

    if jd_path.suffix.lower() == ".docx":
        try:
            import zipfile
            import xml.etree.ElementTree as ET

            with zipfile.ZipFile(jd_path) as archive:
                xml = archive.read("word/document.xml")
            root = ET.fromstring(xml)
            namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            text = " ".join(node.text or "" for node in root.findall(".//w:t", namespace))
            return {"text": text, "source_exists": True}
        except Exception as exc:
            return {"text": "", "source_exists": True, "warning": str(exc)}

    return {"text": jd_path.read_text(encoding="utf-8", errors="ignore"), "source_exists": True}


__all__ = ["parse_jd"]
