# 41934 Advanced BIM - A2: OpenBIM Analysis

## Group 7
|Name|Study Number|
|----|------------|
|Emil Hjort Kristensen|S193924|
|Rasmus Olsen|S184506|

### Description of use case
We have chosen LCA as our use case with the goal of streamlining the process of making a Life Cycle Assessment (LCA) by incorporating Building Information Modeling (BIM). The idea of our script is to extract crucial data from a BIM model that enables the assessment of environmental impacts for each building part. Currently, the script can retrieve and present data for the area and volume of every wall type in an IFC model, provided that the information is defined. The script is a work in progress, with plans to expand the data retrieval for more building parts and include Environmental Product Declarations (EPDs) for the used materials. Ultimately, we aim to compile all the information into a comprehensive Excel file.

### Who is the use case for?
The use case is designed for sustainability engineers and construction companies engaged in LCA initiatives. The objective is to support professionals who are responsible for reporting on the environmental impacts of new constructions in compliance with the most recent added criteria within the Danish building code. 

### What disciplinary (non-BIM) expertise did you use to solve the use case?
We applied a combination of basic programming techniques alongside simple LCA principles to solve the use case. As aforementioned, the script remains a work in development. What we have produced represents the initial phase for a final product that fulfills our use case. 

### What IFC concepts did you use in your script (or would you use in the rest of the tool)?
For the use case, we used the IFC concept quantity sets to define the physical dimensions of objects in the IFC file. We did this so we could extract object quantities like area and volume for walls within the model. Additionally, we established a new dictionary that lists all the wall-related data we extracted.

### What disciplinary analysis does it require?
The disciplinary analysis required for the use case is a combination of basic programming skills and LCA knowledge to develop the script and streamline the process of making an LCA with the use of a BIM model. 

### What building elements are you interested in?
We are primarily interested in building elements that have the most substantial environmental impacts. These elements include walls, floors, ceilings, roofs, foundations, doors, windows, insulation, etc.  

### What (use cases) need to be done before you can start your use case?
The use case can begin once the general architectural concept model has been finalized, and the general material selection has been conducted, accompanied by relevant EPDs for the chosen materials.

### What is the input data for your use case?
We imagine the input data being material quantity and EPDs. 

### What other use cases are waiting for your use case to complete?
Building certifications as well as upholding the Danish building code. Since making an LCA is an iterative process, it will run parallel with other use cases.  

