"""Sample filters for doing mildly useful things using FilterPipes."""

try:
    from FilterPipes import filterpipes  # ST3-style import
except ImportError:
    import filterpipes  # ST2-style import


class ReverseWordsCommand(filterpipes.FilterPipesCommandBase):
    """Reverse the order of selected words. Extremely simple example."""
    def filter(self, data):
        return " ".join(reversed(data.split(" ")))
