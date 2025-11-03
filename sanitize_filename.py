def sanitize_filename(name: str, max_length: int = 100, lowercase: bool = False) -> str:
    """
    Returns a "safe" file name:
    - Replaces spaces with dashes
    - Removes disallowed characters (keeps only letters, digits, dash, underscore, dot)
    - Trims leading/trailing dots or dashes
    - Shortens to `max_length` if too long
    - Optionally converts to lowercase if `lowercase=True`
    """
    if not isinstance(name, str):
        raise TypeError("Expected a string for 'name'")

    s = name.strip()
    s = re.sub(r'\s+', '-', s)
    s = re.sub(r'[^A-Za-z0-9\-\_\.]', '', s)
    s = s.strip('-.')
    
    if len(s) > max_length:
        s = s[:max_length].rstrip('-.')
    
    if not s:
        s = 'file'

    if lowercase:
        s = s.lower()

    return s


if __name__ == "__main__":
    examples = [
        "  My résumé (final).pdf  ",
        "project:alpha/v2!!",
        "    ",
    ]
    for e in examples:
        print(f"Original: {e!r} -> Sanitized: {sanitize_filename(e, lowercase=True)}")
