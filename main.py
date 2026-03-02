import argparse
from agent import summarize_data, ask_question, generate_insights

def main():
    parser = argparse.ArgumentParser(
        description="AI Analyst CLI - Analyze CSV files using AI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Summarize command
    summarize_parser = subparsers.add_parser("summarize")
    summarize_parser.add_argument("file", help="Path to CSV file")

    # Ask command
    ask_parser = subparsers.add_parser("ask")
    ask_parser.add_argument("file", help="Path to CSV file")
    ask_parser.add_argument("question", help="Question about dataset")

    # Insights command
    insights_parser = subparsers.add_parser("insights")
    insights_parser.add_argument("file", help="Path to CSV file")

    args = parser.parse_args()

    if args.command == "summarize":
        summarize_data(args.file)

    elif args.command == "ask":
        ask_question(args.file, args.question)

    elif args.command == "insights":
        generate_insights(args.file)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()