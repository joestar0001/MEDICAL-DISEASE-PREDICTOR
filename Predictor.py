"""
MEDICAL DISEASE PREDICTOR PROGRAM
"""
symptoms_list = [
    {"id": 1, "name": "Fever"}, {"id": 2, "name": "Cough"},
    {"id": 3, "name": "Headache"}, {"id": 4, "name": "Sore Throat"},
    {"id": 5, "name": "Fatigue"}, {"id": 6, "name": "Body Aches"},
    {"id": 7, "name": "Runny Nose"}, {"id": 8, "name": "Nausea"},
    {"id": 9, "name": "Vomiting"}, {"id": 10, "name": "Diarrhea"},
    {"id": 11, "name": "Chest Pain"}, {"id": 12, "name": "Shortness of Breath"},
    {"id": 13, "name": "Dizziness"}, {"id": 14, "name": "Rash"},
    {"id": 15, "name": "Itching"}, {"id": 16, "name": "Sneezing"},
    {"id": 17, "name": "Chills"}, {"id": 18, "name": "Abdominal Pain"},
    {"id": 19, "name": "Loss of Appetite"}, {"id": 20, "name": "Joint Pain"},
]

diseases = [
    {"name": "Common Cold", "ids": [2, 4, 7, 16, 3, 5], "severity": "Mild", "desc": "Viral infection.", "tips": "Rest, fluids."},
    {"name": "Influenza (Flu)", "ids": [1, 2, 3, 5, 6, 17, 4], "severity": "Moderate", "desc": "Respiratory illness.", "tips": "Rest, antivirals."},
    {"name": "Gastroenteritis", "ids": [8, 9, 10, 18, 1, 5, 19], "severity": "Moderate", "desc": "Stomach issue.", "tips": "Hydration, bland diet."},
    {"name": "Migraine", "ids": [3, 8, 13, 5], "severity": "Moderate", "desc": "Bad headaches.", "tips": "Dark room, meds."},
    {"name": "Allergic Reaction", "ids": [14, 15, 16, 7, 12], "severity": "Mild to Severe", "desc": "Immune response.", "tips": "Antihistamines."},
    {"name": "Bronchitis", "ids": [2, 12, 11, 1, 5, 6], "severity": "Moderate", "desc": "Bronchial inflammation.", "tips": "Cough medicine."},
    {"name": "Food Poisoning", "ids": [8, 9, 10, 18, 1, 5], "severity": "Moderate", "desc": "Bad food.", "tips": "Hydration."},
    {"name": "Dehydration", "ids": [13, 5, 3, 19], "severity": "Mild to Severe", "desc": "Need water.", "tips": "Water, electrolytes."}
]

while True:
    print("\n" + "=" * 70)
    print(" " * 20 + "MEDICAL DISEASE PREDICTOR")
    print("=" * 70)

    print("\nAVAILABLE SYMPTOMS:")
    print("-" * 70)
    for symptom in symptoms_list:
        print(f"  [{symptom['id']:2d}] {symptom['name']}")
    print("-" * 70)

    selected_symptoms = []
    
    #input from user:
    user_symptoms = []
    print("\nEnter symptom IDs one by one.")
    print("Type '0' when you are done.")

    while True:
        try:
            choice = int(input("Enter ID: "))
            
            if choice == 0:
                break
            
            #checking input
            if choice > 0 and choice <= 20:
                if choice not in user_symptoms:
                    user_symptoms.append(choice)
            else:
                print("Invalid ID number.")
                
        except ValueError:
            print("Please enter a number.")

    print("You selected:", user_symptoms)

    #calculation: 
    results = []
    if len(user_symptoms) > 0:
        for d in diseases:
            matches = 0
            for s_id in d['ids']:
                if s_id in user_symptoms:
                    matches = matches + 1
            score = int((matches / len(d['ids'])) * 100)
            
            if score > 0:
                results.append([score, d['name'], d['severity'], d['desc'], d['tips']])

        n = len(results)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Compare scores (index 0 is the score)
                if results[j][0] < results[j + 1][0]:
                    results[j], results[j + 1] = results[j + 1], results[j]

    #showing result : 
    print("\n" + "=" * 70)
    print(" " * 25 + "DIAGNOSIS RESULTS")
    print("=" * 70)
    if not results:
        print("No matching diseases.")
    else:
        for r in results:
            print(f"\nDisease: {r[1]}")
            print(f"Match:   {r[0]}%")
            print(f"Sever:   {r[2]}")
            print(f"About:   {r[3]}")
            print(f"Advice:  {r[4]}")
            print("-" * 30)

    again = input("\nPress Enter to restart, or type 'no' to exit: ")
    if again == 'no':
        print("\nThank you for using the Medical disease predictor by BHAWESH KUMAR GAUTAM.")
        break