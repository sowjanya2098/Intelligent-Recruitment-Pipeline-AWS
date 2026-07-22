import json
import boto3


sns = boto3.client("sns")


# Replace this with your SNS Topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:364042450737:CandidateNotificationTopic"


def lambda_handler(event, context):

    try:

        for record in event["Records"]:

            if record["eventName"] not in [
                "INSERT",
                "MODIFY"
            ]:
                continue


            new_image = record["dynamodb"]["NewImage"]


            name = (
                new_image.get("name", {})
                .get("S", "Unknown")
            )


            status = (
                new_image.get("status", {})
                .get("S", "")
            )


            score = (
                new_image.get("match_score", {})
                .get("N", "0")
            )


            skills = []


            if "skills" in new_image:

                for skill in new_image["skills"]["L"]:

                    skills.append(
                        skill["S"]
                    )


            if status == "Shortlisted":


                message = f"""
Candidate Shortlisted

Name:
{name}

Score:
{score}%

Skills:
{', '.join(skills)}
"""


            else:


                message = f"""
Candidate Status Updated

Name:
{name}

Status:
{status}

Score:
{score}%
"""


            sns.publish(

                TopicArn=SNS_TOPIC_ARN,

                Subject="Candidate Recruitment Update",

                Message=message

            )


        return {

            "statusCode":200,

            "body":json.dumps({

                "message":
                "Notification sent"

            })

        }


    except Exception as e:


        return {

            "statusCode":500,

            "body":json.dumps({

                "error":str(e)

            })

        }