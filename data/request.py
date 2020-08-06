import requests
from bs4 import BeautifulSoup
import json


class SonarRequest:
    def __init__(self, sonar_url, key):
        self.key = key
        self.specific = sonar_url + "/api/issues/search?componentKey=" + key
        self.generic = sonar_url + "/api/measures/component?metricKeys="

    def setGenerelMetrics(self, metrics):
        self.generic += str(metrics).strip("[]").replace("\'", "")
        self.generic += "&componentKey=" + self.key

    def makeRequest(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        return json.loads(str(soup))["component"]