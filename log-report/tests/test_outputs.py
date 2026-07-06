import json
import re
from pathlib import Path
from collections import Counter

def _compute_expected():
    paths, ips, total = Counter(), set(), 0
    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            parts = line.split()
            if parts:
                ips.add(parts[0])
            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1
    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0] if paths else None
    }

def test_report_file_exists():
    """The agent must create /app/report.json as a file."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "File /app/report.json does not exist"
    assert report_path.is_file(), "/app/report.json is not a file"

def test_report_json_parsable():
    """The report file /app/report.json must be valid JSON."""
    report_path = Path("/app/report.json")
    try:
        with open(report_path) as f:
            json.load(f)
    except json.JSONDecodeError as e:
        assert False, f"Failed to parse /app/report.json as JSON: {e}"

def test_report_structure_and_values():
    """The report file /app/report.json must contain total_requests, unique_ips, and top_path matching the access log summary metrics exactly."""
    with open("/app/report.json") as f:
        data = json.load(f)
    
    assert isinstance(data, dict), "Report root must be a JSON object"
    
    required_keys = {"total_requests", "unique_ips", "top_path"}
    assert required_keys.issubset(data.keys()), f"Report must contain keys: {required_keys}"
    
    expected = _compute_expected()
    
    assert data["total_requests"] == expected["total_requests"], f"Expected total_requests {expected['total_requests']}, got {data['total_requests']}"
    assert data["unique_ips"] == expected["unique_ips"], f"Expected unique_ips {expected['unique_ips']}, got {data['unique_ips']}"
    assert data["top_path"] == expected["top_path"], f"Expected top_path {expected['top_path']}, got {data['top_path']}"
