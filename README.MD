# Finance_App

## User Stories

**User Registration and Login:**

lets goo
✅ 1. As a new investor, I want to be able to register for the finance app so that I can create an account.

✅ 2. As a registered investor, I want to be able to log in to my account securely.

✅ 3. As a registered investor, I want to be able to log out of my account to ensure security.

**Stock Trading:**

✅ 1. As an investor, I want to be able to buy stocks, specifying the stock symbol and the quantity, so that I can invest in the stock market.

✅ 2. As an investor, I want to be able to sell my stocks, specifying the stock symbol and the quantity, to liquidate my investments.

✅ 3. As an investor, I want to see real-time quotes for the current stock prices to make informed buying and selling decisions.

**Transaction History:**

✅ 1. As an investor, I want to view a history of all my buy and sell operations, including the date and transaction details, so that I can track my investment activities.

**Portfolio Overview:**

✅ 1. As an investor, I want to see a homepage that displays a summary of my current stock holdings, including the stock names, quantities, and their current market values.

**Additional Features:**

🆕 1. As an investor, I want to receive notifications or alerts when significant stock events occur, such as price changes or news related to my holdings.

⏳ 2. As an investor, I want to be able to set up preferences for email or SMS notifications about my account and stock market updates.

🆕 3. As an investor, I want access to a customer support section or chat to get assistance or resolve any issues I encounter.

🆕 4. As an investor, I want to provide feedback or suggestions for improving the app to enhance my user experience.

## Project Setup

To successfully install the project, you need to follow these steps:

1. Make sure you are in the `flask_app` directory.
2. Activate the virtual environment:
   ```
   . .venv/bin/activate
   ```
3. Install all the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Tell Flask where the entry file is:
   ```
   export FLASK_APP=finance_app/__init__.py
   ```
5. Initialize the database:
   ```
   flask --app finance_app init-db
   ```
6. Run the server:

   ```
   flask --app finance_app run --debug
   ```

## Tools

Python Flask Jinja HTML CSS SQLite Postman

## API Documentation

[API Document](API_Doc.pdf)

## Code Style Guide

**Folder Structure:**

```
📦finance_app
 ┣ 📂auth
 ┃ ┣ 📂templates
 ┃ ┃ ┣ 📜login.html
 ┃ ┃ ┗ 📜signup.html
 ┃ ┣ 📜login.py
 ┃ ┣ 📜logout.py
 ┃ ┗ 📜signup.py
 ┣ 📂home
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📜index.html
 ┃ ┗ 📜index.py
 ┣ 📂static
 ┃ ┣ 📜favicon.ico
 ┃ ┗ 📜styles.css
 ┣ 📂templates
 ┃ ┣ 📜apology.html
 ┃ ┗ 📜layout.html
 ┣ 📂transactions
 ┃ ┣ 📂templates
 ┃ ┃ ┣ 📜buy.html
 ┃ ┃ ┣ 📜history.html
 ┃ ┃ ┣ 📜quote.html
 ┃ ┃ ┣ 📜quoted.html
 ┃ ┃ ┗ 📜sell.html
 ┃ ┣ 📜buy.py
 ┃ ┣ 📜history.py
 ┃ ┣ 📜quote.py
 ┃ ┗ 📜sell.py
 ┣ 📜.env
 ┣ 📜__init__.py
 ┣ 📜config.py
 ┣ 📜db.py
 ┣ 📜schema.sql
 ┣ 📜tests.py
 ┣ 📜requirements.txt
 ┗ 📜utils.py
```

**Imports:** Import statements are grouped in the following order: standard library modules, third-party libraries, and then your own modules. Use absolute imports for clarity.

**Use Blueprint:** When developing the app, we use Flask Blueprints to organize your routes, views, and templates into separate modules. This helps in modularity and maintainability.

**Separate Configuration:** Configuration settings are separated from your application code. Store configurations in separate files or use environment variables. Flask has built-in support for configurations.

**Comments:** Add comments to your code when necessary to explain complex logic or to provide context. However, write self-documenting code where possible to minimize the need for comments.

### Naming Conventions

- **Module Names:** Module names should be in lowercase and use underscores. For example, your Flask application file can be named app.py or something relevant to your project, but it should be in lowercase.
- **Variable Names:** Variables should be in lowercase, with words separated by underscores **_(Single Underscore lower case)_**. Variables should have descriptive names that indicate their purpose.
- **Function Names:** Function names should be in lowercase, with words separated by underscores. Function names should be descriptive and indicate their purpose. For example, *create_app, configure_app, configure_session, *etc.
- **Constants:** Constants (variables that should not be modified) should be in uppercase with words separated by underscores. For example, if you define a constant for your database path, you can name it _INITIAL_CASH_.
- **Blueprint Names:** Blueprint names should be descriptive and use underscores if needed. For example, quote_blueprint, buy_blueprint, and so on.
- **Environment Variables:** When using environment variables, it's common to name them in uppercase. For example, _API_KEY_ for your api secret key string.

### Git Commit Conventions

In commit messages:

- **fix:** for fixing bugs (PATCH)
- **feat:** for adding new features (MINOR)
- **BREAKING CHANGE:** for major API changes (MAJOR)
