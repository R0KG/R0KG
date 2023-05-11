import requests

# function to get the current temperature in Moscow
def get_temperature():
    api_key = 'YOUR_API_KEY_HERE'
    city = 'Moscow'
    country_code = 'ru'
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        return None

# main function to answer the question "What is the temperature right now?"
def answer_question(question):
    if "temperature" in question and "right now" in question:
        temperature = get_temperature()
        if temperature is not None:
            response = f"The current temperature in Moscow is {temperature}°C."
        else:
            response = "Sorry, I couldn't fetch the temperature information at this time."
    else:
        response = "I'm sorry, I didn't understand the question."
    return response

# example usage
print(answer_question("What is the temperature right now?"))
