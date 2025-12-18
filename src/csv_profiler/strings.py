def slugify(text: str) -> str:
    edited = text.casefold().lower().strip().split()
    return "-".join(edited)