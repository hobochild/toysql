# toysql [WIP]

I work with sql databases everyday but don't have deep understanding of how they work, this is an attempt to improve my understanding of their implementation. 

This is a dependency free, minimal clone of sql database written in python. I've intentionally tried to keep the code "simple" ignoring edge cases and optimizations so that anyone can read through and improve their understanding of how databases work.

## Questions:

* What format is data stored on disk?
* Joins implementation?
* Indexes implementation?
* How do you handle deleted pages (freenode list)?

## Inspiration:

- https://cstack.github.io/db_tutorial/
- https://github.com/erikgrinaker/toydb
- https://stackoverflow.com/questions/1108/how-does-database-indexing-work
- https://github.com/NicolasLM/bplustree
- https://notes.eatonphil.com/database-basics.html

## Current Features

1. Fixed table schema. (int, str, str)
2. Can insert rows - always indexed by primary key (int)
3. Can select all rows

TODOs:

- Where filter on pk
- Where filter on other columns
- create table (multiple tables)
- WAL with transactions + rollback
- Indexes (btree not b+tree implementation)

What I've learnt so far:

- Difference between Btrees & B+trees.
- Deleting nodes was trickier than I thought, because you now have any empty page in the middle of file, so you need to store a list of these references to empty pages in the same way you would store a list of references to actual values. 
- How tricky it is to debug things on a bit/byte level. After serialising pages by debugging skills diminish quickly.
- How tricky tree algorithms and recursions are to debug, day to day I'm working with much simpler data structures that are easier to reason about.
