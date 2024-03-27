#!/bin/bash
#Sends aPOST with variables to a uRL
curl -sX POST "email:test@gmail.com&subject:I will always be here for PLD" "$1"
