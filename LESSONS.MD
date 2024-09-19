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
#### install aws cli and run
>>> aws configure

#### validate the template
aws cloudformation validate-template --template-body file://D:/DEVOPS/aws/01_cloud_formation/ec2_instance_template.yaml

#### create stack
aws cloudformation create-stack --stack-name MyNewStack1 --template-body file://ec2_instance_template.yaml