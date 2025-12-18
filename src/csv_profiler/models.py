class ColumnProfile:
    def __init__(self, name: str, inferred_type: str, total: int, missing: int, unique: int):
        self.name = name
        self.inferred_type = inferred_type
        self.total = total
        self.missing = missing
        self.unique = unique
        
    @property
    def missing_pct(self) -> float:
        return 100.0 * self.missing / self.total

    def to_dict(self) -> dict:
        return{
            "name":self.name,
            "inferred_type":self.inferred_type,
            "total":self.total,
            "missing":self.missing,
            "unique":self.unique
        }
    
    def __repr__(self) -> str:
        return (
            f"ColumnProfile(name={self.name!r}, type={self.inferred_type!r}, "
            f"missing={self.missing}, total={self.total}, unique={self.unique})"
        )