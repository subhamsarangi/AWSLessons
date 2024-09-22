## 01 CLOUD FORMATION

[link to documentation]( https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html)

Example stack:

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  FirstBucket:
    Type: AWS::S3::Bucket
Outputs:
  FirstBucketDomain:
    Description: "hiiii"
    Value: !GetAtt FirstBucket.DomainName
```

[Using the CLI](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html)

## 02 AWS CLI

#### Create IAM user
With access key and secret key

#### install aws cli and configure
[download link](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

`aws configure`

#### validate the template
`aws cloudformation validate-template --template-body file://ec2_instance_template.yaml`

#### create stack
`aws cloudformation create-stack --stack-name MyNewStack1 --template-body file://ec2_instance_template.yaml
`
## 02 AWS CDK
- cloud developement kit in ts, python, node etc.
- powered by CloudFormation (generates templates as an intermediate step)
- has [CDK constructs](constructs.dev) (a large library of reusable components)
- has CLI
- Pipelines to setup CICD for CDK projects 
- ensures idempotency of infrastructures unlike SDK

#### Idempotency of infra
- In CDK: If you deploy the same infrastructure template twice, it won’t create new resources but will ensure the environment matches the template.
- In SDK: If you make two API calls to create an EC2 instance, you might end up with two instances unless you use safeguards like unique request identifiers.

#### install aws-cdk and deploy
`npm i -g aws-cdk`

`cdk bootstrap`

`cdk deploy`

`cdk destroy`

### aws toolkit
- aws exploer
- aws cdk explorer
- intellisense for ecs files
- create, debug, deploy serverless apps via SAM and CFN

### aws access keys
- aka aws credentials
- never push to a repo
- only 2 keys at a time having diff profile names
- can deactivate keys
- stored in ~/.aws/.credentials as a TOML file.
- use env vars AWS_SECRET_KEY, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION

### aws documentation
- large. very.
- [link] (doc.aws.amazon.com)