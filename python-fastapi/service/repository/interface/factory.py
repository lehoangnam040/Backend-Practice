"""Factory to create repository instances."""


class RepositoryFactory:

    """Factory to create repository instances."""

    def __init__(self: "RepositoryFactory", db_type: str) -> None:
        """Init factory."""
        self.db_type = db_type
