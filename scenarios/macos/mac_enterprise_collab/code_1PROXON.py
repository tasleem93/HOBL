# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging

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
    """Re-enable system proxy for web_replay after Office apps are closed."""
    logging.debug("Executing code block: code_1PROXON.py")

    if hasattr(scenario, 'web_replay_run') and scenario.web_replay_run == '1':
        services = _safe_call(scenario,
            "networksetup -listallnetworkservices",
            "list services")
        if services and hasattr(scenario, 'web_replay_ip') and hasattr(scenario, 'web_replay_http_port'):
            for service in services.splitlines():
                service = service.strip()
                if not service or service.startswith("*") or service.startswith("An asterisk"):
                    continue
                _safe_call(scenario,
                    f"networksetup -setwebproxy '{service}' {scenario.web_replay_ip} {scenario.web_replay_http_port}",
                    f"restore http proxy {service}")
                _safe_call(scenario,
                    f"networksetup -setsecurewebproxy '{service}' {scenario.web_replay_ip} {scenario.web_replay_https_port}",
                    f"restore https proxy {service}")
            logging.info("System proxy re-enabled for web_replay")
        else:
            logging.info("web_replay proxy settings not available, skipping restore")
    else:
        logging.info("web_replay not active, no proxy to restore")
