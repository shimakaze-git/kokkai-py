import json

from urllib.parse import quote
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

from typing import Dict, Any


class KokkaiBase:

    HOST = 'http://kokkai.ndl.go.jp/api/1.0/'
    ACCEPT = 'application/json'

    PARAMS = {
        # 'maximumRecords': 1,
        'recordPacking': 'json'
    }

    def query(self, params=Dict) -> str:

        params = {**params, **self.PARAMS}
        query = '&'.join(
            ['{}={}'.format(key, value) for key, value in params.items()]
        )
        query = "?" + query

        return quote(query)

    def request(self, path=str) -> Any:
        if len(path.split('/')) > 1:
            path = path.replace("/", "")

        url = self.HOST + path
        try:
            req = Request(url)
            with urlopen(req) as res:
                res = res.read().decode('utf8')
                # res = res.read()
        except HTTPError as e:
            print('HTTPError: {}'.format(e.reason))
        except URLError as e:
            print('URLError: {}'.format(e.reason))
        else:
            return res

    def convert_to_dict(self, json_text: str) -> Dict:
        results = json.loads(json_text)
        return results
