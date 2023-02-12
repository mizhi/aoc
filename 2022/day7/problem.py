from functools import reduce

class FSObject:
    def __init__(self, fs_name = "/", fs_type = "dir", fs_size = None):
        self.fs_name = fs_name
        self.fs_type = fs_type
        self.fs_parent = None
        self.fs_size = fs_size


        if fs_type == "dir":
            self.fs_contents = {}

    @property
    def parent(self):
        return self.fs_parent

    def size(self):
        if self.fs_type == "file":
            return self.fs_size

        if self.fs_size is not None:
            return self.fs_size

        total_size = 0
        for fso in self.fs_contents.values():
            total_size += fso.size()

        self.fs_size  = total_size
        return total_size

    def add_entry(self, fso):
        if self.fs_type != "dir":
            raise "Can't add objects to non-directory objects"

        self.fs_contents[fso.fs_name] = fso
        fso.fs_parent = self

    def __repr__(self):
        return "\n".join(self.__recursive_repr__(0))

    def __recursive_repr__(self, depth = 0):
        prefix = depth * " " + "- "

        if self.fs_type == "file":
            return [prefix + f"{self.fs_name} (file, size={self.fs_size})"]

        lines = [prefix + f"{self.fs_name} (dir)"]
        for (name, fso) in self.fs_contents.items():
            lines.extend(fso.__recursive_repr__(depth + 1))

        return lines

fs_root = FSObject()
current_node = fs_root
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()

        # each line has at least two tokens
        # the first token can be used to know the context
        # the second token contains the contextual details
        (context, details) = line.split(" ", maxsplit=1)

        if context == "$": # this is a command
            command = details.split()
            (command, params) = command[0], command[1:]
            if command == "cd":
                subdir = params[0]
                if subdir == "/":
                    current_node = fs_root
                elif subdir == "..":
                    current_node = current_node.fs_parent
                else:
                    current_node = current_node.fs_contents[subdir]
            elif command == "ls": # ls doesn't actually do anything right now
                pass
        elif context == "dir": # this is a directory listing
            new_fso = FSObject(details)
            current_node.add_entry(new_fso)
        else: # is an integer representing filesize
            new_fso = FSObject(details, fs_type="file", fs_size=int(context))
            current_node.add_entry(new_fso)

def gather_dirs(root):
    if root.fs_type == "file":
        return []

    dirs = []
    for fso in root.fs_contents.values():
        dirs.extend(gather_dirs(fso))

    dirs.append(root)

    return dirs

all_dirs = gather_dirs(fs_root)

# problem 1, get all directories below 100000
total_sum = reduce(
    lambda acc, x: acc + x.size(),
    [fso for fso in all_dirs if fso.size() <= 100000],
    0)
print(total_sum)

# problem 2, find directory to delete to allow update
# to proceed
MAX_DISK_SIZE = 70000000
UPDATE_SIZE_REQUIRED = 30000000

sorted_all_dirs = sorted(all_dirs, key=FSObject.size)

free_space = MAX_DISK_SIZE - fs_root.size()
space_needed = UPDATE_SIZE_REQUIRED - free_space

candidate = None
for fso in sorted_all_dirs:
    if fso.size() >= space_needed:
        candidate = fso
        break

print(candidate.fs_name, candidate.size())
