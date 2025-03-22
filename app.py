from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Free Currency Converter API (using exchangerate-api.com)
API_KEY = "YOUR_API_KEY"  # Replace with your API key from exchangerate-api.com
BASE_URL = "https://api.exchangerate-api.com/v4/latest/"

def get_exchange_rates(base_currency="INR"):
    """Fetches exchange rates from exchangerate-api.com."""
    try:
        response = requests.get(BASE_URL + base_currency)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data.get("rates", {})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return {}
    except KeyError:
        print("Invalid API response format.")
        return {}

def convert_currency(amount, from_currency, to_currency):
    """Converts currency."""
    rates = get_exchange_rates(from_currency)
    if not rates:
        return None  # Indicate error

    if to_currency in rates:
        return amount * rates[to_currency]
    else:
        #If the API does not support direct conversion, we convert via the base currency.
        rates_inr = get_exchange_rates("INR")
        if not rates_inr:
            return None

        if to_currency in rates_inr and from_currency in rates_inr:
            inr_amount = amount / rates_inr[from_currency]
            final_amount = inr_amount * rates_inr[to_currency]
            return final_amount

        return None #If neither direct nor indirect conversion is possible

@app.route("/", methods=["GET", "POST"])
def currency_converter():
    """Renders the currency converter page and handles conversions."""
    currencies = list(get_exchange_rates("INR").keys())
    currencies.append("INR") #Add INR to the list of currencies.
    currencies.sort() #Sort the currencies list alphabetically.
    result = None

    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            from_currency = request.form["from_currency"]
            to_currency = request.form["to_currency"]
            result = convert_currency(amount, from_currency, to_currency)
        except ValueError:
            result = "Invalid input. Please enter a valid number."
        except Exception as e:
            result = f"An error occurred: {e}"

    return render_template("index.html", currencies=currencies, result=result)

if __name__ == "__main__":
    app.run(debug=True)
    
