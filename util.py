import logging


def delit(a, b):
    try:
        a / b
        logging.info(f"asas{a} / {b}")
        return a / b
    except:
        logging.warning("saedw", exc_info=True)
        return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_test.log", encoding="utf-8",
                        format="%(asctime)s | %(levelname)s | %(messege)s")
    print(delit(3, 4))
    print(delit(3, 0))