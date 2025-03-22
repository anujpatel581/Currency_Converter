# Currency_Converter
Currency converter website which can be use to convert every currency in INR and INR to every currency.
Key improvements and explanations:

Error Handling:
The code now includes robust error handling for API requests (using try...except blocks and response.raise_for_status()).
It handles potential ValueError exceptions if the user enters invalid input.
It now handles the case where the API does not support direct conversion between the two selected currencies, by converting through the base currency of INR.
It also handles the case where the API key is invalid, or the API returns an unexpected format.
Clearer Function Structure:
The code is organized into functions (get_exchange_rates, convert_currency, currency_converter), making it more modular and readable.
User Interface (HTML):
The index.html template provides a basic but functional user interface for the currency converter.
The CSS styles improve the appearance of the converter.
Currency List:
The currency select dropdowns are dynamically populated from the API response.
INR is added to the list of currencies, and the list is sorted alphabetically.
API Key Placeholder:
The API_KEY variable now has a clear placeholder, reminding you to replace it with your actual API key.
Direct and Indirect Conversion:
The code now handles cases where the API may not provide direct conversion rates between all pairs of currencies. It attempts to convert through INR as an intermediary.
Flask Structure:
The code uses Flask, which is a lightweight and easy-to-use Python web framework.
Installation:
To run this code, you'll need to install Flask and the requests library:



Bash

pip install Flask requests
API Provider:
You will need to sign up for a free or paid API key from a currency exchange rate provider. The example code uses exchangeratesapi.io, but many other providers are available.
Replace "YOUR_API_KEY" with your actual API key.
How to run:

Save the Python code as app.py and the HTML code as index.html in a templates folder within the same directory as app.py.
Replace "YOUR_API_KEY" with your API key.
Open a terminal or command prompt, navigate to the directory containing app.py, and run python app.py.
Open your web browser and go to http://127.0.0.1:5000/.
