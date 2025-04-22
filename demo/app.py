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
st.write ("These are the top 10 most connected categories in the Grammy nomination network, ranked by degree, or how many other categories they frequently overlap with.")
st.write ("First, we calculate the degree for every node in our graph G, where each node is a Grammy category. We use the weight of edges, which tells us how often two categories shared the same artist, song, or album. ")
st.header ("Co-Nomination Network with Weighted Edges")
from pathlib import Path
img_path = Path(__file__).parent / "conomination.png"
st.image(str(img_path), caption="Co-Nomination Network with Weighted Edges")
st.write ("This is a simple co-nomination network. Each node here represents a Grammy category. Each line/edge between them means there was at least one shared nominee between those two categories.")
st.write ("The thicker the line, the more times this overlap occurred. Edge thickness represents weight or frequency of co-nomination.")
st.header ("Scatterplot")
from pathlib import Path
img_path = Path(__file__).parent / "Scatterplot.png"
st.image(str(img_path), caption="Scatterplot of Node Degree with Logarithmic Scale")
st.write ("This scatterplot shows the degree (number of connections) for each Grammy award category on a log-log scale.")
st.write ("Each point represents one category node in the graph.")
st.write ("The x-axis shows the node ID; the y-axis shows how many other categories it’s connected to.")
st.write ("Helps reveal the power-law distribution")
st.header ("Revealed Shared Nominations")
from pathlib import Path
img_path = Path(__file__).parent / "Shared Nominations.png"
st.image(str(img_path), caption="Here are our concluding findings about the amount of shared nominations across categories, over years.")
st.header ("Our Takeaways")
st.markdown("<span style='color:pink;'>We found that major awards (like Album of the Year) act as hubs, they connect to many genre-specific awards. We also found that dance and electronic categories increasingly overlap with general awards, showing genre blending.Lastly, we found that our graph model reveals how the Grammys cluster and group styles, even if categories are named differently.</span>", unsafe_allow_html=True)
