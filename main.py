from fastapi import FastAPI

from scraper import Scraper

# Create a new instance
app = FastAPI()
quotes = Scraper()


@app.get('/{tag}')
async def search_item(tag):
    return quotes.scrape_data(tag)
