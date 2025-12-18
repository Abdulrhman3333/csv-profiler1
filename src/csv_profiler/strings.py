def slugify(text: str) -> str:
    edited = text.casefold().strip().split()
    return "-".join(edited)