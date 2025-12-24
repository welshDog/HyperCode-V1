"""
Quick DB connectivity check using the canonical database_utils helpers.
Run manually or in CI before heavier tests.
"""

from database_utils import check_db_connection, get_db_stats


def main():
    ok = check_db_connection()
    print(f"DB connection: {'OK' if ok else 'FAILED'}")
    if ok:
        stats = get_db_stats()
        print("DB stats:", stats)


if __name__ == "__main__":
    main()
