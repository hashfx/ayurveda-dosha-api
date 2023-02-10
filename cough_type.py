from flask import Flask, request

app = Flask(__name__)

def determine_cough_type(symptoms):
    vata_symptoms = ["dry", "itchy", "light", "irritating"]
    pitta_symptoms = ["sharp", "burning", "acidic", "bitter"]
    kapha_symptoms = ["mucus", "heavy", "sticky", "congested"]
    
    vata_count = 0
    pitta_count = 0
    kapha_count = 0
    
    for symptom in symptoms:
        if symptom in vata_symptoms:
            vata_count += 1
        elif symptom in pitta_symptoms:
            pitta_count += 1
        elif symptom in kapha_symptoms:
            kapha_count += 1
    
    if vata_count >= pitta_count and vata_count >= kapha_count:
        return "vata"
    elif pitta_count >= vata_count and pitta_count >= kapha_count:
        return "pitta"
    else:
        return "kapha"

@app.route("/cough_type", methods=["POST"])
def cough_type():
    symptoms = request.json["symptoms"]
    cough_type = determine_cough_type(symptoms)
    return {"cough_type": cough_type}

if __name__ == "__main__":
    app.run(debug=True)
