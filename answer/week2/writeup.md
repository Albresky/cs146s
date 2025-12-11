# Week 2 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.


## YOUR RESPONSES
For each exercise, please include what prompts you used to generate the answer, in addition to the location of the generated response. Make sure to clearly add comments in your code documenting which parts are generated.

### Exercise 1: Scaffold a New Feature
Prompt: 
```
Implement `extract_action_items_llm` in `week2/app/services/extract.py` using Ollama and Pydantic for structured output, wrap the formattor in a class named `ActionItemList`.
``` 

Generated Code Snippets:
```
week2/app/services/extract.py: Lines 98-123
```

### Exercise 2: Add Unit Tests
Prompt: 
```
Write unit tests for `extract_action_items_llm` in `week2/tests/test_extract.py`, mocking the Ollama chat response.
``` 

Generated Code Snippets:
```
week2/tests/test_extract.py: Lines 23-48
```

### Exercise 3: Refactor Existing Code for Clarity
Prompt: 
```
Refactor the backend to use Pydantic schemas for requests and responses, and clean up the database layer.
``` 

Generated/Modified Code Snippets:
```
week2/app/schemas.py: Created new file
week2/app/routers/notes.py: Updated to use schemas
week2/app/routers/action_items.py: Updated to use schemas
week2/app/db.py: Added get_action_item
week2/app/main.py: Implemented lifespan context manager for DB initialization
```

### Exercise 4: Use Agentic Mode to Automate Small Tasks
Prompt: 
```
Add an endpoint for LLM extraction and update the frontend to include buttons for LLM extraction and listing notes.
``` 

Generated/Modified Code Snippets:
```
week2/app/routers/action_items.py: Added extract_llm endpoint
week2/frontend/index.html: Added buttons and JS logic
```

### Exercise 5: Generate a README from the Codebase
Prompt: 
```
Generate a README.md for the project.
``` 

Generated/Modified Code Snippets:
```
week2/README.md: Created new file
```
```
TODO: List all modified code files with the relevant line numbers. (We anticipate there may be multiple scattered changes here – just produce as comprehensive of a list as you can.)
```


### Exercise 4: Use Agentic Mode to Automate a Small Task
Prompt: 
```
1. Integrate the LLM-powered extraction as a new endpoint. Update the frontend to include an "Extract LLM" button that, when clicked, triggers the extraction process via the new endpoint.

2. Expose one final endpoint to retrieve all notes. Update the frontend to include a "List Notes" button that, when clicked, fetches and displays them.
``` 

Generated Code Snippets:
```
ref: frontend/index.html
```


### Exercise 5: Generate a README from the Codebase
Prompt: 
```
Generate a README.md for the project.
``` 

Generated Code Snippets:
```
week2/README.md
```


## SUBMISSION INSTRUCTIONS
1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields. 
2. Make sure you have all changes pushed to your remote repository for grading.
3. Submit via Gradescope. 