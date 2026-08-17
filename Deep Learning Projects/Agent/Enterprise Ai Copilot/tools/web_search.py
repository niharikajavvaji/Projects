from langchain_community.tools import DuckDuckGoSearchResults

search=DuckDuckGoSearchResults()

def web_search(query:str):
    return search.run(query)