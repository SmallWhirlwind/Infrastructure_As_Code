#!/usr/bin/python
# -*- coding: utf-8 -*-
def test_git_is_installed(Package):
    git = Package("git")
    assert git.is_installed       # git是否安装