#!/usr/bin/env python3

import re

log_file_text = """
2017-04-26 17:45:05,002 - INFO - user:123|action:delete|data:img
2017-04-26 17:45:07,345 - INFO - action:update|user:456
2017-04-26 17:45:07,345 - INFO - action:create|src:home|user:abc
2017-04-26 17:45:07,345 - ERROR - action:delete|user:def|data:img
2017-04-26 17:45:07,345 - INFO - user:789|action:delete|data:img
2017-04-26 17:45:07,345 - INFO - action:delete|user:123|data:var
2017-04-26 17:45:07,345 - ERROR - user:123|action:read|data:home
2017-04-26 17:45:07,345 - INFO - user:8|action:copy|src:img|dest:bak
"""


def natkey(element):
    """Help natsorted compare elements by splitting elements into tuples
       containing strings and numbers
    """

    def intize(e):
        try:
            return int(e)
        except ValueError:
            return e

    return [intize(e)
            for e in re.split('([?!0-9]+)', element)]


def natsorted(elements):
    """Poor mans natural sort
    """

    return sorted(elements, key=natkey)


def parse(log):
    """Extract sorted list of user ids from log entries
       Numbers and strings are processed separately to make natural sorting
       work with negative user ids.
    """

    numbers = []
    strings = []
    for line in log_file_text.split("\n"):
        if not line:
            continue
        try:
            id = re.search("(user:)(.*)", line).group(2).split("|")[0]
            try:
                numbers.append(int(id))
            except ValueError:
                strings.append(id)

        except (AttributeError, IndexError) as _:
            print("ERROR: Unknown line format: {}".format(line))

    ids = sorted(set(numbers)) + natsorted(set(strings))

    return (str(id) for id in ids)

print("User id(s): {}".format(list(parse(log_file_text))))
