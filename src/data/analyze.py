from db.models.url_analyzer import UrlAnalyzer


class UrlAnalyzerData:

    def __init__(self, session):
        self.session = session

    @staticmethod
    def persist_analyzed_result(url, matches: list[dict]):
        analyzed_result = UrlAnalyzer(matches=matches, url=url)
        analyzed_result.save_top_n_records(n=5)
        return analyzed_result
