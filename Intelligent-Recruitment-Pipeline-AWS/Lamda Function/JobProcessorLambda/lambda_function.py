import json
import boto3


dynamodb = boto3.resource("dynamodb")


TABLE_NAME = "JobRequirements"


table = dynamodb.Table(TABLE_NAME)



def lambda_handler(event, context):

    try:

        job_id = event.get(
            "job_id",
            "default-job"
        )


        required_skills = event.get(
            "required_skills",
            []
        )


        table.put_item(

            Item={

                "job_id": job_id,

                "required_skills":
                required_skills

            }

        )


        return {

            "statusCode":200,

            "body":json.dumps({

                "message":
                "Job requirements stored",

                "job_id":
                job_id,

                "skills":
                required_skills

            })

        }


    except Exception as e:


        return {

            "statusCode":500,

            "body":json.dumps({

                "error":
                str(e)

            })

        }