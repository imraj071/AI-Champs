from app.domain.models import ExcelConfig, RunConfig

class ConfigLoader:

    @staticmethod
    def from_db(job):
        return RunConfig(
            dry_run=False,
            excel=ExcelConfig(
                file_path=job.file_path,
                sheet_name=job.sheet_name,
                column_to_validate=job.column_name,
                threshold=job.threshold,
                operation=job.operation,
                output_column=job.output_column,
                mode="overwrite",
            )
        )
