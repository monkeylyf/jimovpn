#!/usr/bin/env python

import setup
import os
import sys
import datetime
from vpn_user.models import Users,Log

def client_disconnect():
    common_name    = os.environ.get("common_name", None)
    time_duration  = int(os.environ.get("time_duration", 0))
    bytes_received = int(os.environ.get("bytes_received", 0))
    bytes_sent     = int(os.environ.get("bytes_sent", 0))
    remote_ip     = os.environ.get("trusted_ip", '??')
    remote_port   = int(os.environ.get("trusted_port", 0))

    if not common_name:
        return False
    
    try:
        log = Log.objects.get(user__username__iexact=common_name, remote_ip__iexact=remote_ip, remote_port__iexact=remote_port)
    except Log.DoesNotExist:
        return False
    log.end_time = datetime.datetime.fromtimestamp(time_unix)
    log.bytes_received = bytes_received
    log.bytes_sent = bytes_received
    log.disconnected = True
    log.save()
    return True

if __name__ == "__main__":
    client_disconnect()
