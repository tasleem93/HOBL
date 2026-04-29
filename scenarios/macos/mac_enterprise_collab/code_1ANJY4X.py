# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging
import os

def run(scenario):
    logging.debug('Executing code block: code_1ANJY4X.py')

    target_path = "scenarios\\abl_resources\\large"

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for i in range(3):
        os.system("fsutil file createnew " + target_path + "\\temp_" + str(i) + ".bin 1395864371")

    logging.info("Large files created for OneDrive copy operations")
