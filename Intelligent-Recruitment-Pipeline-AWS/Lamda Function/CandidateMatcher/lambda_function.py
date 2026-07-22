import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")

TABLE_NAME = "Candidates"

table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):

    try:

        candidate_id = event.get("candidate_id")

        candidate_skills = event.get("skills", [])

        required_skills = [
            "lambda",
            "s3",
            "dynamodb",
            "api gateway",
            "sns",
            "iam",
            "eventbridge"
        ]

        matched_skills = list(
            set(candidate_skills)
            .intersection(set(required_skills))
        )

        score = int(
            (len(matched_skills) /
             len(required_skills)) * 100
        )

        status = (
            "Shortlisted"
            if score >= 60
            else "Rejected"
        )


        table.update_item(
            Key={
                "candidate_id": candidate_id
            },

            UpdateExpression=
            "SET match_score=:score, #st=:status",

            ExpressionAttributeNames={
                "#st": "status"
            },

            ExpressionAttributeValues={
                ":score": score,
                ":status": status
            }
        )


        return {
            "statusCode": 200,
            "body": json.dumps({
                "candidate_id": candidate_id,
                "score": score,
                "status": status,
                "matched_skills": matched_skills
            })
        }


    except Exception as e:

        return {
            "statusCode":500,
            "body":json.dumps({
                "error":str(e)
            })
        }