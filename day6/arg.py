
import argparse


def main():
    parser = argparse.ArgumentParser(description="Tiny Demo")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_greet = sub.add_parser("greet", help="say hello")
    p_greet.add_argument("--name", required=True)
     
    p_add = sub.add_parser("sum", help="sum all numbers")
    p_add.add_argument("a", type=int)
    p_add.add_argument("b", type=int)
    parser.print_help()

    args = parser.parse_args()

    if args.cmd == "greet":
        print(f"Hello, {args.name}!")
    elif args.cmd == "add":
        print(args.a + args.b)


if _name_ == "_main_":
    main()