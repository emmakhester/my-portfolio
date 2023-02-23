== SQL COVID Data Exploration Project ==

This is a small project to serve as an example of what I am capable of doing using SQL, specifically for the purpose of data exploration.

The skills I utilize in this project include:

SELECT statements, WHERE clauses, GROUP BY statements, and the ORDER BY keyword;

Arithmetic operations in SQL statements to create new fields;

CAST() function for when columns in our table happen to be an inappropriate datatype (e.g., NVARCHAR instead of INT);

JOIN clauses;

PARTITION BY clauses (here, it is used to keep a rolling sum of vaccination counts by country);

CTEs (common table expressions) to make getting at certain calculations easier;

Temp tables for a similar purpose, as well as DROP IF EXISTS statements for the temp table;

I also take a closer look at the vaccination data to see if any preliminary conclusions can be drawn about specific countries' COVID testing regimes. 

This data allowed me to hypothesize about the testing practices of several countries, particularly Bosnia and Herzegovina, Bhutan, and South Korea.

Finally, I use several CREATE VIEW statements in order to have some virtual tables that I can use later for visualizations in Tableau or other BI programs.

== Files ==

SQL COVID Data Exploration.sql : The script that I wrote in SQL Server Management Studio.

CovidDeaths.xlsx : Excel workbook containing data about COVID deaths by location and date.

CovidVaccinations.xlsx : Excel workbook containing data about COVID vaccinations by location and date.
