# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import threading

def _upload_large_files(scenario):
    try:
        # Get home directory from DUT and construct iCloud Drive path
        home_dir = scenario._call(["bash", "-c \"echo $HOME\""], expected_exit_code="").strip()
        # iCloud Drive path on macOS (equivalent to OneDrive on Windows)
        icloud_base = f"{home_dir}/Library/Mobile Documents/com~apple~CloudDocs"
        download_dir = f"{icloud_base}/onedrivetest"  # Using same subfolder name as Windows example
        scenario._upload("scenarios/abl_resources/large", download_dir)
        logging.info(f"Successfully uploaded files to {download_dir}")

    except Exception as e:
        logging.error(f"Could not copy large files to onedrive: {e}")

def run(scenario):
    logging.debug('Executing code block: code_1ARKC3A.py')
    t = threading.Thread(target=_upload_large_files, args=(scenario,), name="upload_worker", daemon=True)
    scenario.upload_thread = t  # Persist thread object on scenario
    t.start()
