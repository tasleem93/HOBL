# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
from parameters import Params

def run(scenario):
    # Print loop summary
    val = Params.get("mac_enterprise_collab", "[loop_count]")
    loop_count = int(float(val)) if val else 0
    val = Params.get("mac_enterprise_collab", "[fail_count]")
    fail_count = int(float(val)) if val else 0
    pass_count = loop_count - fail_count
    val = Params.get("mac_enterprise_collab", "[loops]")
    total_loops = val if val else "1"

    logging.info(f"====================================")
    logging.info(f"=== LOOP SUMMARY (after iteration {loop_count} of {total_loops}) ===")
    logging.info(f"  Passed: {pass_count}")
    logging.info(f"  Failed: {fail_count}")
    logging.info(f"====================================")
