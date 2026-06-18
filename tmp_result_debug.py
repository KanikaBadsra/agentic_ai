from app.graphs.main_graph import graph
result = graph.invoke({'question':'why europe sales are down', 'session_id':'demo'})
print(type(result))
print(result)
print('keys', list(result.keys()))
