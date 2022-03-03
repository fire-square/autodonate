from argparse import ArgumentParser

from aiohttp import web

from autodonate import app

def main():
    parser = ArgumentParser(description="Process some integers.")
    parser.add_argument("action", metavar="N", type=str)

    args = parser.parse_args()

    if args.action == "run":
        web.run_app(app)

if __name__ == "__main__":
    main()
