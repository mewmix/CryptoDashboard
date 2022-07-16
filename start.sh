#!/bin/bash
set -a
source .env
set +a 
killall conky
sleep 2s
		
conky -c $HOME/.conky/CryptoDashboard/CryptoDash &> /dev/null &
