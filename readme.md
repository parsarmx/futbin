# FIFA Player Price Updater

## Overview

The FutbinCrawler is a Python application designed to automate the process of fetching and updating player prices from the Futbin website based on a list of player names provided in a CSV file.

## Features

- **CSV Input:** The application reads a CSV file containing a list of player names to fetch prices for.

- **Web Scraping:** Utilizes Selenium for web scraping to extract player prices from the Futbin website.

- **Headless Mode:** Supports headless mode for running the web browser in the background without a visible GUI.

- **User-Agent Spoofing:** Configurable option to spoof the user-agent, making the requests appear more like a regular browser.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/fifa-player-price-updater.git
   cd fifa-player-price-updater

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

2. **Download WebDriver:**
    Download the appropriate WebDriver (e.g., ChromeDriver) and place it in the project directory.

4. **Configuration**
    message me to get the .env file

## Usage

1. **Prepare CSV File:**
    Create a CSV file with a single column containing the player names you want to fetch prices for.
    there is a template in 'client' dir

2. **Run the Script:**
    ```bash
    python main.py