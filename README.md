# Project title
MEDICAL DISEASE PREDICTOR PROGRAM

## Overview of the project
The Medical Symptom Checker is a Python-based command-line interface (CLI) application designed to provide a preliminary diagnosis of health conditions based on user-reported symptoms. The program allows users to select from a list of 20 common symptoms and compares them against a known database of diseases (such as Influenza, Migraine, and Dehydration). It utilizes a matching algorithm to rank potential conditions by probability, offering users descriptions, severity levels, and actionable recommendations

## Features
1. Interactive Symptom Selection: Users can choose multiple symptoms from a curated list.

2. Intelligent Diagnosis Logic: The system calculates a "Match Percentage" based on how many selected symptoms overlap with specific disease profiles.

3. Detailed Health Reports: For every potential match, the program provides:

  a. Match confidence score (Percentage).

  b. Disease Severity (Mild, Moderate, Severe).

  c. Medical Description.

  d. Recommendations for immediate care.

4. Input Validation: Includes error handling to ensure users enter valid symptom IDs.

5. User-Friendly Loop: Allows the user to perform multiple diagnoses in one session without restarting the script.

## Technologies/Tools Used
Programming Language: Python 3.x

Interface: Command Line / Terminal.

## Steps to Install & Run the Project
Step 1: Verify Python 3.x is installed by running python --version in your terminal.

Step 2: Save the script as symptom_checker.py and execute it using the command python symptom_checker.py.

Step 3: Test the diagnosis logic by entering symptom IDs 1, 2, 6 (Flu), typing done, and verifying the result.

Step 4: Follow the on-screen menu to either restart the diagnosis process or exit the application.

## Screenshots
<img width="630" height="738" alt="Screenshot 2025-11-20 at 11 26 37 AM" src="https://github.com/user-attachments/assets/254a0a4c-ce7d-4c82-a2c3-01c7f2f85f3e" />
<img width="568" height="551" alt="Screenshot 2025-11-20 at 11 26 57 AM" src="https://github.com/user-attachments/assets/8d181c19-a4af-4602-bc2b-9701a7be2ec1" />
