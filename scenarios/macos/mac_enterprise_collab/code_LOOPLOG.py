# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
from parameters import Params

def run(scenario):
    # Increment loop counter
    val = Params.get("mac_enterprise_collab", "[loop_count]")
    loop_count = int(float(val)) if val else 0
    loop_count += 1
    Params.setParam("mac_enterprise_collab", "[loop_count]", str(loop_count))

    val = Params.get("mac_enterprise_collab", "[fail_count]")
    fail_count = int(float(val)) if val else 0
    val = Params.get("mac_enterprise_collab", "[loops]")
    total_loops = val if val else "1"

    logging.info(f"=== LOOP STATUS: Starting iteration {loop_count} of {total_loops} | Passed: {loop_count - 1 - fail_count} | Failed: {fail_count} ===")
