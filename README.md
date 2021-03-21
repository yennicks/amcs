# AMCS
AMCS is a minimum viable project with two microservices.

The AMCS project contains two packages:
- AMCS1: A simple service for getting the price of items.
- AMCS2: A simple exchange rate service that processes information from AMCS1 and applies the exchange rate to it.


## Installation


## Usage

## Running and using service AMCS1:
Start AMCS1 using uvicorn: `uvicorn amcs1.main:app --port 8000`.

Do a GET request using curl: `curl http://localhost:8000/items/1`

##Running service AMCS2:
Start AMCS1 using uvicorn: `uvicorn amcs2.main:app --port 8080`

Do a GET request using curl: `curl http://localhost:8080/exchange/1`

## Testing
Perform unit testing using the `pytest` command and PEP 8 style guide validation using `flake8`.
