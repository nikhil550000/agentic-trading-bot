from setuptools import find_packages,setup

setup(name="agentic-trading-system",
       version="0.0.1",
       author="nikhil",
       author_email="nikhilsai550000@gmail.com",
       packages=find_packages(),
       install_requires=['lancedb','langchain','langgraph','tavily-python','polygon']
       )