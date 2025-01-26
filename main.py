# import streamlit as st
# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.youtube_tools import YouTubeTools

# agent = Agent(
#     name='Youtube Agent',
#     model=Groq(id='llama-3.3-70b-versatile',api_key=st.secrets['key']),
#     instructions=["Generated detailed description on the gievn youtube video"],
#     tools=[YouTubeTools()]
#     # show_tool_calls=True,
#     # markdown=True
# )

# st.title('Youtube video summerizer')
# url=st.text_input('Enter the url')
# if st.button('submit'):
#     resp=agent.run(url)
#     st.write(resp.content)
import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.youtube_tools import YouTubeTools

# Modify the phi library version or use a different approach
agent = Agent(
    name='Youtube Agent',
    model=Groq(id='llama-3.3-70b-versatile', api_key=st.secrets['key']),
    instructions=["Generate detailed description of the given YouTube video"],
    tools=[YouTubeTools()]
)

st.title('Youtube Video Summarizer')
url = st.text_input('Enter the URL')
if st.button('Submit'):
    resp = agent.run(url)
    st.write(resp.content)
