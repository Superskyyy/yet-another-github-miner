# How to Dev and Use:

**THE PROJECT IS FOR EDUCATIONAL PURPOSES ONLY, anyone using this scraper is expected to adhere to GitHub regulations**

## Components 

### Scraper
Scraper filters GitHub for matched repos containing the wanted file at any depth,

~Only the first batch of 1000 results will be returned.~ Sample scraper shows a way to overcome the limitation

Example file target: `MLProject`

GitHub Query - `filename:MLProject`

## Install

Install dependencies - `pip install -r requirements.txt`

### Run

Change the `sample_credentials.py` to `crendentials.py` upon cloning, then fill in your GitHub personal access token.

Run `main.py` to filter through repos and paths.

Run `miner_selenium.py` to run the chrome-based selenium scraper.

Run `miner_requests.py` to run the GitHub v3 API scraper.

Run `pickle_loader.py` to see the first 1000 results collected.





