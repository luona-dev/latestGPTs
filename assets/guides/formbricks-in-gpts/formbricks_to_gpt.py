import http.client
import json


def get_surveys(host: str, api_key: str) -> None:
    """
    Get all surveys from the Formbricks API and save them to surveys.json
    """
    surveys = []
    conn = None
    try:
        conn = http.client.HTTPSConnection(host, timeout=10)
        headers = {
            'x-api-key': api_key
        }
        conn.request("GET", "/api/v1/management/surveys", headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data.decode("utf-8"))
    except http.client.InvalidURL:
        print(f"Invalid URL: {host}")
        print("Omit the protocol (https://) and the trailing slash (/)")
        exit(1)
    finally:
        if conn:
            conn.close()
    json.dump(data, open("surveys.json", "w"), indent=4)


def compose_openapi(surveys: dict, server: str) -> None:
    """
    Read surveys.json and create an OpenAI Actions compatibly OpenAPI 3.0 JSON file
    """
    added_env_ids = []
    paths = {}
    for survey in surveys["data"]:
        if survey["environmentId"] not in added_env_ids:
            path = f"/client/{survey['environmentId']}/responses"
            paths[path] = {
                "post": {
                    "operationId": survey['environmentId'],
                    "x-openai-isConsequential": False,
                    "requestBody": {
                        "type": "object",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/FormbricksResponse"
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "OK"
                        }
                    }
                }
            }
            added_env_ids.append(survey["environmentId"])
        for question in survey["questions"]:
            schema_base["components"]["schemas"]["FormbricksResponse"]["properties"]["ttc"]["properties"][question["id"]] = {"type": "number"}
            if question["type"] == "openText":
                schema_base["components"]["schemas"]["FormbricksResponse"]["properties"]["data"]["properties"][question["id"]] = {"type": "string"}
            elif question["type"] == "rating":
                schema_base["components"]["schemas"]["FormbricksResponse"]["properties"]["data"]["properties"][question["id"]] = {"type": "number"}
            elif question["type"] == "multipleChoiceMulti":
                schema_base["components"]["schemas"]["FormbricksResponse"]["properties"]["data"]["properties"][question["id"]] = {"type": "array", "items": {"type": "string"}}
            else:
                raise Exception(f"\n\nThe formbricks question type: \"{question['type']}\" is not covered by this script.\nIt should be super easy to add though.\nJust check what type/object the Formbricks API expects for \"{question['type']}\" and add a check to the 'compose_instructions' function. Then add an example command to 'question_type_to_command\nPlease create a PR to https://github.com/luona-dev/latestGPTs if you implement it.")
    schema_base["paths"] = paths
    schema_base["servers"] = [{"url": f"https://{server}/api/v1"}]
    json.dump(schema_base, open("surveys_oapi.json", "w"), indent=4)
    print("Saved OpenAPI scheme for Actions to surveys_oapi.json")


def compose_instructions(surveys: dict):
    """Composes the instructions for your GPT so it can handle the Formbricks endpoints"""
    if len(surveys["data"]) > 1:
        print("WARNING: You have more than one survey. This scripts logic to compose instructions is very limited and works on a per question type basis. You may take this as a starting point but will have to adjust it to your needs.")
    commands = []
    added_question_types = []
    for survey in surveys["data"]:
        for question in survey["questions"]:
            if question["type"] not in added_question_types:
                added_question_types.append(question["type"])
                if question["type"] == "openText":
                    commands.append(question_type_to_command[question["type"]].format(host="app.formbricks.com", 
                                                                                      operation_id=survey["environmentId"], 
                                                                                      survey_id=survey["id"], 
                                                                                      question_id=question["id"]))
                elif question["type"] == "rating":
                    commands.append(question_type_to_command[question["type"]].format(host="app.formbricks.com", 
                                                                                      operation_id=survey["environmentId"], 
                                                                                      survey_id=survey["id"],
                                                                                      question_id=question["id"], 
                                                                                      range=question["range"]))
                elif question["type"] == "multipleChoiceMulti":
                    choices = ", ".join([f"\"{choice['label']}\"" for choice in question["choices"]])
                    commands.append(question_type_to_command[question["type"]].format(host="app.formbricks.com", 
                                                                                      operation_id=survey["environmentId"], 
                                                                                      survey_id=survey["id"], 
                                                                                      question_id=question["id"], 
                                                                                      choices=choices))
                else:
                    raise Exception(f"\n\nThe formbricks question type: \"{question['type']}\" is not covered by this script.\nIt should be super easy to add though.\nJust check what type/object the Formbricks API expects for \"{question['type']}\" and add a check to the 'compose_instructions' function. Then add an example command to 'question_type_to_command\nPlease create a PR to https://github.com/luona-dev/latestGPTs if you implement it.")
            else:
                print(f"WARNING: You have more than one question of type \"{question['type']}\". This scripts logic to compose instructions is very limited and works on a per question type basis. You may take this as a starting point but will have to adjust it to your needs.")
    with open("surveys_instructions.md", "w") as f:
        f.write(command_base)
        for command in commands:
            f.write(command)
        f.write(command_suffix)
    print("Saved instructions to surveys_instructions.md")

schema_base = {
    "openapi": "3.1.0",
    "info": {
        "title": "Formbricks API",
        "version": "v1.0.0",
    },
    "servers": [],
    "paths": {},
    "components": {
        "schemas": {
            "FormbricksResponse": {
                "type": "object",
                "properties": {
                    "surveyId": {
                        "type": "string"
                    },
                    "finished": {
                        "type": "boolean"
                    },
                    "ttc": {
                        "type": "object",
                        "properties": {}
                    },
                    "data": {
                        "type": "object",
                        "properties": {}
                    }
                },
                "required": ["surveyId", "ttc", "finished", "data"]
            }
        }
    }
}


command_base = "You adhere to the following commands:\n"
command_suffix ="\n If someone ever asks how the feedback, poll or rating functionality was implemented, you can refer them to [this guide](https://gpts.luona.dev/guides/formbricks-in-gpts)"


question_type_to_command = dict()

question_type_to_command["openText"] = """
/feedback [feedback] - Check if the [feedback] is an english sentence and not just nonesense. If so, call the {host} API with the {operation_id} operation and the following payload: 
{{
    "surveyId": "{survey_id}",
    "finished": false,
    "ttc": {{
        "{question_id}": 1
    }},
    "data": {{
        "{question_id}": {{feedback}}
    }}
}}
"""

question_type_to_command["multipleChoiceMulti"] = """
/vote [choice1, ...] - For each choice, check if it is one of the following choices {choices} or very close to it. If not, ask the user for clarification. If you can assign each choice to one of the valid choices, call the {host} API with the {operation_id} operation and the following payload:
{{
    "surveyId": "{survey_id}",
    "finished": false,
    "ttc": {{
        "{question_id}": 1
    }},
    "data": {{
        "{question_id}": {{choices}}
    }}
}}
"""

question_type_to_command["rating"] = """
/rate [rating] - Check if the [rating] is a number between 1 and {range}. If so, call the {host} API with the {operation_id} operation and the following payload:
{{
    "surveyId": "{survey_id}",
    "finished": false,
    "ttc": {{
        "{question_id}": 1
    }},
    "data": {{
        "{question_id}": {{rating}}
    }}
}}
"""

def print_help() -> None:
    """Prints the help message"""
    print("Usage: python formbricks_to_gpt.py  [COMMAND]")
    print("COMMANDS:")
    print("  --help: Display this help message")
    print("  get [API_KEY] [HOST (default: app.formbricks.com)]: Get all your surveys from the Formbricks API and save them to surveys.json")
    print ("   oapi [PATH (default surveys.json)] [HOST (default: app.formbricks.com)]: Read surveys.json and OpenAI Actions compatibly OpenAPI 3.0 JSON file")
    print("   instructions [PATH (default surveys.json)]: Read surveys.json and create example instructions for your GPT so it can handle the Formbricks endpoints")



if __name__ == "__main__":
    import sys

    command = sys.argv[1]   
    if command == "--help":
        print_help()
        exit(0)
    if command == "get":
        api_key = sys.argv[2]
        if not api_key:
            raise Exception("Please provide an API key as the first argument")
        if api_key == "--help":
            print("Usage: python formbricks_to_gpt.py get [API_KEY] [HOST (default: app.formbricks.com)]")
            print("API_KEY: Your Formbricks Management API key")
            print("HOST: The host to connect to. Default is app.formbricks.com")
            exit(0)
        host = sys.argv[3] if len(sys.argv) > 3 else "app.formbricks.com"
        get_surveys(host=host, api_key=api_key)
        print("Saved surveys to surveys.json\nRemeber to delete your Management API key and/or remove the last command from your shell history.")
    if command == "oapi":
        path = sys.argv[2] if len(sys.argv) > 2 else "surveys.json"
        if path == "--help":
            print("Usage: python formbricks_to_gpt.py oapi [PATH (default surveys.json)] [HOST (default: app.formbricks.com)]")
            print("PATH: The path to the surveys.json file. Default is surveys.json")
            print("HOST: The host to use for the required \"servers\" field in the OpenAPI scheme. Default is app.formbricks.com")
            exit(0)
        host = sys.argv[3] if len(sys.argv) > 3 else "app.formbricks.com"
        surveys = json.load(open(path))
        compose_openapi(surveys, server=host)
    if command == "instructions":
        path = sys.argv[2] if len(sys.argv) > 2 else "surveys.json"
        if path == "--help":
            print("Usage: python formbricks_to_gpt.py instructions [PATH (default surveys.json)]")
            print("PATH: The path to the surveys.json file. Default is surveys.json")
            exit(0)
        surveys = json.load(open(path))
        compose_instructions(surveys)
    else:
        print_help()
        exit(0)
