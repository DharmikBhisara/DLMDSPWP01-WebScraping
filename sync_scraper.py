import requests
import pandas as pd
import time
from io import StringIO

# List of dataset URLs
urls = [
    "http://localhost:8000/train.csv",
    "http://localhost:8000/test.csv",
    "http://localhost:8000/ideal.csv"
]

def run_synchronous():
    start = time.time()

    for url in urls:
        r = requests.get(url)
        r.raise_for_status()

        # Read CSV from response text
        df = pd.read_csv(StringIO(r.text))

        # Print filename + shape
        print(f"{url.split('/')[-1]} → {df.shape}")

    end = time.time()
    print("Sync scraping time:", round(end - start, 2), "seconds")

if __name__ == "__main__":
    run_synchronous()
