# Problem statement
Individuals often experience common physical symptoms (such as fever, headache, or nausea) but lack the immediate medical knowledge to associate them with specific ailments. There is a need for a quick, accessible tool that can analyze a set of observed symptoms and suggest probable common diseases, helping users make informed decisions about their initial care or whether to seek professional medical help.

# Scope of the project
This project is a console-based Python application designed to simulate a basic medical diagnostic tool.

## Data Limitations: 
It covers a specific dataset of 20 common symptoms and 8 general diseases (e.g., Common Cold, Influenza, Migraine).

## Functionality: 
The program accepts user inputs for symptoms, compares them against a predefined knowledge base, and calculates a probability match percentage.

## Boundaries: 
It provides basic home remedies and severity estimates but does not perform complex medical analysis, utilize machine learning models, or replace professional medical diagnosis.

# Target users
## General Public: 
Individuals seeking a preliminary self-assessment for common illnesses before visiting a doctor.

## Students/Learners: 
Users interested in understanding basic logic flow between symptoms and disease classification.

## Caregivers: 
People looking for quick references on severity and tips for managing common symptoms at home.

# High-level features
## Symptom Catalog Display: Lists 20 unique symptoms with associated IDs for easy user selection.

## Input Validation: 
Includes error handling to ensure users enter valid numeric IDs and prevents duplicate symptom entries.

## Diagnosis Algorithm: 
implementation of a matching logic that compares user inputs against disease definitions to calculate a "Match Percentage."

## Ranked Results: 
Automatically sorts potential diseases by probability (highest match to lowest) to highlight the most likely conditions.

## Comprehensive Output: 
Displays the disease name along with severity level (e.g., Mild, Moderate), a brief description, and actionable health tips (e.g., "Rest, fluids").

## Interactive Session: 
Allows the user to perform multiple diagnoses in a single session via a restart loop.
