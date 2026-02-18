# Distributed_Transaction_Manager

Title or Subject: Design and implementation of a distributed transaction manager for relational SQL database. 
Introduction:
In todays Distributed computing landscape ensuring correctness of operation across multiple databases is crucial for reliable applications. When transaction span multiple database nodes, failures such as network interruption, system crashes or partial updates can compromise data integrity. The goal of this project is to develop a distributed Transaction manager that coordinates SQL transactions across multiple nodes, ensuring atomicity and consistency. 
A challenge in this project is managing distributed operations where each node executes part of transaction independently, which can lead to inconsistent states if not properly coordinated. to address this the project implements the two-phase commit (2Pc) protocol. 
The project will utilize multiple independent SQL database instances with a central coordinator service managing transaction flow. The project aims to demonstrate reliable distributed transaction management through careful logging, timeout handling and failure simulation. 

Learning Outcome:
Understand Distributed Transaction Fundamentals:

Two-Phase Commit Protocol proficiency:

Transaction Coordination and Failure Handling:

Software Design and Programming Skills




Project Timeline and Due date: March 13 – 6 weeks
Week1 [ 01/26 – 02/01]:
-	Conduct literature review on distributerd transaction manager for relational SQL database, challenges of distributed database and techniques for maintaining consistency across nodes 
-	Conduct literature review on Two phase commit
-	Set up environment 
o	Language, API database 
Week 2 [ 02/02 – 02/08]
-	Implement single-node transaction
Week3 [ 02/16 – 02/22]
-	Simulate multiple nodes 
-	Connect to each database
	
Week4 [ 02/23 – 02/29]:
-	Implement distributed transaction manager
Week 5 [03/01 – 03/07]:
-	Implement two phase commits 

Week 6 [03/08 – 03/13]
	- Handle failures 
	- PowerPoint 
	- Report 





Deliverables: 
• A central coordinator service (Distributed Transaction Manager)
• Multiple independent SQL database nodes (e.g., MySQL / PostgreSQL / SQLite instances)
• Ability to execute one logical transaction across multiple databases
• Guarantee:
•	Atomicity (all commit or all rollback)
•	Consistency across nodes

<img width="468" height="636" alt="image" src="https://github.com/user-attachments/assets/6c0d5808-b6a3-4748-99e7-c264434457aa" />
