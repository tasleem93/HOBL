# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import time

def _safe_call(scenario, cmd, desc=""):
    try:
        result = scenario._call(
            ["bash", f"-c \"{cmd}\""],
            expected_exit_code="", fail_on_exception=False,
        )
        if result is None:
            return ""
        if isinstance(result, dict):
            return str(result.get("stdout", result.get("output", "")))
        return str(result).strip()
    except Exception as e:
        logging.warning(f" ERROR - {desc}: {e}")
        return ""

def run(scenario):
    """Kill Office apps and disable proxy so telemetry uploads to dashboard."""
    logging.debug("Executing code block: code_1KILLOF.py")

    # Kill all Office apps for fresh cold boot
    for app in ["Microsoft Excel", "Microsoft Word", "Microsoft PowerPoint", "Microsoft OneNote"]:
        _safe_call(scenario, f"pkill -f '{app}' 2>/dev/null || true", f"kill {app}")

    time.sleep(2)

    check = _safe_call(scenario,
        "pgrep -fl 'Microsoft Excel|Microsoft Word|Microsoft PowerPoint|Microsoft OneNote' || echo 'ALL_KILLED'",
        "verify kill")
    logging.info(f"Office apps after kill: {check}")

    # Disable system proxy so Office telemetry can upload to dashboard
    services = _safe_call(scenario, "networksetup -listallnetworkservices", "list services")
    if services:
        for service in services.splitlines():
            service = service.strip()
            if not service or service.startswith("*") or service.startswith("An asterisk"):
                continue
            _safe_call(scenario, f"networksetup -setwebproxystate '{service}' off", f"proxy off {service}")
            _safe_call(scenario, f"networksetup -setsecurewebproxystate '{service}' off", f"sproxy off {service}")
        logging.info("System proxy disabled for telemetry upload")

    logging.info("Office apps killed, proxy off — ready for fresh boot")
