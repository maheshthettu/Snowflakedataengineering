# #Password Authentication 

# SNOWFLAKE_CONFIG = {
#     "user": "MAHESH",
#     "password": "*************",
#     "account": "SROTSLD-VP20091",
#     "warehouse": "COMPUTE_WH",
#     "database": "COLLEGE",
#     "schema": "BRANCH"
# }

#token authenticaton 

from dotenv import load_dotenv
import os
load_dotenv()  

SNOWFLAKE_CONFIG = {
    "user": os.getenv("SNOWFLAKE_USER"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA"),
    "private_key_path": os.getenv("SNOWFLAKE_PRIVATE_KEY_PATH")
}