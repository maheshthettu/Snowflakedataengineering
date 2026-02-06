
# #password authentication 

# import snowflake.connector
# from db_connection.config import SNOWFLAKE_CONFIG

# def get_connection():
#     return snowflake.connector.connect(
#         user=SNOWFLAKE_CONFIG["user"],
#         password=SNOWFLAKE_CONFIG["password"],
#         account=SNOWFLAKE_CONFIG["account"],
#         warehouse=SNOWFLAKE_CONFIG["warehouse"],
#         database=SNOWFLAKE_CONFIG["database"],
#         schema=SNOWFLAKE_CONFIG["schema"]
#     )



#token authentication 

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import snowflake.connector
from db_connection.config import SNOWFLAKE_CONFIG

def get_connection():
    with open(SNOWFLAKE_CONFIG["private_key_path"], "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    return snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG["user"],
        account=SNOWFLAKE_CONFIG["account"],
        private_key=private_key,
        warehouse=SNOWFLAKE_CONFIG["warehouse"],
        database=SNOWFLAKE_CONFIG["database"],
        schema=SNOWFLAKE_CONFIG["schema"]
    )