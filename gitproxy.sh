#!/bin/sh
env
logger giiiiitproxy
exit 22
exec ssh vps nc $1 $2
