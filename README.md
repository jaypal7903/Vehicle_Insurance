# 🚗 Vehicle Insurance Prediction — End-to-End MLOps Project

An **end-to-end Machine Learning and MLOps project** for predicting vehicle insurance responses, designed with a production-oriented architecture covering **data ingestion, validation, transformation, model training, evaluation, model registry, prediction serving, containerization, and CI/CD deployment on AWS**.

The project demonstrates how a machine learning model can be transformed from a local development workflow into a **deployable, reproducible, and automated ML application**.

---

## 📌 Project Overview

The objective of this project is to build a complete machine learning pipeline that:

* Collects vehicle insurance data from **MongoDB Atlas**
* Performs data validation using a predefined schema
* Performs preprocessing and feature transformation
* Trains and evaluates machine learning models
* Stores trained models in **AWS S3**
* Provides a prediction API and web interface using **FastAPI**
* Containerizes the application using **Docker**
* Stores Docker images in **AWS ECR**
* Deploys the application on an **AWS EC2 Ubuntu server**
* Automates deployment using **GitHub Actions**
* Uses a **self-hosted GitHub Actions runner** on EC2
* Provides a separate `/training` route for model training

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │     GitHub Repo      │
                         │  Source Code + CI/CD │
                         └──────────┬──────────┘
                                    │
                                    │ Git Push
                                    ▼
                         ┌─────────────────────┐
                         │   GitHub Actions    │
                         │      CI/CD          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Self Hosted Runner │
                         │      AWS EC2        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       Docker        │
                         │   Build Container   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      AWS ECR        │
                         │  Docker Image Store │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      AWS EC2        │
                         │   Ubuntu Server     │
                         │                     │
                         │    FastAPI App      │
                         │      Port 5000      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                              Web Browser
```

---

# 🔄 Machine Learning Pipeline

```text
MongoDB Atlas
     │
     ▼
Data Ingestion
     │
     ▼
Data Validation
     │
     ▼
Data Transformation
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Model Pusher
     │
     ▼
AWS S3 Model Registry
     │
     ▼
Prediction Pipeline
     │
     ▼
FastAPI Application
```

---

# 🧰 Technology Stack

| Category               | Technology                  |
| ---------------------- | --------------------------- |
| Programming Language   | Python 3.10                 |
| Machine Learning       | Scikit-learn                |
| Data Processing        | Pandas, NumPy               |
| Data Visualization     | Matplotlib, Seaborn         |
| Development            | Jupyter Notebook            |
| API / Web Framework    | FastAPI                     |
| Template Engine        | Jinja2                      |
| Database               | MongoDB Atlas               |
| Cloud Platform         | AWS                         |
| Object Storage         | Amazon S3                   |
| Containerization       | Docker                      |
| Container Registry     | Amazon ECR                  |
| Compute                | Amazon EC2                  |
| CI/CD                  | GitHub Actions              |
| CI/CD Runner           | GitHub Self-Hosted Runner   |
| Version Control        | Git & GitHub                |
| Environment Management | Conda / Virtual Environment |
| Configuration          | YAML                        |
| Model Serialization    | Pickle                      |
| Logging                | Python Logging              |
| Exception Handling     | Custom Python Exception     |
| Operating System       | Ubuntu 24.04                |
| Deployment Port        | 5000                        |

---

# ✨ Key Features

### 📊 Data Management

* MongoDB Atlas integration
* Dataset ingestion from MongoDB
* Pandas DataFrame conversion
* Structured data access layer

### 🧪 Data Validation

* Schema-driven validation
* Dataset structure verification
* Feature and datatype validation
* Detection of missing/unexpected columns

### ⚙️ Data Transformation

* Automated preprocessing pipeline
* Feature transformation
* Reusable transformation objects
* Serialized preprocessing artifacts

### 🤖 Model Training

* Modular model training architecture
* Configurable training pipeline
* Model artifact generation
* Training workflow separated from prediction workflow

### 📈 Model Evaluation

* Model performance evaluation
* Configurable evaluation threshold
* Comparison between existing and newly trained models

### ☁️ Model Registry

* AWS S3 based model storage
* Model upload/download functionality
* Centralized model artifact management

### 🌐 Prediction API

* FastAPI-based prediction service
* Web-based prediction interface
* Static CSS/JavaScript assets
* Separate training endpoint

### 🐳 Containerization

* Dockerized application
* `.dockerignore` configuration
* Reproducible deployment environment
* Docker image stored in Amazon ECR

### 🔁 CI/CD

* GitHub Actions workflow
* Automated Docker image build
* Automated deployment workflow
* Self-hosted GitHub Actions runner on AWS EC2

---

# 📁 Project Structure

```text
vehicle-insurance-mlops/
│
├── .github/
│   └── workflows/
│       └── aws.yaml
│
├── .gitignore
├── .dockerignore
├── Dockerfile
├── README.md
├── requirements.txt
├── setup.py
├── pyproject.toml
├── template.py
├── demo.py
├── config/
│
├── notebook/
│   ├── mongoDB_demo.ipynb
│   └── EDA_and_Feature_Engineering.ipynb
│
├── static/
│   └── css/
│
├── templates/
│
├── src/
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   │
│   ├── configuration/
│   │   ├── mongo_db_connections.py
│   │   └── aws_connection.py
│   │
│   ├── data_access/
│   │   └── proj1_data.py
│   │
│   ├── entity/
│   │   ├── config_entity.py
│   │   ├── artifact_entity.py
│   │   ├── estimator.py
│   │   └── s3_estimator.py
│   │
│   ├── aws_storage/
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── utils/
│   │   └── main_utils.py
│   │
│   ├── constants/
│   │   └── __init__.py
│   │
│   ├── exception.py
│   └── logger.py
│
└── app.py
```

---

# 🧩 Modular ML Architecture

The project follows a modular architecture where each stage of the ML lifecycle is implemented as an independent component.

```text
                    Training Pipeline
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
   Data Ingestion   Data Validation   Data Transformation
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                    Model Trainer
                           │
                           ▼
                   Model Evaluation
                           │
                           ▼
                     Model Pusher
                           │
                           ▼
                       AWS S3
```

This separation makes the project easier to:

* Maintain
* Debug
* Test
* Extend
* Deploy
* Reuse

---

# 🗄️ MongoDB Atlas Integration

MongoDB Atlas is used as the project's data source.

### Workflow

```text
Dataset
   │
   ▼
MongoDB Atlas
   │
   ▼
MongoDB Connection
   │
   ▼
Data Access Layer
   │
   ▼
Key-Value Documents
   │
   ▼
Pandas DataFrame
```

### Configuration

Create a MongoDB Atlas cluster and configure the database user.

Set the MongoDB connection string as an environment variable:

### PowerShell

```powershell
$env:MONGODB_URL="mongodb+srv://<username>:<password>@<cluster-url>"
```

Verify:

```powershell
echo $env:MONGODB_URL
```

### Bash

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@<cluster-url>"
```

Verify:

```bash
echo $MONGODB_URL
```

> **Security:** Never hard-code the MongoDB URI or database password inside source code.

---

# 🧪 Exploratory Data Analysis

The `notebook/` directory contains the exploratory data analysis and feature engineering workflow.

Typical workflow:

```text
Raw Dataset
    │
    ▼
Data Exploration
    │
    ├── Missing Value Analysis
    ├── Data Type Analysis
    ├── Distribution Analysis
    ├── Outlier Analysis
    ├── Categorical Analysis
    └── Feature Relationships
    │
    ▼
Feature Engineering
    │
    ▼
Model-Ready Dataset
```

---

# 📝 Logging & Exception Handling

The application contains custom logging and exception handling mechanisms.

### Logging

The project uses Python's logging framework to record:

* Pipeline execution
* Component execution
* Errors
* Important processing events
* Debugging information

### Custom Exception Handling

A custom exception class is used to provide meaningful error information while preserving traceback details.

```text
Application
     │
     ├── Normal execution → Logging
     │
     └── Error
          │
          ▼
     Custom Exception
          │
          ▼
     Detailed Error Information
```

---

# 📥 Data Ingestion

The Data Ingestion component:

1. Reads configuration values
2. Connects to MongoDB Atlas
3. Retrieves documents
4. Converts MongoDB records into a Pandas DataFrame
5. Stores the ingested dataset as an artifact
6. Passes metadata to the next pipeline component

---

# ✅ Data Validation

The validation process uses a schema configuration file:

```text
config.schema.yaml
```

The schema contains information about:

* Expected columns
* Data types
* Dataset structure
* Feature definitions
* Target column

This allows the pipeline to detect changes in incoming data before model training.

---

# 🔄 Data Transformation

The Data Transformation component prepares raw data for machine learning.

```text
Validated Dataset
       │
       ▼
Feature Selection
       │
       ▼
Preprocessing
       │
       ▼
Feature Transformation
       │
       ▼
Transformed Dataset
       │
       ▼
Transformation Object
```

The transformation pipeline is serialized so that the **same preprocessing logic can be reused during prediction**.

---

# 🤖 Model Training

The Model Trainer component:

* Loads transformed training data
* Trains the machine learning model
* Evaluates training output
* Generates the trained model artifact
* Stores the model for subsequent evaluation

Model configuration and estimator definitions are separated from pipeline logic to improve maintainability.

---

# 📊 Model Evaluation

Model evaluation determines whether a newly trained model satisfies the required performance criteria.

The project defines an evaluation threshold:

```python
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
```

A new model is evaluated against the existing model before it is pushed to the model registry.

```text
New Model
    │
    ▼
Evaluation
    │
    ▼
Performance Comparison
    │
    ├── Better Model → Push to S3
    │
    └── Insufficient Improvement → Reject
```

---

# ☁️ AWS Architecture

AWS services used in the project:

```text
                    AWS Cloud
                       │
        ┌──────────────┼───────────────┐
        │              │               │
        ▼              ▼               ▼
      EC2             ECR             S3
        │              │               │
        │              │               │
   FastAPI App     Docker Image    ML Models
        │
        ▼
   Port 5000
```

### AWS Services

#### Amazon EC2

Used to host the production application.

#### Amazon ECR

Used as the private container registry for Docker images.

#### Amazon S3

Used for storing model artifacts and model registry files.

#### AWS IAM

Used for managing permissions and access credentials.

---

# 🪣 AWS S3 Model Registry

The trained model is stored in an S3-based model registry.

Configuration includes:

```python
MODEL_BUCKET_NAME = "my-model-mlopsproj"

MODEL_PUSHER_S3_KEY = "model-registry"
```

The S3 integration supports:

```text
Training
   │
   ▼
Model Artifact
   │
   ▼
Model Evaluation
   │
   ▼
Model Pusher
   │
   ▼
AWS S3
   │
   ▼
Prediction Pipeline
```

---

# 🐳 Docker

The application is containerized using Docker.

Build the image:

```bash
docker build -t vehicleproj .
```

Run locally:

```bash
docker run -p 5000:5000 vehicleproj
```

The application can then be accessed through:

```text
http://localhost:5000
```

### Why Docker?

* Consistent runtime environment
* Dependency isolation
* Reproducible deployments
* Simplified AWS deployment
* Easier CI/CD integration

---

# 📦 Amazon ECR

Docker images are stored in Amazon Elastic Container Registry.

Example repository:

```text
vehicleproj
```

Deployment workflow:

```text
Source Code
     │
     ▼
GitHub
     │
     ▼
GitHub Actions
     │
     ▼
Docker Build
     │
     ▼
Amazon ECR
     │
     ▼
Amazon EC2
     │
     ▼
Running Container
```

---

# 🔁 CI/CD Pipeline

The project implements automated CI/CD using GitHub Actions.

### Pipeline

```text
Developer
    │
    │ git push
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ▼
Self-Hosted Runner
    │
    ▼
Docker Build
    │
    ▼
Amazon ECR
    │
    ▼
EC2 Deployment
    │
    ▼
Vehicle Insurance Application
```

The workflow configuration is located at:

```text
.github/workflows/aws.yaml
```

---

# 🖥️ AWS EC2 Deployment

The application is deployed on an Ubuntu EC2 instance.

### EC2 Configuration

```text
Operating System : Ubuntu Server 24.04
Instance Type    : T2 Medium
Storage          : 30 GB
Application Port : 5000
```

Docker is installed on the EC2 instance:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker ubuntu
newgrp docker
```

Verify Docker:

```bash
docker --version
```

---

# 🔗 GitHub Self-Hosted Runner

The EC2 instance is configured as a GitHub self-hosted runner.

This allows GitHub Actions to execute deployment commands directly on the EC2 machine.

```text
GitHub Actions
      │
      ▼
Self-Hosted Runner
      │
      ▼
AWS EC2
      │
      ▼
Docker Container
```

Runner status can be verified from:

```text
GitHub
 → Repository
 → Settings
 → Actions
 → Runners
```

---

# 🔐 GitHub Secrets

The CI/CD workflow uses GitHub Repository Secrets for sensitive AWS configuration.

Required secrets:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
```

Secrets are referenced by the CI/CD workflow instead of storing credentials inside the repository.

> **Never commit AWS access keys, secret keys, MongoDB passwords, ****`.env`**** files, or private credentials to GitHub.**

---

# 🌐 Application

The deployed FastAPI application runs on:

```text
Port: 5000
```

### Main Application

```text
GET /
```

Provides the vehicle insurance prediction interface.

### Model Training

```text
/training
```

The training route can be used to trigger the model training pipeline.

### Production Endpoint

```text
http://<EC2-PUBLIC-IP>:5000
```

Replace `<EC2-PUBLIC-IP>` with the current public IP of the running EC2 instance.

---

# 🚀 Local Setup

## 1. Clone Repository

```bash
git clone <your-github-repository-url>

cd vehicle-insurance-mlops
```

---

## 2. Generate Project Template

Run:

```bash
python template.py
```

This creates the initial project structure.

---

## 3. Configure Local Package Installation

The project uses:

```text
setup.py
pyproject.toml
```

to configure the project as an installable Python package.

---

## 4. Create Conda Environment

```bash
conda create -n vehicle python=3.10 -y
```

Activate:

```bash
conda activate vehicle
```

---

## 5. Install Dependencies

Add required packages to:

```text
requirements.txt
```

Then install:

```bash
pip install -r requirements.txt
```

Verify:

```bash
pip list
```

The local project package should also be available in the environment.

---

# ⚙️ Environment Variables

Configure the following environment variables before running the application.

### MongoDB

```text
MONGODB_URL
```

### AWS

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
```

Example:

```bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-east-1"
```

For PowerShell:

```powershell
$env:AWS_ACCESS_KEY_ID="your-access-key"
$env:AWS_SECRET_ACCESS_KEY="your-secret-key"
$env:AWS_DEFAULT_REGION="us-east-1"
```

---

# ▶️ Running the Application

Start the FastAPI application:

```bash
python app.py
```

Or using Uvicorn:

```bash
uvicorn app:app --host 0.0.0.0 --port 5000
```

Open:

```text
http://localhost:5000
```

---

# 🧠 Training Pipeline

The complete training workflow can be executed through the training pipeline.

```text
MongoDB
   ↓
Data Ingestion
   ↓
Data Validation
   ↓
Data Transformation
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Pusher
   ↓
AWS S3
```

This design separates the training process from the prediction process and allows the trained model to be reused by the deployed application.

---

# 🔮 Prediction Pipeline

The prediction pipeline loads:

* Trained model
* Transformation/preprocessing object
* User-provided input

and produces the final prediction.

```text
User Input
    │
    ▼
FastAPI
    │
    ▼
Prediction Pipeline
    │
    ├── Load Transformation Object
    │
    ├── Transform Input
    │
    ├── Load Model
    │
    └── Generate Prediction
    │
    ▼
Prediction Result
```

---

# 🔒 Security Considerations

For production environments, the following improvements are recommended:

* Use **AWS IAM roles** instead of long-lived access keys where possible
* Restrict EC2 Security Group rules to trusted IP ranges
* Avoid `0.0.0.0/0` for administrative services
* Keep MongoDB network access restricted
* Store secrets in **AWS Secrets Manager / Parameter Store**
* Keep S3 buckets private whenever public access is unnecessary
* Never commit credentials to Git
* Rotate credentials periodically

---

# 📌 MLOps Concepts Demonstrated

This project demonstrates practical implementation of:

* Modular ML architecture
* Data ingestion pipelines
* Data validation
* Data transformation
* Feature engineering
* Model training
* Model evaluation
* Model versioning
* Model registry
* Cloud storage
* REST API deployment
* Docker containerization
* Container registry
* CI/CD automation
* Infrastructure deployment
* Environment configuration
* Logging
* Exception handling
* GitHub Actions
* Self-hosted CI/CD runners

---

# 📈 Project Workflow Summary

```text
                     DEVELOPMENT
                          │
                          ▼
                   Python Project
                          │
                          ▼
                  Data Exploration
                          │
                          ▼
                    ML Pipeline
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
        MongoDB Atlas              Local Testing
             │
             ▼
       Data Ingestion
             │
             ▼
       Data Validation
             │
             ▼
     Data Transformation
             │
             ▼
       Model Training
             │
             ▼
      Model Evaluation
             │
             ▼
        Model Pusher
             │
             ▼
          AWS S3
             │
             ▼
       Prediction API
             │
             ▼
           Docker
             │
             ▼
        Amazon ECR
             │
             ▼
          AWS EC2
             │
             ▼
        Live Application
             ▲
             │
      GitHub Actions
             ▲
             │
          Git Push
```

---

# 🎯 Future Improvements

Potential extensions for the project include:

* [ ] Add automated unit and integration tests
* [ ] Add test coverage reporting
* [ ] Add MLflow experiment tracking
* [ ] Add model performance dashboards
* [ ] Implement AWS Secrets Manager
* [ ] Implement IAM roles instead of access keys
* [ ] Add HTTPS using Nginx + SSL
* [ ] Add monitoring and application logging
* [ ] Add model drift detection
* [ ] Add automated model retraining
* [ ] Add model versioning
* [ ] Add production-grade database security
* [ ] Deploy using AWS ECS/EKS
* [ ] Add infrastructure as code using Terraform

---

# 💼 Skills Demonstrated

### Machine Learning

`Python` · `Pandas` · `NumPy` · `Scikit-learn` · `Feature Engineering` · `Model Evaluation`

### MLOps

`ML Pipeline` · `Model Registry` · `Artifact Management` · `Pipeline Automation` · `Configuration Management`

### Backend

`FastAPI` · `REST API` · `Jinja2` · `Prediction Pipeline`

### Cloud

`AWS EC2` · `AWS S3` · `AWS ECR` · `AWS IAM`

### DevOps

`Docker` · `GitHub Actions` · `CI/CD` · `Self-Hosted Runner`

### Database

`MongoDB Atlas` · `MongoDB Python Driver`

### Software Engineering

`Modular Architecture` · `Logging` · `Exception Handling` · `Environment Variables` · `Git`

---

# 👨‍💻 Author

**Jaypal**

AI & Data Science Student | Machine Learning | MLOps | Python

Interested in building production-oriented machine learning systems and deploying ML applications using cloud and DevOps technologies.

---

## ⭐ If you find this project useful

Consider giving the repository a **star ⭐** and exploring the implementation.

```text
Machine Learning → MLOps → Docker → CI/CD → AWS → Production Deployment
```
