# Setup Instructions

Follow these steps to get the URL shortening service running:

## Requirements

- Python 3.8 or newer
- MongoDB Atlas account

## Step 1: Clone the repository

Clone the project repository to your local machine:

```
git clone https://github.com/username/url_shortner.git
```

Change to the project directory:

```
cd url_shortner
```

## Step 2: Create a virtual environment and install dependencies

We recommend using a virtual environment to avoid conflicts with other Python projects. Here's how you can create a new virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Next, install the project's dependencies using pip:

```bash
pip install -r requirements.txt
```

## Step 3: Set up MongoDB Atlas

Create a MongoDB Atlas account if you don't already have one. Then, create a new database and get the connection string.

Replace the `DB_PASSWORD` in the `config.py` file with the password for your MongoDB Atlas account.
`config.py` should be created in the base folder

## Step 4: Run the application

You can now run the application using the command:

```bash
python main.py
```

The FastAPI server will start and listen on `http://localhost:8000`. You can interact with the application via this URL. For instance, you can open it in a web browser, or use `curl` or Postman to make HTTP requests.

## Step 5: API Documentation

FastAPI automatically generates API documentation. You can view the documentation by navigating to `http://localhost:8000/docs` in your web browser. 

The documentation provides a detailed description of each endpoint, including the required input format and the output format. You can also test the endpoints directly from the documentation page.

