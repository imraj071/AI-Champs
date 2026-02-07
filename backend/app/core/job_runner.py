from datetime import datetime

class JobRunner:

    def __init__(self, excel_svc, fs_svc, val_svc, log_svc):
        self.excel = excel_svc
        self.fs = fs_svc
        self.val = val_svc
        self.log = log_svc

    def run(self, config):
        self.log.log("Job Started")

        input_path = self.fs.read(config.excel.file_path)

        df = self.excel.load(input_path, config.excel.sheet_name)

        df = self.val.apply(
            df,
            config.excel.column_to_validate,
            config.excel.threshold,
            config.excel.operation,
            config.excel.output_column,
        )

        temp_output = f"updated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        self.excel.save(df, temp_output)

        config.dry_run or self.fs.write(temp_output, config.excel.file_path)

        self.log.log("Job Completed")
