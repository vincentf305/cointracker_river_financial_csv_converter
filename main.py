from crewai import Agent, Task, Crew

from crewai_tools import FileReadTool

from utils import write_results_to_csv_file

cointracker_csv_template = FileReadTool(file_path='./cointracker_csv_template.csv')
river_financial_csv = FileReadTool(file_path='./river_financial_example.csv')

# Agent 1: Data analyst
data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Convert the river financial csv to match the cointracker template",
    tools = [cointracker_csv_template, river_financial_csv],
    verbose=True,
    backstory=(
        "As a data analyst, you will take any size river financial "
        "csv and convert it to the cointracker csv format based on the template file"
    )
)

# Task for Data Analyst Agent: convert river financial csv into cointracker csv
data_analysis_task = Task(
    description=(
        "Convert the river financial csv into the cointracker csv using the cointracker template"
    ),
    expected_output=(
        "A csv file containing the converted data from the river financial csv"
    ),
    agent=data_analyst_agent,
)

crew = Crew(
    agents=[data_analyst_agent],    
    tasks=[data_analysis_task],	
    verbose=True
)

result = crew.kickoff()

write_results_to_csv_file(result.raw)

