# Cloud computing
## Amazon Web Services (AWS)
### AWS Global Infrastructure
#### AWS Regions
#### AWS Availability Zones (AZs)
#### Advantages of Cloud Computing and AWS


#### Cloud Types
```
- Public Cloud
General public to use, store and retrieve data from the cloud
- Private Cloud
Private Section of the cloud owned and operated by an organisation and its employees
- Hybrid Cloud
Combination of Public and Private Clouds or When 2 or more Organisation share a private cloud
```

#### Cloud as Services
```
- IaaS
Cloud provider offers essential compute, storage, networking resources, on a pay-as-you-go basis. IaaS allows developers to up & descale cloud resources.
- PaaS
Purchase a pre-build cloud infrastructure environment to develop and deploy an application
- SaaS
Connect to cloud-based application across the internet, Only reliable for customers data.
```

#### Data Centre
Data centre are physical facility that an organisation can use to house all their data, information and application. These data centre can be accessed from remote locations.

## AWS Services
- Elastic Compute Service `EC2`
  - Provides secure resizable compute capacity in the Cloud
  - Allows running of computing environment
- Simple Storage Service `S3`
  - Online backup
  - Archiving of data and applications
- Virtual Private Cloud `VPC`
  - A private cloud computing environment contained within a public cloud
- Internet Gateway `IG`
  - Allows for communication between VPC and the internet
- Route Tables `RT`
  - Allows for routing between subnets and CIDR within VPC
- Subnet `SN`
  - A range of IP address, which is assign to an instance within the IPv4 CIDR block.
- Network Access Control List `NACL`
  - A `stateless` firewall for controlling inbound and outbound traffic
- Security Groups `SG`
  - A `stateless` firewall for controlling the inbound and outbound traffic
- Cloudwatch `CW`
  -  A way to view data to monitor application and respond to performance changes and data logs and metrics
- Simple Notification Services `SNS`
  - Notification services, to notify user/s
- Load Balancers `LB` - `ALB` - `ELB` - `NLB`
  - Manage traffic load across multiple servers
- Autoscaling Groups `ASG`
  - Autoscale instance depending on traffic
- Amazon Machine Image `AMI`
  - Image of a OS with pre installed and configured dependencies


# Launch EC2 Instance

- ssh debugging
```
eval `ssh-agent`
ssh-add "keyfile.pem"
```
- update and upgrade system
- install nginx
- nginx enabled
- check the public globally

- install node correct version
- install required dependencies
- `app code` currently available on localhost
- task: `find out how to migrate/transfer/copy data from on prem to Cloud`
- npm install
- npm start


## Monolith Architecture
Monolith architecture/ 1-Tier architecture, is a type of architecture that contain the presentation, application logic and database, all on one server. This means that if the architecture is destroyed, then the presentation, application logic and database are all destroyed together. This is ideal for small application.

## 2 -tier Architecture
2-tier Architecture is a type of architecture that the presentation and application running on one server and the database of the application running on a second server, but the servers are connected on the same network.

### Launch a 2-Tier Architecture
```
Create a instance for your presentation/application logic servers
- assign it to an AMI,
- create a Security Group and Default Subnet
- add a Name both Security group and created instance

Create a instance for database server
- assign it to an AMI,
- create a Security Group and Default Subnet
- add a Name both Security group and created instance

Create a connection between instances
- On the App instance Security, Allow:
HTTP: port 80: Source: Anywhere
SSH: port 22: Source: My_IP
CustomTCP: port 3000: Source: Anywhere
CustomTCP: port 27017: Source: Database Security

- On the Database between instances
SSH: port 22 Source: My_IP
CustomTCP: port 27017: Source: App_Instance_IP


Execution & Installation of Commands
- Follow steps and execute the commands in provision script (Depending on instance)
- secure copy of certificate, files and directories need for software to run(node app dir)
- configuration of Nginx proxy file and Mongod.conf file

*OPTIONAL Create a AMI of created instances (makes terminating and re-building easier)
- On AWS/AMI , create a AMI image of your respective instances
- Apply the same configuration to AMI instances
```


![](img/Monitoring.png)

### What should we monitor
```
Application Server - EC2
CPU utilization
Number of requests
Firewall
```

### Questions of Monitoring
- How often we Monitor?
- What tools are we going to use to perform these tasks?
- Who will monitor?
- Who should be notified?

- What are the 4 Golden Signals of monitoring?
  - `Latency` = The time it takes to service a request
  - `Traffic` = The amount of activity in the application
  - `Errors` = The rate and type of request that are failing
  - `Saturation` = How full the service.(utilization metrics)


## Automate the Process
- Application Load Balancers
- Autoscaling Group
- Launch template config - How many instances at all times
  - 2 instances - Minimum = 2 & Maximum = 3
- Polices of scaling out and scaling in
- Scaling on Demand
    `Scaling up: increasing the size of your instances `
    `Scaling out: increasing the amount of instances `



### S3
- `aws s3 ls` = List buckets
- `aws --version` = Check version of AWS
- `aws configure` = To add our keys and config
- `aws s3 mb s3://bucket-name` = Create a bucket
- `aws s3 cp s3://bucket-name/ file.mb` = downloads copy of object of bucket into localhost
- `aws s3 sync s3://bucket-name/ filename.txt ` = sync the copy from localhost to cloud
- `aws s3 rm s3://bucket-name/filename.txt --recursive` = Remove content and objects within bucket
- `aws s3 rb s3://bucket-name/` = Remove the bucket in it entirety




#### AWSCLI
- AWSCLI can be used to create any `aws` recourses required.





#### AutoScaling and Load Balancing
Autoscaling Automatically adjusts the amount of computational resources based on the server Load
Load balancing distributes traffic between EC2 instances so that no one instance gets overwhelmed

![](img/scaling.png)


## Steps For Creating Auto scaling Group

### Tools and Features used when creating Auto Scaling Instances
```
Autoscaling Group: Launch Template or Launch configuration
ALB: Target group HTTP 80
AWS keys
VPC - Subnets - SG
Type of instances
AMI ID
EBS storage
```

### Create launch Template
- Add a Name and select `Auto Scaling Guidance` Option & add a Template Tag
- Add an AMI - Instance type (t2.mirco) - Key Pair
- Add a VPC and Security Group
- In `Advanced Details` add `User data` if needed (This provisions commands on launch)


### Create a Auto Scaling Groups
- Add a Auto Scaling group Name
- Add the launch template  
- Version: Latest
- Add a VPC - Subnet
- Attach Application Load Balancers
- Select Internet-Facing
- Enable Cloud Watch
- Choose a Desired/Minimum & Maximum capacity
- Target Tracking Policy/ Average CPU Utilization/ 30%
- Add Notification for Alerts
- Add Tags

##AWS Networking
- `Virtual Private Cloud` - VPC is an private virtual representation of a physical network
- `Internet Gateway` -  To allow connection between VPC and Internet
- `Route Table` - Controls the flow of traffic between instances and internet gateway
- `Security Groups` - Are stateful, meaning changes made to incoming rules `will` be applied to out going rule. Security groups work on a instances level
- `NACL` - Network Access Control Lists are stateless, meaning any changes made to incoming rules `won't` be applied to outgoing rules. NACL work on a network level



## Creating a Network
```
Step 1: VPC CIDR Block 10.108.0.0/16
Step 2: Internet gateway (IT)
  2.1: Attach the IG to VPC

Step 3: Route Table (RT)
  3.1: Allow 10.0.0.0/16
  3.2: Allow all 0.0.0.0/16

Step 4: Public subnet 10.108.1.0/24 - used for Node-app 3000
  4.1: Connect to our VPC
  4.2: Private Subnets 10.108.2.0/24 -used for Mongodb 27017
Step 5: Associate Subnets to RT
  5.1: Associate public Subnet to public RT
  5.2: Associate private Subnet to private RT

Step 6: Security Groups public and private with required rules for public and private subnets
  6.1: In DB Security Group:
    6.1.a: Port 22 and Port 27017 to Source: App Security Group
  6.2: In App Security Group:
    6.2.a: Port 80 and Port 3000 to Source: 0.0.0.0/16 ,
    6.2.b: Port 22 to Source: My_IP

Step 7: Create The Instances and add subnets and VPC
  7.1: App Instances, add Public subnet
    7.1.a: Ensure public IP is assigned
  7.2: DB Instances, add Private subnet
    7.2.a: Ensure public IP is not assigned

Step 8: Navigate to .ssh folder, execute Commands
  - eval `ssh-agent`
  - ssh-add {XXXXX.pem}
  - ssh -A ubuntu@APP-IP (To get into app instance)
  - ssh ubuntu@DB-IP
```
![](img/VPC.png)
