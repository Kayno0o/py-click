#!/bin/bash

# Set variables
PWD=$(pwd)
SERVICE_FILE="clicklog.python.service"
DEST_PATH="./$SERVICE_FILE"

# Generate service file content with substitutions
cat <<EOF >$SERVICE_FILE
[Unit]
Description=Your Service Description
After=display-manager.service

[Service]
Type=simple
Environment="DISPLAY=:0"
ExecStart=/usr/bin/python3 $PWD/main.py
Restart=always
RestartSec=3
User=$USER
Environment="XAUTHORITY=/home/$USER/.Xauthority"

[Install]
WantedBy=multi-user.target
EOF

echo "Generated service file: $DEST_PATH"
