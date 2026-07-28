import sys

# 1. *objects  -> "2026-07-24", "ERROR", "Database connection failed"
# 2. sep       -> " | "
# 3. end       -> " [LOGGED]\n"
# 4. file      -> sys.stdout
# 5. flush     -> True

print("2026-07-24", "ERROR", "Database connection failed", sep=" | ", end=" [LOGGED]\n", file=sys.stdout, flush=True)