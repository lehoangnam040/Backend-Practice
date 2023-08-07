"""Data Access Object working with table `account`."""
import ormar

from . import PgBaseMeta


class PgAccount(ormar.Model):

    """Data Access Object working with table `account`."""

    class Meta(PgBaseMeta):

        """Metadata of `PgAccount`."""

        tablename = "account"

    uid = ormar.BigInteger(autoincrement=False, primary_key=True)
    username = ormar.String(max_length=64, unique=True)
    hashed_password = ormar.String(max_length=256)
