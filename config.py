from pathlib import Path

# Base directory (automatically detects parent folder)
BASE_DIR = Path(__file__).parent

config = {
    'DATA_PATH': str(BASE_DIR / "data"), 
    'MODEL_PATH': str(BASE_DIR / "model"),
    'BASE_PATH': str(BASE_DIR),  
}

# Validation (optional but recommended)
assert Path(config['DATA_PATH']).exists(), f"Data directory not found at {config['DATA_PATH']}"
assert Path(config['MODEL_PATH']).exists(), f"Model directory not found at {config['MODEL_PATH']}"
