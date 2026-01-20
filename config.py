# model name used across the application
llm_model = "ibm/granite4:350m"   # Other examples: "gemini-2.5-flash", "qwen3:0.6b"

# temperature setting for the LLM
llm_temperature = 0.0

# API key if needed for certain LLMs
llm_api_key = "YOUR_GOOGLE_API_KEY_HERE"  # Replace with your actual API key   # SETUP API KEY if using Google Gemini

# State field names
state_start_blocks_field = "start_blocks"
state_goal_blocks_field = "goal_blocks"
self_solver_output_field = "SelfSolverAgent_output"
tools_usage_solver_output_field = "tools_outputs"
manager_feedback_field = "manager_feedback"



# Can add other configuration settings as needed