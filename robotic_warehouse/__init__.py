import gym
from .warehouse import Warehouse, RewardType, Action
import itertools

_sizes = {
    "tiny": (1, 3),
    "small": (2, 3),
    "medium": (2, 5),
    "large": (3, 5),
}

_perms = itertools.product(
    _sizes.keys(),
    range(1, 20),
)

for size, agents in _perms:
    # normal tasks
    gym.register(
        id=f"rware-{size}-{agents}ag-v0",
        entry_point="robotic_warehouse.warehouse:Warehouse",
        kwargs={
            "column_height": 8,
            "shelf_rows": _sizes[size][0],
            "shelf_columns": _sizes[size][1],
            "n_agents": agents,
            "msg_bits": 0,
            "sensor_range": 1,
            "request_queue_size": agents,
            "max_inactivity_steps": None,
            "max_steps": 500,
            "reward_type": RewardType.INDIVIDUAL,
        },
    )

    # single request tasks
    gym.register(
        id=f"rware-{size}-{agents}ag-onereq-v0",
        entry_point="robotic_warehouse.warehouse:Warehouse",
        kwargs={
            "column_height": 8,
            "shelf_rows": _sizes[size][0],
            "shelf_columns": _sizes[size][1],
            "n_agents": agents,
            "msg_bits": 0,
            "sensor_range": 1,
            "request_queue_size": 1,
            "max_inactivity_steps": None,
            "max_steps": 500,
            "reward_type": RewardType.INDIVIDUAL,
        },
    )

    # double requests compared to agents tasks
    gym.register(
        id=f"rware-{size}-{agents}ag-doublereq-v0",
        entry_point="robotic_warehouse.warehouse:Warehouse",
        kwargs={
            "column_height": 8,
            "shelf_rows": _sizes[size][0],
            "shelf_columns": _sizes[size][1],
            "n_agents": agents,
            "msg_bits": 0,
            "sensor_range": 1,
            "request_queue_size": agents * 2,
            "max_inactivity_steps": None,
            "max_steps": 500,
            "reward_type": RewardType.INDIVIDUAL,
        },
    )


def full_registration():
    _perms = itertools.product(
        range(1, 5), range(3, 10, 2), range(1, 20), range(1, 20), ["indiv", "global", "twostage"]
    )
    _rewards = {
        "indiv": RewardType.INDIVIDUAL,
        "global": RewardType.GLOBAL,
        "twostage": RewardType.TWO_STAGE,
    }

    for rows, cols, agents, req, rew in _perms:
        gym.register(
            id=f"rware-{rows}x{cols}-{agents}ag-{req}req-{rew}-v0",
            entry_point="robotic_warehouse.warehouse:Warehouse",
            kwargs={
                "column_height": 8,
                "shelf_rows": rows,
                "shelf_columns": cols,
                "n_agents": agents,
                "msg_bits": 0,
                "sensor_range": 1,
                "request_queue_size": req,
                "max_inactivity_steps": None,
                "max_steps": 500,
                "reward_type": _rewards[rew],
            },
        )
