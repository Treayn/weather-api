# Intro

Basic proof-of-concept app to pull & cache weather data.

### To-Do

- write client code
- testing
- installation documentation

# Requirements

- The server will be a multithreaded program.
- One thread will download data from openweathermap's REST API, parse the json strings, and store the results on a MongoDB database.
- Another thread will listen for incoming client connections and responds to client queries. the server accept multiple client queries.
- The client program connects to the server and requests parameters such as (get_cities, get_temperature, get_current_temp)