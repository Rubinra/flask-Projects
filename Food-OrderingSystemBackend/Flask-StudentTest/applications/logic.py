import json
import re
import pandas as pd


def queryJson():
    # create multiple raw json from log file And Split Message
    b = []
    dirPath = 'C:/Users/Shon/Desktop/Shon/PYTHON/PythonLanguage/Pycharm/FLASK/Flask-First-Programs/Flask-Student/Flask-StudentTest/applications/vector.log'
    with open(dirPath, 'r') as my_file:
        a = my_file.read().splitlines()
        for i in a:
            b.append(i)
    a = []
    for j in range(len(b)):
        df1 = pd.DataFrame.from_records(eval(b[j]), index=[0])
        a.append(df1)
    df = pd.concat(a).sort_index()
    df.reset_index(drop=True, inplace=True)

    json_out = []
    # loop the index of table
    for ind in df.index:
        # convert raws to json
        data = df.loc[ind].to_json()
        # convert JSON to dict
        json_data = json.loads(data)
        # to get message key values
        text = json_data.get("message")
        unwanted = "!@#$;:!*%)(&^~][)(\/"

        # Date
        date = re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}", text)
        strDate = ""
        # to convert the List to String
        for dl in date:
            strDate = strDate + dl
            strDate = strDate.strip()

        # Time
        time = re.findall("[0-9]{2}:[0-9]{2}", text)
        strTime = ""
        # to convert the List to String
        for tl in time:
            strTime = strTime + tl
            strTime = strTime.strip()

        # FileName**
        fileName = re.findall("[a-z A-Z .:]+", text)
        strFileName = ""
        # to convert the List to String
        for al in fileName:
            strFileName = strFileName + al
            strFileName = strFileName.strip()
        # to split the String

        x = strFileName.split(":", 4)
        strFileName = (x[2])

        # lineNumber
        lineNumber = re.findall("[0-9)(]{5,120}", text)
        strLineNumber = ""
        # to convert the List to String
        for l in lineNumber:
            strLineNumber = strLineNumber + l
            strLineNumber = strLineNumber.strip()

        # To Remove Unwanted Characters
        for char in unwanted:
            strLineNumber = strLineNumber.replace(char, "")

        # priority_level

        priority_level = re.findall("[[[A-Z a-z]+]", text)
        strpriority_level = ""
        # to convert the List to String
        for tl in priority_level:
            strpriority_level = strpriority_level + tl
            strpriority_level = strpriority_level.strip()

        # To Remove Unwanted Characters
        for char in unwanted:
            strpriority_level = strpriority_level.replace(char, "")

        # others
        others = re.findall("[A-Z a-z -:]+$", text)
        strOthers = ""
        # to convert the List to String
        for ol in others:
            strOthers = strOthers + ol
            strOthers = strOthers.strip()

        # To Remove Unwanted Characters
        for char in unwanted:
            strOthers = strOthers.replace(char, "")

        # add all values to Dict

        data = {
            "date": strDate,
            "time": strTime,
            "File_name": strFileName,
            "line_number": strLineNumber,
            "priority_Level": strpriority_level,
            "others": strOthers
        }
        # to change the message key value of dict
        json_data.update({"message": data})

        # add all dict to json_out
        json_out.append(json_data)

    # # convert dict to json
    # json_object = json.dumps(json_out, indent=4)
    # print(json_object)
    # # write the json file to system
    # with open("query.json", "w") as f:
    #     f.write(json_object)
    #     print(json_object)
    return json_out
