import re
from urllib.parse import urlparse, urljoin, urlencode

import requests
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

sources = {
    "News by NATO countries": {
        "bbc": ("BBC (Great Britain)", "https://www.bbc.com/"),
        "foxnews": ("Fox News (America)", "https://www.foxnews.com/"),
        "aljazeera": ("Aljazeera", "https://www.aljazeera.com/"),
        "reuters": ("Reuters", "https://www.reuters.com/")
    },
    "News by Russia": {
        "sputnik": ("Sputnik", "https://sputniknews.com/"),
        "tass": ("TASS", "https://tass.com/")
    }
}


@app.route('/')
def entrypoint():
    source = request.args.get('source')
    url_to_resolve = request.args.get('url')
    if source and any(source in sources[item] for item in sources):
        url = None
        for item in sources:
            if source in sources[item]:
                name, url = sources[item][source]
        domain = urlparse(url).netloc.replace('www.', '')

        if url_to_resolve is not None and urlparse(url_to_resolve).netloc.endswith(domain):
            response = requests.get(url_to_resolve)
        else:
            response = requests.get(url)

        content = response.content.decode('utf-8')

        content = re.sub(r' src="([^"]+)"', lambda m: ' src="' + urljoin(url, m.group(1)) + '"', content)
        content = re.sub(r' href="([^"]+)"', lambda m: ' href="' + urljoin(url, m.group(1)) + '"', content)

        # Replace all URLs by local URLs
        links = re.findall(r'http[s]?://[^/]*' + domain + '/[^"\' ]*', content)
        link_mapping = {
            link: f"/?source={source}&" + urlencode({"url": url})
            for link in sorted(links, key=lambda item: len(item))
        }
        for link, link_resolver in link_mapping.items():
            content = content.replace(link, link_resolver)
        return render_template('source.html', data=content)
    else:
        return render_template('overview.html', sources=sources)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)