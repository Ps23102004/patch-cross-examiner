def dedup(items):
    """Buggy original: tracks `seen` but appends unconditionally."""
    seen = set()
    out = []
    for x in items:
        seen.add(x)
        out.append(x)
    return out
