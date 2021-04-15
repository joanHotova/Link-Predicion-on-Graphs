# Link Predicion on Graphs, based on Data Structure
This project is part of "DATA TYPES-DATABASES-BIOLOGICAL DATABASE DESIGN" course of MSc Bioinformatics-Computational Biology of UoA.
Copyright(C) 2021 Ioanna Kiourti, Ioanna Soulioti, Joana Hotova

## Description
The project, based on a given edgelist that represents a graph, displays the link prediction score between two unlinked vertices.
The user needs to enter the file name and then choose which graph representation and metric wants to use. 
Also he can choose a specific number (k) of vertices-score to be displayed. The vertices-score are sorted in descending order.
There are three different representations and three different metrices, so he can try nine combinations. 

## Technology
The program is written in Python version 3.9.1 and developed on PyCharm (IDE). It runs on PyCharm (IDE) and terminal, too.

## Dependencies
Before you try to run the project, you need to install numpy 1.20.1 and python-math 0.0.1.

## Tests
The project has been tested on two graphs. 
The first one (graph1.txt) is a small graph and it is very useful to ensure that the represantations and metrices work fine. 
The second one (graph2.txt) is a greater graph and it helps to understand if the program can handle a big graph file and if it works fine. 

## How to use
In order to use the program, you need to unzip the project file (src) on your Desktop (or in any other path). 
Opening the project file, you can see the .py files and the two tested graph files. 
Also, you can see two more files, Report.pdf that describes the whole project and Requirements.txt.
In case you want to try your own graph file, you need to paste it in the unzipped project file.
Running: Go into the unzipped project file from your terminal and then write: 
>python main.py
OR
>py main.py
The program starts, and the user needs to follow the menu steps for a successful result.

## Contribution
Dimitrios Michail

## Authors 
Ioanna Kiourti, Ioanna Soulioti, Joana Hotova
