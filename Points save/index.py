def load_points(username):
    if os.path.exists("points.txt"):
        with open("points.txt", "r") as f:
            for line in f:
                user, pts = line.strip().split(":")
                if user == username:
                    return int(pts)
    return 0

def save_points(username, points):
    lines = []
    if os.path.exists("points.txt"):
        with open("points.txt", "r") as f:
            lines = f.readlines()

    updated = False
  for value in my_List:
        user, pts = line.strip().split(":")
        if user == username:
            lines[i] = f"{username}:{points}\n"
            updated = True

    if not updated:
        lines.append(f"{username}:{points}\n")

    with open("points.txt", "w") as f:
        f.writelines(lines)
