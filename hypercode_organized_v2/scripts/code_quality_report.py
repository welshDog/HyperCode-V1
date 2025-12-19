"""
Code Quality Analysis for Hypercode Project

This script analyzes and reports on:
1. Documentation coverage
2. Test coverage
3. Code quality opportunities
"""

from typing import Any, Dict, List

from hypercode_db import CodeEntity, HypercodeDB


def get_undocumented_classes_priority(db: HypercodeDB) -> List[CodeEntity]:
    """Get undocumented classes sorted by importance (more methods = higher priority)."""
    return sorted(
        (
            c
            for c in db.entities
            if (
                c.type == "class"
                and hasattr(c, "methods")
                and c.methods
                and not (getattr(c, "docstring", "") or "").strip()
            )
        ),
        key=lambda x: len(x.methods),
        reverse=True,
    )


def get_least_tested_files(db: HypercodeDB) -> List[Dict[str, Any]]:
    """Get files with most code but least test coverage.

    Returns:
        List of dictionaries containing file test metrics, sorted by test ratio
    """
    file_metrics = [
        {
            "file": file,
            "test_count": sum(
                1
                for e in entities
                if e.type == "function" and e.name.lower().startswith("test_")
            ),
            "code_entities": len(
                [e for e in entities if e.type in ("function", "class")]
            ),
        }
        for file, entities in db.by_file.items()
        if (
            file.endswith(".py")
            and "test" not in file.lower()
            and "venv" not in file.lower()
            and any(e.type in ("function", "class") for e in entities)
        )
    ]

    return sorted(file_metrics, key=lambda x: (x["test_ratio"], -x["code_entities"]))


def find_getter_methods(db: HypercodeDB) -> List[Dict[str, Any]]:
    """Find get_ methods that could be converted to properties.

    Returns:
        List of dictionaries containing information about potential getter methods
        that could be converted to properties.
    """
    # Create a set of all function names for O(1) lookups
    function_set = {(e.name, e.file) for e in db.entities if e.type == "function"}

    potential_getters = []

    for entity in db.entities:
        if (
            entity.type == "function"
            and entity.name.startswith("get_")
            and len(entity.name) > 4
        ):  # Ensure there's more after "get_"
            # Check for corresponding setter
            potential_setter = entity.name.replace("get_", "set_", 1)
            has_setter = (potential_setter, entity.file) in function_set

            potential_getters.append(
                {
                    "name": entity.name,
                    "file": entity.file,
                    "lineno": entity.lineno,
                    "has_setter": has_setter,
                }
            )

    return potential_getters


def generate_code_quality_report(db_path: str = "HYPER_DATABASE.json"):
    """Generate a comprehensive code quality report."""
    print("Loading database for code quality analysis...")
    db = HypercodeDB(db_path)

    # 1. Documentation Analysis
    print("\n=== DOCUMENTATION ANALYSIS ===")
    undocumented = get_undocumented_classes_priority(db)
    print(f"\nTop 10 undocumented classes by complexity (out of {len(undocumented)}):")
    for i, cls in enumerate(undocumented[:10], 1):
        methods = (
            f"{len(cls.methods)} methods" if hasattr(cls, "methods") else "no methods"
        )
        print(f"{i}. {cls.name} ({methods}) in {cls.file}")

    # 2. Test Coverage Analysis
    print("\n=== TEST COVERAGE ANALYSIS ===")
    test_metrics = get_least_tested_files(db)
    print("\nTop 10 files needing test coverage (by code size and test ratio):")
    for i, tm in enumerate(test_metrics[:10], 1):
        print(f"{i}. {tm['file']}")
        print(
            f"   Code Entities: {tm['code_entities']}, Tests: {tm['test_count']}, "
            f"Test Ratio: {tm['test_ratio']:.1%}"
        )

    # 3. Code Quality Analysis
    print("\n=== CODE QUALITY SUGGESTIONS ===")
    getter_methods = find_getter_methods(db)
    print(f"\nFound {len(getter_methods)} classes with potential getter methods")
    print("\nTop candidates for @property conversion:")
    for i, item in enumerate(getter_methods[:10], 1):
        print(f"\n{i}. Class: {item['class']} (in {item['file']})")
        print(f"   Getters: {', '.join(item['getters'])}")
        # Show example of conversion
        for getter in item["getters"][:2]:  # Show first 2 getters as examples
            prop_name = getter[4:]  # Remove 'get_'
            print(f"     - Convert: {getter}() -> @property def {prop_name}")

    print("\n=== RECOMMENDED ACTIONS ===")
    print("1. Document core classes starting with the most complex ones")
    print("2. Add tests for files with high code complexity but low test coverage")
    print("3. Convert simple getter methods to @property decorators")
    print(
        "\nUse the interactive search in hypercode_db.py to explore specific findings."
    )


if __name__ == "__main__":
    generate_code_quality_report()
