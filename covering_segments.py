# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    
    segments = sorted(segments, key=attrgetter('end'))
    points.append(segments[0].end)
    
    for i in range(1, len(segments)):
        if segments[i].start <= points[-1]:
            pass
        else:
            points.append(segments[i].end)
            
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
