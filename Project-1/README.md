# Rule-Based Chatbot using n8n

A simple rule-based chatbot built with n8n as part of my 1-month internship at Decodes Lab.

The chatbot uses predefined user inputs and conditional logic to generate appropriate responses. It can handle greetings, general predefined messages, and exit commands while running continuously in a chat-based workflow.

## Project Overview

The goal of this project is to demonstrate how a basic rule-based chatbot can be created using n8n workflow automation.

Instead of using an external AI model, the chatbot relies on predefined rules and conditional logic to identify the user's input and return the appropriate response.

## Key Features

* Handles common greetings such as `hello`, `hi`, and `hey`
* Responds to predefined user inputs
* Handles exit commands such as `bye` and `exit`
* Uses conditional logic for decision-making
* Maintains a continuous chat interaction
* Built entirely using an n8n workflow
* Demonstrates basic chatbot and automation concepts

## Workflow

The chatbot follows this basic flow:

```text
User Input
    ↓
Chat Trigger
    ↓
Input Processing
    ↓
Rule-Based Conditions
    ↓
Matching Response
    ↓
Chat Response
    ↓
Continue Conversation
```

The workflow checks the user's message against predefined conditions. Based on the matched condition, the chatbot sends the corresponding response.

## Example Interaction

```text
User: Hello
Bot: Hello! How can I help you?

User: Hi
Bot: Hi! Nice to meet you.

User: How are you?
Bot: I'm doing great! How can I help you?

User: Bye
Bot: Goodbye! Have a great day!
```

## Technologies Used

* n8n
* n8n Chat Trigger
* Conditional Logic
* Workflow Automation
* Rule-Based Decision Making

## How It Works

1. The user sends a message through the chat interface.
2. The n8n workflow receives the message through the Chat Trigger.
3. The user's input is checked against predefined rules.
4. Conditional logic determines which response should be returned.
5. The chatbot sends the appropriate response.
6. The conversation continues until an exit command is provided.

## Repository Contents

```text
rule-based-chatbot/
│
├── Rule-Based-Chatbot.json
└── README.md
```

The `Rule-Based-Chatbot.json` file contains the complete n8n workflow and can be imported into n8n.

## How to Import the Workflow

1. Open your n8n instance.
2. Create or open a workflow.
3. Select the option to import a workflow.
4. Upload the `.json` workflow file from this repository.
5. Review the workflow nodes and connections.
6. Activate or run the workflow.
7. Open the chat interface and test the chatbot.

## Key Skills Demonstrated

* Workflow automation
* Control flow
* Conditional decision-making
* Rule-based chatbot development
* User input handling
* n8n workflow building
* Basic AI concepts

## Internship Project

This project was developed as part of my 1-month internship at Decodes Lab.

The project focuses on understanding control flow, decision-making logic, and the fundamentals of building a simple conversational system using workflow automation.

## Author

Workflow

## License

This project is created for educational and internship purposes.
