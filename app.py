from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import logging
import requests

app = Flask(__name__)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

REQUEST_COUNT = Counter(
    "website_requests_total",
    "Total requests to the website"
)

SPLUNK_TOKEN = "b6ceacdc-5acb-4749-a4ad-b455745d1b70"
SPLUNK_URL = "https://prd-p-duutw.splunkcloud.com:8088/services/collector"

def send_to_splunk(message):
    headers = {
        "Authorization": f"Splunk {SPLUNK_TOKEN}"
    }

    payload = {
        "event": message,
        "source": "food-app",
        "sourcetype": "flask",
        "index": "main"
    }

    try:
        response = requests.post(
            SPLUNK_URL,
            headers=headers,
            json=payload,
            verify=False,
            timeout=5
        )
        print("Splunk Response:", response.status_code, response.text)
    except Exception as e:
        print("Splunk Error:", e)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    logging.info("Home page accessed")
    send_to_splunk("Home page accessed")
    return "<h1>My new mobile App Website is Working</h1>"

@app.route("/order")
def order():
    REQUEST_COUNT.inc()
    logging.info("Order page accessed")
    send_to_splunk("Order page accessed")
    return "<h1>Order page opened</h1>"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)