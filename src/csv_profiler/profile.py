def basic_profile(rows: list[dict[str, str]]) -> dict:


    columns = list(rows[0].keys())
    missing = {c: 0 for c in columns}
    non_empty = {c: 0 for c in columns}

    for row in rows:
        for c in columns:
            v = (row.get(c) or "").strip()
            if v == "":
                missing[c] += 1
            else:
                non_empty[c] += 1
    
    return {
        "total_rows": len(rows),
        "columns": [
            {
                "name": c,
                "missing": missing[c],
                "non_empty": non_empty[c]
            }
            for c in columns
        ]
    }