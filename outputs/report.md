# CSV Profiling Report
- Source: data/sample.csv

## Summary
- Rows: 6
- Columns: 4

## Columns (table)
| Column | Type | Missing % | Unique | Extra |
|---|---|---:|---:|---|
| name | text | 0.0% | 6 | top: Aisha(1), Fahad(1), Noor(1) |
| age | number | 33.3% | 4 | min=23.0, max=34.0, mean=29.25 |
| city | text | 16.7% | 4 | top: Jeddah(2), Riyadh(1), Dammam(1) |
| salary | number | 33.3% | 4 | min=9000.0, max=15000.0, mean=11777.75 |

## Columns (details)

### name
- Type: text
- Non-empty: 6
- Missing: 0
- Top values:
  - Aisha: 1
  - Fahad: 1
  - Noor: 1
  - Salem: 1
  - Ahmed: 1

### age
- Type: number
- Non-empty: 4
- Missing: 2
- Min: 23.0
- Max: 34.0
- Mean: 29.25

### city
- Type: text
- Non-empty: 5
- Missing: 1
- Top values:
  - Jeddah: 2
  - Riyadh: 1
  - Dammam: 1
  - Khobar: 1

### salary
- Type: number
- Non-empty: 4
- Missing: 2
- Min: 9000.0
- Max: 15000.0
- Mean: 11777.75

