class Retriever:

    def __init__(self, vector_db):
        self.vector_db = vector_db

    def retrieve(self, question):

        return self.vector_db.similarity_search_with_score(
            question,
            k=10
        )