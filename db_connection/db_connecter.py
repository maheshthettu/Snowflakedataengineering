
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

import snowflake.connector
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from snowflake.connector.errors import Error as SnowflakeError
from db_connection.config import SNOWFLAKE_CONFIG


def get_connection():
    try:
        # Load private key
        with open(SNOWFLAKE_CONFIG["private_key_path"], "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )

        # Create connection
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_CONFIG["user"],
            account=SNOWFLAKE_CONFIG["account"],
            private_key=private_key,
            warehouse=SNOWFLAKE_CONFIG["warehouse"],
            database=SNOWFLAKE_CONFIG["database"],
            schema=SNOWFLAKE_CONFIG["schema"]
        )

        return conn

    except FileNotFoundError:
        raise Exception(
            f"Private key file not found at: {SNOWFLAKE_CONFIG['private_key_path']}"
        )

    except SnowflakeError as e:
        raise Exception(
            f"Unable to connect to Snowflake account "
            f"{SNOWFLAKE_CONFIG['account']} as user {SNOWFLAKE_CONFIG['user']}. "
            f"Error: {str(e)}"
        )

    except Exception as e:
        raise Exception(f"Unexpected error during Snowflake connection: {str(e)}")
