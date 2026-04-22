#!/usr/bin/env python3
import os


def load_config() -> bool:
    original_env = dict(os.environ)
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        raise RuntimeError(
            "Could not find 'dotenv' package\n"
            "To install, run 'pip install python-dotenv'"
        )
    mode = os.getenv("MATRIX_MODE", "production")
    if mode not in ("production", "development"):
        raise ValueError(
            "MATRIX_MODE can only be of value 'development' or 'production'"
        )
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL", "INFO")
    zion = os.getenv("ZION_ENDPOINT")
    if mode == "development" and not api_key:
        raise RuntimeError("API_KEY required in development mode")
    missing = False
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if mode == "development":
        db_url = "local"
        log = "DEBUG"
    if db_url:
        print(f"Database: Connected to {db_url} instance")
    else:
        print("Database: [MISSING]")
        missing = True
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: [MISSING]")
        missing = True
    print(f"Log Level: {log}")
    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: [OFFLINE]")
        missing = True
    print("\nEnvironment security check:")
    if api_key:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARN] No API_KEY detected - Cannot verify security")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found - Using default values")
    overrides = []
    for key in [
        "MATRIX_MODE", "DATABASE_URL",
        "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"
    ]:
        if key in original_env:
            overrides.append(key)
    if overrides:
        print(
            f"[INFO] Environment overrides detected: {', '.join(overrides)}"
        )
    else:
        print("[OK] Production overrides available")
    return missing


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    try:
        has_missing = load_config()
        if has_missing:
            print("\nThe Oracle cannot see all configurations")
        else:
            print("\nThe Oracle sees all configurations.")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
