## Medallion Architecture Data Pipeline

### Overview

This project implements a data pipeline based on the Medallion Architecture, leveraging Microsoft Azure services including Azure Data Factory, Azure Databricks, and DBT (Data Build Tool). The pipeline facilitates the efficient extraction, transformation and loading (ETL) of data, enabling seamless data processing and analysis.

### Architecture

The Medallion Architecture is a data processing framework designed to ensure scalability, reliability, and maintainability of data pipelines. Our implementation utilizes the following components:

1. Azure Data Factory: Orchestrates and automates data movement and transformation workflows. It provides a visual interface for constructing, monitoring, and managing pipelines.

2. Azure Databricks: A unified analytics platform that integrates with Azure services for big data processing. Databricks clusters enable scalable data processing using Apache Spark, and its notebooks facilitate collaborative development and execution of data transformation logic.

3. DBT (Data Build Tool): A command-line tool that enables the transformation of data in your warehouse more effectively. It's specifically designed for data analysts and engineers who want to build analytics code that's modular, verifiable, and optimized for change.

### Features

1. Modular Pipeline: The pipeline is modular, allowing easy addition or modification of data sources, transformations, and destinations.
   
2. Scalability: Leveraging Azure services ensures scalability to handle large volumes of data and varying workloads.
   
3. Automated Workflow: Data movement, transformation, and orchestration are automated, reducing manual intervention and potential errors.
 
4. Version Control: DBT enables version control of data transformation logic, promoting collaboration and ensuring reproducibility.

### Getting Started

To get started with the data pipeline, follow the steps mentioned in the Procedure.txt. Feel free to make modifications in the data flow structure while creating your own pipeline. 
