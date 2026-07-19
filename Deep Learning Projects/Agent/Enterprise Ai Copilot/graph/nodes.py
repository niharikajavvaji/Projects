from services.llm import LLMService
from prompts.chat import chat_prompt
from services.rag.rag import RAGService
from prompts.rag import rag_prompt
from prompts.planner import planner_prompt
from services.rag.reranker import RerankerService
from tools.calculator import calculator

llm=LLMService()
rag=RAGService()
rag.load_vector_store()
reranker=RerankerService()

def chat_node(state):
    print("\n===== Chat Node =====")
    messages = chat_prompt.invoke(
        {
            "history": [],
            "question": state["question"]
        }
    ).to_messages()

    response = llm.invoke(messages)

    state["answer"]=response.content

    return state

def retrieve_node(state):
    print("\n===== Retrieve Node =====")
    docs,scores=rag.retrieve(state["question"])
    documents = reranker.rerank(
    question=state["question"],
    documents=docs,
    top_k=3
    )
    state["documents"]=documents
    state["scores"]=scores
    return state

def answer_node(state):
    print("\n===== Answer Node =====")

    scores = state["scores"]

    best_score = min(scores)

    if best_score > 0.8:
        state["answer"] = (
            "I couldn't find relevant information in the uploaded documents."
        )
        return state


    context="\n\n".join(
        doc.page_content
        for doc in state["documents"]
    )

    sources = []

    for doc in state["documents"]:
        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "Unknown")

        sources.append(
        f"{source} (Page {page + 1})"
        )

    messages=rag_prompt.invoke(
        {
        "context":context,
        "question":state["question"]
        }
    ).to_messages()

    response=llm.invoke(messages)

    unique_sources = list(dict.fromkeys(sources))

    state["answer"] = (
        response.content
        + "\n\nSources:\n"
        + "\n".join(unique_sources)
    )

    return state

def planner_node(state):

    print("\n===== Planner Node =====")

    messages = planner_prompt.invoke(
        {
            "question": state["question"]
        }
    ).to_messages()

    response = llm.invoke(messages)

    route = response.content.strip().lower()

    print("Planner Decision:", route)

    state["route"] = route

    return state


