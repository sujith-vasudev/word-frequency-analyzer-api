import re
from collections import Counter

import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException

from data.analyze import UrlAnalyzerData

STOP_WORDS = set([
    "a", "an", "the", "and", "or", "but", "if", "while", "to", "of", "in", "on", "for", "with", "at", "by"
])


def get_url_response(url):
    try:
        response = requests.get(url, timeout=5)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch data from url: {url}")
    return response.text


def get_texts(text):
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text(separator=" ")
    return text


def extract_top_words(text: str, top_n: int = 10):
    words = re.findall(r'\b\w+\b', text.lower())
    filtered = [word for word in words if word not in STOP_WORDS]
    counter = Counter(filtered)
    top_words = counter.most_common(top_n)
    return [{"word": word, "count": count} for word, count in top_words]


def analyze_url(session, url: str, current_user):
    response_text: str = get_url_response(url=url)
    normalized_text: str = get_texts(response_text)
    top_words: list[dict] = extract_top_words(text=normalized_text)

    analyzed_obj = UrlAnalyzerData(session=session).persist_analyzed_result(url=url, matches=top_words)
    current_user.analysis_result.append(analyzed_obj)
    return analyzed_obj.matches
