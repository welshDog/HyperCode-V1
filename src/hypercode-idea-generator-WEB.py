"""
HyperCode Community Idea Generator - Web Interface (HTML/CSS/JS)

A beautiful, accessible interface for community to explore and vote on ideas.
Fully responsive, neurodivergent-friendly design.
"""

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HyperCode Idea Generator - Shape the Future</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', 'Helvetica', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            letter-spacing: 0.5px;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Header */
        header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        /* Category Selector */
        .selector {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-bottom: 40px;
        }

        .selector-group {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .selector-group label {
            display: block;
            font-weight: bold;
            margin-bottom: 10px;
            color: #333;
        }

        .selector-group select {
            width: 100%;
            padding: 10px;
            border: 2px solid #667eea;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            background-color: #f9f9f9;
        }

        /* Ideas Grid */
        .ideas-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }

        .idea-card {
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            border-left: 5px solid #667eea;
        }

        .idea-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }

        .idea-card.high-impact {
            border-left-color: #ff6b6b;
        }

        .idea-card.medium-impact {
            border-left-color: #ffa500;
        }

        .idea-card.low-impact {
            border-left-color: #4ecdc4;
        }

        .idea-title {
            font-size: 1.3rem;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }

        .idea-description {
            color: #666;
            margin-bottom: 15px;
            font-size: 0.95rem;
        }

        .idea-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 15px;
            font-size: 0.9rem;
        }

        .meta-tag {
            background: #f0f0f0;
            padding: 5px 10px;
            border-radius: 20px;
            color: #666;
        }

        .meta-tag.impact {
            background: #ffe5e5;
            color: #c92a2a;
        }

        .meta-tag.effort {
            background: #e5f4ff;
            color: #0066cc;
        }

        .meta-tag.community {
            background: #f0e5ff;
            color: #7c3aed;
        }

        .vote-section {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid #eee;
        }

        .vote-button {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.3s;
        }

        .vote-button:hover {
            background: #764ba2;
        }

        .vote-count {
            font-weight: bold;
            color: #667eea;
            font-size: 1.1rem;
        }

        /* Loading State */
        .loading {
            text-align: center;
            color: white;
            font-size: 1.2rem;
        }

        /* Stats Bar */
        .stats-bar {
            background: white;
            padding: 20px;
            border-radius: 10px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .stat {
            text-align: center;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
        }

        .stat-label {
            color: #666;
            font-size: 0.9rem;
            margin-top: 5px;
        }

        /* Footer */
        footer {
            text-align: center;
            color: white;
            margin-top: 50px;
            padding-top: 30px;
            border-top: 1px solid rgba(255,255,255,0.3);
        }

        /* Accessibility */
        @media (prefers-reduced-motion: reduce) {
            * {
                transition: none !important;
                animation: none !important;
            }
        }

        @media (max-width: 768px) {
            header h1 {
                font-size: 1.8rem;
            }

            .selector {
                grid-template-columns: 1fr;
            }

            .ideas-grid {
                grid-template-columns: 1fr;
            }

            .stats-bar {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        /* Focus visible for accessibility */
        button:focus-visible,
        select:focus-visible {
            outline: 3px solid #ffd700;
            outline-offset: 2px;
        }

        /* Dark mode support */
        @media (prefers-color-scheme: dark) {
            body {
                background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            }

            .idea-card,
            .selector-group,
            .stats-bar {
                background: #2d2d44;
                color: #e0e0e0;
            }

            .idea-title {
                color: #ffffff;
            }

            .idea-description {
                color: #b0b0b0;
            }

            .meta-tag {
                background: #404050;
                color: #d0d0d0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 HyperCode Idea Generator</h1>
            <p>Shape the future of programming for neurodivergent developers</p>
        </header>

        <div class="stats-bar">
            <div class="stat">
                <div class="stat-number" id="total-ideas">32</div>
                <div class="stat-label">Ideas Proposed</div>
            </div>
            <div class="stat">
                <div class="stat-number" id="total-votes">0</div>
                <div class="stat-label">Community Votes</div>
            </div>
            <div class="stat">
                <div class="stat-number" id="trending">-</div>
                <div class="stat-label">Trending Now</div>
            </div>
        </div>

        <div class="selector">
            <div class="selector-group">
                <label for="category">📚 Category</label>
                <select id="category">
                    <option value="">-- Select Category --</option>
                    <option value="language_design">🔤 Language Design</option>
                    <option value="features_tooling">🛠️ Features & Tooling</option>
                    <option value="community">🤝 Community</option>
                    <option value="accessibility">♿ Accessibility</option>
                </select>
            </div>

            <div class="selector-group">
                <label for="difficulty">⚡ Difficulty Level</label>
                <select id="difficulty">
                    <option value="">-- All Levels --</option>
                    <option value="beginner">Beginner (Low effort)</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced (High impact)</option>
                </select>
            </div>

            <div class="selector-group">
                <label for="sort">📊 Sort By</label>
                <select id="sort">
                    <option value="votes">Most Voted</option>
                    <option value="impact">Highest Impact</option>
                    <option value="effort">Lowest Effort</option>
                </select>
            </div>
        </div>

        <div id="ideas-container" class="ideas-grid">
            <div class="loading">Loading ideas...</div>
        </div>

        <footer>
            <p>💓 Built for the HyperCode movement | Powered by AI-powered recommendations</p>
            <p>All ideas are community-driven. Vote for your favorites!</p>
        </footer>
    </div>

    <script>
        // Simulated ideas data (would come from backend API)
        const ideas = [
            {
                id: 'ld_001',
                category: 'language_design',
                difficulty: 'beginner',
                title: '3D Spatial Mode Extension',
                description: 'Extend @ (2D mode) to support Z-axis for 3D spatial thinking.',
                impact: 'High',
                effort: 'Medium',
                community: 'Visual learners',
                votes: 0
            },
            // ... more ideas would be populated here
        ];

        // UI Functions
        function renderIdeas() {
            const container = document.getElementById('ideas-container');
            const category = document.getElementById('category').value;
            const difficulty = document.getElementById('difficulty').value;

            let filtered = ideas;

            if (category) {
                filtered = filtered.filter(i => i.category === category);
            }

            if (difficulty) {
                filtered = filtered.filter(i => i.difficulty === difficulty);
            }

            if (filtered.length === 0) {
                container.innerHTML = '<div class="loading">No ideas found. Try different filters!</div>';
                return;
            }

            container.innerHTML = filtered.map(idea => `
                <div class="idea-card ${idea.impact.toLowerCase()}-impact">
                    <div class="idea-title">${idea.title}</div>
                    <div class="idea-description">${idea.description}</div>
                    <div class="idea-meta">
                        <span class="meta-tag impact">Impact: ${idea.impact}</span>
                        <span class="meta-tag effort">Effort: ${idea.effort}</span>
                        <span class="meta-tag community">${idea.community}</span>
                    </div>
                    <div class="vote-section">
                        <button class="vote-button" onclick="vote('${idea.id}')">👍 Vote</button>
                        <span class="vote-count">${idea.votes}</span>
                    </div>
                </div>
            `).join('');
        }

        function vote(id) {
            const idea = ideas.find(i => i.id === id);
            if (idea) {
                idea.votes++;
                renderIdeas();
                updateStats();
            }
        }

        function updateStats() {
            const totalVotes = ideas.reduce((sum, i) => sum + i.votes, 0);
            document.getElementById('total-votes').textContent = totalVotes;
        }

        // Event Listeners
        document.getElementById('category').addEventListener('change', renderIdeas);
        document.getElementById('difficulty').addEventListener('change', renderIdeas);
        document.getElementById('sort').addEventListener('change', renderIdeas);

        // Initial render
        renderIdeas();
        updateStats();
    </script>
</body>
</html>
"""

# Write to file
if __name__ == "__main__":
    with open("hypercode-idea-generator.html", "w") as f:
        f.write(HTML)
    print("✅ Created hypercode-idea-generator.html")
    print("📱 Open in browser to see the interactive idea generator!")
