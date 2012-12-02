#!/usr/bin/env python

import setup
import os
import sys

def authenticate(username, password):
    remote_ip = os.environ.get("untrusted_ip", "0.0.0.0")
    return username == "rx201"

if __name__ == "__main__":
    username = os.environ.get('username', '')
    password = os.environ.get('password', '')
    if authenticate(username, password):
        sys.exit(0)
    else:
        sys.exit(1)

