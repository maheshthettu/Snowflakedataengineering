import snowflake.connector
from .config import SNOWFLAKE_CONFIG

def get_connection():
    try:
        return snowflake.connector.connect(
            user=SNOWFLAKE_CONFIG["user"],
            password=SNOWFLAKE_CONFIG["password"],
            account=SNOWFLAKE_CONFIG["account"]
        )
    except Exception as e:
        raise ConnectionError("Snowflake connection failed") from e
