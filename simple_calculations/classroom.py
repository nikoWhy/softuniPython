from math import floor

l = float(input())
w = float(input())

num_workspaces_rows = floor(l / 1.2)
num_workspace_colomns = floor((w-1) / 0.7

number_work_space = (num_workspace_colomns * num_workspaces_rows) - 3

print(number_work_space)