from requests_html import HTMLSession


class Scraper():

    def scrape_data(self, tag):
        url = f'http://quotes.toscrape.com/tag/{tag}'
        s = HTMLSession()
        r = s.get(url)

        print(r.status_code)

        qlist = []
        quotes = r.html.find('div.quote')

        for q in quotes:

            print(q, q.find('span.text', first=True).text.strip())
            item = {
                # 'text': q.find('span.text', first=True).text.strip(),
                # 'Author': q.find('small.author', first=True).text.strip(),
                "tags": q.find('div.tags', first=True).text.strip()
            }
            # print(item)
            qlist.append(item)

            return qlist


quotes = Scraper()
