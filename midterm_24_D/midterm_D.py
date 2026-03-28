import json
if __name__ == "__main__":
    pass
    patient_values = [75, 99, 62]  # hmotnost, saturace, tepova frekvence
    weight_trend = [71, 71, 71, 71, 70, 71, 73, 75]
    available_dates = {5, 8, 15, 25}
    today = 25
    # main(patient_values, weight_trend, available_dates, today)

def new_data_load(patient_values):
    filename = input("Enter file name: ")
    if filename == "" or filename is None:
        filename = "new_patient_values.json"

    weight = patient_values[0]
    saturation = patient_values[1]
    heart_rate = patient_values[2]

    if weight == "":
        return "Empty weight value"

    data = {
        "weight": weight,
        "saturation": saturation,
        "heart_rate": heart_rate
    }


    with open(filename, "w", encoding='utf_8') as json_file:
        json.dump(data, json_file)

    return data


def update_data(data, patient_values, weight_trend):
    data = list(data.values())

    patient_values = data.copy()

    weight_trend.append(data[0])
    return patient_values, weight_trend

def risk_assessment(patient_values, weight_trend):
    riziko = 0

    weight = patient_values[0]
    saturation = patient_values[1]
    heart_rate = patient_values[2]

    if patient_values[0] > patient_values[6]:
        riziko += patient_values[0] - patient_values[6]

    if saturation < 95:
        riziko += 10

    if heart_rate > 120 and (sum(weight_trend[-1:-3])/len(weight_trend)) > 120:
        riziko += 10

    return riziko










