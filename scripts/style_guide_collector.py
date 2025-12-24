#!/usr/bin/env python3
"""
🎨 HyperCode Style Guide Feedback Collector

This script collects and analyzes feedback from the community to help shape
HyperCode's official style guide, with a focus on neurodivergent accessibility.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


class StyleGuideCollector:
    """🎨 Collects and analyzes style guide feedback from the community"""

    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.feedback_file = self.repo_path / "data" / "style_feedback.json"
        self.analysis_file = self.repo_path / "data" / "style_analysis.json"

        # 📊 Ensure data directory exists
        self.feedback_file.parent.mkdir(exist_ok=True)

        # 🧠 Initialize feedback storage
        self.feedback_data = self._load_feedback()

    def _load_feedback(self) -> Dict[str, Any]:
        """📂 Load existing feedback data"""
        if self.feedback_file.exists():
            with open(self.feedback_file, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return {
                "version": "1.0.0",
                "created_at": datetime.now().isoformat(),
                "feedback_entries": [],
                "analysis": {
                    "total_entries": 0,
                    "common_patterns": {},
                    "accessibility_insights": {},
                    "naming_preferences": {},
                    "formatting_preferences": {},
                },
            }

    def _save_feedback(self):
        """💾 Save feedback data"""
        self.feedback_data["updated_at"] = datetime.now().isoformat()

        with open(self.feedback_file, "w", encoding="utf-8") as f:
            json.dump(self.feedback_data, f, indent=2, ensure_ascii=False)

        print(f"✅ Feedback saved to {self.feedback_file}")

    def add_feedback(self, feedback: Dict[str, Any]) -> bool:
        """
        📝 Add new feedback entry

        Args:
            feedback: Dictionary containing feedback data

        Returns:
            bool: True if feedback was added successfully
        """
        try:
            # 🧠 Validate required fields
            required_fields = ["feedback_type", "examples", "user_experience"]
            for field in required_fields:
                if field not in feedback:
                    print(f"❌ Missing required field: {field}")
                    return False

            # 📊 Create feedback entry
            entry = {
                "id": len(self.feedback_data["feedback_entries"]) + 1,
                "timestamp": datetime.now().isoformat(),
                "feedback": feedback,
                "processed": False,
            }

            # ➕ Add to feedback list
            self.feedback_data["feedback_entries"].append(entry)

            # 🔄 Update analysis
            self._update_analysis(entry)

            # 💾 Save changes
            self._save_feedback()

            print(f"✅ Feedback entry #{entry['id']} added successfully")
            return True

        except Exception as e:
            print(f"❌ Error adding feedback: {e}")
            return False

    def _update_analysis(self, entry: Dict[str, Any]):
        """
        📊 Update analysis based on new feedback

        Args:
            entry: New feedback entry
        """
        feedback = entry["feedback"]
        analysis = self.feedback_data["analysis"]

        # 📈 Update total count
        analysis["total_entries"] += 1

        # 🎯 Track common patterns
        if "patterns" in feedback:
            for pattern in feedback["patterns"]:
                if pattern not in analysis["common_patterns"]:
                    analysis["common_patterns"][pattern] = 0
                analysis["common_patterns"][pattern] += 1

        # 🧠 Track accessibility insights
        if "accessibility_needs" in feedback:
            for need in feedback["accessibility_needs"]:
                if need not in analysis["accessibility_insights"]:
                    analysis["accessibility_insights"][need] = 0
                analysis["accessibility_insights"][need] += 1

        # 🏷️ Track naming preferences
        if "naming_preferences" in feedback:
            for pref_type, preferences in feedback["naming_preferences"].items():
                if pref_type not in analysis["naming_preferences"]:
                    analysis["naming_preferences"][pref_type] = {}

                for pref in preferences:
                    if pref not in analysis["naming_preferences"][pref_type]:
                        analysis["naming_preferences"][pref_type][pref] = 0
                    analysis["naming_preferences"][pref_type][pref] += 1

        # 📏 Track formatting preferences
        if "formatting_preferences" in feedback:
            for fmt_type, preferences in feedback["formatting_preferences"].items():
                if fmt_type not in analysis["formatting_preferences"]:
                    analysis["formatting_preferences"][fmt_type] = {}

                for pref in preferences:
                    if pref not in analysis["formatting_preferences"][fmt_type]:
                        analysis["formatting_preferences"][fmt_type][pref] = 0
                    analysis["formatting_preferences"][fmt_type][pref] += 1

    def analyze_feedback(self) -> Dict[str, Any]:
        """
        📊 Generate comprehensive analysis of all feedback

        Returns:
            Dict containing analysis results
        """
        analysis = {
            "summary": {
                "total_entries": len(self.feedback_data["feedback_entries"]),
                "processed_entries": sum(
                    1 for e in self.feedback_data["feedback_entries"] if e["processed"]
                ),
                "last_updated": self.feedback_data.get(
                    "updated_at", datetime.now().isoformat()
                ),
            },
            "top_patterns": self._get_top_items(
                self.feedback_data["analysis"]["common_patterns"], 10
            ),
            "top_accessibility_needs": self._get_top_items(
                self.feedback_data["analysis"]["accessibility_insights"], 10
            ),
            "naming_consensus": self._calculate_consensus(
                self.feedback_data["analysis"]["naming_preferences"]
            ),
            "formatting_consensus": self._calculate_consensus(
                self.feedback_data["analysis"]["formatting_preferences"]
            ),
            "recommendations": self._generate_recommendations(),
        }

        # 💾 Save analysis
        with open(self.analysis_file, "w", encoding="utf-8") as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False)

        return analysis

    def _get_top_items(self, items: Dict[str, int], limit: int) -> List[Dict[str, Any]]:
        """
        📊 Get top items from a frequency dictionary

        Args:
            items: Dictionary of item frequencies
            limit: Maximum number of items to return

        Returns:
            List of top items with counts and percentages
        """
        total = sum(items.values())
        sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)

        result = []
        for item, count in sorted_items[:limit]:
            percentage = (count / total * 100) if total > 0 else 0
            result.append(
                {"item": item, "count": count, "percentage": round(percentage, 1)}
            )

        return result

    def _calculate_consensus(
        self, preference_data: Dict[str, Dict[str, int]]
    ) -> Dict[str, Any]:
        """
        📊 Calculate consensus for preference categories

        Args:
            preference_data: Nested dictionary of preferences

        Returns:
            Dictionary with consensus analysis
        """
        consensus = {}

        for category, preferences in preference_data.items():
            if not preferences:
                continue

            total_votes = sum(preferences.values())
            top_choice = max(preferences.items(), key=lambda x: x[1])

            consensus[category] = {
                "top_choice": top_choice[0],
                "top_votes": top_choice[1],
                "total_votes": total_votes,
                "consensus_percentage": (
                    round((top_choice[1] / total_votes * 100), 1)
                    if total_votes > 0
                    else 0
                ),
                "all_options": preferences,
            }

        return consensus

    def _generate_recommendations(self) -> List[Dict[str, Any]]:
        """
        💡 Generate style guide recommendations based on feedback

        Returns:
            List of recommendations with rationale
        """
        recommendations = []
        analysis = self.feedback_data["analysis"]

        # 🧠 Accessibility recommendations
        if analysis["accessibility_insights"]:
            top_needs = self._get_top_items(analysis["accessibility_insights"], 5)
            for need in top_needs:
                if need["percentage"] >= 60:  # Strong consensus
                    recommendations.append(
                        {
                            "category": "accessibility",
                            "recommendation": f"Prioritize {need['item']} in style guide",
                            "rationale": f"{need['percentage']}% of users identified this as important",
                            "priority": (
                                "high" if need["percentage"] >= 80 else "medium"
                            ),
                        }
                    )

        # 🏷️ Naming convention recommendations
        if analysis["naming_preferences"]:
            for category, consensus in self._calculate_consensus(
                analysis["naming_preferences"]
            ).items():
                if consensus["consensus_percentage"] >= 70:
                    recommendations.append(
                        {
                            "category": "naming",
                            "recommendation": f"Use {consensus['top_choice']} for {category}",
                            "rationale": f"{consensus['consensus_percentage']}% consensus",
                            "priority": (
                                "high"
                                if consensus["consensus_percentage"] >= 85
                                else "medium"
                            ),
                        }
                    )

        # 📏 Formatting recommendations
        if analysis["formatting_preferences"]:
            for category, consensus in self._calculate_consensus(
                analysis["formatting_preferences"]
            ).items():
                if consensus["consensus_percentage"] >= 70:
                    recommendations.append(
                        {
                            "category": "formatting",
                            "recommendation": f"Use {consensus['top_choice']} for {category}",
                            "rationale": f"{consensus['consensus_percentage']}% consensus",
                            "priority": (
                                "high"
                                if consensus["consensus_percentage"] >= 85
                                else "medium"
                            ),
                        }
                    )

        # 🎯 Pattern recommendations
        if analysis["common_patterns"]:
            top_patterns = self._get_top_items(analysis["common_patterns"], 3)
            for pattern in top_patterns:
                if pattern["percentage"] >= 50:
                    recommendations.append(
                        {
                            "category": "patterns",
                            "recommendation": f"Standardize {pattern['item']} pattern",
                            "rationale": f"{pattern['percentage']}% of users mentioned this pattern",
                            "priority": "medium",
                        }
                    )

        return sorted(
            recommendations,
            key=lambda x: (x["priority"] == "high", x["priority"] == "medium"),
            reverse=True,
        )

    def import_github_issues(self, github_token: str = None) -> int:
        """
        📥 Import feedback from GitHub issues

        Args:
            github_token: GitHub API token (optional)

        Returns:
            Number of issues imported
        """
        try:
            # 🐙 This would integrate with GitHub API
            # For now, return placeholder
            print("🔧 GitHub integration not yet implemented")
            print(
                "📝 Please manually create issues using the style_feedback.md template"
            )
            return 0

        except Exception as e:
            print(f"❌ Error importing GitHub issues: {e}")
            return 0

    def generate_report(self, output_file: str = None) -> str:
        """
        📊 Generate comprehensive feedback report

        Args:
            output_file: Optional file to save report

        Returns:
            Report content as string
        """
        analysis = self.analyze_feedback()

        # 📝 Generate report
        report = f"""# 🎨 HyperCode Style Guide Feedback Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Total Feedback Entries:** {analysis['summary']['total_entries']}

## 📊 Summary

- **Total Entries:** {analysis['summary']['total_entries']}
- **Processed Entries:** {analysis['summary']['processed_entries']}
- **Last Updated:** {analysis['summary']['last_updated']}

## 🧠 Top Accessibility Needs

"""

        for need in analysis["top_accessibility_needs"][:5]:
            report += f"- **{need['item']}**: {need['count']} mentions ({need['percentage']}%)\n"

        report += "\n## 🏷️ Naming Convention Consensus\n\n"

        for category, consensus in analysis["naming_consensus"].items():
            report += f"### {category.replace('_', ' ').title()}\n"
            report += f"- **Recommended:** {consensus['top_choice']}\n"
            report += f"- **Consensus:** {consensus['consensus_percentage']}%\n\n"

        report += "## 📏 Formatting Consensus\n\n"

        for category, consensus in analysis["formatting_consensus"].items():
            report += f"### {category.replace('_', ' ').title()}\n"
            report += f"- **Recommended:** {consensus['top_choice']}\n"
            report += f"- **Consensus:** {consensus['consensus_percentage']}%\n\n"

        report += "## 💡 Recommendations\n\n"

        for i, rec in enumerate(analysis["recommendations"], 1):
            priority_emoji = (
                "🔴"
                if rec["priority"] == "high"
                else "🟡"
                if rec["priority"] == "medium"
                else "🟢"
            )
            report += f"{i}. {priority_emoji} **{rec['recommendation']}**\n"
            report += f"   - *Rationale:* {rec['rationale']}\n"
            report += f"   - *Priority:* {rec['priority']}\n\n"

        # 💾 Save report if requested
        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"📊 Report saved to {output_file}")

        return report

    def interactive_feedback(self):
        """
        🎯 Interactive feedback collection from command line
        """
        print("🎨 HyperCode Style Guide Feedback Collector")
        print("=" * 50)
        print("🧠 Help us create a better style guide for neurodivergent developers!")
        print()

        feedback = {}

        # 📋 Feedback Type
        print("📋 What type of feedback are you providing?")
        print("1. 🧠 Neurodivergent Accessibility")
        print("2. 📝 Code Formatting")
        print("3. 🏷️ Naming Conventions")
        print("4. 🎯 Structure Patterns")
        print("5. 💬 Comment Style")
        print("6. 🔤 Syntax Usage")
        print("7. 📊 Error Handling")
        print("8. 🧪 Testing Style")

        choice = input("\nEnter your choice (1-8): ").strip()
        feedback_types = {
            "1": "neurodivergent_accessibility",
            "2": "code_formatting",
            "3": "naming_conventions",
            "4": "structure_patterns",
            "5": "comment_style",
            "6": "syntax_usage",
            "7": "error_handling",
            "8": "testing_style",
        }

        feedback["feedback_type"] = feedback_types.get(choice, "other")

        # 📝 Examples
        print("\n📝 Share specific examples (good and bad):")
        print("✅ What works well (leave empty if none):")
        good_example = input("> ").strip()

        print("❌ What could be improved (leave empty if none):")
        bad_example = input("> ").strip()

        print("💡 Your suggestions (leave empty if none):")
        suggestions = input("> ").strip()

        feedback["examples"] = {
            "good": good_example,
            "bad": bad_example,
            "suggestions": suggestions,
        }

        # 🧠 Accessibility needs
        print("\n🧠 What accessibility needs are most important to you?")
        print(
            "(comma-separated, e.g., visual clarity, reduced cognitive load, clear structure)"
        )
        accessibility_needs = input("> ").strip()
        if accessibility_needs:
            feedback["accessibility_needs"] = [
                need.strip() for need in accessibility_needs.split(",")
            ]

        # 🏷️ Naming preferences
        print("\n🏷️ Variable naming preference:")
        print("1. snake_case (user_name)")
        print("2. camelCase (userName)")
        print("3. kebab-case (user-name)")
        print("4. Other")

        var_choice = input("Enter choice (1-4): ").strip()
        naming_prefs = {"1": "snake_case", "2": "camelCase", "3": "kebab-case"}
        feedback["naming_preferences"] = {
            "variables": [naming_prefs.get(var_choice, "other")]
        }

        # 📏 Formatting preferences
        print("\n📏 Indentation preference:")
        print("1. 2 spaces")
        print("2. 4 spaces")
        print("3. Tabs")

        indent_choice = input("Enter choice (1-3): ").strip()
        indent_prefs = {"1": "2_spaces", "2": "4_spaces", "3": "tabs"}
        feedback["formatting_preferences"] = {
            "indentation": [indent_prefs.get(indent_choice, "other")]
        }

        # 👤 User experience
        print("\n👤 About your experience (optional):")
        experience = input("How long have you used HyperCode? ").strip()
        background = input("Programming background? ").strip()

        feedback["user_experience"] = {
            "hypercode_experience": experience,
            "programming_background": background,
        }

        # ➕ Add feedback
        if self.add_feedback(feedback):
            print("\n✅ Thank you! Your feedback has been recorded.")
            print("🎉 You're helping make HyperCode better for everyone!")
        else:
            print("\n❌ Sorry, there was an error saving your feedback.")
            print("📧 Please try again or contact style@hypercode.dev")


def main():
    """🚀 Main entry point"""
    parser = argparse.ArgumentParser(
        description="🎨 HyperCode Style Guide Feedback Collector"
    )
    parser.add_argument("--repo-path", default=".", help="Path to HyperCode repository")
    parser.add_argument(
        "--interactive", action="store_true", help="Run interactive feedback collection"
    )
    parser.add_argument("--report", help="Generate feedback report to file")
    parser.add_argument(
        "--analyze", action="store_true", help="Analyze existing feedback"
    )
    parser.add_argument(
        "--import-github", help="Import feedback from GitHub (requires token)"
    )

    args = parser.parse_args()

    collector = StyleGuideCollector(args.repo_path)

    if args.interactive:
        collector.interactive_feedback()
    elif args.analyze:
        analysis = collector.analyze_feedback()
        print("📊 Analysis complete!")
        print(f"📝 Total entries: {analysis['summary']['total_entries']}")
        print(f"💡 Recommendations generated: {len(analysis['recommendations'])}")
    elif args.report:
        collector.generate_report(args.report)
    elif args.import_github:
        collector.import_github_issues(args.import_github)
    else:
        print("🎨 HyperCode Style Guide Feedback Collector")
        print("Use --help to see available options")
        print("\n🚀 Quick start:")
        print("python style_guide_collector.py --interactive")


if __name__ == "__main__":
    main()
