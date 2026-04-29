# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
from parameters import Params

def run(scenario):
    # Increment failure counter
    val = Params.get("mac_enterprise_collab", "[fail_count]")
    fail_count = int(float(val)) if val else 0
    fail_count += 1
    Params.setParam("mac_enterprise_collab", "[fail_count]", str(fail_count))

    val = Params.get("mac_enterprise_collab", "[loop_count]")
    loop_count = int(float(val)) if val else 0

    logging.info(f"=== LOOP FAILURE: Iteration {loop_count} FAILED | Total failures so far: {fail_count} ===")
