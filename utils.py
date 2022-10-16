import json


def open_json():
    with open("candidates.json", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_candidate(candidate_id):
    data = open_json()
    for i in data:
        if i["id"] == candidate_id:
            return i


def get_candidates_by_name(candidate_name):
    data = open_json()
    result = []
    cnt = 0
    for i in data:
        if candidate_name in i["name"]:
            cnt = cnt + 1
            result.append(i)
    return result,cnt


def get_candidates_by_skill(skill):
    data = open_json()
    cnt = 0
    result = []
    for i in data:
        if skill in i["skills"].lower().split(", "):
            cnt = cnt + 1
            result.append(i)
    return result, cnt


#get_candidates_by_name("Bauer")
#get_candidates_by_skill("python")
