# AI Recommendation Logic

## Overview

This project is a simple recommendation system built using n8n as part of my Decodes Lab internship.

The system takes user preferences as input, matches them with a predefined dataset using logic-based preference matching, calculates a match score, and displays the top recommendations.

## Objective

The objective of this project is to understand and implement basic recommendation logic using user preferences, pattern matching, scoring, and ranking.

## Key Requirements

- Take user input such as choices or interests
- Match user preferences using logic or similarity
- Calculate match scores
- Display recommended items

## How It Works

1. The user enters their preferences through the n8n chat interface.
2. The system extracts supported preferences from the user input.
3. The preferences are compared with the available items.
4. A match score is calculated for each item.
5. Items are sorted according to their match scores.
6. The top recommendations are displayed to the user.

## Workflow

User Input  
↓  
Preference Extraction  
↓  
Preference Matching  
↓  
Match Score Calculation  
↓  
Recommendation Ranking  
↓  
Display Recommendations

## Technologies Used

- n8n
- JavaScript
- Rule-based recommendation logic

## Recommendation Logic

Each item contains a set of attributes or genres.

The system compares these attributes with the user's preferences.

For every matching preference, the item receives one point.

Items with higher match scores are ranked higher, and the top matching items are returned as recommendations.

## Example

### User Input

I like action and sci-fi movies.

### Detected Preferences

- action
- sci-fi

### Recommendation

The system compares the detected preferences with the available movie dataset and recommends the items with the highest matching scores.

## Key Skills Demonstrated

- Logic building
- Pattern matching
- JavaScript
- Data processing
- Recommendation concepts
- n8n workflow automation

## Project Type

Project 3 of 4  
Decodes Lab 1-Month Internship
