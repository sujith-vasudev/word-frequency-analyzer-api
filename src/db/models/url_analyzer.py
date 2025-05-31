import uuid


class UrlAnalyzer:
    def __init__(self, url: str, matches: list[dict]):
        self.analyzer_id: str = uuid.uuid4().hex
        self.url = url
        self.user_id = None
        self.matches = matches
        self.created_on = None
        self.modified_on = None

    def save_top_n_records(self, n):
        matches_count = len(self.matches)
        if matches_count < n: n = matches_count
        self.matches = self.matches[:n]
