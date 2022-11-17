import streamlit as st
import graphviz as graphviz

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

st.write("Hi Dirk on Page1 😎")
x="hhhhh"
st.markdown(f"""
Streamlit is **_really_ cool**.  
`print(f)`  
# Header {x} 
## Subheader  
lorem ipsum asdfklöjasdfölkjöasjdfsadf asdfasdf
asdf   

--- 

````
some code
more codee   
    an more
```
""")


# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)