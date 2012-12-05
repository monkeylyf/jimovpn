#!/usr/bin/env python

import setup
import os
import sys
import datetime

from vpn_user.models import Log
from vpn_user.models import Users

def client_connect():
    if len(sys.argv) > 1:
        directive_file = sys.argv[1]
    else:
        directive_file = None
    username    = os.environ.get("username", None)
    assigned_ip = os.environ.get("ifconfig_pool_remote_ip", '??')
    time_unix   = int(os.environ.get("time_unix", "0"))
    remote_ip   = os.environ.get("trusted_ip", '??')
    remote_port   = int(os.environ.get("trusted_port", 0))

    if not username:
        return False
        
    log = Log()
    user = None
    try:
        user = Users.objects.get(username__iexact=username)
    except Users.DoesNotExist:
        return False
    
    log.user = user
    log.start_time = datetime.datetime.fromtimestamp(time_unix)
    log.remote_ip = remote_ip
    log.remote_port = remote_port
    log.vpn_ip = assigned_ip
    log.save()

    return True


if __name__ == "__main__":
    if not client_connect():
        sys.exit(1)
