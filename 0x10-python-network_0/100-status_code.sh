#!/bin/bash
#Displays only the status code of the response.
curl -sILw "%{http_code}" "$1"
