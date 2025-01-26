import streamlit as st
import datetime
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.youtube_tools import YouTubeTools

agent = Agent(
    name='Youtube Agent',
    model=Groq(id='llama-3.3-70b-versatile'),
    instructions=["Generated detailed description on the gievn youtube video"],
    tools=[YouTubeTools()]
    # show_tool_calls=True,
    # markdown=True
)

st.title('Youtube video summerizer')
url=st.text_input('Enter the url')
if st.button('submit'):
    resp=agent.run(url)
    st.write(resp.content)