import json
from html.parser import HTMLParser
import json


class Parser(HTMLParser):
    lines = [""]

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag != 'span':
            self.lines.append("")

    def handle_data(self, data):
        self.lines[-1] += data + ' '


if __name__ == "__main__":
    parser = Parser()
    filenumber = 25
    with open(f"search_results/pages/{filenumber}.json", encoding='utf8') as file:
        data = json.load(file)
    page_source = data['response']['result']['SourceD']
    page = parser.feed(page_source)
    for line in parser.lines:
        print(line)
