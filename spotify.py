from bmtools.agent.singletool import load_single_tools, STQuestionAnswerer

tool_name, tool_url = 'spotify',  "http://127.0.0.1:8079/tools/spotify/"
tools_name, tools_config = load_single_tools(tool_name, tool_url)
print(tools_name, tools_config)

qa = STQuestionAnswerer()

agent = qa.load_tools(tools_name, tools_config)
#Similar artists like Taylor Swift
#Recommend songs like Taylor Swifr's style
#What's the link for Welcome to New York
agent("What's the link for Welcome to New York")
#https://github.com/spotipy-dev/spotipy/tree/master/examples