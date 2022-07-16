#!/bin/bash

killall conky
sleep 2s
		
conky -c $HOME/.conky/CryptoDash/CryptoDash &> /dev/null &
