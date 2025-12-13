"""
Flask web application for browsing research data.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from pathlib import Path
import sqlite3
from datetime import datetime
from typing import Dict, List, Any, Optional, Union, Tuple
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify,
    Response,
)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key-for-research-app")

# Configuration
BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "research.db"

# Ensure data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_db_connection() -> sqlite3.Connection:
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index() -> str:
    """Home page showing recent research entries."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT re.*, GROUP_CONCAT(t.name, ', ') as tag_list
    FROM research_entries re
    LEFT JOIN research_entry_tags ret ON re.id = ret.entry_id
    LEFT JOIN tags t ON ret.tag_id = t.id
    GROUP BY re.id
    ORDER BY re.date DESC, re.updated_at DESC
    LIMIT 10
    """)

    entries = [dict(row) for row in cursor.fetchall()]

    # Convert tag strings to lists
    for entry in entries:
        if entry["tag_list"]:
            entry["tags"] = [
                tag.strip() for tag in entry["tag_list"].split(",") if tag.strip()
            ]
        else:
            entry["tags"] = []
        del entry["tag_list"]

    # Get all unique tags for the sidebar
    cursor.execute("SELECT DISTINCT name FROM tags ORDER BY name")
    all_tags = [row[0] for row in cursor.fetchall()]

    conn.close()
    return render_template("index.html", entries=entries, all_tags=all_tags)


@app.route("/entry/<entry_id>")
def view_entry(entry_id: str) -> str:
    """View a specific research entry."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT re.*, GROUP_CONCAT(t.name, ', ') as tag_list
    FROM research_entries re
    LEFT JOIN research_entry_tags ret ON re.id = ret.entry_id
    LEFT JOIN tags t ON ret.tag_id = t.id
    WHERE re.id = ?
    GROUP BY re.id
    """,
        (entry_id,),
    )

    entry = cursor.fetchone()

    if not entry:
        flash("Entry not found", "error")
        return redirect(url_for("index"))

    # Convert to dict and process tags
    entry = dict(entry)
    if entry["tag_list"]:
        entry["tags"] = [
            tag.strip() for tag in entry["tag_list"].split(",") if tag.strip()
        ]
    else:
        entry["tags"] = []
    del entry["tag_list"]

    # Get all unique tags for the sidebar
    cursor.execute("SELECT DISTINCT name FROM tags ORDER BY name")
    all_tags = [row[0] for row in cursor.fetchall()]

    conn.close()
    return render_template("entry.html", entry=entry, all_tags=all_tags)


@app.route("/search")
def search() -> str:
    """Search for research entries."""
    query = request.args.get("q", "").strip()
    tag = request.args.get("tag", "").strip()

    if not query and not tag:
        return redirect(url_for("index"))

    conn = get_db_connection()
    cursor = conn.cursor()

    # Build the query
    sql = """
    SELECT DISTINCT re.*, GROUP_CONCAT(t.name, ', ') as tag_list
    FROM research_entries re
    LEFT JOIN research_entry_tags ret ON re.id = ret.entry_id
    LEFT JOIN tags t ON ret.tag_id = t.id
    """

    params = []
    conditions = []

    if query:
        conditions.append("""
        (re.topic LIKE ? OR re.summary LIKE ? OR re.details LIKE ?)
        """)
        search_term = f"%{query}%"
        params.extend([search_term, search_term, search_term])

    if tag:
        conditions.append("""
        re.id IN (
            SELECT ret.entry_id FROM research_entry_tags ret
            JOIN tags t ON ret.tag_id = t.id
            WHERE t.name = ?
        )
        """)
        params.append(tag)

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    sql += " GROUP BY re.id ORDER BY re.date DESC, re.updated_at DESC"

    cursor.execute(sql, params)
    entries = [dict(row) for row in cursor.fetchall()]

    # Convert tag strings to lists
    for entry in entries:
        if entry["tag_list"]:
            entry["tags"] = [
                tag.strip() for tag in entry["tag_list"].split(",") if tag.strip()
            ]
        else:
            entry["tags"] = []
        del entry["tag_list"]

    # Get all unique tags for the sidebar
    cursor.execute("SELECT DISTINCT name FROM tags ORDER BY name")
    all_tags = [row[0] for row in cursor.fetchall()]

    conn.close()

    return render_template(
        "search.html",
        entries=entries,
        all_tags=all_tags,
        search_query=query,
        selected_tag=tag,
    )


@app.route("/tags")
def list_tags() -> str:
    """List all tags with counts."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get tags with counts
    cursor.execute("""
    SELECT t.name, COUNT(ret.entry_id) as count
    FROM tags t
    LEFT JOIN research_entry_tags ret ON t.id = ret.tag_id
    GROUP BY t.name
    ORDER BY count DESC, t.name
    """)

    tags = [{"name": row[0], "count": row[1]} for row in cursor.fetchall()]

    # Get all unique tags for the sidebar
    cursor.execute("SELECT DISTINCT name FROM tags ORDER BY name")
    all_tags = [row[0] for row in cursor.fetchall()]

    conn.close()
    return render_template("tags.html", tags=tags, all_tags=all_tags)


@app.route("/api/entries")
def api_entries() -> jsonify:
    """API endpoint to get all entries in JSON format."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT re.*, GROUP_CONCAT(t.name, ',') as tags
    FROM research_entries re
    LEFT JOIN research_entry_tags ret ON re.id = ret.entry_id
    LEFT JOIN tags t ON ret.tag_id = t.id
    GROUP BY re.id
    ORDER BY re.date DESC, re.updated_at DESC
    """)

    entries = []
    for row in cursor.fetchall():
        entry = dict(row)
        entry["tags"] = (
            [tag for tag in entry["tags"].split(",") if tag] if entry["tags"] else []
        )
        entries.append(entry)

    conn.close()
    return jsonify(entries)


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple[str, int]:
    """Handle 404 errors."""
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e: Exception) -> tuple[str, int]:
    """Handle 500 errors."""
    return render_template("500.html"), 500


@app.template_filter("format_date")
def format_date_filter(date_str: str, format: str = "%B %d, %Y") -> str:
    """Format a date string."""
    if not date_str:
        return ""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime(format)
    except (ValueError, TypeError):
        return date_str


if __name__ == "__main__":
    # Create necessary directories
    templates_dir = Path(__file__).parent / "templates"
    templates_dir.mkdir(exist_ok=True)

    static_dir = Path(__file__).parent / "static"
    static_dir.mkdir(exist_ok=True)

    # Run the app
    app.run(debug=True, port=5000)
