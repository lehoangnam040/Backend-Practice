import os
import sys
from glob import glob
from importlib import util
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../../../")

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
from service.databases.postgres import DB_URL, metadata
from service.databases.postgres import account, product

# def import_submodules(start_path: str):
#     start_path = os.path.abspath(start_path)
#     py_files = [f for f in glob(os.path.join(start_path, "*.py"))] # if not f.endswith("__.py")
#     for py_file in py_files:
#         spec = util.spec_from_file_location("", py_file)
#         module = util.module_from_spec(spec)
#         spec.loader.exec_module(module)
# import_submodules(myPath + "/../../../service/databases/postgres/")
target_metadata = metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=DB_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    print(DB_URL)
    connectable = create_engine(DB_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
