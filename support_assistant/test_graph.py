from graph import app_graph

result = app_graph.invoke(
    {
        "query":
        "Who is Virat Kohli?"
    }
)

print(result)

