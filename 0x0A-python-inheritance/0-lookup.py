#!/usr/bin/python3
"""Defines an objectattribute lookup function."""

def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    attributes = dir(obj)
    return attributes
