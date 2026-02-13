import json
import logging
import pandas as pd

# -------------------------------------
# Logging Setup
# -------------------------------------
logging.basicConfig(
    filename="model_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_message(message):
    logging.info(message)


# -------------------------------------
# Schema Validation
# -------------------------------------
def validate_schema(input_df, expected_schema):
    missing_cols = [col for col in expected_schema if col not in input_df.columns]
    
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")
    
    return True
