#!/bin/bash 
echo Executing >> /tmp/config.log
echo Params: 1: $1 2: $2 3: $3 4: $4>> /tmp/config.log

cd /tmp

echo STORAGE_QUEUE_NAME = \'$1\' > config.py
echo STORAGE_ACCOUNT_NAME = \'$2\' >> config.py
echo STORAGE_ACCOUNT_KEY = \'$3\' >> config.py

/bin/wget https://github.com/circadence/scripts/raw/master/requirements.txt
/bin/wget https://github.com/circadence/scripts/raw/master/listener.py

sudo yum install -y python3
pip3 install virtualenv
/usr/local/bin/virtualenv -p python3 venv
. venv/bin/activate
venv/bin/python -m pip install -r requirements.txt
( venv/bin/python listener.py | tee /tmp/listener.log ) &
