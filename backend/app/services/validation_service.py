from app.domain.rules import OPERATIONS

class ValidationService:

    def apply(self, df, col, threshold, op, out_col):
        rule = OPERATIONS.get(op)
        df[out_col] = df[col].apply(
            lambda x: "Success" if rule(x, threshold) else "Fail"
        )
        return df
