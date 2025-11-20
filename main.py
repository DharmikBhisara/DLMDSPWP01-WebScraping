# main.py
# Entry point to run both synchronous and asynchronous scraping tests

from src.sync_scraper import run_synchronous
from src.async_scraper import run_asynchronous
import asyncio

print("\n========================")
print(" RUNNING SYNCHRONOUS ")
print("========================\n")
run_synchronous()

print("\n===========================")
print(" RUNNING ASYNCHRONOUS ")
print("===========================\n")
asyncio.run(run_asynchronous())

print("\nDone.")
