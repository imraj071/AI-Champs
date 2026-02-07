import pandas as pd

class ExcelService:

    def load(self, path, sheet):
        return pd.read_excel(path, sheet_name=sheet)

    def save(self, df, path):
        df.to_excel(path, index=False)
        del df

