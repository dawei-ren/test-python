import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s;%(levelname)s;%(message)s"
                    )


def test(a):
    logging.info("log: start: " + a)


def main():
    a = "Hello World"
    test(a)


if __name__ == '__main__':
    main()
