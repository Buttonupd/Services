#!/bin/sh

ssh kali@192.168.1.103 <<EOF
  cd /home/kali/Applications/Engineering/Services/Tutorial
  git pull
  source env/bin/activate
  pip install -r requirements.txt
  ./manage.py migrate
  sudo supervisorctl restart Tutorial
  exit
EOF
