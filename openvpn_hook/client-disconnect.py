#!/usr/bin/env python

import setup
import os
import sys

def client_disconnect():
    common_name    = os.environ.get("common_name", None)
    time_duration  = int(os.environ.get("time_duration", 0))
    bytes_received = int(os.environ.get("bytes_received", 0))
    bytes_sent     = int(os.environ.get("bytes_sent", 0))
    remote_ip     = os.environ.get("trusted_ip", None)
    remote_port   = os.environ.get("trusted_port", None)

if __name__ == "__main__":
    client_disconnect()
