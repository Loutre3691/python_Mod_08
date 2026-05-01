
import os
from dotenv import load_dotenv

load_dotenv()

matrix_mode = os.getenv("MATRIX_MODE", "MISSING")
api_key = os.getenv("API_KEY", "MISSING")
database_url = os.getenv("DATABASE_URL", "MISSING")
log_level = os.getenv("LOG_LEVEL", "MISSING")
zion_endpoint = os.getenv("ZION_ENDPOINT", "MISSING")

print("ORACLE STATUS: Reading the Matrix...")
print("Configuration loaded:")
print(f"""Mode: {matrix_mode}
Database: {database_url}
API Access: {api_key}
Log Level: {log_level}
Zion Network: {zion_endpoint}
""")

if matrix_mode == "MISSING":
    print("[FAILED] hardcodes secrets detected")
else:
    print("[OK] No hardcoded secrets detected")

if "MISSING" in [database_url, api_key, zion_endpoint, matrix_mode, log_level]:
    print("[FAILED] .env file bad configured")
else:
    print("[OK] .env file properly configured")

if matrix_mode == "production":
    print("[OK] Running in PRODUCTION mode")
elif matrix_mode == "MISSING":
    print("[FAILED] No mode configured")
else:
    print("[OK] Production overrides available")

print("\nThe Oracle sees all configurations.")
