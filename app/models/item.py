from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    __tablename__ = "items"

    id: int | None = Field(default=None, primary_key=True)
    nom: str = Field(index=True)
    prix: float
<<<<<<< HEAD

    def _legacy_method(self):
        pass
=======
>>>>>>> 46bded4 (chore: setup pre-commit hooks for linting, formatting and security)
