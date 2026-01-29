# 📘 Day 11

## Web Scraping

## Table of Contents

1. [What is Web Scrapping](#what-is-web-scraping)
2. [Installation](#installation)
3. [Basic Concepts](#basic-concepts)
4. [Intermediate Techniques](#intermediate-techniques)
5. [Legal and Ethical Considerations](#legal-and-ethical-considerations)
6. [Additional Resources](#additional-resources)

---

## What is Web Scraping?

Web scraping is the automated process of extracting data from websites. It involves fetching web pages and parsing their HTML/XML content to retrieve specific information.

**Use cases:**

- Data collection and analysis
- Price monitoring
- News aggregation
- Research and academic projects
- Automated testing
- Content migration

## Installation

### With UV (recommended)

```bash
# Create project
uv init web-scraper
cd web-scraper

# Add required packages
uv add requests beautifulsoup4 lxml

# Optional: Add selenium for JavaScript-heavy sites
uv add selenium

# Optional: Add scrapy for large-scale projects
uv add scrapy
```

### Recommended Project Structure

```
web-scraper/
├── .venv/
├── pyproject.toml
├── src/
│   ├── main.py
│   ├── scrapers/
│   │   ├── news_scraper.py
│   │   └── product_scraper.py
│   ├── parsers/
│   │   └── html_parser.py
│   └── data/
│       ├── output.json
│       └── output.csv
├── logs/
└── README.md
```

## Basic Concepts

### 1. Making HTTP Requests

#### Using requests library

```python
import requests

# Simple GET request
response = requests.get('https://example.com')

# Check if request was successful
if response.status_code == 200:
    html_content = response.text
    print("Success!")
else:
    print(f"Error: {response.status_code}")

# With headers (to mimic browser)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get('https://example.com', headers=headers)

# With timeout
response = requests.get('https://example.com', timeout=10)

# POST request
data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://example.com/login', data=data)
```

### 2. Parsing HTML with BeautifulSoup

```python
from bs4 import BeautifulSoup
import requests

# Fetch and parse
url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

# Find elements by tag
title = soup.find('title')
print(title.text)

# Find all elements
all_links = soup.find_all('a')
for link in all_links:
    print(link.get('href'))

# Find by class
articles = soup.find_all('div', class_='article')

# Find by id
header = soup.find(id='main-header')

# CSS selectors
products = soup.select('.product-item')
first_product = soup.select_one('.product-item')

# Navigate the tree
parent = element.parent
children = element.children
siblings = element.next_sibling
```

### 3. Extracting Data

```python
from bs4 import BeautifulSoup
import requests

url = 'https://example.com/products'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

# Extract product information
products = []

for item in soup.find_all('div', class_='product'):
    product = {
        'name': item.find('h2', class_='title').text.strip(),
        'price': item.find('span', class_='price').text.strip(),
        'rating': item.find('div', class_='rating')['data-rating'],
        'url': item.find('a')['href']
    }
    products.append(product)

print(products)
```

## Intermediate Techniques

### 1. Session Management

```python
import requests

# Maintain cookies and session data
session = requests.Session()

# Login
login_data = {'username': 'user', 'password': 'pass'}
session.post('https://example.com/login', data=login_data)

# Subsequent requests use the same session
response = session.get('https://example.com/dashboard')

# Close session
session.close()
```

### 2. Handling Pagination

```python
import requests
from bs4 import BeautifulSoup

base_url = 'https://example.com/products?page='
all_products = []

for page in range(1, 11):  # Pages 1-10
    url = f'{base_url}{page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    products = soup.find_all('div', class_='product')
    all_products.extend(products)

    print(f'Scraped page {page}')

print(f'Total products: {len(all_products)}')
```

### 3. Rate Limiting and Delays

```python
import requests
import time
from bs4 import BeautifulSoup

urls = ['url1', 'url2', 'url3']

for url in urls:
    response = requests.get(url)
    # Process response

    # Wait between requests (be respectful!)
    time.sleep(2)  # 2 seconds delay
```

### 4. Error Handling

```python
import requests
from bs4 import BeautifulSoup
import time


def scrape_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise error for bad status
            return BeautifulSoup(response.content, 'lxml')

        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt + 1}")
            if attempt < max_retries - 1:
                time.sleep(5)

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)

    return None


# Usage
soup = scrape_with_retry('https://example.com')
if soup:
    # Process data
    pass
```

## Legal and Ethical Considerations

### Things to Remember:

1. **Check Terms of Service**: Always read the website's ToS
2. **Respect robots.txt**: Follow crawling rules
3. **Rate Limiting**: Don't overload servers
4. **Personal Data**: Be careful with PII (Personally Identifiable Information)
5. **Copyright**: Respect intellectual property
6. **Attribution**: Give credit where due
7. **API First**: Use official APIs when available

### When NOT to Scrape:

- ❌ Sites explicitly prohibiting scraping in ToS
- ❌ Password-protected content you're not authorized to access
- ❌ Sites with available APIs (use the API instead)
- ❌ Content behind paywalls
- ❌ Personal/private data

## Additional Resources

### Official Documentation
- [Requests](https://requests.readthedocs.io/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Scrapy](https://docs.scrapy.org/)
- [Selenium](https://selenium-python.readthedocs.io/)

### Tools and Libraries
- `requests-html` - Requests with JavaScript support
- `playwright` - Modern alternative to Selenium
- `httpx` - Async HTTP client
- `parsel` - HTML/XML parsing

### Practice Sites
- [Quotes to Scrape](http://quotes.toscrape.com/) - Practice scraping
- [Books to Scrape](http://books.toscrape.com/) - E-commerce practice
- [Scrapy Tutorial Sites](https://docs.scrapy.org/en/latest/intro/tutorial.html)


[<< Day 10](../day_10/day_10.md) | [Day 12 >>](../day_12/day_12.md)