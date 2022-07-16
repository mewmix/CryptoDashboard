#!/bin/bash

killall conky
sleep 2s
		
conky -c $HOME/.conky/CryptoDashboard/CryptoDash &> /dev/null &
