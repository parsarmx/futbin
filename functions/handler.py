from urllib.parse import urlencode, urljoin


class RequestHandler:
    def __init__(self, base_url: str, queries: dict):
        self.base_url = base_url
        self.queries = queries

    def get_player_static_url(self):
        path = self.base_url
        encoded_paramas = urlencode(self.queries)
        full_path = f"{path}?{encoded_paramas}"

        return full_path
