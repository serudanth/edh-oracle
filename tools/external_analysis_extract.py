#!/usr/bin/env python3
"""External Deck-Analysis Data Extraction & Normalization Sub-Tool.

Extracts, normalizes, and archives external deck-analysis data from supported services
(ScryCheck, EDHCheck, RateMyDecks, CommanderPowerMeter, ArcMind, PowerDeckAI) into a
standardized schema.

Usage:
    python tools/external_analysis_extract.py --url <Moxfield-or-Archidekt-URL>
    python tools/external_analysis_extract.py --input payload.json
    python tools/external_analysis_extract.py --input - < payload.json
    cat input.json | python tools/external_analysis_extract.py
"""
import argparse
import datetime
import json
import sys
import threading
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional

SUPPORTED_SOURCES = [
    "ScryCheck",
    "EDHCheck",
    "RateMyDecks",
    "CommanderPowerMeter",
    "ArcMind",
    "PowerDeckAI",
]

STANDARD_METRICS = [
    "power_score",
    "bracket",
    "combo_score",
    "interaction_score",
    "ramp_score",
    "consistency_score",
    "speed_score",
    "tutor_count",
    "fast_mana_count",
    "combo_count",
]

TEXT_FIELDS = [
    "summary",
    "explanations",
    "strengths",
    "weaknesses",
    "recommendations",
    "suggested_changes",
    "combo_lines",
    "mulligan_advice",
]


def create_empty_metrics() -> Dict[str, Any]:
    return {key: None for key in STANDARD_METRICS}


def create_empty_text() -> Dict[str, Any]:
    return {
        "summary": None,
        "explanations": [],
        "strengths": [],
        "weaknesses": [],
        "recommendations": [],
        "suggested_changes": [],
        "combo_lines": [],
        "mulligan_advice": [],
    }


def create_source_entry(
    source_name: str,
    status: str = "unavailable",
    error: Optional[str] = None,
    metrics: Optional[Dict[str, Any]] = None,
    source_metrics: Optional[Dict[str, Any]] = None,
    text: Optional[Dict[str, Any]] = None,
    raw_result: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Creates a normalized source result object adhering strictly to the schema."""
    norm_metrics = create_empty_metrics()
    if metrics:
        for k, v in metrics.items():
            if k in norm_metrics:
                norm_metrics[k] = v

    norm_text = create_empty_text()
    if text:
        for k, v in text.items():
            if k in norm_text:
                if isinstance(norm_text[k], list):
                    norm_text[k] = list(v) if isinstance(v, (list, tuple)) else ([v] if v is not None else [])
                else:
                    norm_text[k] = v

    return {
        "source": source_name,
        "status": status,
        "error": error,
        "metrics": norm_metrics,
        "source_metrics": source_metrics if source_metrics is not None else {},
        "text": norm_text,
        "raw_result": raw_result if raw_result is not None else {},
    }


def fetch_deck_info(deck_url: str) -> tuple[Optional[str], Optional[str]]:
    """Retrieves deck name and commander from Archidekt or Moxfield URL when available."""
    if not deck_url:
        return None, None

    try:
        if "archidekt.com" in deck_url:
            # Extract deck ID
            parts = deck_url.split("/decks/")
            if len(parts) > 1:
                deck_id = parts[1].split("/")[0].split("?")[0]
                req = urllib.request.Request(
                    f"https://archidekt.com/api/decks/{deck_id}/",
                    headers={"Accept": "application/json", "User-Agent": "edh-oracle/1.0"},
                )
                with urllib.request.urlopen(req, timeout=5) as resp:
                    data = json.load(resp)
                    deck_name = data.get("name")
                    cards = data.get("cards", [])
                    cmd_names = [
                        c["card"]["oracleCard"]["name"]
                        for c in cards
                        if "Commander" in (c.get("categories") or [])
                    ]
                    commander = " // ".join(cmd_names) if cmd_names else None
                    return deck_name, commander

        elif "moxfield.com" in deck_url:
            parts = deck_url.split("/decks/")
            if len(parts) > 1:
                deck_id = parts[1].split("/")[0].split("?")[0]
                req = urllib.request.Request(
                    f"https://api2.moxfield.com/v3/decks/all/{deck_id}",
                    headers={"Accept": "application/json", "User-Agent": "edh-oracle/1.0"},
                )
                with urllib.request.urlopen(req, timeout=5) as resp:
                    data = json.load(resp)
                    deck_name = data.get("name")
                    commanders = data.get("commanders", {})
                    cmd_names = list(commanders.keys())
                    commander = " // ".join(cmd_names) if cmd_names else None
                    return deck_name, commander
    except Exception:
        # Network call or parsing failed; fallback gracefully without interrupting extraction
        pass

    return None, None


def normalize_extraction_request(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Processes input payload and constructs normalized external analysis output structure."""
    deck_url = input_data.get("deck_url")
    requested = input_data.get("requested_sources")

    if requested is None:
        sources_to_process = list(SUPPORTED_SOURCES)
    else:
        sources_to_process = [s for s in requested if s in SUPPORTED_SOURCES]

    deck_name = input_data.get("deck_name")
    commander = input_data.get("commander")

    # Fetch deck name and commander if not supplied directly
    if (not deck_name or not commander) and deck_url:
        fetched_name, fetched_cmd = fetch_deck_info(deck_url)
        deck_name = deck_name or fetched_name
        commander = commander or fetched_cmd

    # Ingest pre-supplied raw/parsed source results if provided in payload
    raw_sources_input = input_data.get("raw_sources", {})

    processed_sources = []
    successful_sources = []
    failed_sources = []

    for source in sources_to_process:
        if source in raw_sources_input:
            raw_entry = raw_sources_input[source]
            status = raw_entry.get("status", "success")
            error = raw_entry.get("error")
            metrics = raw_entry.get("metrics")
            source_metrics = raw_entry.get("source_metrics")
            text = raw_entry.get("text")
            raw_res = raw_entry.get("raw_result")

            entry = create_source_entry(
                source_name=source,
                status=status,
                error=error,
                metrics=metrics,
                source_metrics=source_metrics,
                text=text,
                raw_result=raw_res,
            )
        else:
            # Default un-executed source status
            entry = create_source_entry(
                source_name=source,
                status="unavailable",
                error="Service endpoint not directly automated in offline pass",
            )

        processed_sources.append(entry)
        if entry["status"] in ("success", "partial"):
            successful_sources.append(source)
        else:
            failed_sources.append(source)

    analysis_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    output = {
        "deck_name": deck_name,
        "commander": commander,
        "sources": processed_sources,
        "metadata": {
            "deck_url": deck_url,
            "analysis_time": analysis_time,
            "successful_sources": successful_sources,
            "failed_sources": failed_sources,
        },
    }
    return output


def read_stdin_if_available(timeout: float = 0.1) -> Optional[str]:
    """Reads stdin if data is available, without blocking indefinitely when stdin is empty/open."""
    if sys.stdin.isatty():
        return None

    content: List[str] = []

    def _read_target():
        try:
            data = sys.stdin.read()
            if data:
                content.append(data)
        except Exception:
            pass

    t = threading.Thread(target=_read_target, daemon=True)
    t.start()
    t.join(timeout)
    if t.is_alive():
        # Reading stdin blocked (no EOF / no piped data)
        return None

    return content[0].strip() if content else None


def main():
    parser = argparse.ArgumentParser(description="Extract & normalize external EDH deck analysis data.")
    parser.add_argument("--url", help="Moxfield or Archidekt deck URL")
    parser.add_argument("--input", help="JSON file containing extraction request payload or '-' for stdin")
    parser.add_argument("--sources", nargs="*", help="List of requested sources")

    args = parser.parse_args()

    input_payload: Dict[str, Any] = {}

    if args.input == "-":
        stdin_text = sys.stdin.read().strip()
        if stdin_text:
            input_payload = json.loads(stdin_text)
    elif args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            input_payload = json.load(f)
    else:
        stdin_text = read_stdin_if_available(timeout=0.1)
        if stdin_text:
            try:
                input_payload = json.loads(stdin_text)
            except Exception:
                pass

    if args.url:
        input_payload["deck_url"] = args.url
    if args.sources:
        input_payload["requested_sources"] = args.sources

    if not input_payload.get("deck_url") and "requested_sources" not in input_payload:
        input_payload = {"deck_url": None, "requested_sources": None}

    result = normalize_extraction_request(input_payload)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
