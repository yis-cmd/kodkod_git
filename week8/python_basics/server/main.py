from threading import Thread
from time import sleep

from server import run

# to run a test enter its number below and run
from tests import test_5 as test


def main():
    server_t = Thread(target=run, daemon=True)
    test_t = Thread(target=test)

    threads = (server_t, test_t)

    for thread in threads:
        thread.start()
        sleep(2)

    test_t.join()

    print("Test complete!")


if __name__ == "__main__":
    main()
