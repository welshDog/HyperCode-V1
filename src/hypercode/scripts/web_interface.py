# scripts/web_interface.py
import json
import os
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_from_directory

app = Flask(__name__)

# Paths
BASE_DIR = Path(__file__).parent.parent
KNOWLEDGE_BASE_DIR = BASE_DIR / "data" / "processed" / "knowledge_base"
INDEX_FILE = KNOWLEDGE_BASE_DIR / "index.json"
DOCUMENTS_DIR = KNOWLEDGE_BASE_DIR / "documents"


# Load the knowledge base index
def load_index():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# Search function
def search_documents(query, limit=10):
    index = load_index()
    results = []
    query = query.lower()

    for doc in index["documents"]:
        try:
            doc_path = DOCUMENTS_DIR / f"{doc['id']}.json"
            with open(doc_path, "r", encoding="utf-8") as f:
                doc_data = json.load(f)
                content = str(doc_data).lower()
                if query in content:
                    results.append(
                        {
                            "id": doc["id"],
                            "file_name": doc["file_name"],
                            "relative_path": doc["relative_path"],
                            "file_type": doc["file_type"],
                            "snippet": (
                                (str(doc_data.get("content", ""))[:200] + "...")
                                if "content" in doc_data
                                else ""
                            ),
                        }
                    )
                    if len(results) >= limit:
                        break
        except Exception as e:
            print(f"Error processing {doc.get('file_name', 'unknown')}: {str(e)}")
            continue

    return results


# Routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/search")
def search():
    query = request.args.get("q", "")
    limit = min(int(request.args.get("limit", 10)), 50)  # Limit to 50 results max
    results = search_documents(query, limit)
    return jsonify(results)


@app.route("/api/document/<doc_id>")
def get_document(doc_id):
    doc_path = DOCUMENTS_DIR / f"{doc_id}.json"
    if doc_path.exists():
        with open(doc_path, "r", encoding="utf-8") as f:
            return jsonify(json.load(f))
    return jsonify({"error": "Document not found"}), 404


@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)


def create_template_if_not_exists():
    """Create the template directory and index.html if they don't exist"""
    os.makedirs("templates", exist_ok=True)
    os.makedirs("static", exist_ok=True)

    template_path = "templates/index.html"
    if not os.path.exists(template_path):
        with open(template_path, "w", encoding="utf-8") as f:
            f.write(
                """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>HyperCode Knowledge Base</title>
                <script src="https://cdn.tailwindcss.com"></script>
                <style>
                    .loader {
                        border: 3px solid #f3f3f3;
                        border-top: 3px solid #3498db;
                        border-radius: 50%;
                        width: 20px;
                        height: 20px;
                        animation: spin 1s linear infinite;
                        display: inline-block;
                        margin-left: 10px;
                        vertical-align: middle;
                    }
                    @keyframes spin {
                        0% { transform: rotate(0deg); }
                        100% { transform: rotate(360deg); }
                    }
                </style>
            </head>
            <body class="bg-gray-100 min-h-screen">
                <div class="container mx-auto px-4 py-8">
                    <div class="max-w-4xl mx-auto">
                        <h1 class="text-3xl font-bold mb-2 text-blue-800">HyperCode Knowledge Base</h1>
                        <p class="text-gray-600 mb-6">Search through code, documentation, and research</p>
                        
                        <div class="mb-8 bg-white p-6 rounded-lg shadow-md">
                            <div class="relative">
                                <input 
                                    type="text" 
                                    id="searchInput" 
                                    placeholder="Search documents (min 2 characters)..." 
                                    class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                    autocomplete="off"
                                >
                                <div id="searchStatus" class="absolute right-3 top-3 hidden">
                                    <div class="loader"></div>
                                </div>
                            </div>
                            <div class="mt-2 text-sm text-gray-500">
                                <span id="resultCount">0</span> results found
                            </div>
                        </div>
                        
                        <div id="results" class="space-y-4">
                            <div class="text-center text-gray-500 py-10">
                                <p>Enter a search term to begin</p>
                            </div>
                        </div>
                        
                        <div id="noResults" class="hidden text-center py-10">
                            <p class="text-gray-500">No results found. Try different keywords.</p>
                        </div>
                    </div>
                </div>

                <script>
                    let searchTimeout;
                    const searchInput = document.getElementById('searchInput');
                    const resultsDiv = document.getElementById('results');
                    const resultCount = document.getElementById('resultCount');
                    const noResultsDiv = document.getElementById('noResults');
                    const searchStatus = document.getElementById('searchStatus');
                    
                    // Debounce search
                    searchInput.addEventListener('input', (e) => {
                        const query = e.target.value.trim();
                        
                        // Clear previous timeout
                        clearTimeout(searchTimeout);
                        
                        if (query.length < 2) {
                            resultsDiv.innerHTML = `
                                <div class="text-center text-gray-500 py-10">
                                    <p>Enter at least 2 characters to search</p>
                                </div>`;
                            noResultsDiv.classList.add('hidden');
                            resultCount.textContent = '0';
                            return;
                        }
                        
                        // Show loading indicator
                        searchStatus.classList.remove('hidden');
                        
                        // Set new timeout
                        searchTimeout = setTimeout(() => {
                            performSearch(query);
                        }, 300);
                    });
                    
                    async function performSearch(query) {
                        try {
                            const response = await fetch(`/api/search?q=${encodeURIComponent(query)}&limit=20`);
                            const results = await response.json();
                            
                            // Update result count
                            resultCount.textContent = results.length;
                            
                            if (results.length === 0) {
                                resultsDiv.classList.add('hidden');
                                noResultsDiv.classList.remove('hidden');
                            } else {
                                resultsDiv.classList.remove('hidden');
                                noResultsDiv.classList.add('hidden');
                                
                                // Display results
                                resultsDiv.innerHTML = results.map(result => `
                                    <div class="bg-white p-4 rounded-lg shadow hover:shadow-md transition-shadow">
                                        <div class="flex justify-between items-start">
                                            <div>
                                                <h2 class="text-xl font-semibold text-blue-700">${escapeHtml(result.file_name)}</h2>
                                                <p class="text-sm text-gray-500 mb-2">${escapeHtml(result.relative_path)}</p>
                                            </div>
                                            <span class="px-2 py-1 text-xs rounded-full bg-blue-100 text-blue-800">
                                                ${result.file_type.toUpperCase()}
                                            </span>
                                        </div>
                                        <p class="mt-2 text-gray-700 line-clamp-2">${escapeHtml(result.snippet)}</p>
                                        <div class="mt-3 text-right">
                                            <a href="/api/document/${result.id}" 
                                               class="text-blue-600 hover:underline text-sm"
                                               target="_blank">
                                                View Full Document
                                            </a>
                                        </div>
                                    </div>
                                `).join('');
                            }
                        } catch (error) {
                            console.error('Search error:', error);
                            resultsDiv.innerHTML = `
                                <div class="bg-red-50 border-l-4 border-red-500 p-4">
                                    <div class="flex">
                                        <div class="flex-shrink-0">
                                            <svg class="h-5 w-5 text-red-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.28 7.22a.75.75 0 00-1.06 1.06L8.94 10l-1.72 1.72a.75.75 0 101.06 1.06L10 11.06l1.72 1.72a.75.75 0 101.06-1.06L11.06 10l1.72-1.72a.75.75 0 00-1.06-1.06L10 8.94 8.28 7.22z" clip-rule="evenodd" />
                                            </svg>
                                        </div>
                                        <div class="ml-3">
                                            <p class="text-sm text-red-700">Error performing search. Please try again.</p>
                                        </div>
                                    </div>
                                </div>`;
                        } finally {
                            searchStatus.classList.add('hidden');
                        }
                    }
                    
                    // Helper function to escape HTML
                    function escapeHtml(unsafe) {
                        if (!unsafe) return '';
                        return unsafe
                            .toString()
                            .replace(/&/g, "&amp;")
                            .replace(/</g, "&lt;")
                            .replace(/>/g, "&gt;")
                            .replace(/"/g, "&quot;")
                            .replace(/'/g, "&#039;");
                    }
                    
                    // Focus search input on page load
                    window.addEventListener('load', () => {
                        searchInput.focus();
                    });
                </script>
            </body>
            </html>
            """
            )


if __name__ == "__main__":
    create_template_if_not_exists()
    print("Starting HyperCode Knowledge Base server...")
    print(f"Access the interface at: http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)
