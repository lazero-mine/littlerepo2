#!/bin/bash
find | grep -o ".*\.sh$" | xargs chmod +x
