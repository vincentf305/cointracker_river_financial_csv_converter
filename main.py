from crewai import Agent, Task, Crew

from crewai_tools import FileReadTool

import os

import sys
sys.path.append('../utils')  

openai_api_key = os.environ["OPENAI_API_KEY"]
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

river_financial_csv = FileReadTool(file_path='./river_financial_example.csv')
cointracker_template_csv = FileReadTool(file_path='./cointracker_csv_template.csv')

# Agent 1: Data analyst
data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Convert a given csv file from river financial to a cointracker.io csv file to be imported",
    tools = [cointracker_template_csv, river_financial_csv],
    verbose=True,
    backstory="As a data analyst, you convert csv files downloaded "
              "from river financial so they can be imported into cointracker.io as a csv wallet"    
)

# Task convert the river financial data into a cointracker.io csv
convertion_task = Task(
    description=(
        "Using the tools convert the river financial csv to work with cointracker.io csv import by changing the columns to match the cointracker csv import file"
    ),
    expected_output=(
        "The data in the river financial csv should be reformatted to work with cointracker.io csv import."
    ),
    output_file="results.csv",
    agent=data_analyst_agent
)

crew = Crew(
    agents=[data_analyst_agent],    
    tasks=[convertion_task],	
    verbose=True,
	memory=True
)

crew.kickoff()

