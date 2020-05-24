#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example of global variable
"""


def init_stats():
    global _stats
    _stats = {}
    
def event_occurred(event):
    global _stats
    try:
        _stats[event] += 1
    except KeyError:
        _stats[event] = 1

def get_stats():
    global _stats
    return sorted(_stats.items())
