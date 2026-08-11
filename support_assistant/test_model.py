from models import AskRequest, AnswerResponse

request = AskRequest(
    query="What is the delivery time?"
)

print("REQUEST")
print(request)
print("Query:", request.query)


response = AnswerResponse(
    answer="Based on the retrieved context: Zepto delivers grocery and household essentials.",
    sources=["doc_01"],
    confidence=1.0
)

print()
print("RESPONSE")
print(response)
print()
print("Answer:", response.answer)
print("Sources:", response.sources)
print("Confidence:", response.confidence)
print()
print("JSON RESPONSE")
print(response.model_dump_json())