#!/usr/bin/env python

import setup
import os
import sys
from vpn_user.models import Users
from vpn_user.hashers import MyPBKDF2PasswordHasher

def authenticate(username, password):
    remote_ip = os.environ.get("untrusted_ip", "0.0.0.0")
    try:
        user = Users.objects.get(username__iexact=username)
        return user.enabled and MyPBKDF2PasswordHasher().verify(password, user.password)
    except Users.DoesNotExist:
        pass
    return False

if __name__ == "__main__":
    username = os.environ.get('username', '')
    password = os.environ.get('password', '')
    if authenticate(username, password):
        sys.exit(0)
    else:
        sys.exit(1)

