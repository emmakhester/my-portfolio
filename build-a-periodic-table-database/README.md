== Build a Periodic Table Database ==

This was a project I completed as part of the freeCodeCamp.org Relational Database Certification. I was tasked to create a Bash script to get information about chemical elements by querying a periodic table PostgreSQL database.

== element.sh ==

This script takes a single argument when called in the terminal.

The argument must be an atomic number, element symbol, or element name, and the script tests for each case using regular expressions.

Then, using the atomic number of the element specified by the user, it queries a PostgreSQL database to fetch the properties of that element and prints them in the terminal in readable format.

If the element is not present in the database, the script says as much and exits.

== periodic_table.sql ==

This is a PostgreSQL database dump for recreating the database I created and used in development and testing.
