from crewai import Crew

from tasks import MeetingPreparationTasks
from agents import MeetingPreparationAgents

tasks = MeetingPreparationTasks()
agents = MeetingPreparationAgents()

print("## Welcomee to the Meeting Prep Crew")
print("------------------------------------")

participants = input("What are the emails for the participants (other than you) in the meeting?\n")
context = input("What is the context of the meeting?\n")
objective = input("What is your objective for this meeting?\n")

# print(f"participants: {participants} | context: {context} | objective: {objective}")

researcher_agent = agents.research_agent()
industry_analyst_agent = agents.industry_analysis_agent()
meeting_strategy_agent = agents.meeting_strategy_agent()
summary_and_briefing_agent = agents.summary_and_briefing_agent()

research = tasks.research_task(researcher_agent, participants, context)
industry_analysis = tasks.industry_analysis_task(industry_analyst_agent, participants, context)
meeting_strategy = tasks.meeting_strategy_task(meeting_strategy_agent, context, objective)
summary_and_briefing = tasks.summary_and_briefing_task(summary_and_briefing_agent, context, objective)

crew = Crew(
    agents=[
        researcher_agent, 
        industry_analyst_agent,
        meeting_strategy_agent, 
        summary_and_briefing_agent
    ], 
    tasks=[
        research, 
        industry_analysis,
        meeting_strategy,
        summary_and_briefing
    ]
)

game = crew.kickoff()

print("## Here is the result ##")
print(game)