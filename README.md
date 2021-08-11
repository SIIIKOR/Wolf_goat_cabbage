## Wolf_goat_cabbage
Program that solves Wolf, goat and cabbage problem for arbitrary number and type of animals|objects and boat size.
## usage
Program is run via riddle_solver.py script.


```bash
python3 riddle_solver.py -h
```

Program requires specific input file format. Look for them in examples folder.

## tldr;
line with "2 Goat" means that two goats are added to the starting state aka left shore.
line with "Cheese" means that one cheese is added to the starting state.
line with "Wolf Goat" means that wolf eats Goat. There maybe more than one animal which is being eaten for example "Wolf Goat Cat" means that Wolf eats Goat and Cat.

These lines are cumulative.
