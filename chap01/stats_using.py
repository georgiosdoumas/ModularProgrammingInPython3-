#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple example of calling a module that has a global variable and some functions
In the same dir there must exist file stats.py 
"""

import stats
stats.init_stats()
stats.event_occurred("meal_eaten")
stats.event_occurred("snack_eaten")
stats.event_occurred("meal_eaten")
stats.event_occurred("snack_eaten")
stats.event_occurred("meal_eaten")
stats.event_occurred("diet_started")
stats.event_occurred("meal_eaten")
stats.event_occurred("meal_eaten")
stats.event_occurred("meal_eaten")
stats.event_occurred("diet_abandoned")
stats.event_occurred("snack_eaten")

for event, number_of_times in stats.get_stats():
    print("{} occured {} times".format(event, number_of_times))
