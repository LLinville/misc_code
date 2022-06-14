import re, time
import urllib.request

with open("search_results/results.html", encoding="utf8") as results_file:
    results = results_file.readline()

matches = re.findall('data-id="[0-9]+', results)

ids = [int(match[9:]) for match in matches]
ids.sort()

ids=[14]
last_retrieved = 13

for page_id in ids:
    if page_id <= last_retrieved:
        continue
    print(f"Opening page {page_id}/{max(ids)}")
    with urllib.request.URLopener().open(f"http://castor.gorazd.org:8080/gorazd/show_record_id?value={page_id}&xslFile=0&fields=&_=1649978393678") as page:
        if page.code != 200:
            print(f"Page {page_id} returned status {page.code}")
            break
        with open(f"search_results/pages/{page_id}.json", 'wb') as out_file:
            out_file.write(page.file.read())
    time.sleep(10)
