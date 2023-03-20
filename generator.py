import argparse
from math import cos, sin, radians
from typing import List, Tuple
from random import randint


def generate_astroid(
    angle_min: int, angle_max: int, r_min: int, r_max: int
) -> List[Tuple[int, int]]:
    total_angle = 0
    points = []
    while total_angle < 360:
        new_angle = randint(angle_min, angle_max)
        total_angle += new_angle
        new_r = randint(r_min, r_max)
        x = new_r * cos(radians(total_angle))
        y = new_r * sin(radians(total_angle))
        points.append((int(x) + r_max, int(y) + r_max))
    return points


def create_polygon_from_points(points: List[Tuple[int, int]]) -> str:
    polygon_str = '<polygon points="'
    for point in points:
        polygon_str += f"{point[0]},{point[1]} "
    polygon_str += '" style="stroke:white;stroke-width:3" />'
    return polygon_str


def save_astroid_to_file(polygon: str, output_file: str = "output.svg"):
    with open(output_file, "w") as f:
        f.write(
            '<svg version="1.1" width="300" height="200" xmlns="http://www.w3.org/2000/svg">\n'
        )
        f.write(polygon)
        f.write("\n")
        f.write("</svg>")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", type=int, default=1)
    parser.add_argument("-p", "--prefix", type=str, default="astroid")
    parser.add_argument("-a", "--angle-min", type=int, default=5)
    parser.add_argument("-A", "--angle-max", type=int, default=30)
    parser.add_argument("-r", "--radians-min", type=int, default=30)
    parser.add_argument("-R", "--radians-max", type=int, default=50)

    args = parser.parse_args()

    for i in range(args.count):
        points = generate_astroid(
            angle_min=args.angle_min,
            angle_max=args.angle_max,
            r_min=args.radians_min,
            r_max=args.radians_max
        )
        polygon = create_polygon_from_points(points)
        save_astroid_to_file(polygon, f"{args.prefix}{i}.svg")


