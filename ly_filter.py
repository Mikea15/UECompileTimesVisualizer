import sys

log_file = "Log.txt" if len(sys.argv) < 2 else sys.argv[1]
output_file = "result" if len(sys.argv) < 3 else sys.argv[2]

with open(log_file, "r", encoding="utf-8-sig") as file, open(output_file, "w", encoding="utf-8-sig") as ofile:
    for line in file.readlines():
        if "warning LNK" in line:
            continue
        if "Creating library" in line:
            continue
        if line.lstrip().startswith("["):
            continue
        if not line.strip():
            continue
        if line:
            ofile.write(line)

