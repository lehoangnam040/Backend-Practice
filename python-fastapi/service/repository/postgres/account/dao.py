"""Data Access Object working with table `account`."""
import ormar

from service.repository.postgres import database, metadata


class PgAccount(ormar.Model):

    """Data Access Object working with table `account`."""

    class Meta:

        """Metadata of `PgAccount`."""

        tablename = "account"
        metadata = metadata
        database = database

    uid = ormar.BigInteger(autoincrement=False, primary_key=True)
    username = ormar.String(max_length=64, unique=True)
    hashed_password = ormar.String(max_length=256)
