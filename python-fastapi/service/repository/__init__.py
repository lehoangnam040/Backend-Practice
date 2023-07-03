"""Repository layer to deal with data layer."""
from service.configs.setting import settings_factory
from service.repository.interface.factory import RepositoryFactory

settings = settings_factory()
factory = RepositoryFactory(db_type=settings.db_type)
