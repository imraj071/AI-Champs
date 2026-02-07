from app.infrastructure.repositories import JobConfigRepository

repo = JobConfigRepository()

repo.create_config(
    file_path="input.xlsx",
    sheet_name="Sheet1",
    column_name="Bot",
    threshold=50,
    operation=">",
    output_column="Validation"
)

print("Seed data inserted.")
