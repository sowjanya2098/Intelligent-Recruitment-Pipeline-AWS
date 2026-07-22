import json
import boto3


lambda_client = boto3.client("lambda")


# Candidate Matcher Lambda name
MATCHER_FUNCTION = "candidatematcher"


# Skill cleaning dictionary
SKILL_MAPPING = {
    "aws lambda": "lambda",
    "lambda function": "lambda",
    "amazon lambda": "lambda",

    "amazon s3": "s3",
    "aws s3": "s3",

    "amazon dynamodb": "dynamodb",
    "aws dynamodb": "dynamodb",

    "api gateway service": "api gateway",
    "amazon api gateway": "api gateway",

    "amazon sns": "sns",
    "aws sns": "sns"
}


def normalize_skill(skill):

    skill = skill.lower().strip()

    if skill in SKILL_MAPPING:
        return SKILL_MAPPING[skill]

    return skill



def lambda_handler(event, context):

    try:

        updated_candidates = []


        for record in event["Records"]:

            if record["eventName"] != "MODIFY":
                continue


            new_image = record["dynamodb"]["NewImage"]


            candidate_id = (
                new_image["candidate_id"]["S"]
            )


            skills = []


            for item in new_image["skills"]["L"]:

                skills.append(
                    normalize_skill(
                        item["S"]
                    )
                )


            skills = list(set(skills))


            payload = {

                "candidate_id": candidate_id,

                "skills": skills
            }


            lambda_client.invoke(

                FunctionName=MATCHER_FUNCTION,

                InvocationType="RequestResponse",

                Payload=json.dumps(payload)

            )


            updated_candidates.append(
                candidate_id
            )


        return {

            "statusCode":200,

            "body":json.dumps({

                "message":
                "Skills normalized",

                "updated_candidates":
                updated_candidates

            })

        }


    except Exception as e:


        return {

            "statusCode":500,

            "body":json.dumps({

                "error":str(e)

            })

        }