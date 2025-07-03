from datetime import datetime

def main():
    now = datetime.now()
    print(f"✅ Daily job ran at {now.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
