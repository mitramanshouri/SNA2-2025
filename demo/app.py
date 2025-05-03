import streamlit as st
st.title("SNA2 Final Website")
st.write("By Sam, Clémentine, and Mitra")
st.header("Our Dataset")
st.write("""The dataset we used compiles historical Grammy Award winners and nominees, including details such as the award category, artist, song or album, and year of recognition.
The data was sourced from grammy.com and can be used for music trend analysis, industry research, and historical insights""")
st.header("Network Topic")
st.write ("We created an award category co-nomination network")
st.write ("Our nodes were grammy award categories")
st.write ("Edges are used to represent when a connection exists between 2 categories if the same artist/song/album was nominated in both")
st.write ("Our network highlights categories that often recognize the same works (e.g., “Album of the Year” and “Best Pop Vocal Album”).")
st.header ("Purpose of our Project")
st.write ("Our project allows us to uncover patterns and overlaps in how the Grammys recognize musical works.")
st.write ("Some award categories may appear different but often acknowledge the same entries which can indicate genre blending, prestige stacking, and how the Recording Academy tends to group styles or types of music.")
st.header ("Our Process in Google CoLab")
st.write ("We began by filtering our dataset by creating two subsequent CSV files: edges and nodes")
st.write ("We then created our data frame, and loaded our edges and nodes CSV files.")
st.write ("Through this, we found the strongest co-nomination links which allowed us to create a co-nomination network with weighted edges")
st.write ("Then, we counted nodes and edges and created our graph using Sigma(G)")
st.write ("This allowed us to then create a scatterplot, and histogram")
st.header ("Network Statistics")
st.write ("We had a total of 773 nodes, so categories.")
st.write ("We found a total of 10256 total co-nomination links (edges).")
st.write ("Our graph's density=0.0344")
st.markdown("<span style='color:red;'>The most connected categories were: Album of the Year, Record of the Year, and Song of the Year </span>", unsafe_allow_html=True)
st.header ("Histogram")
from pathlib import Path
img_path = Path(__file__).parent / "histogram.png"
st.image(str(img_path), caption="Histogram")
st.write ("First, we calculate the degree for every node in our graph G, where each node is a Grammy category. We use the weight of edges, which tells us how often two categories shared the same artist, song, or album. ")

st.write ("We found that major awards (like Album of the Year) act as hubs, they connect to many genre-specific awards. We also found that dance and electronic categories increasingly overlap with general awards, showing genre blending.Lastly, we found that our graph model reveals how the Grammys cluster and group styles, even if categories are named differently.")
st.header ("Co-Nomination Network with Weighted Edges")
from pathlib import Path
img_path = Path(__file__).parent / "conomination.png"
st.image(str(img_path), caption="Co-Nomination Network with Weighted Edges")
st.write ("This simplified co-nomination network highlights how different Grammy award categories are connected based on shared nominations, specifically when the same artist, album, or song was nominated in more than one category. Each node here represents a Grammy category, and every line or edge between them means there was at least one shared nominee between those two categories. The thicker the line, the more times it overlaps, and the edge thickness represents weight or frequency of co-nomination.")

st.header ("Scatterplot")
from pathlib import Path
img_path = Path(__file__).parent / "Scatterplot.png"

st.image(str(img_path), caption="Scatterplot of Node Degree with Logarithmic Scale")
st.write ("This scatterplot visualizes the degree of each node in the Grammy nomination network, using a logarithmic scale on both axes. It highlights how most categories have relatively few connections, while a few, like Album of the Year, act as highly connected hubs. The log-log scale helps reveal a power-law distribution, a common feature in real-world networks where a small number of nodes dominate. This pattern suggests that certain Grammy categories consistently bridge multiple genres, making them central to the award landscape.")
st.header ("Shared Nominations")
from pathlib import Path
img_path = Path(__file__).parent / "Shared Nominations.png"
st.image(str(img_path), caption="Here are our concluding findings about the amount of shared nominations across categories, over years.")
st.header ("Sigma(G) Graph")
from pathlib import Path
img_path = Path(__file__).parent / "big graph.png"
st.image(str(img_path), caption="Sigma(G) Graph")
st.write("The graph includes 773 nodes and 10,256 edges, forming a dense network.Clusters and heavily connected regions suggest groups of categories that frequently recognize the same works — for example, pop-related awards or genre-specific groupings.This network helps uncover how categories are interrelated and which ones often overlap in nominations.")
st.header ("Our Takeaways")
st.markdown("<span style='color:pink;'>We found that major awards (like Album of the Year) act as hubs, they connect to many genre-specific awards. We also found that dance and electronic categories increasingly overlap with general awards, showing genre blending.Lastly, we found that our graph model reveals how the Grammys cluster and group styles, even if categories are named differently.</span>", unsafe_allow_html=True)
