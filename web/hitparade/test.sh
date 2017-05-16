#!/bin/bash -ex

time ./manage.py test $1 --keepdb
