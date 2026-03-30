import json


def new_data_load(filename="new_patient_values.json"):
    with open(filename, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def update_data(data, patient_values, weight_trend):
    updated_values = patient_values.copy()

    if "weight" in data:
        updated_values[0] = data["weight"]

    if "saturation" in data:
        updated_values[1] = data["saturation"]

    if "heart_rate" in data:
        updated_values[2] = data["heart_rate"]

    updated_weight_trend = weight_trend.copy()
    updated_weight_trend.append(updated_values[0])

    return updated_values, updated_weight_trend


def risk_assessment(patient_values, weight_trend):
    riziko = 0

    weight = patient_values[0]
    saturation = patient_values[1]
    heart_rate = patient_values[2]

    if len(weight_trend) >= 8:
        weight_week_ago = weight_trend[-8]
        if weight > weight_week_ago:
            riziko += weight - weight_week_ago

    if saturation < 95:
        riziko += 10

    if len(weight_trend) >= 3:
        avg_last_3 = sum(weight_trend[-3:]) / 3
        if heart_rate > 120 and avg_last_3 > 120:
            riziko += 10

    return int(riziko)










