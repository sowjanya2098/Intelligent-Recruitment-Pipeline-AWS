import json
import boto3
import urllib.parse


textract = boto3.client("textract")
s3 = boto3.client("s3")


def lambda_handler(event, context):

    try:

        for record in event["Records"]:

            bucket_name = (
                record["s3"]["bucket"]["name"]
            )

            file_name = urllib.parse.unquote_plus(
                record["s3"]["object"]["key"]
            )


            response = textract.detect_document_text(

                Document={

                    "S3Object": {

                        "Bucket": bucket_name,

                        "Name": file_name

                    }

                }

            )


            extracted_text = []


            for item in response["Blocks"]:

                if item["BlockType"] == "LINE":

                    extracted_text.append(
                        item["Text"]
                    )


            resume_text = "\n".join(
                extracted_text
            )


            print(
                "Extracted Resume Text:"
            )

            print(resume_text)


            return {

                "statusCode":200,

                "body":json.dumps({

                    "message":
                    "Resume processed successfully",

                    "resume_text":
                    resume_text

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