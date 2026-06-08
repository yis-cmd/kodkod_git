from database.base_models import Column, Constraint

id_constraints = [
    Constraint.model_validate({"type": "AUTO_INCREMENT"}),
    Constraint.model_validate({"type": "PRIMARY KEY"}),
]

id_column = Column.model_validate(
    {"name": "id", "type": "INT", "constraints": id_constraints}
)

tables = {
    "students": [
        id_column,
        Column.model_validate(
            {
                "name": "course_name",
                "type": "VARCHAR(100)",
            }
        ),
        Column.model_validate(
            {
                "name": "email",
                "type": "VARCHAR(100)",
            }
        ),
    ],
    "courses": [
        id_column,
        Column.model_validate(
            {
                "name": "full_name",
                "type": "VARCHAR(100)",
            }
        ),
        Column.model_validate(
            {
                "name": "price",
                "type": "DECIMAL(10,2)",
            }
        ),
    ],
    "teachers": [
        id_column,
        Column.model_validate(
            {
                "name": "full_name",
                "type": "VARCHAR(100)",
            }
        ),
        Column.model_validate(
            {
                "name": "salary",
                "type": "DECIMAL(10,2)",
            }
        ),
    ],
}
