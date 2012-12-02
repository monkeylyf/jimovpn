#!/usr/bin/env python

import setup
import os
import sys

def client_connect():
    if len(sys.argv) > 1:
        directive_file = sys.argv[1]
    else:
        directive_file = None
    common_name = os.environ.get("common_name", None)
    assigned_ip = os.environ.get("ifconfig_pool_remote_ip", None)
    time_unix   = int(os.environ.get("time_unix", "0"))
    remote_ip   = os.environ.get("trusted_ip", None)
    remote_port = os.environ.get("trusted_port", None)

if __name__ == "__main__":
    client_connect()
