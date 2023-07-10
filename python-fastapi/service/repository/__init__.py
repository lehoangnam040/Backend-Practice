"""Repository layer to deal with data layer."""
from service.configs.setting import settings_factory
from service.repository.interface.factory import RepositoryFactory, SupportedDbType

settings = settings_factory()
factory = RepositoryFactory(db_type=SupportedDbType(settings.db_type))

account_repository = factory.create_account_repository()
