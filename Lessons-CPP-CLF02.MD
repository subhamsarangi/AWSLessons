# AWS Certified Cloud Practitioner

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

## 02 Developer Tools
### 2.1 AWS CLI

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
### 2.2 AWS CDK
- cloud development kit in ts, python, node etc.
- powered by CloudFormation (generates templates as an intermediate step)
- has [CDK constructs](constructs.dev) (a large library of reusable components)
- has CLI
- Pipelines to setup CICD for CDK projects 
- ensures idempotency of infrastructures unlike SDK

#### Idempotency of infra
- In CDK: If you deploy the same infrastructure template twice, it won’t create new resources but will ensure the environment matches the template.
- In SDK: If you make two API calls to create an EC2 instance, you might end up with two instances unless you use safeguards like unique request identifiers.

#### install aws-cdk and deploy
[github link for hello-cdk](https://github.com/aws/aws-cdk)

`npm i -g aws-cdk`

`cdk bootstrap`

`cdk deploy`

`cdk destroy`

### 2.3 aws toolkit for VS Code
- aws explorer
- aws cdk explorer
- intellisense for ECS files
- create, debug, deploy serverless apps via SAM and CFN

### 2.4 aws access keys
- aka AWS credentials
- never push to a repo
- only 2 keys at a time having diff profile names
- can deactivate keys
- stored in ~/.aws/.credentials as a TOML file.
- use env vars AWS_SECRET_KEY, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION

### 2.5 aws documentation
- large. very.
- [link](doc.aws.amazon.com)

## 03 shared responsibility model
### Data vs Config
- **AWS CSP {security _OF_ the cloud}**
  - _software_ (compute, storage, db, networking)
  - _hardware_ (regions, zones, locations)
- **Customers {security _IN_ the cloud}**
  - _Managed services config_ (platforms, applications, IAM)
  - _Virtual infra config_ (OS, network, firewall)
  - _Data security config_ (all around encryption, traffic protection, customer data)

### Types of Customer responsibility
- On prem all: application, data, runtime, middleware, os, Virtualization, Servers, Storage, Networking)
- IaaS (all except Virtualization, Servers, Storage, Networking)
- PaaS (only the application and data)
- SaaS (nothing)

### Types of Customer responsibility: Alternate model
- **Customer responsibility**
  - SaaS (Content, usage, access policies)
  - PaaS (also deployment, app security)
  - IaaS (identity, operations, access and authentication, network sec, guest os, data & content)

- **CSP reponsibilty** (audit logging, networking, storage+encryption, hardened kernel+IPC, boot, hardware)


### Compute in AWS
- IaaS (EC2 bare metal: OS and hypervisor) (EC2 Virtual Machine: OS, container runtime) (ECS containers: config, deployment and storage of containers)
- PasS (ELastic Beanstalk: code, deployment strategies, configs)
- SasS (WorkDocs content collab: contents, file mgmt, access controls)
- FaaS (Lambda: code only)

### Level of Control
- Code > Containers > Runtime > OS

### Architecture
- Traditional/VM: EBS, EC2
- Microservice/Containers: Fargate, ECS, EKS
- Serverless/Functions: Lambda, Amplify

## 04 Compute

### Virtual machine
- EC2
  - highly configurable
  - AMI (amazon machine image) a VM config
  - backbone of AWS along with AWS Network.
- Lightsail
  - managed virtual server service
  - friendly EC2

### Containers
- ECS
  - container orchestration
  - cluster of servers on EC2 instances with Docker installed
- ECR
  - repository of container images
- Fargate
  - pay on demand per running container
  - no need to manually scale
- EKS
  - manged kubernetes service

### Serverless
- Lambda
  - function 
  - memory and time can be configured
  - pay per run

## 05 HPC (high performance computing)
- used for simulations, deep learning workloads
- runs on C5 instances
- install aws-parallelcluster using pip
- configure and create cluster using the `pcluster` cli

## 06 Edge and Hybrid computing
- Edge: to push workloads outside the cloud network
    - AWS Wavelength (launch in telecom datacenters), AWS LocalZones (edge datacenters outside Regions)
- Hybrid: to run workloads on both aws and on-prem
    - AWS Outposts (a rack of servers), VMWareCloud on AWS (om-prem using VMWare)

## 07 Cost and Capacity Management
- Cost: save money
- Capacity: demand of traffic
- EC2 spot instances, reserved instances, savings plan
- AWS Batch, AWS compute optimizer, EC2 ASG (autoscaling groups), ELB (elastic load balancer)
- AWS Elastic Beanstalk PaaS similar to Heroku

## 08 Storage services
- Block (EBS - ELastic Block Store,  OS has direct access)
- File (EFS - Elastic FIle Storage, network share, supports locks)
- Object (S3 - Simple Storage Service, no scaling limit, no worrying no locks)
- Hybrid (Storage Gateway, extends onprem)
- Backup (managed backup service for multiple services)
- CloudEndure (replicates data continuously)
- FSx (file system, linux, windows)

### 8.1 Snow family
- devices to move data physically OUT of the cloud.
- Snowcone 8-14TB, SnowballEdge 50-80TB, SnowMobile 100PB

### 8.2 S3
- has key, value, metadata, versionid
- buckets hold objects and folders
- size 0b to 5Tb
- S3 Storage Classes
  - default/standard: 99.99% availability, >=3 zones
  - intelligent tiering: uses ML
  - standard-IA - infrequent access, less available
  - One-zone-IA - 99.5% available, less durable, cheaper than standard-IA
  - glacier: can take minutes to hours. long-term cold storage
  - glacier deep archive: 12 hour retrieval time, lowest cost
- Features
  - can be set up to move an object to slower storage after a specific amount of time using Lifecycle rules
  - can be made into a static site
  - max 100 buckets

