# run_pipeline.py

import subprocess

print("Running ETL Pipeline...")

subprocess.run(
    ["python", "scripts/etl_pipeline.py"]
)

print("Completed")