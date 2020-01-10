# AWS Cloudformation Example

This is a sample template for sam-app - Below is a brief explanation of what we have generated for you:

```bash
.
├── README.md                   <-- This instructions file
├── event.json                  <-- API Gateway Proxy Integration event payload
├── src                         <-- Source code for a lambda function
│   ├── __init__.py
│   ├── app.py                  <-- Lambda function code
│   ├── requirements.txt        <-- Lambda function requeriments
├── template.yaml               <-- SAM Template
└── tests                       <-- Unit tests
    └── unit
        ├── __init__.py
        └── test_handler.py
```

## Requirements
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) 
* [AWS CLI](https://docs.aws.amazon.com/es_es/cli/latest/userguide/install-cliv1.html) already configured with Administrator permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)

## Setup process

### Local development

**Invoking function locally using a local sample payload**

```bash
sam local invoke GetItemFunction --event event.json
```

**Invoking function locally through local API Gateway**

```bash
sam local start-api
```

## Deployment by console
### Create S3 Bucket in AWS
before execute the command lines you should create a s3 bucket, as the instructions below:

- [AWS S3 Docs](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)

### Command lines
**1) Compress the source code**
```bash
zip -r source.zip src/
```

**2) Upload the zipped code to AWS S3**
```bash
aws s3 cp source.zip s3://{BucketName}}/ 
```

**3) Package the AWS SAM Template**
```bash
aws cloudformation package --template template.yaml --s3-bucket {BucketName} --output-template template-export.yaml
```

**4) Deploy the clodformation stack**
```bash
aws cloudformation deploy --template-file template-export.yaml --stack-name example-dashboard --parameter-overrides DashboardName="ExampleDashboard" FunctionName="GetItemFunction" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --no-fail-on-empty-changeset
```

