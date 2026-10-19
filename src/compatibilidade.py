
"""Compatibilidade entre a biblioteca Experta e Python 3.11."""

import collections
import collections.abc


def preparar_experta():
    """Disponibiliza Mapping para dependências antigas da Experta."""
    if not hasattr(collections, "Mapping"):
        collections.Mapping = collections.abc.Mapping
