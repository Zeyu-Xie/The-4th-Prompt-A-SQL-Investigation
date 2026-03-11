import numpy as np
import os
import pandas as pd
import base64
import random

SEEDS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "seeds")
RNG_SEED = 42
N = 1 + 1 * 2 + 1 * 2 * 3 + 1 * 2 * 3 * 2 + 1 * 2 * 3 * 2 * 3

rng = random.Random(RNG_SEED)


def random_base64(min_len=60, max_len=180):
    target_len = rng.randint(min_len, max_len)
    n_bytes = (target_len * 3 // 4) + 3
    raw_bytes = bytes([rng.getrandbits(8) for _ in range(n_bytes)])
    b64_str = base64.b64encode(raw_bytes).decode("utf-8")
    return b64_str[:target_len]


parent = np.zeros(N, dtype=int)
parent[0] = -1
idx = 0


def dfs(step, current):
    global idx
    if step == 4:
        return
    elif step == 3:
        for _ in range(3):
            idx += 1
            parent[idx] = current
            dfs(step + 1, idx)
    elif step == 2:
        for _ in range(2):
            idx += 1
            parent[idx] = current
            dfs(step + 1, idx)
    elif step == 1:
        for _ in range(3):
            idx += 1
            parent[idx] = current
            dfs(step + 1, idx)
    else:
        for _ in range(2):
            idx += 1
            parent[idx] = current
            dfs(step + 1, idx)


dfs(0, 0)

system_audits_inner = []

for id, parent_id in enumerate(parent):
    for i in range(91):
        system_audits_inner.append(
            {
                "id": id * 100 + i,
                "parent_id": parent_id * 100 + i if parent_id >= 0 else -2,
                "sha-256": random_base64(),
            }
        )


def generate_all_system_audits_inner():
    return system_audits_inner
