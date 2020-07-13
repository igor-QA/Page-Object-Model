# Page-Object-Model
Before running a project in Chrome, check that the version of ChromeDriver matches the version of your Chrome browser

Run:

all tests:

pytest .

tests for review:

pytest -v --tb=line --language=en -m need_review test_product_page.py
