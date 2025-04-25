import pandas as pd
import random
from faker import Faker

# Initialize Faker and set seeds for reproducibility
fake = Faker()
Faker.seed(42)
random.seed(42)

def generate_patient():
    gender = random.choice(["Male", "Female"])
    age = random.randint(18, 90)
    weight = round(random.uniform(50, 120), 1)
    height = round(random.uniform(150, 200), 1)
    bmi = round(weight / ((height / 100) ** 2), 1)
    
    return {
        "Patient_ID": fake.uuid4(),
        "Name": fake.name(),
        "Age": age,
        "Gender": gender,
        "Weight_kg": weight,
        "Height_cm": height,
        "BMI": bmi,
        "BP_Systolic": random.randint(90, 180),
        "BP_Diastolic": random.randint(60, 120),
        "Sugar_Level": round(random.uniform(70, 250), 1),
        "Cholesterol": round(random.uniform(100, 300), 1),
        "Hemoglobin": round(random.uniform(10, 18), 1)
    }

# Generate 10,000 records and save to CSV
pd.DataFrame([generate_patient() for _ in range(10000)]).to_csv("patients_data.csv", index=False)
print("10,000 patient records generated and saved as 'patients_data.csv'")
