from random import random


def monte_carlo_integral(func, a, b, n):
    result = 0.0
    for _ in range(n):
        result += func(random.uniform(a, b))
    return (b-a)/float(n)*result


import scipy.integrate as integrate
from tabulate import tabulate
import numpy as np

func1 = lambda x : 1 / (x**2)
func2 = lambda x: 1 / np.sqrt(x**5+8)
func3 = lambda x: x**2 + 2*x

table = [
           ["1 / (x**2)", '(1, 2)', monte_carlo_integral(func1, 1, 2, 1000), integrate.quad(f1, 1, 2)[0]],
           ["1 / np.sqrt(x**5+8)", '(1,6)', monte_carlo_integral(func2, 1, 6, 1000), integrate.quad(f2, 1, 6)[0]],
           ["x**2 + 2*x", '(1, 22)', monte_carlo_integral(func3, 1, 22, 1000), integrate.quad(f3, 1, 22)[0]]
]

print(tabulate(table, headers=['Function', 'Interval', 'Monte Carlo', 'Scipy'], floatfmt=".8f", tablefmt="fancy_grid"))



def ball_volume(R, N):
  n = 0
  cube_volume = (2*R)**3
  for _ in range(N):
    x = random.uniform(-R, R)
    y = random.uniform(-R, R)
    z = random.uniform(-R, R)
    if x ** 2 + y ** 2 + z ** 2 <= R ** 2: #check if the ball includes the point
      n += 1
  return (n / N) * cube_volume

R = 5
numpy_volume = 4/3 * np.pi * R**3

table = [
           ["128", ball_volume(R, 128), numpy_volume],
           ["512", ball_volume(R, 512), numpy_volume],
           ["2048", ball_volume(R, 2048), numpy_volume],
           ["8192", ball_volume(R, 8192), numpy_volume],
           ["16384", ball_volume(R, 16384), numpy_volume]
]

print("kula o promieniu 5:")
print(tabulate(table, headers=['points', 'calculated volume', 'nupy volume'], floatfmt=".8f", tablefmt="fancy_grid"))



def cone_volume(R, H, N):
  n = 0
  cube_volume = (2*R)**2*H
  for _ in range(N):
    x = random.uniform(-R, R)
    y = random.uniform(-R, R)
    z = random.uniform(-R, R)
    if x ** 2 + y ** 2 <= ((z * R) / H) ** 2: #check if the cone includes the point
      n += 1
  return (n / N) * cube_volume

R = 10
H = 10
numpy_volume = 1/3 * np.pi * R**2 * H

table = [
           ["128", cone_volume(R, H, 128), numpy_volume],
           ["512", cone_volume(R, H, 512), numpy_volume],
           ["2048", cone_volume(R, H, 2048), numpy_volume],
           ["8192", cone_volume(R, H, 8192), numpy_volume],
           ["16384", cone_volume(R, H, 16384), numpy_volume]
]

print("stożek o wysokości 10 i promieniu podstawy 10:")
print(tabulate(table, headers=['points', 'calculated volume', 'nupy volume'], floatfmt=".8f", tablefmt="fancy_grid"))



def in_ball(x, y, z, R):
    return x ** 2 + y ** 2 + z ** 2 <= R ** 2

def in_cylinder(x, y, z, R, H):
    return x ** 2 + y ** 2 <= R ** 2 and z >= -H / 2 and z <= H / 2

def ball_cylinder_difference_volume(R_ball, R_cylinder, H, N):
  n = 0
  block_volume = (2*R_ball)**3
  for _ in range(N):
    x = random.uniform(-R, R)
    y = random.uniform(-R, R)
    z = random.uniform(-R, R)
    if in_ball(x, y, z, R_ball) and not in_cylinder(x, y, z, R_cylinder, H): #check if point is in the ball and is not in the cylinder
      n += 1
  return (n / N) * block_volume

R_ball = 10
R_cylinder = 3
H = 6
numpy_volume = 4/3 * np.pi * R_ball**3 - np.pi * R_cylinder ** 2 * H

table = [
           ["128", ball_cylinder_difference_volume(R_ball, R_cylinder, H, 128), numpy_volume],
           ["512", ball_cylinder_difference_volume(R_ball, R_cylinder, H, 512), numpy_volume],
           ["2048", ball_cylinder_difference_volume(R_ball, R_cylinder, H, 2048), numpy_volume],
           ["8192", ball_cylinder_difference_volume(R_ball, R_cylinder, H, 8192), numpy_volume],
           ["16384", ball_cylinder_difference_volume(R_ball, R_cylinder, H, 16384), numpy_volume]
]

print("bryła będąca różnicą kuli o promieniu 10 i walca o wysokości 6 i promieniu podstawy 3:")
print(tabulate(table, headers=['points', 'calculated volume', 'nupy volume'], floatfmt=".8f", tablefmt="fancy_grid"))