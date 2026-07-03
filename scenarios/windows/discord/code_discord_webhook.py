# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import logging


def run(scenario):
    logging.debug('Executing code block: code_discord_webhook.py')

    webhook_url = "https://discord.com/api/webhooks/1521100214251950221/94JEnSVYto3Gq5Ufl6i9pyO3-m40B5-P8k3R3kj6OO3OyxHB-izCN2pt_81WCxTGk_Ln"

    ps_command = (
        f"for ($i=1; $i -le 3; $i++) {{"
        f" Invoke-RestMethod -Uri '{webhook_url}'"
        f" -Method POST"
        f" -Body (@{{content=\"Hello test $i\"}} | ConvertTo-Json)"
        f" -ContentType 'application/json';"
        f" Start-Sleep 15"
        f" }}"
    )

    scenario._host_call(
        ["powershell.exe", "-NoProfile", "-Command", ps_command],
        expected_exit_code="0",
        timeout=90
    )
