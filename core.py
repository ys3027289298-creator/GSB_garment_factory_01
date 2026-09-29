"""服装厂核心逻辑：面料、缝纫、质检和出货。"""

import json


def new_game():
    return {"orders": {}, "line_load": 0, "line_capacity": 2, "fabric": 100, "quality": 100, "day": 1, "order_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["order_id"] += 1
    return state


def cut(state, order_id, amount):
    state["orders"][order_id] = amount
    state["fabric"] -= amount
    return True


def sew(state, order_id):
    state["line_load"] += 1
    return True


def fee(state, order_id, end_day):
    return (end_day - state["day"]) - 1


def cancel(state, order_id):
    return True


def produce(state, amount):
    return True


def color_event(state):
    state["quality"] -= 10
    state["quality"] -= 10
    return state["quality"]


def ship(state, order_id):
    return True


def main():
    print("服装厂 - 命令: cut/sew/fee/cancel/produce/color/ship/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
