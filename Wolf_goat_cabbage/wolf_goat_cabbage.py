from collections import deque
from .functions import dict_to_tuple, power_set, set_difference, tuple_difference


class Reader:
    def __init__(self):
        """
        Contains information about how many there are animals in total
        and what animal eat other animals.
        """
        self.animals = {"Human": 1}
        self.prey_of = {"Human": set([])}

    def read(self, file_name):
        """ Reads these information from standard txt format. """
        with open(file_name, "r") as f:
            for line in f.readlines():
                line_contents = line.split()
                if line_contents[0].isdigit():  # digit times animal added
                    num, animal = line_contents
                    num = int(num)
                    if animal not in self.animals:
                        self.animals[animal] = num
                        self.prey_of[animal] = set([])
                    else:
                        self.animals[animal] += num
                else:  # first element is string case
                    animal = line_contents[0]
                    if len(line_contents) == 1:  # single animal added
                        self.animals[animal] = 1
                        self.prey_of[animal] = set([])
                    else:  # animals eating other animals
                        if animal not in self.animals:
                            self.prey_of[animal] = set(line_contents[1:])
                        else:
                            for eatable_animal in line_contents[1:]:
                                self.prey_of[animal].add(eatable_animal)


class State_node:
    def __init__(self, animals, shore):
        """
        Contains information about animals
        which are with the human and about possible next states.
        """
        self.left_shore = shore
        self.contents = animals
        self.neighbours = []

    def is_allowed(self, all_animals, prey_of):
        """ Checks if current state is possible. """
        other_shore = set_difference(all_animals, self.contents)
        for animal in other_shore:
            for prey in prey_of[animal]:
                if prey in other_shore:
                    return False
        return True

    def get_neighbours(self, all_animals_state, prey_of, boat_size):
        """
        Returns all neighbours of a node that are allowed.

        A - all_animals_state aka full set aka start_state
        B - self.contents aka left_shore with the human
        C - other_shore
        C = A-B
        D - move aka set with b which are being moved
        E - updated move aka other_shore with moved b
        E = C+E
        """
        moves = power_set(self.contents, boat_size)
        for move in moves:
            other_shore = set_difference(all_animals_state, self.contents)
            move.update(other_shore)
            node = State_node(move, not self.left_shore)  # node is the new state after movement so shore is changed
            if node.is_allowed(all_animals_state, prey_of):
                self.neighbours.append(node)
        return self.neighbours

    def get_identifier(self, all_animals_state):
        """ Always returns contents of the left shore in tuple format. """
        if self.left_shore:
            return dict_to_tuple(self.contents)
        else:
            return dict_to_tuple(set_difference(all_animals_state, self.contents))


class Graph:
    def __init__(self):
        self.start_state = None
        self.prey_of = None
        self.contents = None
        self.path = None

    def add_start_state(self, file_name):
        """ Reads input file and gathers required data to start. """
        r = Reader()
        r.read(file_name)
        self.start_state = State_node(r.animals, True)
        self.prey_of = r.prey_of

    def construct(self, boat_size):
        """
        Tuple_to_node is used to connect identifier with node.
        Dist is used to remember from which node we entered to given node.
        """
        queue = deque([self.start_state])
        start_node_id = dict_to_tuple(self.start_state.contents)

        identifiers = {start_node_id: self.start_state}
        dist = {start_node_id: start_node_id}
        explored = set([])

        while queue:
            current = queue.popleft()
            current_id = current.get_identifier(self.start_state)
            if current_id not in explored:
                explored.add(current.get_identifier(self.start_state))
                for neighbour in current.get_neighbours(self.start_state, self.prey_of, boat_size):
                    neighbour_id = neighbour.get_identifier(self.start_state)
                    if neighbour_id not in explored:
                        identifiers[neighbour_id] = neighbour
                        dist[neighbour_id] = current_id
                        if len(neighbour_id) == 0:
                            return dist
                        queue.append(neighbour)
        return dist

    def get_path(self, boat_size):
        """ Functions used to retrieve path from the graph. """
        graph = self.construct(boat_size)
        path = []
        if () in graph:
            curr = ()
            while curr != graph[curr]:
                path.append(curr)
                curr = graph[curr]
            path.append(curr)
            self.path = path[::-1]
        else:
            raise Exception("No path")

    def visualise(self):
        """ Function used to visualise steps. """
        if self.path is not None:
            print("Start", end="\n\n")
            for i, step in enumerate(self.path):
                first_line = "" + str(step) + 5*" " +\
                             str(tuple(tuple_difference(dict_to_tuple(self.start_state.contents), step)))
                if i != len(self.path)-1:
                    print(first_line, end="\n\n")
                    print((len(first_line)//2) * " " + "|")
                    print((len(first_line) // 2) * " " + "v", end="\n\n")
                else:
                    print(first_line, end="\n\n")
                    print("Done! :)")
        else:
            raise Exception("No path")
