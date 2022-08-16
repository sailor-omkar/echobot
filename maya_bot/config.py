#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """Bot Configuration"""

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "1b7f2d31-d9dc-4ad0-b32a-45363f9c66aa")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "M@ya0123456789")
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
