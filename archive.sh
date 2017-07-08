#!/usr/bin/env bash 
git archive --format tar  HEAD  |  gzip  > site.tgz 
