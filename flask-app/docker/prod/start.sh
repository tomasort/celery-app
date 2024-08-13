#!/bin/sh

flask db migrate
flask db upgrade
uwsgi uwsgi.ini