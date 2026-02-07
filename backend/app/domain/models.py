from pydantic import BaseModel

class ExcelConfig(BaseModel):
    file_path: str
    sheet_name: str
    column_to_validate: str
    threshold: float
    operation: str
    output_column: str
    mode: str  # overwrite | new_version


class RunConfig(BaseModel):
    dry_run: bool
    excel: ExcelConfig
