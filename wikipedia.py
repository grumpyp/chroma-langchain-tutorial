import requests
import pypandoc
import datetime
import re

_ALGORITHMS = ["Isolation Forest", "Random Forest", "K Nearest Neighbour", "One class SVM", "Linear Regression",
               "Logistic Regression", "Support Vector Machine", "K Means Clustering", "Hierarchical Clustering",
                "Simpsonsons", "Python", "JavaScript"]

class Wikipedia:
    def __init__(self):
        self.wikipedia = {}

    def pull_content(self, topic: str):
        url = f"https://en.wikipedia.org/w/api.php?action=parse&page={topic}&format=json"
        response = requests.get(url)
        data = response.json()
        if data.get("error", None) is None:
            html_content = data["parse"]["text"]["*"]
            redirect_link_pattern = r'<div class=\"redirectMsg\">.*?<a href=\"([^"]*)\" title=\"([^"]*)\">'
            match = re.search(redirect_link_pattern, html_content, re.DOTALL)
            if match:
                redirected_topic = match.group(2)
                url = f"https://en.wikipedia.org/w/api.php?action=parse&page={redirected_topic}&format=json"
                response = requests.get(url)
                data = response.json()
            self.wikipedia[topic] = data["parse"]["text"]["*"]
        else:
            if self.wikipedia.get("error", None) is None:
                self.wikipedia["error"] = []
            self.wikipedia["error"].append(topic)
        return self

    @property
    def errors(self):
        return self.wikipedia["errors"]

    @property
    def topics(self):
        return self.wikipedia.keys()

    @property
    def topics(self):
        return [self.wikipedia[topic] for topic in self.wikipedia.keys() if topic != "errors"]

    def get_content(self, topic: str):
        return self.wikipedia[topic]

    def merge_content_to_plaintext(self):
        content = ""
        for i in self.wikipedia.values():
            # don't include error list
            if isinstance(i, list):
                continue
            content += Wikipedia.html_to_plaintext(i.replace('\n', '')).replace('\n', '')
        return content

    @staticmethod
    def html_to_plaintext(html: str):
        return pypandoc.convert_text(html, "plain", format="html")

    @staticmethod
    def to_txt(text: str, path: str = str(datetime.datetime.now())):
        with open(f"{path}.txt", "w") as f:
            f.write(text)
            f.close()
        return f"saved to {path}"

if __name__ == "__main__":
    wiki = Wikipedia()
    for algorithm in _ALGORITHMS:
        wiki.pull_content(algorithm)
    # print(wiki.topics)
    # print(wiki.html_to_plaintext(wiki.get_content("Isolation Forest")))
    # print(wiki.to_txt(wiki.html_to_plaintext(wiki.get_content("Isolation Forest"))))
    print(wiki.merge_content_to_plaintext())
    print(wiki.to_txt(wiki.merge_content_to_plaintext()))
