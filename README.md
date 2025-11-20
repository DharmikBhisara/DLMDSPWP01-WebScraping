# DLMDSPWP01 – Web Scraping Performance Comparison  
## Synchronous vs Asynchronous Web Scraping in Python

### 📌 Overview

This project is part of the IU module *Programming with Python (DLMDSPWP01)*.  
It compares the performance of **synchronous** (`requests`) and **asynchronous** (`aiohttp + asyncio`) web scraping approaches in Python.

The goal is to analyse:
- Execution time differences
- Behaviour in network-bound tasks
- Reliability and correctness of downloaded datasets

The experiment downloads multiple CSV datasets and measures how long each approach takes to complete the same task.

---

### 📁 Project Structure

```text
.
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── ideal.csv
├── src/
│   ├── sync_scraper.py
│   ├── async_scraper.py
│   ├── performance_measurement.py
│   ├── data_loader.py
│   └── visualization.py
├── tests/
│   └── test_scrapers.py
├── requirements.txt
├── main.py
└── README.md

