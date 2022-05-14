#! /bin/bash

ssh <user>@$1 "cd $HOME/git/projects/ ; git pull origin master"
