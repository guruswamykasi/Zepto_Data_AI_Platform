from pathlib import Path



DOCS_PATH = Path(__file__).parent / "docs"


def load_documents():

    documents = []

    for file_path in sorted(DOCS_PATH.glob("*.txt")):

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()

        document = {
            "id": file_path.stem,
            "content": content
        }

        documents.append(document)

    return documents


if __name__ == "__main__":

    documents = load_documents()

    print("Documents folder:", DOCS_PATH)
    print("Number of documents:", len(documents))

    for document in documents:

        print("\n--------------------")
        print("ID:", document["id"])
        print("Content:", document["content"][:100])

