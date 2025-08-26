# News Aggregator

A Python-based news aggregation system that collects, parses, and stores news articles from multiple sources using a clean, extensible object-oriented architecture.

## 🚀 Features

- **Multi-source Support** - Currently supports NewsAPI.org with easy extensibility for other sources
- **Clean Architecture** - Interface-based design with Abstract Factory pattern
- **Database Storage** - MySQL integration for persistent article storage
- **Configurable** - External configuration files for easy customization
- **Extensible** - Easy to add new news sources, parsers, and storage backends
- **Error Resilient** - Built-in error handling and logging

## 📋 Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Environment Variables](#environment-variables)
- [Database Schema](#database-schema)
- [Usage](#usage)
- [API Key Requirements](#api-key-requirements)
- [Architecture](#architecture)
- [Adding New Sources](#adding-new-sources)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## 🛠 Installation

### Prerequisites

- Python 3.8+
- MySQL 5.7+ or MariaDB 10.2+
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/shchukova/news-aggregator.git
cd news-aggregator
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create Requirements File (if not exists)

Create a `requirements.txt` file with the following dependencies:

```txt
requests>=2.28.0
mysql-connector-python>=8.0.33
python-dotenv>=1.0.0
configparser>=5.3.0
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root directory:

```env
# Database Configuration
MYSQL_USER=your_mysql_username
MYSQL_PASS=your_mysql_password
MYSQL_HOST=localhost

# API Keys
NEWSAPI_KEY=your_newsapi_org_api_key
```

### News Source Configuration

Edit `config/newsorg_config.ini`:

```ini
[DEFAULT]
url = https://newsapi.org/v2/top-headlines
url_params_list = ['apiKey', 'country','from', 'to', 'pageSize']
url_params_value_country = us
request_per_day_limit = 1000
```

## 🗄️ Database Schema

### Automatic Setup

The application will automatically create the required database and tables on first run.

### Manual Setup (Optional)

If you prefer to set up the database manually:

```sql
CREATE DATABASE news;
USE news;

CREATE TABLE news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    url TEXT NOT NULL,
    published_at DATETIME,
    author VARCHAR(255),
    url_to_image TEXT,
    source_id_external VARCHAR(100),
    source_name_external VARCHAR(255),
    content TEXT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_url (url(255))
);
```

## 📚 API Key Requirements

### NewsAPI.org

1. **Sign up** at [https://newsapi.org/](https://newsapi.org/)
2. **Get your API key** from the dashboard
3. **Add it to your `.env` file**:
   ```env
   NEWSAPI_KEY=your_actual_api_key_here
   ```

### Rate Limits

- **Free Plan**: 1,000 requests per day
- **Developer Plan**: Up to 50,000 requests per day
- **Business Plan**: Up to 200,000 requests per day

## 🎯 Usage

### Basic Usage

```bash
python main.py
```

### Programmatic Usage

```python
from NewsAggregator.Config.NewsOrgConfig import NewsOrgConfig
from NewsAggregator.Scrapper.NewsOrgApiScrapper import NewsOrgApiScrapper
from NewsAggregator.Parser.NewsOrgParser import NewsOrgParser
from NewsAggregator.Storage.Db.MySqlDbStorage import MySqlDbStorage
from NewsAggregator.NewsAggregator import NewsAggregator
from NewsAggregator.Loader.NewsLoader import NewsLoader

# Load configuration
config = NewsOrgConfig('./config/newsorg_config.ini')

# Initialize components
storage = MySqlDbStorage('user', 'password', 'localhost')
scrapper = NewsOrgApiScrapper(config)
parser = NewsOrgParser()

# Create news loader and aggregator
news_loader = NewsLoader(scrapper, parser)
news_aggregator = NewsAggregator(storage)
news_aggregator.add(news_loader)

# Run the aggregation
news_aggregator.run()
```

### Example Output

```bash
$ python main.py
2024-08-26 10:30:15 - INFO - Starting news aggregation...
2024-08-26 10:30:16 - INFO - Fetching from NewsAPI.org...
2024-08-26 10:30:18 - INFO - Parsed 20 articles successfully
2024-08-26 10:30:19 - INFO - Saved 20 new articles to database
2024-08-26 10:30:19 - INFO - Aggregation completed successfully
```

## 🏗️ Architecture

### Design Patterns Used

- **Abstract Factory Pattern**: `AbstractNewsLoaderFactory` for creating components
- **Strategy Pattern**: Interchangeable parsers and scrapers
- **Singleton Pattern**: Database connection management
- **Interface Segregation**: Separate interfaces for different concerns

### Core Components

```
NewsAggregator/
├── Config/              # Configuration management
├── Scrapper/           # Data fetching from external sources
├── Parser/             # Data parsing and transformation
├── Storage/            # Data persistence layer
├── Loader/             # Coordination between scrapper and parser
└── Internal/Data/      # Data models and collections
```

### Component Relationships

```
NewsAggregator
├── Uses multiple NewsLoader instances
│
NewsLoader
├── Contains IScrapper (fetches data)
├── Contains IParser (parses data)
└── Returns NewsCollection
│
NewsCollection
├── Contains multiple NewsItem objects
└── Provides iteration interface
```

## 🔧 Adding New Sources

### 1. Create New Scrapper

```python
# NewsAggregator/Scrapper/CustomNewsScrapper.py
from NewsAggregator.IScrapper import IScrapper
from NewsAggregator.Internal.Data.Item.PageContent import PageContent

class CustomNewsScrapper(IScrapper):
    def get_data(self, url: str) -> PageContent:
        # Implement your scraping logic
        pass
    
    def get_requested_url(self) -> str:
        # Return the URL to scrape
        pass
```

### 2. Create New Parser

```python
# NewsAggregator/Parser/CustomNewsParser.py
from NewsAggregator.IParser import IParser
from NewsAggregator.Internal.Data.Collection.NewsCollection import NewsCollection

class CustomNewsParser(IParser):
    def parse(self, page: PageContent) -> NewsCollection:
        # Implement your parsing logic
        pass
```

### 3. Create Configuration

```python
# NewsAggregator/Config/CustomNewsConfig.py
from NewsAggregator.IConfig import IConfig

class CustomNewsConfig(IConfig):
    def get_url(self) -> str:
        # Return base URL
        pass
    
    def get_params(self) -> str:
        # Return parameters
        pass
    
    def get_request_per_day_limit(self) -> str:
        # Return rate limit
        pass
```

### 4. Register New Source

```python
# In main.py or your application
custom_config = CustomNewsConfig('config/custom_config.ini')
custom_scrapper = CustomNewsScrapper(custom_config)
custom_parser = CustomNewsParser()
custom_loader = NewsLoader(custom_scrapper, custom_parser)

news_aggregator.add(custom_loader)
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test module
python -m pytest tests/unitests/NewsAggregatorTest/ConfigTest/

# Run with coverage
python -m pytest --cov=NewsAggregator tests/
```

### Test Structure

```
tests/
├── unitests/
│   └── NewsAggregatorTest/
│       ├── ConfigTest/
│       ├── ParserTest/
│       ├── ScrapperTest/
│       └── StorageTest/
└── integration/
    └── test_full_pipeline.py
```

### Writing Tests

Example test for a new component:

```python
import unittest
from NewsAggregator.YourComponent import YourComponent

class TestYourComponent(unittest.TestCase):
    def setUp(self):
        self.component = YourComponent()
    
    def test_functionality(self):
        result = self.component.some_method()
        self.assertEqual(result, expected_value)
```

## 🔍 Troubleshooting

### Common Issues

**1. MySQL Connection Error**
```bash
Error: Access denied for user 'username'@'localhost'
```
- Verify MySQL credentials in `.env` file
- Ensure MySQL service is running
- Check user permissions

**2. API Key Error**
```bash
Error: 401 Unauthorized
```
- Verify API key in `.env` file
- Check API key validity on provider's website
- Ensure you haven't exceeded rate limits

**3. Module Import Error**
```bash
ModuleNotFoundError: No module named 'NewsAggregator'
```
- Ensure you're in the project root directory
- Activate your virtual environment
- Check PYTHONPATH if needed

### Logging

Enable debug logging by adding to your main.py:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Performance Optimization

### Recommended Settings

- **Database**: Use connection pooling for high-volume operations
- **API Calls**: Implement caching to reduce redundant requests
- **Processing**: Use batch inserts for database operations
- **Memory**: Process articles in batches for large datasets

### Monitoring

Monitor these metrics:
- API rate limit usage
- Database connection count
- Memory consumption
- Processing time per article

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Make your changes**
4. **Add tests** for new functionality
5. **Run the test suite**: `python -m pytest`
6. **Commit your changes**: `git commit -am 'Add new feature'`
7. **Push to the branch**: `git push origin feature/new-feature`
8. **Submit a Pull Request**

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to all public methods
- Include type hints where appropriate
- Write unit tests for new functionality

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
