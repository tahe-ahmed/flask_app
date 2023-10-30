# Finance_App

## User Stories

**User Registration and Login:**

✅ 1. As a new investor, I want to be able to register for the finance app so that I can create an account.
✅ 2. As a registered investor, I want to be able to log in to my account securely.
✅ 3. As a registered investor, I want to be able to log out of my account to ensure security.

**Stock Trading:**
✅ 1. As an investor, I want to be able to buy stocks, specifying the stock symbol and the quantity, so that I can invest in the stock market.
✅ 2. As an investor, I want to be able to sell my stocks, specifying the stock symbol and the quantity, to liquidate my investments.
✅ 3. As an investor, I want to see real-time quotes for the current stock prices to make informed buying and selling decisions.

**Transaction History:**
⏳ 1. As an investor, I want to view a history of all my buy and sell operations, including the date and transaction details, so that I can track my investment activities.

**Portfolio Overview:**
🆕 1. As an investor, I want to see a homepage that displays a summary of my current stock holdings, including the stock names, quantities, and their current market values.

**Additional Features:**
🆕 1. As an investor, I want to receive notifications or alerts when significant stock events occur, such as price changes or news related to my holdings.
🆕 2. As an investor, I want to be able to set up preferences for email or SMS notifications about my account and stock market updates.
🆕 3. As an investor, I want access to a customer support section or chat to get assistance or resolve any issues I encounter.
🆕 4. As an investor, I want to provide feedback or suggestions for improving the app to enhance my user experience.

## Thoughts and process around implementing the app

## Project Setup

## Tools

## API Documentation

```

```

> #### GET /history
>
> **Description:** This endpoint retrieves the transaction history for the logged-in user.
>
> **Authentication:** The user must be logged in (authenticated) to access this endpoint.
>
> **Parameters:** None
>
> **Response:**
>
> - **Status Code 200 (OK):** Transaction history retrieved successfully.
> - **Content-Type:** text/html
> - **Body:** The response body contains an HTML template named "history.html" displaying the transaction history.
>
> - **Status Code 401 (Unauthorized):** The user is not logged in.
> - **Body:** An error message or a login form may be displayed.
>
> #### POST /buy
>
> **Description:** This endpoint allows the user to buy shares of a stock.
>
> **Authentication:** The user must be logged in (authenticated) to access this endpoint.
>
> **Parameters:**
>
> - symbol (string): The stock symbol to buy.
> - shares (integer): The number of shares to purchase.
>
> **Response:**
>
> - **Status Code 200 (OK):** The purchase is successful, and the user's cash is updated.
> - **Content-Type:** text/html
> - **Body:** Redirects the user to the home page.
>
> - **Status Code 400 (Bad Request):** Invalid input data.
> - **Body:** An error message describing the issue (e.g., invalid symbol or share count).
>
> - **Status Code 403 (Forbidden):** Insufficient funds to make the purchase.
> - **Body:** An error message indicating that the user does not have enough cash.
>
> #### GET /quote
>
> **Description:** This endpoint allows the user to retrieve a stock quote.
>
> **Authentication:** The user must be logged in (authenticated) to access this endpoint.
>
> **Parameters:**
>
> - symbol (string): The stock symbol for which to retrieve a quote.
>
> **Response:**
>
> - **Status Code 200 (OK):** The stock quote is retrieved successfully.
> - **Content-Type:** text/html
> - **Body:** Displays the stock name, symbol, and price.
>
> - **Status Code 400 (Bad Request):** Invalid stock symbol.
> - **Body:** An error message indicating that the stock symbol is invalid.
>
> #### POST /register
>
> **Description:** This endpoint allows a new user to register.
>
> **Authentication:** None, as this endpoint is for user registration.
>
> **Parameters:**
>
> - username (string): The chosen username for registration.
> - password (string): The chosen password for registration.
> - confirmation (string): Password confirmation.
>
> **Response:**
>
> - **Status Code 200 (OK):** User registration is successful.
> - **Content-Type:** text/html
> - **Body:** Redirects the user to the home page after successful registration.
>
> - **Status Code 400 (Bad Request):** Invalid input data or username already in use.
> - **Body:** An error message indicating the issue (e.g., empty fields, non-matching passwords, or username in use).
>
> #### POST /sell
>
> **Description:** This endpoint allows the user to sell shares of a stock.
>
> **Authentication:** The user must be logged in (authenticated) to access this endpoint.
>
> **Parameters:**
>
> - symbol (string): The stock symbol to sell.
> - shares (integer): The number of shares to sell.
>
> **Response:**
>
> - **Status Code 200 (OK):** The sale is successful, and the user's cash is updated.
> - **Content-Type:** text/html
> - **Body:** Redirects the user to the home page.
>
> - **Status Code 400 (Bad Request):** Invalid input data or insufficient shares to sell.
> - **Body:** An error message indicating the issue (e.g., invalid symbol, share count, or insufficient shares).
>
> #### GET /login
>
> **Description:** This endpoint allows a user to log in.
>
> **Authentication:** None, as this endpoint is for user login.
>
> **Parameters:**
>
> - username (string): The username.
> - password (string): The password.
>
> **Response:**
>
> - **Status Code 200 (OK):** User login is successful.
> - **Content-Type:** text/html
> - **Body:** Redirects the user to the home page after successful login.
>
> - **Status Code 403 (Forbidden):** Invalid login credentials.
> - **Body:** An error message indicating that the username or password is incorrect.
>
> ### GET /logout
>
> **Description:** This endpoint allows a user to log out.
>
> **Authentication:** The user must be logged in (authenticated) to access this endpoint.
>
> **Parameters:** None
>
> **Response:**
>
> - **Status Code 200 (OK):** User logout is successful.
>   - **Content-Type:** text/html
>   - **Body:** Redirects the user to the login form.

## Code Style Guide

**Organize Your Project:** Structure your project in a clear and organized manner.

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
 ┃ ┃ ┗ 📜index.html
 ┃ ┗ 📜index.py
 ┣ 📂quote
 ┃ ┣ 📂templates
 ┃ ┃ ┣ 📜quote.html
 ┃ ┃ ┗ 📜quoted.html
 ┃ ┗ 📜quote.py
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
 ┃ ┃ ┗ 📜sell.html
 ┃ ┣ 📜buy.py
 ┃ ┣ 📜history.py
 ┃ ┗ 📜sell.py
 ┣ 📜.env
 ┣ 📜__init__.py
 ┣ 📜config.py
 ┣ 📜db.py
 ┣ 📜schema.sql
 ┗ 📜utils.py
```

**Imports:** Import statements should be grouped in the following order: standard library modules, third-party libraries, and then your own modules. Use absolute imports for clarity.

**Use Blueprint:** When developing the app, we use Flask Blueprints to organize your routes, views, and templates into separate modules. This helps in modularity and maintainability.

**Separate Configuration:** Keep your configuration settings separate from your application code. Store configurations in separate files or use environment variables. Flask has built-in support for configurations.

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
