"""Data Access Object working with table `account`."""
import ormar

from . import PgBaseMeta


class PgProduct(ormar.Model):

    class Meta(PgBaseMeta):
        tablename = "product"

    pid = ormar.BigInteger(autoincrement=False, primary_key=True)
    product_name = ormar.String(max_length=256)
    description = ormar.Text()
