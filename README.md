## Medallion Architecture Data Pipeline

![3-Layer System Architecture](https://github.com/abhishekshah25/3-layer-Medallion-Data-Pipeline/assets/147745895/9d496bd2-4530-42a7-9627-165e79cdf631)

### Overview

This project implements a data pipeline based on the Medallion Architecture, leveraging Microsoft Azure services including Azure Data Factory, Azure Databricks and DBT (Data Build Tool). The pipeline facilitates the efficient extraction, transformation and loading (ETL) of data, enabling seamless data processing & analysis.

### Architecture

The Medallion Architecture is a data processing framework designed to ensure scalability, reliability & maintainability of data pipelines. Our implementation utilizes the following components:

1. Azure Data Factory: Orchestrates and automates data movement & transformation workflows. It provides a visual interface for constructing, monitoring & managing data pipelines.

2. Azure Databricks: A unified analytics platform that integrates with Azure services for big data processing. Databricks clusters enable scalable data processing using Apache Spark and it's notebooks facilitate collaborative development and execution of data transformation logic.

3. DBT (Data Build Tool): A command line tool that enables the transformation of data in your warehouse more effectively. It is specifically designed for those who want to build code that's modular, verifiable & optimized for change.

![Data_Factory](https://github.com/abhishekshah25/3-layer-Medallion-Data-Pipeline/assets/147745895/c8c1d3a1-6874-4f99-b078-ecaac353490f)

### Features

1. Modular Pipeline: The pipeline is modular, allowing easy addition or modification of data sources, transformations and destinations.
   
2. Scalability: Leveraging Azure services ensures scalability to handle large volumes of data & varying workloads.
   
3. Automated Workflow: Data movement, transformation and orchestration are automated, thereby reducing manual intervention & potential errors.
 
4. Version Control: DBT enables version control of data transformation logic, promoting collaboration and ensuring reproducibility.

### Getting Started

To get started with this pipeline, follow the steps mentioned in the Procedure.pdf file. Feel free to make modifications in the data flow structure while creating your own pipeline. 
