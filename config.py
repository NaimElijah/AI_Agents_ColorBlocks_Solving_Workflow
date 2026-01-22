# model name used across the application
llm_model = "ibm/granite4:350m"   # Other examples: "gemini-2.5-flash", "qwen3:0.6b"

# temperature setting for the LLM
llm_temperature = 0.0

# API key if needed for certain LLMs (like Google's Gemini)
llm_api_key = "YOUR_GOOGLE_API_KEY_HERE"  # Replace with your actual API key   # SETUP API KEY if using Google Gemini

# State field names
state_start_blocks_field = "start_blocks"
state_goal_blocks_field = "goal_blocks"
self_solver_output_field = "SelfSolverAgent_output"
tools_usage_solver_output_field = "ToolSolverAgent_output"
manager_feedback_field = "manager_feedback"

# Problem inputs (In a "start_blocks|goal_blocks" format)
problems = [
    # Example 1
    "(5,2),(1,3),(9,22),(21,4)|2,22,4,3",
    # Example 2
    "(5,2),(1,3),(9,22),(21,4)|2,1,9,21",
    # Example 3
    "(5,2),(1,3),(9,22),(21,4),(11,12),(12,13),(13,14)|11,2,1,14,9,13,21"
]


# Can add other configuration settings as needed