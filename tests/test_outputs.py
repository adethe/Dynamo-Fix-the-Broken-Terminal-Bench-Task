import json
from collections import Counter
from pathlib import Path


def get_expected_metrics():
    log_path = Path("/app/access.log")
    if not log_path.exists():
        return {"total_requests": 0, "unique_ips": 0, "top_path": ""}

    ips = set()
    paths = []
    total_requests = 0

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total_requests += 1
            parts = line.split()
            if parts:
                ips.add(parts[0])

            try:
                first_quote = line.find('"')
                second_quote = line.find('"', first_quote + 1)
                if first_quote != -1 and second_quote != -1:
                    request_line = line[first_quote + 1 : second_quote]
                    req_parts = request_line.split()
                    if len(req_parts) >= 2:
                        paths.append(req_parts[1])
            except Exception:
                pass

    top_path = Counter(paths).most_common(1)[0][0] if paths else ""
    return {
        "total_requests": total_requests,
        "unique_ips": len(ips),
        "top_path": top_path,
    }


def test_report_values():
    report_path = Path("/app/report.json")
    assert report_path.exists(), "no report.json found"

    with open(report_path, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            assert False, "report.json is not valid JSON"

    expected = get_expected_metrics()

    assert "total_requests" in data, "Missing 'total_requests' key"
    assert "unique_ips" in data, "Missing 'unique_ips' key"
    assert "top_path" in data, "Missing 'top_path' key"

    assert (
        data["total_requests"] == expected["total_requests"]
    ), f"Incorrect total_requests. Got {data['total_requests']}, expected {expected['total_requests']}"
    assert (
        data["unique_ips"] == expected["unique_ips"]
    ), f"Incorrect unique_ips. Got {data['unique_ips']}, expected {expected['unique_ips']}"
    assert (
        data["top_path"] == expected["top_path"]
    ), f"Incorrect top_path. Got '{data['top_path']}', expected '{expected['top_path']}'"