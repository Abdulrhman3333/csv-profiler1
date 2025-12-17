# def basic_profile(rows: list[dict[str, str]]) -> dict:
#     columns = list(rows[0].keys())
#     missing = {c: 0 for c in columns}
#     non_empty = {c: 0 for c in columns}

#     for row in rows:
#         for c in columns:
#             v = (row.get(c) or "").strip()
#             if v == "":
#                 missing[c] += 1
#             else:
#                 non_empty[c] += 1
    
#     return {
#         "total_rows": len(rows),
#         "columns": [
#             {
#                 "name": c,
#                 "missing": missing[c],
#                 "non_empty": non_empty[c]
#             }
#             for c in columns
#         ],
#         "summary":,
        
#     }

def basic_profile(rows: list[dict[str, str]]) -> dict:
    columns_old = list(rows[0].keys())
    missing = {c: 0 for c in columns}
    non_empty = {c: 0 for c in columns}
    columns = {}

    for column in columns_old:
        col_val = column_values(rows,column)
        col_info = {}
        col_info['type'] = infer_type(col_val)
        if col_info['type'] == 'text':
            col_info['stats'] = text_stats(col_val)
        else:
            col_info['stats'] = numeric_stats(col_val)

        columns[column] = col_info    
    return {
        "summary":{"columns:":len(rows[0].keys()),"rows:":len(rows)},
        "columns":columns
    }
    

MISSING = {"", "na", "n/a", "null", "none", "nan"}
def is_missing(value: str | None) -> bool:
    if value is None:
        return True
    return value.strip().casefold() in MISSING

def try_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None

def infer_type(values: list[str]) -> str:
    usable = [v for v in values if not is_missing(v)]
    if not usable:
        return "text"
    for v in usable:
        if try_float(v) is None:
            return "text"
    return "number"

def column_values(rows: list[dict[str, str]], col: str) -> list[str]:
    return [row.get(col, "") for row in rows]

def numeric_stats(values: list[str]) -> dict:
    usable = []
    for v in values:
        if is_missing(v):
            continue
        else:
            usable.append(v)
    
    nums = [try_float(v) for v in usable]
    
    count = len(nums)
    missing = len(values) - count
    unique = len(set(nums))
    min_val = min(nums)
    max_val = max(nums)
    mean_val = sum(nums) / count
    return{
        "count":count,
        "missing":missing,
        "unique": unique,
        "min":min_val,
        "max":max_val,
        "mean":mean_val
    }

def text_stats(values: list[str], top_k: int = 5) -> dict:
    usable = []
    for v in values:
        if is_missing(v):
            continue
        else:
            usable.append(v)

    count = len(usable)
    missing = len(values) - count
    unique = len(set(usable))
    counts: dict[str, int] = {}
    for v in usable:
        counts[v] = counts.get(v, 0) + 1

    
    top_items = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:top_k]
    top = [{"value": v, "count": c} for v, c in top_items]

    return{
        "count":count,
        "missing":missing,
        "unique": unique,
        "top-k":top

    }