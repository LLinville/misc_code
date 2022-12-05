import re, time
import urllib.request
for page_id in range(40000):
    print(f"Opening page {page_id}/40000")
    with urllib.request.URLopener().open(f"http://castor.gorazd.org:8080/gorazd/show_record_id?value={page_id}&xslFile=0&fields=&_=1649978393678") as page:
        with open(f"search_results/pages/{page_id}.json", 'wb') as out_file:
            out_file.write(page.file.read())
    time.sleep(3)
