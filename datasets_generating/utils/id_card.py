import numpy as np
import uuid

RNG_SEED = 42
UUID_VERSION = 4
ARR_NUM_ID_CARDS = [1, 2, 3, 4, 5, 6]
PROB_NUM_ID_CARDS = [0.8, 0.19, 9e-3, 9e-4, 9e-5, 1e-5]

rng = np.random.default_rng(seed=RNG_SEED)


def random_uuid():
    return uuid.UUID(bytes=rng.bytes(length=16), version=UUID_VERSION)


def random_id_card(citizen_id: str, is_active: bool) -> object:
    card_id = random_uuid()
    citizen_id = citizen_id
    is_active = is_active
    return {"card_id": card_id, "citizen_id": citizen_id, "is_active": is_active}


def random_id_cards(citizen_id: str) -> list[object]:
    cards = []
    n = rng.choice(ARR_NUM_ID_CARDS, p=PROB_NUM_ID_CARDS)
    for _ in range(n - 1):
        cards.append(random_id_card(citizen_id=citizen_id, is_active=False))
    cards.append(random_id_card(citizen_id=citizen_id, is_active=True))
    return cards
