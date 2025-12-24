# 📊 Code Quality Metrics
*Generated: 2025-12-07T19:28:15.326585*

## 📈 Summary Statistics
- Total Entities: 7146
- Functions: 5259
- Classes: 1063
- Modules: 824
- Documentation Coverage: 73.4%
- High Complexity Functions: 125

## 🎯 Recommendations
### 📝 Improve Documentation
The following files have low documentation coverage:
- `hypercode\tests\test_tag_channels.py`: 0.0% documented (3 entities)
- `hypercode\tests\test_v01_core.py`: 0.0% documented (7 entities)
- `hypercode\scripts\web_interface.py`: 14.3% documented (7 entities)
- `hypercode\scripts\hc-manifest-lint.py`: 16.7% documented (6 entities)
- `hypercode\scripts\extract-manifests.py`: 20.0% documented (10 entities)
- ...and 163 more files

### 🔍 Refactor Complex Functions
Consider refactoring these high complexity functions:
- `hypercode\hypercode\build-hyper-database.py:179` - `generate_markdown_report()`
- `hypercode\scripts\build-hyper-database.py:165` - `generate_markdown_report()`
- `hypercode\scripts\enhanced_database_builder.py:393` - `_generate_recommendations()`
- `hypercode\scripts\style_guide_collector.py:101` - `_update_analysis()`
- `hypercode\scripts\style_guide_collector.py:230` - `_generate_recommendations()`
- ...and 120 more functions