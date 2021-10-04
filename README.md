# How to Dev and Use:

**THE PROJECT IS FOR EDUCATIONAL PURPOSES ONLY**

## Components 

### Criteria Assessment 
Based on GitHub API v3 and GraphQL API v4, add new ones to `apis`

### Scraper
Scraper filters the entire GitHub for matched repos containing the wanted file at any depth

For example: `MLProject`

GitHub Query - `filename:MLProject`

## Install

Install dependencies - `pip install -r requirements.txt`

### Run

Change the `sample_credentials.py` to `crendentials.py` upon cloning, then fill in your GitHub personal access token.

Run `main.py` to filter through repos and paths.

Run `miner_selenium.py` to run the chrome-based selenium scraper.

Run `pickle_loader.py` to see the first 1000 results collected.





