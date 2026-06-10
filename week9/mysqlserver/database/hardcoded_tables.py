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
    "items": [
        id_column,
        Column(
            name="name", type="VARCHAR(100)", constraints=[Constraint(type="NOT NULL")]
        ),
        Column(name="description", type="TEXT", constraints=[Constraint(type="NULL")]),
        Column(name="price", type="FLOAT", constraints=[Constraint(type="NOT NULL")]),
        Column(name="category", type="VARCHAR(50)"),
        Column(
            name="is_active",
            type="BOOLEAN",
            constraints=[Constraint(type="DEFAULT TRUE")],
        ),
        Column(
            name="created_at",
            type="DATETIME",
            constraints=[Constraint(type="DEFAULT CURRENT_TIMESTAMP")],
        )
    ],
}
