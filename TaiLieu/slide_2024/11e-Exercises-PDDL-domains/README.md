## AI&ML Course 2021/2022 - Lab 2: Deterministic Planning

This is Lab 2 of the AI&ML course 2021/2022.  

### PDDL Domain Examples

The folder contains four different PDDL examples, ordered by modelling complexity.

1) box: a STRIPS representation of the SitCalc exercise.
2) hanoi: the Towers-of-Hanoi problem, formulated as a planning problem.
3) blocksworld: this is probably the most famous planning problem from the 
International Planning Competion. It involves stacking a set of blocks.
4) logistics (mod.): this is a modified instance of the logistics problem from 
the International Planning Competition. It involves a truck to move packages 
between several locations.
5) miconic-ADL: a planning benchmark domain from the 2000
  International Planning Competition, which models a complex elevator
  transportation problem (created in cooperation with Schindler Lifts
  Inc), using complex logical operator preconditions.

### Call the Solver

In this folder, you can find a Linux executable of the FF planner. You can use
it to solve planning problems. To call the planner, just enter the terminal in 
the `pddl/` folder and run the following  command:

```bash
./ff -o 0-box/domain.pddl -f 0-box/problem.pddl
```
