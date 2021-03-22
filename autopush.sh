#!/bin/bash
message=$(sh gencommit.sh)
git config credential.helper store
git add .
git commit -m "$message"
git push origin master
