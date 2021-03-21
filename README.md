# AMCS
AMCS is a minimum viable project with two microservices.

The AMCS project contains two packages:
- AMCS1: A simple service for getting the price of items.
- AMCS2: A simple exchange rate service that processes information from AMCS1 and applies the exchange rate to it.


## Installation

### Prerequisites
Requires Python 3.8 or newer.

### Virtual Environment

It is strongly recommended to install using a virtual environment

1. Create a virtual environment:

`python -m venv amcs`

2. Activate the virtual environment:

a. Windows CMD:
`amcs\Scripts\activate.bat`

b. Powershell:
`amcs\Scripts\Activate.ps1`

c. Unix-like shells:
`source amcs\bin\activate`

### Install from Git repository
The project and its dependencies can be installed using pip:

`pip install git+https://github.com/yennicks/amcs`


## Usage
The virtual environment must be activated before running the project if it was used to install this software.

Both AMCS1 and AMCS2 will not spawn in the background.
Therefore multiple terminals should be used for running AMCS1 and AMCS2 concurrently.

## Running and using service AMCS1
Start AMCS1 using uvicorn on port 8000: `uvicorn amcs1.main:app --port 8000`

Do a GET request using curl: `curl http://localhost:8000/items/1`

## Running and using service AMCS2
Start AMCS2 using uvicorn on port 8080: `uvicorn amcs2.main:app --port 8080`

AMCS2 needs to access resources from AMCS1 to properly function.
Therefore AMCS1 should be running before using AMCS2.

Do a GET request using curl: `curl http://localhost:8080/exchange/1`

## Development
The source code can be cloned from git: `git clone https://github.com/yennicks/amcs`

The following commands can be used from the project root:
- `pytest`: Unit testing
- `flake8`: PEP 8 style guide validation
