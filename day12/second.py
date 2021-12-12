from collections import defaultdict


def is_small_cave(node_name) -> bool:
    return node_name[0] >= 'a' and node_name not in ['start', 'end']


def is_part1_compliant(visited) -> bool:
    """
    >>> is_part1_compliant('start,A,b,A,b,A,c,A,end')
    True
    """
    last = visited[-1]
    if is_small_cave(last):
        if last in visited[:-1]:
            return False

    i = 0
    while i < len(visited) - 3:
        if visited[i] == visited[-2] and visited[i + 1] == visited[-1]:
            return False
        i += 1

    return True


def is_part2_compliant(visited) -> bool:
    last = visited[-1]

    if is_small_cave(last):
        small_caves = [n for n in visited if is_small_cave(n)]
        counting = defaultdict(lambda: 0)
        for cave in small_caves:
            counting[cave] += 1
        if len(counting) + 1 < sum(counting.values()):
            return False
    else:
        i = 0
        while i < len(visited) - 5:
            if visited[i] == visited[-3] and visited[i + 1] == visited[-2] and visited[i + 2] == visited[-1]:
                if sum([is_small_cave(visited[i]), is_small_cave(visited[i + 1]), is_small_cave(visited[i + 2])]) > 1:
                    return False
            i += 1

    return True


class Node:
    def __init__(self, name) -> None:
        self._name = name
        self._neighbours = []

    def add_edge(self, other):
        self._neighbours.append(other)

    def __str__(self):
        return self._name

    def all_routes_to_end(self, end, visited, rules):
        visited = list(visited)
        visited.append(str(self))

        if self is end:
            return [visited]

        if not rules(visited):
            return []

        ret = []
        for n in self._neighbours:
            for p in n.all_routes_to_end(end, visited, rules):
                ret.append(p)

        return ret


class Graph:
    """
    >>> g = Graph.from_list(['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']); len(g.all_routes_from_start_to_end(is_part1_compliant))
    10
    >>> g = Graph.from_list(['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']); len(g.all_routes_from_start_to_end(is_part2_compliant))
    36
    """

    def __init__(self) -> None:
        self._nodes = {}

    @classmethod
    def from_list(cls, edges) -> 'Graph':
        graph = Graph()
        for edge in edges:
            (b, e) = edge.strip().split('-')
            if b != 'end' and e != 'start':
                graph.add_edge(b, e)

            if e != 'end' and b != 'start':
                graph.add_edge(e, b)
        return graph

    def add_edge(self, node1, node2):
        if node1 not in self._nodes:
            self._nodes[node1] = Node(node1)

        if node2 not in self._nodes:
            self._nodes[node2] = Node(node2)

        self._nodes[node1].add_edge(self._nodes[node2])

    def all_routes_from_start_to_end(self, rules) -> list:
        start = self._nodes['start']
        end = self._nodes['end']

        return start.all_routes_to_end(end, [], rules)


if __name__ == '__main__':
    with open('input') as f:
        graph = Graph.from_list([line.strip() for line in f.readlines()])

        print('Part 1:', len(graph.all_routes_from_start_to_end(is_part1_compliant)))
        print('Part 2:', len(graph.all_routes_from_start_to_end(is_part2_compliant)))
