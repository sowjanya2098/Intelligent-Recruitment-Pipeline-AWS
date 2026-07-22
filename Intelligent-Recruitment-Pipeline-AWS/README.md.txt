# Intelligent AI-Powered Recruitment Pipeline Using AWS

## Project Overview

This project is an AI-powered recruitment automation system built using AWS serverless services.

The system automatically processes resumes, extracts candidate skills, matches candidates with job requirements, calculates a match score, and sends recruiter notifications.

---

## Objective

The main objective is to reduce manual resume screening effort by automating:

- Resume processing
- Skill extraction
- Candidate matching
- Candidate ranking
- Recruiter notification

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon Textract
- Amazon Comprehend
- Amazon DynamoDB
- DynamoDB Streams
- Amazon SNS
- IAM
- Amazon CloudWatch

---

## Project Workflow

Resume Upload
|
↓
Amazon S3
|
↓
ResumeParser Lambda
|
↓
Amazon Textract
|
↓
Amazon Comprehend
|
↓
DynamoDB Candidates Table
|
↓
SkillNormalizer Lambda
|
↓
CandidateMatcher Lambda
|
↓
Match Score Generation
|
↓
DynamoDB Stream
|
↓
CandidateNotification Lambda
|
↓
Amazon SNS
|
↓
Recruiter Email


---

## Features

### Resume Processing
- Upload resumes to Amazon S3
- Extract text using Amazon Textract

### Skill Extraction
- Identify candidate skills using NLP

### Skill Normalization
- Removes duplicate skills
- Standardizes skill names

### Candidate Matching

The system compares candidate skills with job requirements and generates a match percentage.

Example:

Candidate:
Srikar Ryali

Score:
78%

Status:
Shortlisted


### Notification System

When a candidate is shortlisted, recruiters receive an email notification through Amazon SNS.

---

## DynamoDB Candidate Table

Table Name:
Candidates


Primary Key:

candidate_id


Attributes:

| Attribute | Description |
|---|---|
| candidate_id | Unique candidate identifier |
| name | Candidate name |
| skills | Candidate skills |
| experience | Candidate experience |
| location | Candidate location |
| match_score | Matching percentage |
| status | Shortlisted/Rejected |

---

## Project Outcome

The project successfully implements an end-to-end serverless recruitment pipeline using AWS services.

The final system can automatically analyze resumes, rank candidates, and notify recruiters.

---

## Author

Sowjanya Bandakavi