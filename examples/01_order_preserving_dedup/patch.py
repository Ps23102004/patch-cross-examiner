def dedup(items):
    """AI-written patch: removes duplicates, but loses first-seen order."""
    return list(set(items))
