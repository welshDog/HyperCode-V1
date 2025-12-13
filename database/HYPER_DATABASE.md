# 🗃️ HYPER CODE DATABASE
*Generated: 2025-12-07T19:28:13.406717*
*Scan Time: 7146 entities in 1021 files*

## 📊 Health Snapshot
| Metric | Value |
|--------|-------|
| **Files Scanned** | 1021 |
| **Total Entities** | 7146 |
| **Functions** | 5259 |
| **Classes** | 1063 |
| **Documentation** | 5242/7146 (73.4%) |
| **High Complexity** | 125 |

## 🏗️ Project Structure
```
data\cli_main.py:
  function: cli (line 25)
  function: database (line 42)
  function: init (line 48)
  function: reset (line 61)
  function: status (line 82)
  function: research (line 115)
  function: auto_research (line 126)
  function: run (line 147)
  function: process_papers (line 172)
  function: process_all (line 199)
  function: agents (line 227)
  function: knowledge (line 260)
  function: nodes (line 268)
  function: relationships (line 308)
  function: graph (line 350)
  function: system (line 404)
  function: version (line 410)
  function: health (line 429)
data\db.py:
  class: DatabaseConfig (line 21)
  function: create_db_engine (line 59)
  function: set_sqlite_pragma (line 83)
  function: init_db (line 108)
  function: get_db (line 124)
  function: get_db_context (line 130)
  function: close_db (line 151)
  function: check_db_connection (line 161)
  function: get_db_stats (line 173)
  function: db_cli (line 202)
  function: init (line 208)
  function: reset (line 216)
  function: stats (line 225)
  function: migrate (line 235)
data\models.py:
  class: ResearchPaper (line 35)
  class: ResearchAgent (line 67)
  class: ResearchTask (line 99)
  class: KnowledgeNode (line 141)
  class: KnowledgeRelationship (line 187)
  class: ConflictRecord (line 217)
  class: ResearchMetrics (line 243)
data\research_agent.py:
  class: AgentType (line 31)
  class: TaskStatus (line 45)
  class: TaskResult (line 54)
  class: BaseResearchAgent (line 67)
  function: __init__ (line 73)
  function: execute (line 81)
  function: log_execution (line 85)
  class: DocumentRetrievalAgent (line 103)
  function: execute (line 110)
  class: FilteringAgent (line 159)
  function: execute (line 166)
  class: SummarizationAgent (line 203)
  function: execute (line 210)
  class: EntityExtractionAgent (line 246)
  function: execute (line 254)
  class: RelationshipExtractionAgent (line 292)
  function: execute (line 299)
  class: SchemaAlignmentAgent (line 336)
  function: execute (line 344)
  class: ConflictResolutionAgent (line 388)
  function: execute (line 396)
  class: EvaluationAgent (line 438)
  function: execute (line 449)
  class: ControllerAgent (line 491)
  function: __init__ (line 499)
  function: register_agent (line 503)
  function: execute (line 507)
  class: AutoResearchManager (line 560)
  function: __init__ (line 566)
  function: initialize_agents (line 571)
  function: process_research_task (line 590)
  function: auto_research_mode (line 610)
hypercode-research\scripts\ai-researcher.py:
  module: ai-researcher (line 0)
  class: ResearchAgent (line 52)
  function: __init__ (line 55)
  function: search_topic (line 60)
  function: categorize_result (line 85)
  function: generate_draft_entry (line 105)
  function: save_draft (line 170)
  function: run_daily_scan (line 188)
  function: main (line 244)
hypercode-research\scripts\knowledge-graph.py:
  module: knowledge-graph (line 0)
  class: KnowledgeGraphGenerator (line 24)
  function: __init__ (line 27)
  function: extract_frontmatter (line 39)
  function: scan_research_entries (line 49)
  function: generate_json (line 102)
  function: generate_mermaid (line 120)
  function: generate_ascii_graph (line 159)
  function: generate_graphviz_dot (line 191)
  function: main (line 224)
hypercode-research\scripts\link-validator.py:
  module: link-validator (line 0)
  class: LinkValidator (line 20)
  function: __init__ (line 23)
  function: extract_links (line 32)
  function: scan_files (line 44)
  function: check_url (line 56)
  function: validate_links (line 66)
  function: report (line 89)
  function: main (line 116)
hypercode\accessibility\adhd_optimizer.py:
  module: adhd_optimizer (line 0)
hypercode\accessibility\autism_preset.py:
  module: autism_preset (line 0)
hypercode\accessibility\dyslexia_formatter.py:
  module: dyslexia_formatter (line 0)
hypercode\accessibility\sensory_customizer.py:
  module: sensory_customizer (line 0)
hypercode\accessibility\wcag_auditor.py:
  module: wcag_auditor (line 0)
hypercode\archive\new-files-to-check\backend\research\__init__.py:
  module: __init__ (line 0)
hypercode\archive\new-files-to-check\backend\research\db.py:
  module: db (line 0)
  function: _get_database_url (line 35)
hypercode\archive\new-files-to-check\backend\research\models.py:
  module: models (line 0)
  class: Study (line 32)
  function: __repr__ (line 52)
  class: Source (line 56)
  function: __repr__ (line 81)
  class: LanguageVersion (line 85)
  function: __repr__ (line 102)
  class: Task (line 106)
  function: __repr__ (line 124)
  class: Participant (line 128)
  function: __repr__ (line 144)
  class: Session (line 148)
  function: __repr__ (line 169)
  class: Event (line 176)
  function: __repr__ (line 193)
  class: Feedback (line 197)
  function: __repr__ (line 219)
hypercode\archive\new-files-to-check\backend\research\scripts\import_sources_from_folder.py:
  module: import_sources_from_folder (line 0)
  function: infer_kind (line 25)
  function: main (line 36)
hypercode\archive\new-files-to-check\backend\research\scripts\seed_basic_data.py:
  module: seed_basic_data (line 0)
  function: main (line 25)
hypercode\code_insights.py:
  function: analyze_code_patterns (line 8)
  function: find_undocumented_code (line 29)
  function: analyze_test_coverage (line 45)
  function: summarize_manifests (line 92)
hypercode\code_quality_report.py:
  module: code_quality_report (line 0)
  function: get_undocumented_classes_priority (line 15)
  function: get_least_tested_files (line 33)
  function: find_getter_methods (line 69)
  function: generate_code_quality_report (line 103)
hypercode\core\benchmarks\__init__.py:
  function: benchmark_lexer (line 12)
  function: print_benchmark_results (line 36)
hypercode\core\benchmarks\benchmarks_lexer.py:
  function: benchmark_lexer (line 6)
  function: print_benchmark_results (line 30)
hypercode\core\src\ai_gateway\base_gateway.py:
  module: base_gateway (line 0)
hypercode\core\src\ai_gateway\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\ai_gateway\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\ai_gateway\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\ai_gateway\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\ai_gateway\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode\core\src\ai_gateway\rag_engine.py:
  module: rag_engine (line 0)
hypercode\core\src\base_gateway.py:
  module: base_gateway (line 0)
hypercode\core\src\build.py:
  module: build (line 0)
  function: build (line 34)
hypercode\core\src\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\core\__init__.py:
  module: __init__ (line 0)
hypercode\core\src\core\ast.py:
  module: ast (line 0)
  class: Node (line 11)
  class: Program (line 18)
  class: Function (line 25)
  class: VariableDeclaration (line 34)
  class: Literal (line 42)
  class: BinaryOp (line 50)
  class: UnaryOp (line 59)
  class: Variable (line 67)
  class: Call (line 74)
  class: Return (line 82)
  class: Block (line 89)
  class: If (line 96)
  class: While (line 105)
  class: For (line 113)
  class: Assign (line 123)
  class: Logical (line 131)
hypercode\core\src\core\ast_nodes.py:
  module: ast_nodes (line 0)
  class: Node (line 24)
  class: Expression (line 31)
  class: Statement (line 38)
  class: Program (line 45)
  class: Identifier (line 52)
  class: Literal (line 59)
  class: VariableDeclaration (line 66)
  class: BinaryOperation (line 75)
hypercode\core\src\core\hypercode-\DuelCode\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode\core\src\core\hypercode-\DuelCode\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode\core\src\core\hypercode-\DuelCode\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode\core\src\core\hypercode-\DuelCode\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode\core\src\core\hypercode-\DuelCode\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode\core\src\core\hypercode-\DuelCode\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode\core\src\core\hypercode-\accessibility\adhd_optimizer.py:
  module: adhd_optimizer (line 0)
hypercode\core\src\core\hypercode-\accessibility\autism_preset.py:
  module: autism_preset (line 0)
hypercode\core\src\core\hypercode-\accessibility\dyslexia_formatter.py:
  module: dyslexia_formatter (line 0)
hypercode\core\src\core\hypercode-\accessibility\sensory_customizer.py:
  module: sensory_customizer (line 0)
hypercode\core\src\core\hypercode-\accessibility\wcag_auditor.py:
  module: wcag_auditor (line 0)
hypercode\core\src\core\hypercode-\ai_gateway\base_gateway.py:
  module: base_gateway (line 0)
hypercode\core\src\core\hypercode-\ai_gateway\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\core\hypercode-\ai_gateway\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\core\hypercode-\ai_gateway\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\core\hypercode-\ai_gateway\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\core\hypercode-\ai_gateway\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode\core\src\core\hypercode-\ai_gateway\rag_engine.py:
  module: rag_engine (line 0)
hypercode\core\src\core\hypercode-\code_analyzer_ai.py:
  module: code_analyzer_ai (line 0)
  class: CodeAnalyzerAI (line 20)
  function: __init__ (line 23)
  function: analyze_file (line 26)
  function: _analyze_complexity (line 73)
  function: _check_docstrings (line 114)
  function: _get_ai_code_analysis (line 156)
  function: analyze_project (line 184)
  function: _get_project_ai_insights (line 231)
  function: save_analysis (line 263)
  function: print_summary (line 271)
  function: main (line 289)
hypercode\core\src\core\hypercode-\debug_search.py:
  module: debug_search (line 0)
  function: debug_search (line 15)
hypercode\core\src\core\hypercode-\demo_ai_research.py:
  module: demo_ai_research (line 0)
  function: demo_ai_research_queries (line 16)
  function: test_document_specific_queries (line 90)
hypercode\core\src\core\hypercode-\demo_enhanced_client.py:
  module: demo_enhanced_client (line 0)
  function: demo_knowledge_base_integration (line 16)
  function: demonstrate_memory_persistence (line 131)
hypercode\core\src\core\hypercode-\final_integration_test.py:
  module: final_integration_test (line 0)
  function: final_integration_test (line 15)
hypercode\core\src\core\hypercode-\health_scanner_ai.py:
  module: health_scanner_ai (line 0)
  class: HealthScannerAI (line 19)
  function: __init__ (line 22)
  function: analyze_project_structure (line 26)
  function: analyze_dependencies (line 69)
  function: analyze_security (line 111)
  function: get_ai_recommendations (line 144)
  function: run_full_scan (line 171)
  function: save_report (line 222)
  function: print_summary (line 228)
  function: main (line 248)
hypercode\core\src\core\hypercode-\import-helper.py:
  module: import-helper (line 0)
  class: SpaceImportHelper (line 13)
  function: __init__ (line 16)
  function: validate_document (line 21)
  function: load_template (line 63)
  function: validate_all (line 83)
  function: generate_report (line 95)
  function: create_import_script (line 141)
  function: create_template_instructions (line 193)
  function: main (line 264)
hypercode\core\src\core\hypercode-\import_all_space_data.py:
  module: import_all_space_data (line 0)
  function: format_content (line 16)
  function: import_all_hypercode_data (line 41)
hypercode\core\src\core\hypercode-\import_hypercode_data.py:
  module: import_hypercode_data (line 0)
  function: import_hypercode_space_data (line 16)
hypercode\core\src\core\hypercode-\import_perplexity_space.py:
  module: import_perplexity_space (line 0)
  function: create_manual_import_script (line 17)
  function: create_json_import_template (line 86)
  function: import_from_json (line 115)
  function: test_imported_data (line 153)
  function: show_import_menu (line 188)
hypercode\core\src\core\hypercode-\knowledge_graph\graph_builder.py:
  module: graph_builder (line 0)
hypercode\core\src\core\hypercode-\knowledge_graph\sparql_query.py:
  module: sparql_query (line 0)
hypercode\core\src\core\hypercode-\knowledge_graph\update_agent.py:
  module: update_agent (line 0)
hypercode\core\src\core\hypercode-\live_research\doc_generator.py:
  module: doc_generator (line 0)
hypercode\core\src\core\hypercode-\live_research\github_publisher.py:
  module: github_publisher (line 0)
hypercode\core\src\core\hypercode-\live_research\paper_indexer.py:
  module: paper_indexer (line 0)
hypercode\core\src\core\hypercode-\live_research\research_crawler.py:
  module: research_crawler (line 0)
hypercode\core\src\core\hypercode-\live_research\synthesis_engine.py:
  module: synthesis_engine (line 0)
hypercode\core\src\core\hypercode-\mcp\__init__.py:
  module: __init__ (line 0)
hypercode\core\src\core\hypercode-\mcp\servers\__init__.py:
  module: __init__ (line 0)
hypercode\core\src\core\hypercode-\mcp\servers\aws_cli.py:
  function: main (line 4)
hypercode\core\src\core\hypercode-\mcp\servers\aws_resource_manager.py:
  function: main (line 4)
hypercode\core\src\core\hypercode-\mcp\servers\code_analysis.py:
  function: main (line 4)
hypercode\core\src\core\hypercode-\mcp\servers\dataset_downloader.py:
  function: main (line 4)
hypercode\core\src\core\hypercode-\mcp\servers\file_system.py:
  function: main (line 4)
hypercode\core\src\core\hypercode-\mcp\servers\human_input.py:
  function: main (line 4)
hypercode\core\src\core\hypercode-\mcp\servers\hypercode_syntax.py:
  module: hypercode_syntax (line 0)
  class: HyperCodeSyntaxServer (line 28)
  function: __init__ (line 31)
  function: handle_request (line 35)
  function: _initialize (line 56)
  function: _document_changed (line 79)
  function: _text_hover (line 98)
  function: _completion (line 121)
  function: _parse_document (line 150)
  function: _validate_neurodiversity (line 179)
  function: _generate_diagnostics (line 216)
  function: _get_annotation_hover_info (line 266)
  function: main (line 294)
hypercode\core\src\core\hypercode-\mcp\servers\path_service.py:
  function: main (line 4)
hypercode\core\src\core\hypercode-\mcp\servers\user_profile_manager.py:
  function: main (line 4)
hypercode\core\src\core\hypercode-\mcp\servers\valkey_service.py:
  function: check_redis_connection (line 40)
  function: health_check (line 59)
  function: set_key (line 67)
  function: get_key (line 80)
  function: hset_key (line 95)
  function: hget_key (line 107)
  function: hgetall_hash (line 126)
  function: main (line 144)
hypercode\core\src\core\hypercode-\mcp\servers\web_search.py:
  function: main (line 4)
hypercode\core\src\core\hypercode-\mcp\setup.py:
  module: setup (line 0)
  function: install_dependencies (line 16)
  function: verify_setup (line 31)
  function: show_next_steps (line 54)
  function: main (line 72)
hypercode\core\src\core\hypercode-\mcp\start_servers.py:
  module: start_servers (line 0)
  function: start_server (line 34)
  function: list_servers (line 59)
  function: main (line 66)
hypercode\core\src\core\hypercode-\mcp\test_mcp.py:
  module: test_mcp (line 0)
  function: test_server_imports (line 15)
  function: main (line 47)
hypercode\core\src\core\hypercode-\perplexity_space_collector.py:
  module: perplexity_space_collector (line 0)
  function: quick_copy_paste_collector (line 18)
  function: create_structured_template (line 117)
  function: show_bro_hacks (line 167)
  function: main_menu (line 207)
hypercode\core\src\core\hypercode-\perplexity_space_integration.py:
  module: perplexity_space_integration (line 0)
  function: main (line 16)
hypercode\core\src\core\hypercode-\scripts\style_guide_collector.py:
  module: style_guide_collector (line 0)
  class: StyleGuideCollector (line 16)
  function: __init__ (line 19)
  function: _load_feedback (line 30)
  function: _save_feedback (line 49)
  function: add_feedback (line 58)
  function: _update_analysis (line 100)
  function: analyze_feedback (line 149)
  function: _get_top_items (line 187)
  function: _calculate_consensus (line 210)
  function: _generate_recommendations (line 243)
  function: import_github_issues (line 323)
  function: generate_report (line 346)
  function: interactive_feedback (line 413)
  function: main (line 521)
hypercode\core\src\core\hypercode-\scripts\test_perplexity_api.py:
  module: test_perplexity_api (line 0)
  function: main (line 17)
hypercode\core\src\core\hypercode-\src\build.py:
  module: build (line 0)
  function: build (line 34)
hypercode\core\src\core\hypercode-\src\core\ast_nodes.py:
  module: ast_nodes (line 0)
  class: Node (line 24)
  class: Expression (line 31)
  class: Statement (line 38)
  class: Program (line 45)
  class: Identifier (line 52)
  class: Literal (line 59)
  class: VariableDeclaration (line 66)
  class: BinaryOperation (line 75)
hypercode\core\src\core\hypercode-\src\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 15)
  class: Lexer (line 32)
  function: __init__ (line 49)
  function: tokenize (line 110)
  function: is_at_end (line 134)
  function: scan_token (line 137)
  function: advance (line 228)
  function: add_token (line 233)
  function: error (line 246)
  function: synchronize (line 262)
  function: previous (line 274)
  function: peek_next (line 280)
  function: match (line 286)
  function: peek (line 295)
  function: string (line 300)
  function: is_digit (line 362)
  function: number (line 366)
  function: is_alpha (line 421)
  function: is_alphanumeric (line 425)
  function: is_hex_digit (line 429)
  function: identifier (line 433)
hypercode\core\src\core\hypercode-\src\core\optimizer.py:
  module: optimizer (line 0)
hypercode\core\src\core\hypercode-\src\core\parser.py:
  class: ParseError (line 8)
  class: Parser (line 12)
  function: __init__ (line 13)
  function: parse (line 17)
  function: declaration (line 26)
  function: var_declaration (line 39)
  function: statement (line 64)
  function: print_statement (line 71)
  function: expression_statement (line 76)
  function: block (line 81)
  function: expression (line 88)
  function: assignment (line 91)
  function: equality (line 106)
  function: comparison (line 116)
  function: term (line 129)
  function: factor (line 137)
  function: unary (line 145)
  function: primary (line 152)
  function: match (line 184)
  function: consume (line 191)
  function: error (line 201)
  function: synchronize (line 207)
  function: check (line 227)
  function: advance (line 232)
  function: is_at_end (line 237)
  function: peek (line 240)
  function: previous (line 243)
hypercode\core\src\core\hypercode-\src\hypercode-backend-js-COMPLETE.py:
  module: hypercode-backend-js-COMPLETE (line 0)
  class: JSCompiler (line 19)
  function: __init__ (line 30)
  function: compile (line 42)
  function: _generate_header (line 65)
  function: _generate_setup (line 74)
  function: _generate_main (line 110)
  function: _generate_footer (line 162)
  function: _indent (line 179)
  function: optimize_ast (line 183)
  function: main (line 200)
hypercode\core\src\core\hypercode-\src\hypercode-idea-generator-WEB.py:
  module: hypercode-idea-generator-WEB (line 0)
hypercode\core\src\core\hypercode-\src\hypercode-launch-kit.py:
  module: hypercode-launch-kit (line 0)
  class: HyperCodeLaunchKit (line 23)
  function: __init__ (line 26)
  function: create_readme (line 30)
  function: create_launch_checklist (line 367)
  function: create_launch_script (line 620)
  function: create_first_30_days (line 718)
  function: print_summary (line 974)
  function: main (line 1007)
hypercode\core\src\core\hypercode-\src\hypercode-lexer-COMPLETE.py:
  module: hypercode-lexer-COMPLETE (line 0)
  class: TokenType (line 21)
  class: Token (line 45)
  function: __repr__ (line 54)
  class: LexerError (line 59)
  function: __init__ (line 62)
  class: HyperCodeLexer (line 69)
  function: __init__ (line 95)
  function: tokenize (line 110)
  function: _advance_position (line 169)
  function: _skip_comment (line 179)
  function: get_tokens (line 184)
  function: filter_tokens (line 188)
  function: print_tokens (line 205)
  function: get_statistics (line 236)
  function: main (line 250)
hypercode\core\src\core\hypercode-\src\hypercode-parser-COMPLETE.py:
  module: hypercode-parser-COMPLETE (line 0)
  class: NodeType (line 22)
  class: ASTNode (line 38)
  function: __repr__ (line 51)
  class: ParserError (line 68)
  function: __init__ (line 71)
  class: HyperCodeParser (line 80)
  function: __init__ (line 94)
  function: parse (line 105)
  function: _parse_statement (line 127)
  function: _parse_loop (line 174)
  function: _advance (line 209)
  function: _is_at_end (line 215)
  function: validate (line 222)
  function: print_ast (line 237)
  function: main (line 251)
hypercode\core\src\core\hypercode-\src\hypercode\__init__.py:
  module: __init__ (line 0)
hypercode\core\src\core\hypercode-\src\hypercode\__main__.py:
  function: main (line 6)
hypercode\core\src\core\hypercode-\src\hypercode\config.py:
  module: config (line 0)
  class: Config (line 16)
  function: get_headers (line 27)
hypercode\core\src\core\hypercode-\src\hypercode\core\__init__.py:
  module: __init__ (line 0)
hypercode\core\src\core\hypercode-\src\hypercode\core\ast.py:
  class: Node (line 9)
  function: accept (line 10)
  class: Expr (line 20)
  class: Literal (line 25)
  class: Variable (line 30)
  class: Assign (line 35)
  class: Binary (line 41)
  class: Unary (line 48)
  class: Grouping (line 54)
  class: Call (line 59)
  class: Get (line 66)
  class: Stmt (line 73)
  class: Expression (line 78)
  class: Print (line 83)
  class: Var (line 88)
  class: Block (line 94)
  class: Intent (line 99)
  class: Program (line 106)
hypercode\core\src\core\hypercode-\src\hypercode\core\cli.py:
  module: cli (line 0)
hypercode\core\src\core\hypercode-\src\hypercode\core\error_handler.py:
  function: report_parse_error (line 5)
  function: report (line 12)
hypercode\core\src\core\hypercode-\src\hypercode\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 32)
  function: __init__ (line 35)
  class: Lexer (line 42)
  function: __init__ (line 109)
  function: tokenize (line 126)
  function: _match_patterns (line 161)
  function: _update_position (line 187)
  function: _add_token (line 206)
  function: _handle_unknown (line 270)
hypercode\core\src\core\hypercode-\src\hypercode\core\optimizer.py:
  module: optimizer (line 0)
hypercode\core\src\core\hypercode-\src\hypercode\core\parser.py:
  class: ParseError (line 24)
  class: Parser (line 28)
  function: __init__ (line 29)
  function: parse (line 33)
  function: declaration (line 42)
  function: var_declaration (line 51)
  function: statement (line 67)
  function: print_statement (line 76)
  function: intent_statement (line 81)
  function: expression_statement (line 96)
  function: block (line 101)
  function: expression (line 108)
  function: assignment (line 111)
  function: equality (line 126)
  function: comparison (line 136)
  function: term (line 149)
  function: factor (line 157)
  function: unary (line 165)
  function: primary (line 172)
  function: _primary (line 189)
  function: finish_call (line 220)
  function: match (line 233)
  function: consume (line 240)
  function: error (line 247)
  function: synchronize (line 253)
  function: check (line 273)
  function: advance (line 278)
  function: is_at_end (line 283)
  function: peek (line 286)
  function: previous (line 289)
hypercode\core\src\core\hypercode-\src\hypercode\core\semantic_analyzer.py:
  module: semantic_analyzer (line 0)
hypercode\core\src\core\hypercode-\src\hypercode\core\tokens.py:
  class: TokenType (line 6)
  class: Token (line 61)
  function: __str__ (line 68)
hypercode\core\src\core\hypercode-\src\hypercode\enhanced_perplexity_client.py:
  module: enhanced_perplexity_client (line 0)
  class: EnhancedPerplexityClient (line 18)
  function: __init__ (line 21)
  function: query_with_context (line 25)
  function: add_research_data (line 61)
  function: search_research_data (line 71)
  function: list_research_documents (line 75)
  function: get_document (line 79)
  function: delete_document (line 83)
  function: import_from_perplexity_space (line 87)
  function: test_context_integration (line 123)
  function: create_perplexity_space_import_template (line 175)
hypercode\core\src\core\hypercode-\src\hypercode\knowledge_base.py:
  module: knowledge_base (line 0)
  class: ResearchDocument (line 17)
  function: __post_init__ (line 28)
  function: generate_id (line 36)
  function: validate (line 41)
  function: update_timestamp (line 53)
  class: HyperCodeKnowledgeBase (line 100)
  function: __init__ (line 103)
  function: load (line 109)
  function: save (line 125)
  function: add_document (line 135)
  function: search_documents (line 163)
  function: get_context_for_query (line 226)
  function: list_documents (line 256)
  function: get_document (line 260)
  function: delete_document (line 264)
  function: update_document (line 272)
  function: search_by_tags (line 286)
  function: get_document_statistics (line 305)
  function: export_format (line 330)
  function: validate_all_documents (line 352)
  function: cleanup_duplicates (line 362)
  function: initialize_sample_data (line 383)
hypercode\core\src\core\hypercode-\src\hypercode\perplexity_client.py:
  module: perplexity_client (line 0)
  class: PerplexityClient (line 12)
  function: __init__ (line 15)
  function: query (line 30)
  function: test_connection (line 72)
hypercode\core\src\core\hypercode-\src\hypercode\repl.py:
  function: run_repl (line 7)
  function: run (line 22)
hypercode\core\src\core\hypercode-\src\hypercode_idea_generator.py:
  module: hypercode_idea_generator (line 0)
  class: HyperCodeIdeaGenerator (line 431)
  function: __init__ (line 439)
  function: get_ideas_by_category (line 443)
  function: get_top_ideas (line 468)
  function: vote_for_idea (line 487)
  function: get_trending_ideas (line 497)
  function: format_idea_card (line 502)
  function: main (line 528)
hypercode\core\src\core\hypercode-\src\hypercode_lexer_fixed.py:
  module: hypercode_lexer_fixed (line 0)
  class: TokenType (line 19)
  class: Token (line 44)
  function: __repr__ (line 54)
  class: LexerError (line 68)
  function: __init__ (line 71)
  class: HyperCodeLexerFixed (line 84)
  function: __init__ (line 125)
  function: tokenize (line 145)
  function: _parse_string (line 217)
  function: _skip_comment (line 300)
  function: _advance (line 305)
  function: print_tokens (line 315)
  function: run_tests (line 329)
  function: main (line 446)
hypercode\core\src\core\hypercode-\src\hypercode_poc.py:
  module: hypercode_poc (line 0)
  class: TokenType (line 18)
  class: Token (line 34)
  class: UserConfidenceLevel (line 41)
  class: EnhancedLexer (line 48)
  function: __init__ (line 51)
  function: tokenize (line 74)
  function: handle_string (line 115)
  function: handle_number (line 141)
  function: handle_identifier (line 149)
  function: advance (line 171)
  class: ContextAwareErrorMessenger (line 176)
  function: __init__ (line 179)
  function: format_error (line 182)
  class: SemanticContextStreamer (line 189)
  function: analyze (line 192)
  class: ConfidenceTracker (line 209)
  function: __init__ (line 212)
  function: record (line 216)
  class: HyperCodePOC (line 222)
  function: __init__ (line 225)
  function: compile (line 232)
hypercode\core\src\core\hypercode-\src\parser\debug_ascii.py:
  module: debug_ascii (line 0)
  function: test_regex_patterns (line 14)
hypercode\core\src\core\hypercode-\src\parser\debug_full.py:
  module: debug_full (line 0)
  function: debug_full_parsing (line 14)
hypercode\core\src\core\hypercode-\src\parser\debug_parser.py:
  module: debug_parser (line 0)
  function: debug_annotation_detection (line 14)
hypercode\core\src\core\hypercode-\src\parser\debug_simple.py:
  module: debug_simple (line 0)
  function: debug_simple (line 14)
hypercode\core\src\core\hypercode-\src\parser\test_parser.py:
  module: test_parser (line 0)
  function: test_first_click_moment (line 14)
hypercode\core\src\core\hypercode-\src\parser\visual_syntax_parser.py:
  module: visual_syntax_parser (line 0)
  class: SemanticMarker (line 18)
  class: SemanticAnnotation (line 37)
  function: __str__ (line 46)
  class: ParsedFunction (line 51)
  function: get_annotations_by_type (line 62)
  class: VisualSyntaxParser (line 69)
  function: __init__ (line 72)
  function: _build_semantic_patterns (line 76)
  function: _build_color_scheme (line 105)
  function: parse_file (line 123)
  function: parse_content (line 130)
  function: _is_function_definition (line 170)
  function: _start_new_function (line 179)
  function: _parse_line_annotations (line 202)
  function: _parse_annotation_params (line 223)
  function: generate_syntax_highlighting (line 265)
  function: extract_semantic_summary (line 277)
  function: validate_neurodiversity_compliance (line 311)
hypercode\core\src\core\hypercode-\src\scaffold (1).py:
  module: scaffold (1) (line 0)
  function: create_directories (line 141)
  function: create_python_files (line 151)
  function: create_example_files (line 165)
  function: create_root_files (line 202)
  function: create_healthcheck (line 213)
  function: print_summary (line 234)
  function: main (line 259)
hypercode\core\src\core\hypercode-\src\scaffold.py:
  module: scaffold (line 0)
  function: create_directories (line 153)
  function: create_python_files (line 184)
  function: create_example_files (line 254)
  function: create_root_files (line 291)
  function: create_healthcheck (line 541)
  function: print_summary (line 583)
  function: main (line 621)
hypercode\core\src\core\hypercode-\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode\core\src\core\hypercode-\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode\core\src\core\hypercode-\test_intent_blocks.py:
  module: test_intent_blocks (line 0)
  function: test_intent_block (line 13)
hypercode\core\src\core\hypercode-\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode\core\src\core\hypercode-\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode\core\src\core\hypercode-\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 183)
hypercode\core\src\core\hypercode-\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode\core\src\core\hypercode-\tests\benchmark_knowledge_base.py:
  module: benchmark_knowledge_base (line 0)
  class: BenchmarkSuite (line 24)
  function: __init__ (line 27)
  function: _get_system_info (line 34)
  function: generate_test_data (line 43)
  function: benchmark_operation (line 93)
  function: run_benchmark_suite (line 118)
  function: _calculate_summary (line 274)
  function: _generate_recommendations (line 296)
  function: generate_markdown_report (line 338)
  function: save_json_results (line 467)
  function: main (line 474)
hypercode\core\src\core\hypercode-\tests\test_accessibility.py:
  module: test_accessibility (line 0)
hypercode\core\src\core\hypercode-\tests\test_ai_gateway.py:
  module: test_ai_gateway (line 0)
hypercode\core\src\core\hypercode-\tests\test_backends.py:
  module: test_backends (line 0)
hypercode\core\src\core\hypercode-\tests\test_core.py:
  module: test_core (line 0)
  function: run_test (line 29)
hypercode\core\src\core\hypercode-\tests\test_integration.py:
  module: test_integration (line 0)
hypercode\core\src\core\hypercode-\tests\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestKnowledgeBaseSearch (line 12)
  function: sample_documents (line 16)
  function: knowledge_base (line 40)
  function: test_basic_search (line 48)
  function: test_search_with_exact_match (line 54)
  function: test_search_case_insensitive (line 59)
  function: test_search_empty_query (line 65)
  function: test_search_no_matches (line 71)
  function: test_search_ranking (line 77)
  function: test_query_normalization (line 90)
  function: test_multi_word_query (line 98)
  function: test_tag_based_search (line 103)
  class: TestEdgeCases (line 112)
  function: knowledge_base (line 116)
  function: test_very_short_query (line 121)
  function: test_very_long_query (line 126)
  function: test_special_characters_in_query (line 136)
  function: test_unicode_in_query (line 141)
  function: test_sql_injection_attempt (line 146)
  function: test_repeated_queries (line 151)
  class: TestPerformance (line 159)
  function: large_knowledge_base (line 163)
  function: test_search_response_time (line 179)
  function: test_concurrent_searches (line 189)
  function: test_memory_usage (line 207)
  class: TestIntegrationWithPerplexity (line 213)
  function: mock_perplexity_client (line 217)
  function: mock_knowledge_base (line 229)
  function: test_enhanced_query_with_context (line 243)
  function: test_fallback_to_perplexity_api (line 259)
  function: test_context_ranking_and_selection (line 273)
  class: TestDocumentManagement (line 288)
  function: knowledge_base (line 292)
  function: test_add_document (line 300)
  function: test_update_document (line 310)
  function: test_remove_document (line 315)
hypercode\core\src\core\hypercode-\tests\test_knowledge_base_comprehensive.py:
  module: test_knowledge_base_comprehensive (line 0)
  class: TestKnowledgeBaseUnit (line 20)
  function: temp_kb (line 24)
  function: sample_docs (line 36)
  function: test_init_empty_kb (line 59)
  function: test_add_single_document (line 65)
  function: test_add_multiple_documents (line 74)
  function: test_save_and_load (line 84)
  function: test_search_exact_match (line 102)
  function: test_search_partial_match (line 113)
  function: test_search_tag_matching (line 124)
  function: test_search_case_insensitive (line 135)
  function: test_empty_search (line 147)
  function: test_nonexistent_search (line 155)
  function: test_get_context_for_query (line 165)
  function: test_context_length_limit (line 176)
  function: test_document_update (line 186)
  function: test_list_documents (line 202)
  function: test_delete_document (line 213)
  class: TestKnowledgeBaseIntegration (line 229)
  function: populated_kb (line 233)
  function: test_complex_search_queries (line 277)
  function: test_search_ranking_quality (line 291)
  function: test_related_term_expansion (line 301)
  function: test_performance_with_large_dataset (line 313)
  function: test_concurrent_access_simulation (line 332)
  class: TestKnowledgeBasePerformance (line 356)
  function: large_kb (line 360)
  function: test_search_performance_large_dataset (line 382)
  function: test_save_performance_large_dataset (line 396)
  function: test_load_performance_large_dataset (line 409)
  function: test_memory_usage_large_dataset (line 423)
  class: TestKnowledgeBaseEdgeCases (line 446)
  function: edge_case_kb (line 450)
  function: test_empty_title_handling (line 494)
  function: test_special_characters_handling (line 499)
  function: test_very_long_titles (line 507)
  function: test_empty_content_handling (line 512)
  function: test_none_tags_handling (line 517)
  function: test_malformed_json_handling (line 531)
  function: test_file_permission_handling (line 544)
hypercode\core\src\core\hypercode-\tests\test_lexer.py:
  function: test_lexer_basic_tokens (line 5)
  function: test_lexer_strings (line 23)
  function: test_lexer_operators (line 48)
hypercode\core\src\core\hypercode-\tests\test_lexer_extended.py:
  function: test_lexer_escaped_strings (line 5)
  function: test_lexer_numbers (line 18)
  function: test_lexer_operators (line 39)
  function: test_lexer_comments (line 86)
  function: test_lexer_whitespace (line 115)
  function: test_lexer_error_handling (line 130)
  function: test_lexer_hex_numbers (line 139)
  function: test_lexer_binary_numbers (line 157)
  function: test_lexer_scientific_notation (line 169)
  function: test_lexer_string_escapes (line 180)
  function: test_lexer_keywords (line 197)
  function: test_lexer_position_tracking (line 223)
  function: test_lexer_error_recovery (line 243)
  function: test_lexer_error_messages (line 252)
hypercode\core\src\core\hypercode-\tests\test_parser.py:
  function: test_parse_literal (line 12)
  function: test_parse_variable_declaration (line 24)
  function: test_parse_binary_expression (line 37)
hypercode\core\src\core\hypercode-\tests\unit\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestHyperCodeKnowledgeBase (line 20)
  function: temp_kb (line 24)
  function: sample_documents (line 33)
  function: test_init_empty_kb (line 56)
  function: test_add_document (line 61)
  function: test_add_multiple_documents (line 82)
  function: test_save_and_load (line 92)
  function: test_search_exact_match (line 113)
  function: test_search_tag_matching (line 126)
  function: test_search_related_terms (line 139)
  function: test_search_space_data_boost (line 153)
  function: test_get_context_for_query (line 180)
  function: test_context_length_limit (line 192)
  function: test_list_documents (line 203)
  function: test_empty_search (line 216)
  function: test_search_nonexistent_term (line 221)
  function: test_document_update (line 231)
  class: TestResearchDocument (line 250)
  function: test_document_creation (line 253)
  function: test_document_optional_fields (line 273)
hypercode\core\src\core\hypercode-\tests\unit\test_search_algorithm.py:
  module: test_search_algorithm (line 0)
  class: TestSearchAlgorithm (line 20)
  function: populated_kb (line 24)
  function: test_exact_title_match_highest_score (line 80)
  function: test_space_data_boosting (line 92)
  function: test_related_term_expansion (line 105)
  function: test_tag_matching_scoring (line 126)
  function: test_content_frequency_scoring (line 136)
  function: test_partial_word_matching (line 149)
  function: test_query_word_ordering (line 167)
  function: test_case_insensitive_search (line 179)
  function: test_empty_query_returns_no_results (line 202)
  function: test_limit_parameter_respected (line 210)
  function: test_no_results_for_nonexistent_terms (line 219)
  function: test_special_characters_in_query (line 227)
  function: test_unicode_characters (line 237)
  function: test_search_performance_with_large_kb (line 256)
  function: test_search_result_consistency (line 277)
  class: TestSearchScoringDetails (line 292)
  function: scoring_kb (line 296)
  function: test_title_match_beats_content_match (line 324)
  function: test_space_data_boosting_works (line 332)
  function: test_frequency_scoring (line 340)
hypercode\core\src\core\interpreter.py:
  class: RuntimeError (line 8)
  function: __init__ (line 9)
  class: Environment (line 15)
  function: __init__ (line 16)
  function: define (line 20)
  function: get (line 23)
  function: assign (line 30)
  class: Callable (line 40)
  function: arity (line 41)
  function: call (line 44)
  class: HyperCodeFunction (line 48)
  function: __init__ (line 49)
  function: call (line 53)
  function: arity (line 65)
  class: ReturnException (line 69)
  function: __init__ (line 70)
  class: Interpreter (line 74)
  function: __init__ (line 75)
  class: Clock (line 82)
  function: arity (line 83)
  function: call (line 86)
  function: __str__ (line 89)
  class: Double (line 92)
  function: arity (line 93)
  function: call (line 96)
  function: __str__ (line 101)
  class: Square (line 104)
  function: arity (line 105)
  function: call (line 108)
  function: __str__ (line 113)
  function: execute_block (line 120)
  function: interpret (line 129)
  function: execute (line 141)
  function: evaluate (line 144)
  function: visit_Expression (line 147)
  function: visit_Print (line 151)
  function: visit_Let (line 158)
  function: visit_Block (line 165)
  function: visit_BlockDecl (line 169)
  function: visit_Intent (line 175)
  function: visit_Function (line 180)
  function: visit_Return (line 185)
  function: visit_Literal (line 191)
  function: visit_Grouping (line 194)
  function: visit_Variable (line 197)
  function: visit_Assign (line 200)
  function: visit_Pipe (line 205)
  function: visit_State (line 234)
  function: visit_Call (line 244)
  function: visit_Binary (line 262)
  function: visit_Unary (line 293)
  function: is_truthy (line 301)
  function: stringify (line 308)
  function: get_output (line 322)
hypercode\core\src\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 17)
  class: Lexer (line 33)
  function: __init__ (line 41)
  function: scan_tokens (line 77)
  function: scan_token (line 87)
  function: number (line 164)
  function: string (line 197)
  function: docstring (line 242)
  function: identifier (line 268)
  function: error (line 278)
  function: is_at_end (line 294)
  function: advance (line 298)
  function: match (line 307)
  function: peek (line 317)
  function: peek_next (line 323)
  function: add_token (line 329)
hypercode\core\src\core\optimizer.py:
  module: optimizer (line 0)
hypercode\core\src\core\parser.py:
  class: ParseError (line 7)
  class: Parser (line 11)
  function: __init__ (line 12)
  function: parse (line 16)
  function: declaration (line 25)
  function: let_declaration (line 38)
  function: block_declaration (line 48)
  function: statement (line 54)
  function: print_statement (line 65)
  function: expression_statement (line 70)
  function: block (line 75)
  function: expression (line 84)
  function: pipe (line 87)
  function: assignment (line 103)
  function: equality (line 118)
  function: comparison (line 128)
  function: term (line 141)
  function: factor (line 149)
  function: unary (line 157)
  function: primary (line 164)
  function: function (line 194)
  function: if_statement (line 215)
  function: return_statement (line 227)
  function: match (line 237)
  function: consume (line 244)
  function: error (line 249)
  function: synchronize (line 255)
  function: check (line 276)
  function: advance (line 281)
  function: is_at_end (line 286)
  function: peek (line 289)
  function: previous (line 292)
hypercode\core\src\core\tokens.py:
  module: tokens (line 0)
  class: TokenType (line 12)
  class: Token (line 74)
  function: __init__ (line 86)
  function: __str__ (line 95)
  function: __repr__ (line 98)
hypercode\core\src\duelcode\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode\core\src\duelcode\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode\core\src\duelcode\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode\core\src\duelcode\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode\core\src\duelcode\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode\core\src\duelcode\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode\core\src\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode\core\src\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode\core\src\hypercode-backend-js-COMPLETE.py:
  module: hypercode-backend-js-COMPLETE (line 0)
  class: JSCompiler (line 19)
  function: __init__ (line 30)
  function: compile (line 42)
  function: _generate_header (line 65)
  function: _generate_setup (line 74)
  function: _generate_main (line 110)
  function: _generate_footer (line 162)
  function: _indent (line 179)
  function: optimize_ast (line 183)
  function: main (line 200)
hypercode\core\src\hypercode-idea-generator-WEB.py:
  module: hypercode-idea-generator-WEB (line 0)
hypercode\core\src\hypercode-launch-kit.py:
  module: hypercode-launch-kit (line 0)
  class: HyperCodeLaunchKit (line 23)
  function: __init__ (line 26)
  function: create_readme (line 30)
  function: create_launch_checklist (line 367)
  function: create_launch_script (line 620)
  function: create_first_30_days (line 718)
  function: print_summary (line 974)
  function: main (line 1007)
hypercode\core\src\hypercode-lexer-COMPLETE.py:
  module: hypercode-lexer-COMPLETE (line 0)
  class: TokenType (line 21)
  class: Token (line 45)
  function: __repr__ (line 54)
  class: LexerError (line 59)
  function: __init__ (line 62)
  class: HyperCodeLexer (line 69)
  function: __init__ (line 95)
  function: tokenize (line 110)
  function: _advance_position (line 169)
  function: _skip_comment (line 179)
  function: get_tokens (line 184)
  function: filter_tokens (line 188)
  function: print_tokens (line 205)
  function: get_statistics (line 236)
  function: main (line 250)
hypercode\core\src\hypercode-parser-COMPLETE.py:
  module: hypercode-parser-COMPLETE (line 0)
  class: NodeType (line 22)
  class: ASTNode (line 38)
  function: __repr__ (line 51)
  class: ParserError (line 68)
  function: __init__ (line 71)
  class: HyperCodeParser (line 80)
  function: __init__ (line 94)
  function: parse (line 105)
  function: _parse_statement (line 127)
  function: _parse_loop (line 174)
  function: _advance (line 209)
  function: _is_at_end (line 215)
  function: validate (line 222)
  function: print_ast (line 237)
  function: main (line 251)
hypercode\core\src\hypercode\__init__.py:
  module: __init__ (line 0)
hypercode\core\src\hypercode\__main__.py:
  function: main (line 6)
hypercode\core\src\hypercode\cli\__init__.py:
  module: __init__ (line 0)
  function: main (line 14)
hypercode\core\src\hypercode\config.py:
  module: config (line 0)
  class: Config (line 16)
  function: get_headers (line 27)
hypercode\core\src\hypercode\core\__init__.py:
  module: __init__ (line 0)
hypercode\core\src\hypercode\core\cli.py:
  module: cli (line 0)
hypercode\core\src\hypercode\core\error_handler.py:
  function: report_parse_error (line 5)
  function: report (line 12)
hypercode\core\src\hypercode\core\hypercode_ast.py:
  class: Node (line 9)
  function: accept (line 10)
  class: Expr (line 20)
  class: Literal (line 25)
  class: Variable (line 30)
  class: Assign (line 35)
  class: Binary (line 41)
  class: Unary (line 48)
  class: Grouping (line 54)
  class: Call (line 59)
  class: Get (line 66)
  class: Stmt (line 73)
  class: Expression (line 78)
  class: Print (line 83)
  class: Var (line 88)
  class: Block (line 94)
  class: If (line 99)
  class: Fun (line 106)
  class: Return (line 113)
  class: Intent (line 119)
  class: Program (line 126)
hypercode\core\src\hypercode\core\interpreter.py:
  class: Return (line 6)
  function: __init__ (line 7)
  class: HyperCodeFunction (line 11)
  function: __init__ (line 12)
  function: __str__ (line 16)
  function: arity (line 19)
  function: call (line 22)
  class: Environment (line 35)
  function: __init__ (line 36)
  function: define (line 40)
  function: get (line 43)
  function: assign (line 50)
  class: Interpreter (line 60)
  function: __init__ (line 61)
  function: interpret (line 65)
  function: execute (line 72)
  function: execute_block (line 75)
  function: evaluate (line 84)
  function: visit_Expression (line 87)
  function: visit_Print (line 90)
  function: visit_Var (line 94)
  function: visit_Block (line 100)
  function: visit_Assign (line 103)
  function: visit_Binary (line 108)
  function: visit_Grouping (line 151)
  function: visit_Literal (line 154)
  function: visit_Unary (line 157)
  function: visit_Variable (line 170)
  function: visit_If (line 173)
  function: is_truthy (line 179)
  function: visit_Fun (line 186)
  function: visit_Return (line 190)
  function: visit_Call (line 196)
  function: is_callable (line 214)
  class: Visitor (line 219)
  function: visit_Expression (line 220)
  function: visit_Print (line 223)
  function: visit_Var (line 226)
  function: visit_Block (line 229)
  function: visit_If (line 232)
  function: visit_Fun (line 235)
  function: visit_Return (line 238)
  function: visit_Assign (line 241)
  function: visit_Binary (line 244)
  function: visit_Grouping (line 247)
  function: visit_Literal (line 250)
  function: visit_Unary (line 253)
  function: visit_Variable (line 256)
  function: visit_Call (line 259)
hypercode\core\src\hypercode\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 28)
  function: __init__ (line 35)
  class: Lexer (line 42)
  function: __init__ (line 45)
  function: tokenize (line 59)
  function: is_at_end (line 89)
  class: LexerError (line 102)
  function: __init__ (line 105)
  class: Lexer (line 112)
  function: __init__ (line 122)
  function: tokenize (line 136)
  function: scan_token (line 164)
  function: string (line 251)
  function: number (line 273)
  function: identifier (line 306)
  function: match (line 316)
  function: peek (line 327)
  function: peek_next (line 333)
  function: advance (line 339)
  function: add_token (line 349)
  function: error (line 357)
  function: is_at_end (line 371)
hypercode\core\src\hypercode\core\optimizer.py:
  module: optimizer (line 0)
hypercode\core\src\hypercode\core\parser.py:
  class: ParseError (line 8)
  class: Parser (line 12)
  function: __init__ (line 13)
  function: parse (line 17)
  function: declaration (line 26)
  function: var_declaration (line 37)
  function: statement (line 53)
  function: print_statement (line 66)
  function: return_statement (line 71)
  function: intent_statement (line 79)
  function: expression_statement (line 92)
  function: if_statement (line 97)
  function: function (line 109)
  function: block (line 128)
  function: expression (line 135)
  function: assignment (line 138)
  function: equality (line 153)
  function: comparison (line 163)
  function: term (line 176)
  function: factor (line 184)
  function: unary (line 192)
  function: primary (line 199)
  function: _primary (line 214)
  function: finish_call (line 245)
  function: match (line 258)
  function: consume (line 265)
  function: error (line 272)
  function: synchronize (line 278)
  function: check (line 298)
  function: advance (line 303)
  function: is_at_end (line 308)
  function: peek (line 311)
  function: previous (line 314)
hypercode\core\src\hypercode\core\semantic_analyzer.py:
  module: semantic_analyzer (line 0)
hypercode\core\src\hypercode\core\sensory_profile.py:
  module: sensory_profile (line 0)
  class: VisualNoiseLevel (line 15)
  class: AnimationSpeed (line 22)
  class: VisualSettings (line 29)
  class: AudioSettings (line 43)
  class: AnimationSettings (line 58)
  class: SensoryProfile (line 68)
  function: to_dict (line 77)
  function: from_dict (line 93)
  function: save (line 115)
  function: load (line 121)
  class: ProfileManager (line 128)
  function: __init__ (line 131)
  function: _ensure_default_profiles (line 141)
  function: _create_minimal_profile (line 154)
  function: _create_enhanced_profile (line 171)
  function: _create_high_contrast_profile (line 198)
  function: list_profiles (line 224)
  function: get_profile (line 228)
  function: save_profile (line 235)
  function: delete_profile (line 240)
  function: get_profile (line 251)
  function: list_profiles (line 263)
hypercode\core\src\hypercode\core\tokens.py:
  class: TokenType (line 6)
  class: Token (line 96)
  function: __str__ (line 103)
hypercode\core\src\hypercode\enhanced_perplexity_client.py:
  module: enhanced_perplexity_client (line 0)
  class: EnhancedPerplexityClient (line 18)
  function: __init__ (line 21)
  function: query_with_context (line 25)
  function: add_research_data (line 61)
  function: search_research_data (line 71)
  function: list_research_documents (line 75)
  function: get_document (line 79)
  function: delete_document (line 83)
  function: import_from_perplexity_space (line 87)
  function: test_context_integration (line 123)
  function: create_perplexity_space_import_template (line 175)
hypercode\core\src\hypercode\knowledge_base.py:
  module: knowledge_base (line 0)
  class: ResearchDocument (line 17)
  function: __post_init__ (line 28)
  function: generate_id (line 36)
  function: validate (line 41)
  function: update_timestamp (line 53)
  class: HyperCodeKnowledgeBase (line 100)
  function: __init__ (line 103)
  function: load (line 109)
  function: save (line 125)
  function: add_document (line 135)
  function: search_documents (line 163)
  function: get_context_for_query (line 227)
  function: list_documents (line 257)
  function: get_document (line 261)
  function: delete_document (line 265)
  function: update_document (line 273)
  function: search_by_tags (line 287)
  function: get_document_statistics (line 306)
  function: export_format (line 331)
  function: validate_all_documents (line 353)
  function: cleanup_duplicates (line 363)
  function: initialize_sample_data (line 384)
hypercode\core\src\hypercode\perplexity_client.py:
  module: perplexity_client (line 0)
  class: PerplexityClient (line 12)
  function: __init__ (line 15)
  function: query (line 30)
  function: test_connection (line 72)
hypercode\core\src\hypercode\repl.py:
  function: run_repl (line 11)
  function: run (line 32)
  function: show_help (line 51)
hypercode\core\src\hypercode_idea_generator.py:
  module: hypercode_idea_generator (line 0)
  class: HyperCodeIdeaGenerator (line 431)
  function: __init__ (line 439)
  function: get_ideas_by_category (line 443)
  function: get_top_ideas (line 468)
  function: vote_for_idea (line 487)
  function: get_trending_ideas (line 497)
  function: format_idea_card (line 502)
  function: main (line 528)
hypercode\core\src\hypercode_poc.py:
  module: hypercode_poc (line 0)
  class: TokenType (line 18)
  class: Token (line 34)
  class: UserConfidenceLevel (line 41)
  class: EnhancedLexer (line 48)
  function: __init__ (line 51)
  function: tokenize (line 74)
  function: handle_string (line 115)
  function: handle_number (line 141)
  function: handle_identifier (line 149)
  function: advance (line 171)
  class: ContextAwareErrorMessenger (line 176)
  function: __init__ (line 179)
  function: format_error (line 182)
  class: SemanticContextStreamer (line 189)
  function: analyze (line 192)
  class: ConfidenceTracker (line 209)
  function: __init__ (line 212)
  function: record (line 216)
  class: HyperCodePOC (line 222)
  function: __init__ (line 225)
  function: compile (line 232)
hypercode\core\src\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\core\src\parser\debug_ascii.py:
  module: debug_ascii (line 0)
  function: test_regex_patterns (line 14)
hypercode\core\src\parser\debug_full.py:
  module: debug_full (line 0)
  function: debug_full_parsing (line 14)
hypercode\core\src\parser\debug_parser.py:
  module: debug_parser (line 0)
  function: debug_annotation_detection (line 14)
hypercode\core\src\parser\debug_simple.py:
  module: debug_simple (line 0)
  function: debug_simple (line 14)
hypercode\core\src\parser\test_parser.py:
  module: test_parser (line 0)
  function: test_first_click_moment (line 14)
hypercode\core\src\parser\visual_syntax_parser.py:
  module: visual_syntax_parser (line 0)
  class: SemanticMarker (line 18)
  class: SemanticAnnotation (line 37)
  function: __str__ (line 46)
  class: ParsedFunction (line 51)
  function: get_annotations_by_type (line 62)
  class: VisualSyntaxParser (line 69)
  function: __init__ (line 72)
  function: _build_semantic_patterns (line 76)
  function: _build_color_scheme (line 105)
  function: parse_file (line 123)
  function: parse_content (line 130)
  function: _is_function_definition (line 170)
  function: _start_new_function (line 179)
  function: _parse_line_annotations (line 202)
  function: _parse_annotation_params (line 223)
  function: generate_syntax_highlighting (line 265)
  function: extract_semantic_summary (line 277)
  function: validate_neurodiversity_compliance (line 311)
hypercode\core\src\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode\core\src\rag_engine.py:
  module: rag_engine (line 0)
hypercode\core\src\scaffold (1).py:
  module: scaffold (1) (line 0)
  function: create_directories (line 141)
  function: create_python_files (line 151)
  function: create_example_files (line 165)
  function: create_root_files (line 202)
  function: create_healthcheck (line 213)
  function: print_summary (line 234)
  function: main (line 259)
hypercode\core\src\scaffold.py:
  module: scaffold (line 0)
  function: create_directories (line 153)
  function: create_python_files (line 184)
  function: create_example_files (line 254)
  function: create_root_files (line 291)
  function: create_healthcheck (line 541)
  function: print_summary (line 583)
  function: main (line 621)
hypercode\core\src\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode\core\src\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode\core\src\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode\core\src\utils\code_analyzer_ai.py:
  module: code_analyzer_ai (line 0)
  class: CodeAnalyzerAI (line 19)
  function: __init__ (line 22)
  function: analyze_file (line 25)
  function: _analyze_complexity (line 61)
  function: _check_docstrings (line 98)
  function: _get_ai_code_analysis (line 134)
  function: analyze_project (line 162)
  function: _get_project_ai_insights (line 206)
  function: save_analysis (line 238)
  function: print_summary (line 244)
  function: main (line 262)
hypercode\core\src\utils\debug_search.py:
  module: debug_search (line 0)
  function: debug_search (line 15)
hypercode\core\src\utils\demo_ai_research.py:
  module: demo_ai_research (line 0)
  function: demo_ai_research_queries (line 16)
  function: test_document_specific_queries (line 90)
hypercode\core\src\utils\demo_enhanced_client.py:
  module: demo_enhanced_client (line 0)
  function: demo_knowledge_base_integration (line 16)
  function: demonstrate_memory_persistence (line 131)
hypercode\core\src\utils\final_integration_test.py:
  module: final_integration_test (line 0)
  function: final_integration_test (line 15)
hypercode\core\src\utils\health_scanner_ai.py:
  module: health_scanner_ai (line 0)
  class: HealthScannerAI (line 18)
  function: __init__ (line 21)
  function: analyze_project_structure (line 25)
  function: analyze_dependencies (line 64)
  function: analyze_security (line 100)
  function: get_ai_recommendations (line 137)
  function: run_full_scan (line 164)
  function: save_report (line 215)
  function: print_summary (line 221)
  function: main (line 241)
hypercode\core\src\utils\import-helper.py:
  module: import-helper (line 0)
  class: SpaceImportHelper (line 13)
  function: __init__ (line 16)
  function: validate_document (line 21)
  function: load_template (line 63)
  function: validate_all (line 83)
  function: generate_report (line 95)
  function: create_import_script (line 141)
  function: create_template_instructions (line 193)
  function: main (line 264)
hypercode\core\src\utils\import_all_space_data.py:
  module: import_all_space_data (line 0)
  function: format_content (line 16)
  function: import_all_hypercode_data (line 41)
hypercode\core\src\utils\import_hypercode_data.py:
  module: import_hypercode_data (line 0)
  function: import_hypercode_space_data (line 16)
hypercode\core\src\utils\import_perplexity_space.py:
  module: import_perplexity_space (line 0)
  function: create_manual_import_script (line 17)
  function: create_json_import_template (line 86)
  function: import_from_json (line 115)
  function: test_imported_data (line 153)
  function: show_import_menu (line 188)
hypercode\core\src\utils\local_health_scanner.py:
  module: local_health_scanner (line 0)
  class: ProjectScanner (line 19)
  function: __init__ (line 22)
  function: scan_project (line 34)
  function: _scan_directory (line 42)
  function: _analyze_file (line 51)
  function: _analyze_ast (line 74)
  function: _check_documentation (line 94)
  function: _check_tests (line 106)
  function: _calculate_metrics (line 117)
  function: print_health_report (line 128)
  function: main (line 158)
hypercode\core\src\utils\perplexity_space_collector.py:
  module: perplexity_space_collector (line 0)
  function: quick_copy_paste_collector (line 18)
  function: create_structured_template (line 117)
  function: show_bro_hacks (line 167)
  function: main_menu (line 207)
hypercode\core\src\utils\perplexity_space_integration.py:
  module: perplexity_space_integration (line 0)
  function: main (line 16)
hypercode\core\src\utils\run_lexer.py:
  function: run_lexer (line 12)
hypercode\core\src\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode\core\tests\benchmark_knowledge_base.py:
  module: benchmark_knowledge_base (line 0)
  class: BenchmarkSuite (line 24)
  function: __init__ (line 27)
  function: _get_system_info (line 34)
  function: generate_test_data (line 43)
  function: benchmark_operation (line 93)
  function: run_benchmark_suite (line 118)
  function: _calculate_summary (line 274)
  function: _generate_recommendations (line 296)
  function: generate_markdown_report (line 338)
  function: save_json_results (line 467)
  function: main (line 474)
hypercode\core\tests\conftest.py:
  function: sample_hypercode (line 16)
  function: sample_lexer_tokens (line 27)
hypercode\core\tests\test_accessibility.py:
  module: test_accessibility (line 0)
hypercode\core\tests\test_ai_gateway.py:
  module: test_ai_gateway (line 0)
hypercode\core\tests\test_backends.py:
  module: test_backends (line 0)
hypercode\core\tests\test_core.py:
  module: test_core (line 0)
  function: run_test (line 30)
hypercode\core\tests\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode\core\tests\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode\core\tests\test_integration.py:
  module: test_integration (line 0)
hypercode\core\tests\test_intent_blocks.py:
  module: test_intent_blocks (line 0)
  function: test_intent_block (line 13)
hypercode\core\tests\test_interpreter.py:
  function: run_code (line 10)
  class: TestInterpreter (line 28)
  function: test_if_statement_then (line 30)
  function: test_if_statement_else (line 42)
  function: test_function_call (line 54)
  function: test_function_with_parameters (line 64)
  function: test_function_with_return (line 74)
  function: test_recursive_function_call (line 85)
  function: test_scoping (line 99)
hypercode\core\tests\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestKnowledgeBaseSearch (line 12)
  function: sample_documents (line 16)
  function: knowledge_base (line 40)
  function: test_basic_search (line 48)
  function: test_search_with_exact_match (line 54)
  function: test_search_case_insensitive (line 59)
  function: test_search_empty_query (line 65)
  function: test_search_no_matches (line 71)
  function: test_search_ranking (line 77)
  function: test_query_normalization (line 90)
  function: test_multi_word_query (line 98)
  function: test_tag_based_search (line 103)
  class: TestEdgeCases (line 112)
  function: knowledge_base (line 116)
  function: test_very_short_query (line 121)
  function: test_very_long_query (line 126)
  function: test_special_characters_in_query (line 136)
  function: test_unicode_in_query (line 141)
  function: test_sql_injection_attempt (line 146)
  function: test_repeated_queries (line 151)
  class: TestPerformance (line 159)
  function: large_knowledge_base (line 163)
  function: test_search_response_time (line 179)
  function: test_concurrent_searches (line 189)
  function: test_memory_usage (line 207)
  class: TestIntegrationWithPerplexity (line 213)
  function: mock_perplexity_client (line 217)
  function: mock_knowledge_base (line 229)
  function: test_enhanced_query_with_context (line 243)
  function: test_fallback_to_perplexity_api (line 259)
  function: test_context_ranking_and_selection (line 273)
  class: TestDocumentManagement (line 288)
  function: knowledge_base (line 292)
  function: test_add_document (line 300)
  function: test_update_document (line 310)
  function: test_remove_document (line 315)
hypercode\core\tests\test_knowledge_base_comprehensive.py:
  module: test_knowledge_base_comprehensive (line 0)
  class: TestKnowledgeBaseUnit (line 20)
  function: temp_kb (line 24)
  function: sample_docs (line 36)
  function: test_init_empty_kb (line 59)
  function: test_add_single_document (line 65)
  function: test_add_multiple_documents (line 74)
  function: test_save_and_load (line 84)
  function: test_search_exact_match (line 102)
  function: test_search_partial_match (line 113)
  function: test_search_tag_matching (line 124)
  function: test_search_case_insensitive (line 135)
  function: test_empty_search (line 147)
  function: test_nonexistent_search (line 155)
  function: test_get_context_for_query (line 165)
  function: test_context_length_limit (line 176)
  function: test_document_update (line 186)
  function: test_list_documents (line 202)
  function: test_delete_document (line 213)
  class: TestKnowledgeBaseIntegration (line 229)
  function: populated_kb (line 233)
  function: test_complex_search_queries (line 277)
  function: test_search_ranking_quality (line 291)
  function: test_related_term_expansion (line 301)
  function: test_performance_with_large_dataset (line 313)
  function: test_concurrent_access_simulation (line 332)
  class: TestKnowledgeBasePerformance (line 356)
  function: large_kb (line 360)
  function: test_search_performance_large_dataset (line 382)
  function: test_save_performance_large_dataset (line 396)
  function: test_load_performance_large_dataset (line 409)
  function: test_memory_usage_large_dataset (line 423)
  class: TestKnowledgeBaseEdgeCases (line 446)
  function: edge_case_kb (line 450)
  function: test_empty_title_handling (line 494)
  function: test_special_characters_handling (line 499)
  function: test_very_long_titles (line 507)
  function: test_empty_content_handling (line 512)
  function: test_none_tags_handling (line 517)
  function: test_malformed_json_handling (line 531)
  function: test_file_permission_handling (line 544)
hypercode\core\tests\test_lexer.py:
  function: test_lexer_basic_tokens (line 5)
  function: test_lexer_strings (line 23)
  function: test_lexer_operators (line 48)
hypercode\core\tests\test_lexer_extended.py:
  function: test_lexer_escaped_strings (line 5)
  function: test_lexer_numbers (line 18)
  function: test_lexer_operators (line 39)
  function: test_lexer_comments (line 86)
  function: test_lexer_whitespace (line 115)
  function: test_lexer_error_handling (line 130)
  function: test_lexer_hex_numbers (line 139)
  function: test_lexer_binary_numbers (line 157)
  function: test_lexer_scientific_notation (line 169)
  function: test_lexer_string_escapes (line 180)
  function: test_lexer_keywords (line 197)
  function: test_lexer_position_tracking (line 223)
  function: test_lexer_error_recovery (line 243)
  function: test_lexer_error_messages (line 252)
hypercode\core\tests\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode\core\tests\test_parser.py:
  function: test_parse_literal (line 12)
  function: test_parse_variable_declaration (line 24)
  function: test_parse_binary_expression (line 37)
hypercode\core\tests\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode\core\tests\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 185)
hypercode\core\tests\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode\core\tests\test_sensory_profiles.py:
  module: test_sensory_profiles (line 0)
  function: test_visual_settings_creation (line 21)
  function: test_audio_settings_creation (line 35)
  function: test_animation_settings_creation (line 44)
  function: test_sensory_profile_creation (line 55)
  function: test_profile_serialization (line 71)
  function: test_profile_file_io (line 92)
  function: test_profile_manager_initialization (line 115)
  function: test_profile_manager_get_profile (line 129)
  function: test_profile_manager_save_custom_profile (line 142)
  function: test_profile_manager_delete_profile (line 169)
hypercode\core\tests\test_syntax.py:
  module: test_syntax (line 0)
  function: test_program_structure (line 8)
  function: test_function_definition (line 26)
  function: test_io_operations (line 49)
  function: test_variables (line 73)
  function: test_loops (line 96)
  function: test_conditionals (line 117)
  function: test_goto (line 142)
  function: test_comments (line 167)
hypercode\core\tests\tests\test_lexer_enhanced.py:
  function: test_lexer_edge_cases (line 7)
  function: test_lexer_error_handling (line 28)
  function: test_lexer_number_literals (line 43)
  function: test_lexer_string_interpolation (line 65)
  function: test_lexer_docstrings (line 79)
hypercode\core\tests\unit\lexer\test_lexer_basic.py:
  module: test_lexer_basic (line 0)
  class: TestLexerBasic (line 9)
  function: test_empty_source (line 12)
  function: test_whitespace_handling (line 19)
  function: test_single_character_tokens (line 27)
  function: test_comments_are_ignored (line 52)
  function: test_string_literals (line 72)
  function: test_number_literals (line 87)
  function: test_identifiers_and_keywords (line 103)
  function: test_error_handling (line 139)
hypercode\core\tests\unit\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode\core\tests\unit\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode\core\tests\unit\test_intent_blocks.py:
  module: test_intent_blocks (line 0)
  function: test_intent_block (line 13)
hypercode\core\tests\unit\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestHyperCodeKnowledgeBase (line 20)
  function: temp_kb (line 24)
  function: sample_documents (line 33)
  function: test_init_empty_kb (line 56)
  function: test_add_document (line 61)
  function: test_add_multiple_documents (line 82)
  function: test_save_and_load (line 92)
  function: test_search_exact_match (line 113)
  function: test_search_tag_matching (line 126)
  function: test_search_related_terms (line 139)
  function: test_search_space_data_boost (line 153)
  function: test_get_context_for_query (line 180)
  function: test_context_length_limit (line 192)
  function: test_list_documents (line 203)
  function: test_empty_search (line 216)
  function: test_search_nonexistent_term (line 221)
  function: test_document_update (line 231)
  class: TestResearchDocument (line 250)
  function: test_document_creation (line 253)
  function: test_document_optional_fields (line 273)
hypercode\core\tests\unit\test_lexer.py:
  module: test_lexer (line 0)
  function: test_lexer (line 12)
  function: run_tests (line 42)
hypercode\core\tests\unit\test_lexer_pytest.py:
  module: test_lexer_pytest (line 0)
  function: test_basic_arithmetic (line 9)
  function: test_variable_declaration (line 25)
  function: test_string_literals (line 40)
hypercode\core\tests\unit\test_mcp_connection.py:
  function: check_port (line 26)
  function: find_running_servers (line 36)
  function: test_server_connection (line 49)
  function: test_all_servers (line 90)
  function: check_dependencies (line 139)
hypercode\core\tests\unit\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode\core\tests\unit\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode\core\tests\unit\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 185)
hypercode\core\tests\unit\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode\core\tests\unit\test_search_algorithm.py:
  module: test_search_algorithm (line 0)
  class: TestSearchAlgorithm (line 20)
  function: populated_kb (line 24)
  function: test_exact_title_match_highest_score (line 80)
  function: test_space_data_boosting (line 92)
  function: test_related_term_expansion (line 105)
  function: test_tag_matching_scoring (line 126)
  function: test_content_frequency_scoring (line 136)
  function: test_partial_word_matching (line 149)
  function: test_query_word_ordering (line 167)
  function: test_case_insensitive_search (line 179)
  function: test_empty_query_returns_no_results (line 202)
  function: test_limit_parameter_respected (line 210)
  function: test_no_results_for_nonexistent_terms (line 219)
  function: test_special_characters_in_query (line 227)
  function: test_unicode_characters (line 237)
  function: test_search_performance_with_large_kb (line 256)
  function: test_search_result_consistency (line 277)
  class: TestSearchScoringDetails (line 292)
  function: scoring_kb (line 296)
  function: test_title_match_beats_content_match (line 324)
  function: test_space_data_boosting_works (line 332)
  function: test_frequency_scoring (line 340)
hypercode\database_analyzer.py:
  module: database_analyzer (line 0)
  class: EntityMetrics (line 15)
  class: DocstringStats (line 21)
  class: DatabaseAnalyzer (line 28)
  function: __init__ (line 29)
  function: load_database (line 48)
  function: analyze_documentation (line 64)
  function: analyze_test_coverage (line 96)
  function: analyze_code_structure (line 112)
  function: generate_report (line 135)
  function: get_entities_needing_docs (line 185)
  function: get_untested_entities (line 191)
  function: main (line 196)
hypercode\fix_database_issues.py:
  module: fix_database_issues (line 0)
  class: FixedCodeEntity (line 19)
  function: from_dict (line 47)
  function: __post_init__ (line 70)
  function: _validate_required_fields (line 81)
  function: _validate_field_types (line 88)
  function: _normalize_fields (line 101)
  function: _clean_docstring (line 139)
  function: to_dict (line 153)
  class: DatabaseFixer (line 171)
  function: __init__ (line 174)
  function: load_database (line 188)
  function: _check_for_issues (line 225)
  function: fix_issues (line 252)
  function: save_database (line 280)
  function: generate_report (line 306)
  function: main (line 347)
hypercode\hypercode\accessibility\adhd_optimizer.py:
  module: adhd_optimizer (line 0)
hypercode\hypercode\accessibility\autism_preset.py:
  module: autism_preset (line 0)
hypercode\hypercode\accessibility\dyslexia_formatter.py:
  module: dyslexia_formatter (line 0)
hypercode\hypercode\accessibility\sensory_customizer.py:
  module: sensory_customizer (line 0)
hypercode\hypercode\accessibility\wcag_auditor.py:
  module: wcag_auditor (line 0)
hypercode\hypercode\benchmarks\__init__.py:
  function: benchmark_lexer (line 13)
  function: print_benchmark_results (line 38)
hypercode\hypercode\benchmarks\benchmarks_lexer.py:
  function: benchmark_lexer (line 7)
  function: print_benchmark_results (line 32)
hypercode\hypercode\build-hyper-database.py:
  module: build-hyper-database (line 0)
  class: HyperDatabaseBuilder (line 39)
  function: __init__ (line 42)
  function: scan_python_file (line 50)
  function: scan_javascript_file (line 96)
  function: should_skip_directory (line 125)
  function: build (line 145)
  function: generate_markdown_report (line 179)
  function: generate_json_report (line 266)
  function: main (line 281)
hypercode\hypercode\knowledge_graph\graph_builder.py:
  module: graph_builder (line 0)
hypercode\hypercode\knowledge_graph\sparql_query.py:
  module: sparql_query (line 0)
hypercode\hypercode\knowledge_graph\update_agent.py:
  module: update_agent (line 0)
hypercode\hypercode\live_research\doc_generator.py:
  module: doc_generator (line 0)
hypercode\hypercode\live_research\github_publisher.py:
  module: github_publisher (line 0)
hypercode\hypercode\live_research\paper_indexer.py:
  module: paper_indexer (line 0)
hypercode\hypercode\live_research\research_crawler.py:
  module: research_crawler (line 0)
hypercode\hypercode\live_research\synthesis_engine.py:
  module: synthesis_engine (line 0)
hypercode\hypercode\mcp\__init__.py:
  module: __init__ (line 0)
hypercode\hypercode\mcp\servers\__init__.py:
  module: __init__ (line 0)
hypercode\hypercode\mcp\servers\aws_cli.py:
  function: main (line 4)
hypercode\hypercode\mcp\servers\aws_resource_manager.py:
  function: main (line 4)
hypercode\hypercode\mcp\servers\code_analysis.py:
  function: main (line 4)
hypercode\hypercode\mcp\servers\dataset_downloader.py:
  function: main (line 4)
hypercode\hypercode\mcp\servers\file_system.py:
  function: main (line 4)
hypercode\hypercode\mcp\servers\human_input.py:
  function: main (line 4)
hypercode\hypercode\mcp\servers\hypercode_syntax.py:
  module: hypercode_syntax (line 0)
  class: HyperCodeSyntaxServer (line 28)
  function: __init__ (line 31)
  function: handle_request (line 35)
  function: _initialize (line 56)
  function: _document_changed (line 79)
  function: _text_hover (line 98)
  function: _completion (line 121)
  function: _parse_document (line 150)
  function: _validate_neurodiversity (line 179)
  function: _generate_diagnostics (line 216)
  function: _get_annotation_hover_info (line 266)
  function: main (line 294)
hypercode\hypercode\mcp\servers\path_service.py:
  function: main (line 4)
hypercode\hypercode\mcp\servers\user_profile_manager.py:
  function: main (line 4)
hypercode\hypercode\mcp\servers\valkey_service.py:
  function: check_redis_connection (line 40)
  function: health_check (line 59)
  function: set_key (line 67)
  function: get_key (line 80)
  function: hset_key (line 95)
  function: hget_key (line 107)
  function: hgetall_hash (line 126)
  function: main (line 144)
hypercode\hypercode\mcp\servers\web_search.py:
  function: main (line 4)
hypercode\hypercode\mcp\setup.py:
  module: setup (line 0)
  function: install_dependencies (line 16)
  function: verify_setup (line 31)
  function: show_next_steps (line 54)
  function: main (line 72)
hypercode\hypercode\mcp\start_servers.py:
  module: start_servers (line 0)
  function: start_server (line 34)
  function: list_servers (line 59)
  function: main (line 66)
hypercode\hypercode\mcp\test_mcp.py:
  module: test_mcp (line 0)
  function: test_server_imports (line 15)
  function: main (line 47)
hypercode\hypercode\new files to check\backend\research\__init__.py:
  module: __init__ (line 0)
hypercode\hypercode\new files to check\backend\research\db.py:
  module: db (line 0)
  function: _get_database_url (line 35)
hypercode\hypercode\new files to check\backend\research\models.py:
  module: models (line 0)
  class: Study (line 32)
  function: __repr__ (line 52)
  class: Source (line 56)
  function: __repr__ (line 81)
  class: LanguageVersion (line 85)
  function: __repr__ (line 102)
  class: Task (line 106)
  function: __repr__ (line 124)
  class: Participant (line 128)
  function: __repr__ (line 144)
  class: Session (line 148)
  function: __repr__ (line 169)
  class: Event (line 176)
  function: __repr__ (line 193)
  class: Feedback (line 199)
  function: __repr__ (line 221)
hypercode\hypercode\new files to check\backend\research\scripts\import_sources_from_folder.py:
  module: import_sources_from_folder (line 0)
  function: infer_kind (line 25)
  function: main (line 36)
hypercode\hypercode\new files to check\backend\research\scripts\seed_basic_data.py:
  module: seed_basic_data (line 0)
  function: main (line 25)
hypercode\hypercode\run_lexer.py:
  function: run_lexer (line 13)
hypercode\hypercode\scripts\style_guide_collector.py:
  module: style_guide_collector (line 0)
  class: StyleGuideCollector (line 18)
  function: __init__ (line 21)
  function: _load_feedback (line 32)
  function: _save_feedback (line 51)
  function: add_feedback (line 60)
  function: _update_analysis (line 102)
  function: analyze_feedback (line 151)
  function: _get_top_items (line 189)
  function: _calculate_consensus (line 212)
  function: _generate_recommendations (line 247)
  function: import_github_issues (line 331)
  function: generate_report (line 354)
  function: interactive_feedback (line 419)
  function: main (line 527)
hypercode\hypercode\scripts\test_perplexity_api.py:
  module: test_perplexity_api (line 0)
  function: main (line 17)
hypercode\hypercode\src\ai_gateway\base_gateway.py:
  module: base_gateway (line 0)
hypercode\hypercode\src\ai_gateway\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\hypercode\src\ai_gateway\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\hypercode\src\ai_gateway\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\hypercode\src\ai_gateway\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\hypercode\src\ai_gateway\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode\hypercode\src\ai_gateway\rag_engine.py:
  module: rag_engine (line 0)
hypercode\hypercode\src\base_gateway.py:
  module: base_gateway (line 0)
hypercode\hypercode\src\build.py:
  module: build (line 0)
  function: build (line 34)
hypercode\hypercode\src\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\hypercode\src\core\__init__.py:
  module: __init__ (line 0)
hypercode\hypercode\src\core\ast.py:
  class: Node (line 9)
  function: accept (line 10)
  class: Expr (line 20)
  class: Literal (line 25)
  class: Variable (line 30)
  class: Assign (line 35)
  class: Binary (line 41)
  class: Unary (line 48)
  class: Grouping (line 54)
  class: Call (line 59)
  class: Get (line 66)
  class: Stmt (line 73)
  class: Expression (line 78)
  class: Print (line 83)
  class: Var (line 88)
  class: Block (line 94)
  class: Intent (line 99)
  class: Function (line 104)
  class: If (line 111)
  class: Return (line 118)
  class: Program (line 125)
hypercode\hypercode\src\core\ast_nodes.py:
  module: ast_nodes (line 0)
  class: Node (line 24)
  class: Expression (line 31)
  class: Statement (line 38)
  class: Program (line 45)
  class: Identifier (line 52)
  class: Literal (line 59)
  class: VariableDeclaration (line 66)
  class: BinaryOperation (line 75)
hypercode\hypercode\src\core\interpreter.py:
  class: RuntimeError (line 8)
  function: __init__ (line 9)
  class: Environment (line 15)
  function: __init__ (line 16)
  function: define (line 20)
  function: get (line 23)
  function: assign (line 30)
  class: Callable (line 40)
  function: arity (line 41)
  function: call (line 44)
  class: Function (line 48)
  function: __init__ (line 49)
  function: call (line 53)
  function: arity (line 65)
  class: ReturnException (line 69)
  function: __init__ (line 70)
  class: Interpreter (line 74)
  function: __init__ (line 75)
  class: Clock (line 82)
  function: arity (line 83)
  function: call (line 86)
  function: __str__ (line 89)
  function: execute_block (line 94)
  function: interpret (line 103)
  function: execute (line 112)
  function: evaluate (line 115)
  function: visit_Expression (line 118)
  function: visit_Print (line 122)
  function: visit_Var (line 129)
  function: visit_Block (line 136)
  function: visit_Expression (line 140)
  function: visit_Print (line 144)
  function: visit_Intent (line 150)
  function: visit_Function (line 155)
  function: visit_Return (line 160)
  function: visit_Literal (line 166)
  function: visit_Grouping (line 169)
  function: visit_Variable (line 172)
  function: visit_Assign (line 175)
  function: visit_Call (line 180)
  function: visit_Binary (line 198)
  function: visit_Unary (line 229)
  function: is_truthy (line 237)
  function: stringify (line 244)
  function: get_output (line 256)
hypercode\hypercode\src\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 17)
  class: Lexer (line 34)
  function: __init__ (line 42)
  function: scan_tokens (line 99)
  function: scan_token (line 109)
  function: number (line 168)
  function: string (line 203)
  function: docstring (line 252)
  function: identifier (line 278)
  function: error (line 288)
  function: is_at_end (line 312)
  function: advance (line 316)
  function: match (line 325)
  function: peek (line 335)
  function: peek_next (line 341)
  function: add_token (line 347)
hypercode\hypercode\src\core\optimizer.py:
  module: optimizer (line 0)
hypercode\hypercode\src\core\parser.py:
  class: ParseError (line 7)
  class: Parser (line 11)
  function: __init__ (line 12)
  function: parse (line 16)
  function: declaration (line 25)
  function: var_declaration (line 36)
  function: statement (line 61)
  function: print_statement (line 72)
  function: expression_statement (line 77)
  function: block (line 82)
  function: expression (line 91)
  function: assignment (line 94)
  function: equality (line 109)
  function: comparison (line 119)
  function: term (line 132)
  function: factor (line 140)
  function: unary (line 148)
  function: primary (line 155)
  function: function (line 177)
  function: if_statement (line 200)
  function: return_statement (line 212)
  function: match (line 222)
  function: consume (line 229)
  function: error (line 239)
  function: synchronize (line 245)
  function: check (line 265)
  function: advance (line 270)
  function: is_at_end (line 275)
  function: peek (line 278)
  function: previous (line 281)
hypercode\hypercode\src\core\tokens.py:
  module: tokens (line 0)
  class: TokenType (line 11)
  class: Token (line 71)
  function: __init__ (line 83)
  function: __str__ (line 92)
  function: __repr__ (line 95)
hypercode\hypercode\src\duelcode\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode\hypercode\src\duelcode\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode\hypercode\src\duelcode\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode\hypercode\src\duelcode\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode\hypercode\src\duelcode\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode\hypercode\src\duelcode\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode\hypercode\src\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode\hypercode\src\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode\hypercode\src\hypercode-backend-js-COMPLETE.py:
  module: hypercode-backend-js-COMPLETE (line 0)
  class: JSCompiler (line 19)
  function: __init__ (line 30)
  function: compile (line 42)
  function: _generate_header (line 65)
  function: _generate_setup (line 74)
  function: _generate_main (line 110)
  function: _generate_footer (line 162)
  function: _indent (line 179)
  function: optimize_ast (line 183)
  function: main (line 200)
hypercode\hypercode\src\hypercode-idea-generator-WEB.py:
  module: hypercode-idea-generator-WEB (line 0)
hypercode\hypercode\src\hypercode-launch-kit.py:
  module: hypercode-launch-kit (line 0)
  class: HyperCodeLaunchKit (line 23)
  function: __init__ (line 26)
  function: create_readme (line 30)
  function: create_launch_checklist (line 367)
  function: create_launch_script (line 620)
  function: create_first_30_days (line 718)
  function: print_summary (line 974)
  function: main (line 1007)
hypercode\hypercode\src\hypercode-lexer-COMPLETE.py:
  module: hypercode-lexer-COMPLETE (line 0)
  class: TokenType (line 21)
  class: Token (line 45)
  function: __repr__ (line 54)
  class: LexerError (line 59)
  function: __init__ (line 62)
  class: HyperCodeLexer (line 69)
  function: __init__ (line 95)
  function: tokenize (line 110)
  function: _advance_position (line 169)
  function: _skip_comment (line 179)
  function: get_tokens (line 184)
  function: filter_tokens (line 188)
  function: print_tokens (line 205)
  function: get_statistics (line 236)
  function: main (line 250)
hypercode\hypercode\src\hypercode-parser-COMPLETE.py:
  module: hypercode-parser-COMPLETE (line 0)
  class: NodeType (line 22)
  class: ASTNode (line 38)
  function: __repr__ (line 51)
  class: ParserError (line 68)
  function: __init__ (line 71)
  class: HyperCodeParser (line 80)
  function: __init__ (line 94)
  function: parse (line 105)
  function: _parse_statement (line 127)
  function: _parse_loop (line 174)
  function: _advance (line 209)
  function: _is_at_end (line 215)
  function: validate (line 222)
  function: print_ast (line 237)
  function: main (line 251)
hypercode\hypercode\src\hypercode\__init__.py:
  module: __init__ (line 0)
hypercode\hypercode\src\hypercode\__main__.py:
  function: main (line 6)
hypercode\hypercode\src\hypercode\config.py:
  module: config (line 0)
  class: Config (line 16)
  function: get_headers (line 27)
hypercode\hypercode\src\hypercode\core\__init__.py:
  module: __init__ (line 0)
hypercode\hypercode\src\hypercode\core\ast.py:
  class: Node (line 9)
  function: accept (line 10)
  class: Expr (line 20)
  class: Literal (line 25)
  class: Variable (line 30)
  class: Assign (line 35)
  class: Binary (line 41)
  class: Unary (line 48)
  class: Grouping (line 54)
  class: Call (line 59)
  class: ListLiteral (line 66)
  class: PipeChain (line 71)
  class: Get (line 81)
  class: Stmt (line 88)
  class: Expression (line 93)
  class: Print (line 98)
  class: Var (line 103)
  class: Block (line 109)
  class: If (line 114)
  class: Fun (line 121)
  class: Return (line 128)
  class: Intent (line 134)
  class: Program (line 141)
hypercode\hypercode\src\hypercode\core\cli.py:
  module: cli (line 0)
hypercode\hypercode\src\hypercode\core\error_handler.py:
  function: report_parse_error (line 4)
  function: report (line 11)
hypercode\hypercode\src\hypercode\core\interpreter.py:
  class: Return (line 7)
  function: __init__ (line 8)
  class: HyperCodeFunction (line 12)
  function: __init__ (line 13)
  function: __str__ (line 17)
  function: arity (line 20)
  function: call (line 23)
  class: Environment (line 36)
  function: __init__ (line 37)
  function: define (line 41)
  function: get (line 44)
  function: assign (line 51)
  class: Interpreter (line 61)
  function: __init__ (line 62)
  function: interpret (line 75)
  function: execute (line 82)
  function: execute_block (line 85)
  function: evaluate (line 94)
  function: visit_Expression (line 97)
  function: visit_Print (line 100)
  function: visit_Var (line 104)
  function: visit_Block (line 110)
  function: visit_Assign (line 113)
  function: visit_Binary (line 118)
  function: visit_Grouping (line 161)
  function: visit_Literal (line 164)
  function: visit_Unary (line 167)
  function: visit_Variable (line 180)
  function: visit_If (line 183)
  function: is_truthy (line 189)
  function: visit_Fun (line 196)
  function: visit_Return (line 200)
  function: visit_Call (line 206)
  function: is_callable (line 219)
  function: visit_ListLiteral (line 223)
  function: visit_PipeChain (line 226)
  class: BuiltinFunction (line 247)
  function: __init__ (line 248)
  function: __str__ (line 252)
  function: arity (line 255)
  function: call (line 259)
  class: Visitor (line 264)
  function: visit_Expression (line 265)
  function: visit_Print (line 268)
  function: visit_Var (line 271)
  function: visit_Block (line 274)
  function: visit_If (line 277)
  function: visit_Fun (line 280)
  function: visit_Return (line 283)
  function: visit_Assign (line 286)
  function: visit_Binary (line 289)
  function: visit_Grouping (line 292)
  function: visit_Literal (line 295)
  function: visit_Unary (line 298)
  function: visit_Variable (line 301)
  function: visit_Call (line 304)
hypercode\hypercode\src\hypercode\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 32)
  function: __init__ (line 35)
  class: Lexer (line 42)
  function: __init__ (line 111)
  function: tokenize (line 128)
  function: _match_patterns (line 163)
  function: _update_position (line 189)
  function: _add_token (line 208)
  function: _handle_unknown (line 272)
hypercode\hypercode\src\hypercode\core\optimizer.py:
  module: optimizer (line 0)
hypercode\hypercode\src\hypercode\core\parser.py:
  class: ParseError (line 7)
  class: Parser (line 11)
  function: __init__ (line 12)
  function: parse (line 16)
  function: declaration (line 25)
  function: var_declaration (line 36)
  function: statement (line 52)
  function: print_statement (line 65)
  function: return_statement (line 70)
  function: intent_statement (line 78)
  function: expression_statement (line 93)
  function: if_statement (line 98)
  function: function (line 110)
  function: block (line 129)
  function: expression (line 136)
  function: pipe_expression (line 140)
  function: assignment (line 151)
  function: equality (line 173)
  function: comparison (line 183)
  function: term (line 196)
  function: factor (line 204)
  function: unary (line 212)
  function: primary (line 219)
  function: _primary (line 236)
  function: finish_call (line 276)
  function: match (line 289)
  function: consume (line 296)
  function: error (line 303)
  function: synchronize (line 309)
  function: check (line 329)
  function: advance (line 334)
  function: is_at_end (line 339)
  function: peek (line 342)
  function: previous (line 345)
hypercode\hypercode\src\hypercode\core\semantic_analyzer.py:
  module: semantic_analyzer (line 0)
hypercode\hypercode\src\hypercode\core\sensory_profile.py:
  module: sensory_profile (line 0)
  class: VisualNoiseLevel (line 15)
  class: AnimationSpeed (line 22)
  class: VisualSettings (line 29)
  class: AudioSettings (line 43)
  class: AnimationSettings (line 58)
  class: SensoryProfile (line 68)
  function: to_dict (line 77)
  function: from_dict (line 85)
  function: save (line 107)
  function: load (line 113)
  class: ProfileManager (line 120)
  function: __init__ (line 123)
  function: _ensure_default_profiles (line 133)
  function: _create_minimal_profile (line 146)
  function: _create_enhanced_profile (line 163)
  function: _create_high_contrast_profile (line 190)
  function: list_profiles (line 216)
  function: get_profile (line 220)
  function: save_profile (line 227)
  function: delete_profile (line 232)
  function: get_profile (line 243)
  function: list_profiles (line 248)
hypercode\hypercode\src\hypercode\core\tokens.py:
  class: TokenType (line 6)
  class: Token (line 65)
  function: __str__ (line 72)
hypercode\hypercode\src\hypercode\enhanced_perplexity_client.py:
  module: enhanced_perplexity_client (line 0)
  class: EnhancedPerplexityClient (line 18)
  function: __init__ (line 21)
  function: query_with_context (line 25)
  function: add_research_data (line 61)
  function: search_research_data (line 71)
  function: list_research_documents (line 75)
  function: get_document (line 79)
  function: delete_document (line 83)
  function: import_from_perplexity_space (line 87)
  function: test_context_integration (line 123)
  function: create_perplexity_space_import_template (line 175)
hypercode\hypercode\src\hypercode\knowledge_base.py:
  module: knowledge_base (line 0)
  class: ResearchDocument (line 17)
  function: __post_init__ (line 28)
  function: generate_id (line 36)
  function: validate (line 41)
  function: update_timestamp (line 53)
  class: HyperCodeKnowledgeBase (line 100)
  function: __init__ (line 103)
  function: load (line 109)
  function: save (line 125)
  function: add_document (line 135)
  function: search_documents (line 163)
  function: get_context_for_query (line 227)
  function: list_documents (line 257)
  function: get_document (line 261)
  function: delete_document (line 265)
  function: update_document (line 273)
  function: search_by_tags (line 287)
  function: get_document_statistics (line 306)
  function: export_format (line 331)
  function: validate_all_documents (line 353)
  function: cleanup_duplicates (line 363)
  function: initialize_sample_data (line 384)
hypercode\hypercode\src\hypercode\perplexity_client.py:
  module: perplexity_client (line 0)
  class: PerplexityClient (line 12)
  function: __init__ (line 15)
  function: query (line 30)
  function: test_connection (line 72)
hypercode\hypercode\src\hypercode\repl.py:
  function: run_repl (line 12)
  function: run (line 33)
  function: show_help (line 54)
hypercode\hypercode\src\hypercode\std\__init__.py:
  module: __init__ (line 0)
hypercode\hypercode\src\hypercode\std\builtins.py:
  module: builtins (line 0)
  function: echo (line 12)
  function: to_string (line 17)
  function: length (line 22)
  function: sum_items (line 32)
  function: add (line 42)
  function: multiply (line 47)
  function: to_list (line 52)
  function: upper (line 66)
  function: head (line 71)
  function: tail (line 79)
  function: get_builtins (line 87)
hypercode\hypercode\src\hypercode_idea_generator.py:
  module: hypercode_idea_generator (line 0)
  class: HyperCodeIdeaGenerator (line 431)
  function: __init__ (line 439)
  function: get_ideas_by_category (line 443)
  function: get_top_ideas (line 468)
  function: vote_for_idea (line 487)
  function: get_trending_ideas (line 497)
  function: format_idea_card (line 502)
  function: main (line 528)
hypercode\hypercode\src\hypercode_poc.py:
  module: hypercode_poc (line 0)
  class: TokenType (line 18)
  class: Token (line 34)
  class: UserConfidenceLevel (line 41)
  class: EnhancedLexer (line 48)
  function: __init__ (line 51)
  function: tokenize (line 74)
  function: handle_string (line 115)
  function: handle_number (line 141)
  function: handle_identifier (line 149)
  function: advance (line 171)
  class: ContextAwareErrorMessenger (line 176)
  function: __init__ (line 179)
  function: format_error (line 182)
  class: SemanticContextStreamer (line 189)
  function: analyze (line 192)
  class: ConfidenceTracker (line 209)
  function: __init__ (line 212)
  function: record (line 216)
  class: HyperCodePOC (line 222)
  function: __init__ (line 225)
  function: compile (line 232)
hypercode\hypercode\src\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\hypercode\src\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\hypercode\src\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\hypercode\src\parser\debug_ascii.py:
  module: debug_ascii (line 0)
  function: test_regex_patterns (line 14)
hypercode\hypercode\src\parser\debug_full.py:
  module: debug_full (line 0)
  function: debug_full_parsing (line 14)
hypercode\hypercode\src\parser\debug_parser.py:
  module: debug_parser (line 0)
  function: debug_annotation_detection (line 14)
hypercode\hypercode\src\parser\debug_simple.py:
  module: debug_simple (line 0)
  function: debug_simple (line 14)
hypercode\hypercode\src\parser\test_parser.py:
  module: test_parser (line 0)
  function: test_first_click_moment (line 14)
hypercode\hypercode\src\parser\visual_syntax_parser.py:
  module: visual_syntax_parser (line 0)
  class: SemanticMarker (line 18)
  class: SemanticAnnotation (line 37)
  function: __str__ (line 46)
  class: ParsedFunction (line 51)
  function: get_annotations_by_type (line 62)
  class: VisualSyntaxParser (line 69)
  function: __init__ (line 72)
  function: _build_semantic_patterns (line 76)
  function: _build_color_scheme (line 105)
  function: parse_file (line 123)
  function: parse_content (line 130)
  function: _is_function_definition (line 170)
  function: _start_new_function (line 179)
  function: _parse_line_annotations (line 202)
  function: _parse_annotation_params (line 223)
  function: generate_syntax_highlighting (line 265)
  function: extract_semantic_summary (line 277)
  function: validate_neurodiversity_compliance (line 311)
hypercode\hypercode\src\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode\hypercode\src\rag_engine.py:
  module: rag_engine (line 0)
hypercode\hypercode\src\scaffold (1).py:
  module: scaffold (1) (line 0)
  function: create_directories (line 141)
  function: create_python_files (line 151)
  function: create_example_files (line 165)
  function: create_root_files (line 202)
  function: create_healthcheck (line 213)
  function: print_summary (line 234)
  function: main (line 259)
hypercode\hypercode\src\scaffold.py:
  module: scaffold (line 0)
  function: create_directories (line 153)
  function: create_python_files (line 184)
  function: create_example_files (line 254)
  function: create_root_files (line 291)
  function: create_healthcheck (line 541)
  function: print_summary (line 583)
  function: main (line 621)
hypercode\hypercode\src\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode\hypercode\src\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode\hypercode\src\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode\hypercode\src\utils\code_analyzer_ai.py:
  module: code_analyzer_ai (line 0)
  class: CodeAnalyzerAI (line 19)
  function: __init__ (line 22)
  function: analyze_file (line 25)
  function: _analyze_complexity (line 72)
  function: _check_docstrings (line 113)
  function: _get_ai_code_analysis (line 155)
  function: analyze_project (line 183)
  function: _get_project_ai_insights (line 230)
  function: save_analysis (line 262)
  function: print_summary (line 270)
  function: main (line 288)
hypercode\hypercode\src\utils\debug_search.py:
  module: debug_search (line 0)
  function: debug_search (line 15)
hypercode\hypercode\src\utils\demo_ai_research.py:
  module: demo_ai_research (line 0)
  function: demo_ai_research_queries (line 16)
  function: test_document_specific_queries (line 90)
hypercode\hypercode\src\utils\demo_enhanced_client.py:
  module: demo_enhanced_client (line 0)
  function: demo_knowledge_base_integration (line 16)
  function: demonstrate_memory_persistence (line 131)
hypercode\hypercode\src\utils\final_integration_test.py:
  module: final_integration_test (line 0)
  function: final_integration_test (line 15)
hypercode\hypercode\src\utils\health_scanner_ai.py:
  module: health_scanner_ai (line 0)
  class: HealthScannerAI (line 18)
  function: __init__ (line 21)
  function: analyze_project_structure (line 25)
  function: analyze_dependencies (line 68)
  function: analyze_security (line 110)
  function: get_ai_recommendations (line 143)
  function: run_full_scan (line 170)
  function: save_report (line 221)
  function: print_summary (line 227)
  function: main (line 247)
hypercode\hypercode\src\utils\import-helper.py:
  module: import-helper (line 0)
  class: SpaceImportHelper (line 13)
  function: __init__ (line 16)
  function: validate_document (line 21)
  function: load_template (line 63)
  function: validate_all (line 83)
  function: generate_report (line 95)
  function: create_import_script (line 141)
  function: create_template_instructions (line 193)
  function: main (line 264)
hypercode\hypercode\src\utils\import_all_space_data.py:
  module: import_all_space_data (line 0)
  function: format_content (line 16)
  function: import_all_hypercode_data (line 41)
hypercode\hypercode\src\utils\import_hypercode_data.py:
  module: import_hypercode_data (line 0)
  function: import_hypercode_space_data (line 16)
hypercode\hypercode\src\utils\import_perplexity_space.py:
  module: import_perplexity_space (line 0)
  function: create_manual_import_script (line 17)
  function: create_json_import_template (line 86)
  function: import_from_json (line 115)
  function: test_imported_data (line 153)
  function: show_import_menu (line 188)
hypercode\hypercode\src\utils\local_health_scanner.py:
  module: local_health_scanner (line 0)
  class: ProjectScanner (line 20)
  function: __init__ (line 23)
  function: scan_project (line 35)
  function: _scan_directory (line 43)
  function: _analyze_file (line 52)
  function: _analyze_ast (line 77)
  function: _check_documentation (line 97)
  function: _check_tests (line 109)
  function: _calculate_metrics (line 120)
  function: print_health_report (line 132)
  function: main (line 163)
hypercode\hypercode\src\utils\perplexity_space_collector.py:
  module: perplexity_space_collector (line 0)
  function: quick_copy_paste_collector (line 18)
  function: create_structured_template (line 117)
  function: show_bro_hacks (line 167)
  function: main_menu (line 207)
hypercode\hypercode\src\utils\perplexity_space_integration.py:
  module: perplexity_space_integration (line 0)
  function: main (line 16)
hypercode\hypercode\src\utils\run_lexer.py:
  function: run_lexer (line 13)
hypercode\hypercode\src\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode\hypercode\test_mcp_connection.py:
  function: check_port (line 26)
  function: find_running_servers (line 36)
  function: test_server_connection (line 49)
  function: test_all_servers (line 90)
  function: check_dependencies (line 139)
hypercode\hypercode\tests\benchmark_knowledge_base.py:
  module: benchmark_knowledge_base (line 0)
  class: BenchmarkSuite (line 24)
  function: __init__ (line 27)
  function: _get_system_info (line 34)
  function: generate_test_data (line 43)
  function: benchmark_operation (line 93)
  function: run_benchmark_suite (line 118)
  function: _calculate_summary (line 274)
  function: _generate_recommendations (line 296)
  function: generate_markdown_report (line 338)
  function: save_json_results (line 467)
  function: main (line 474)
hypercode\hypercode\tests\test_accessibility.py:
  module: test_accessibility (line 0)
hypercode\hypercode\tests\test_ai_gateway.py:
  module: test_ai_gateway (line 0)
hypercode\hypercode\tests\test_backends.py:
  module: test_backends (line 0)
hypercode\hypercode\tests\test_core.py:
  module: test_core (line 0)
  function: run_test (line 30)
hypercode\hypercode\tests\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode\hypercode\tests\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode\hypercode\tests\test_integration.py:
  module: test_integration (line 0)
hypercode\hypercode\tests\test_intent_blocks.py:
  module: test_intent_blocks (line 0)
  function: test_intent_block (line 13)
hypercode\hypercode\tests\test_interpreter.py:
  function: run_code (line 10)
  class: TestInterpreter (line 28)
  function: test_if_statement_then (line 30)
  function: test_if_statement_else (line 42)
  function: test_function_call (line 54)
  function: test_function_with_parameters (line 64)
  function: test_function_with_return (line 74)
  function: test_recursive_function_call (line 85)
  function: test_scoping (line 99)
hypercode\hypercode\tests\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestKnowledgeBaseSearch (line 12)
  function: sample_documents (line 16)
  function: knowledge_base (line 40)
  function: test_basic_search (line 48)
  function: test_search_with_exact_match (line 54)
  function: test_search_case_insensitive (line 59)
  function: test_search_empty_query (line 65)
  function: test_search_no_matches (line 71)
  function: test_search_ranking (line 77)
  function: test_query_normalization (line 90)
  function: test_multi_word_query (line 98)
  function: test_tag_based_search (line 103)
  class: TestEdgeCases (line 112)
  function: knowledge_base (line 116)
  function: test_very_short_query (line 121)
  function: test_very_long_query (line 126)
  function: test_special_characters_in_query (line 136)
  function: test_unicode_in_query (line 141)
  function: test_sql_injection_attempt (line 146)
  function: test_repeated_queries (line 151)
  class: TestPerformance (line 159)
  function: large_knowledge_base (line 163)
  function: test_search_response_time (line 179)
  function: test_concurrent_searches (line 189)
  function: test_memory_usage (line 207)
  class: TestIntegrationWithPerplexity (line 213)
  function: mock_perplexity_client (line 217)
  function: mock_knowledge_base (line 229)
  function: test_enhanced_query_with_context (line 243)
  function: test_fallback_to_perplexity_api (line 259)
  function: test_context_ranking_and_selection (line 273)
  class: TestDocumentManagement (line 288)
  function: knowledge_base (line 292)
  function: test_add_document (line 300)
  function: test_update_document (line 310)
  function: test_remove_document (line 315)
hypercode\hypercode\tests\test_knowledge_base_comprehensive.py:
  module: test_knowledge_base_comprehensive (line 0)
  class: TestKnowledgeBaseUnit (line 20)
  function: temp_kb (line 24)
  function: sample_docs (line 36)
  function: test_init_empty_kb (line 59)
  function: test_add_single_document (line 65)
  function: test_add_multiple_documents (line 74)
  function: test_save_and_load (line 84)
  function: test_search_exact_match (line 102)
  function: test_search_partial_match (line 113)
  function: test_search_tag_matching (line 124)
  function: test_search_case_insensitive (line 135)
  function: test_empty_search (line 147)
  function: test_nonexistent_search (line 155)
  function: test_get_context_for_query (line 165)
  function: test_context_length_limit (line 176)
  function: test_document_update (line 186)
  function: test_list_documents (line 202)
  function: test_delete_document (line 213)
  class: TestKnowledgeBaseIntegration (line 229)
  function: populated_kb (line 233)
  function: test_complex_search_queries (line 277)
  function: test_search_ranking_quality (line 291)
  function: test_related_term_expansion (line 301)
  function: test_performance_with_large_dataset (line 313)
  function: test_concurrent_access_simulation (line 332)
  class: TestKnowledgeBasePerformance (line 356)
  function: large_kb (line 360)
  function: test_search_performance_large_dataset (line 382)
  function: test_save_performance_large_dataset (line 396)
  function: test_load_performance_large_dataset (line 409)
  function: test_memory_usage_large_dataset (line 423)
  class: TestKnowledgeBaseEdgeCases (line 446)
  function: edge_case_kb (line 450)
  function: test_empty_title_handling (line 494)
  function: test_special_characters_handling (line 499)
  function: test_very_long_titles (line 507)
  function: test_empty_content_handling (line 512)
  function: test_none_tags_handling (line 517)
  function: test_malformed_json_handling (line 531)
  function: test_file_permission_handling (line 544)
hypercode\hypercode\tests\test_lexer.py:
  function: test_lexer_basic_tokens (line 5)
  function: test_lexer_strings (line 23)
  function: test_lexer_operators (line 48)
hypercode\hypercode\tests\test_lexer_extended.py:
  function: test_lexer_escaped_strings (line 5)
  function: test_lexer_numbers (line 18)
  function: test_lexer_operators (line 39)
  function: test_lexer_comments (line 86)
  function: test_lexer_whitespace (line 115)
  function: test_lexer_error_handling (line 130)
  function: test_lexer_hex_numbers (line 139)
  function: test_lexer_binary_numbers (line 157)
  function: test_lexer_scientific_notation (line 169)
  function: test_lexer_string_escapes (line 180)
  function: test_lexer_keywords (line 197)
  function: test_lexer_position_tracking (line 223)
  function: test_lexer_error_recovery (line 243)
  function: test_lexer_error_messages (line 252)
hypercode\hypercode\tests\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode\hypercode\tests\test_parser.py:
  function: test_parse_literal (line 12)
  function: test_parse_variable_declaration (line 24)
  function: test_parse_binary_expression (line 37)
hypercode\hypercode\tests\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode\hypercode\tests\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 185)
hypercode\hypercode\tests\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode\hypercode\tests\test_sensory_profiles.py:
  module: test_sensory_profiles (line 0)
  function: test_visual_settings_creation (line 21)
  function: test_audio_settings_creation (line 35)
  function: test_animation_settings_creation (line 44)
  function: test_sensory_profile_creation (line 55)
  function: test_profile_serialization (line 71)
  function: test_profile_file_io (line 92)
  function: test_profile_manager_initialization (line 115)
  function: test_profile_manager_get_profile (line 129)
  function: test_profile_manager_save_custom_profile (line 142)
  function: test_profile_manager_delete_profile (line 169)
hypercode\hypercode\tests\tests\test_lexer_enhanced.py:
  function: test_lexer_edge_cases (line 7)
  function: test_lexer_error_handling (line 28)
  function: test_lexer_number_literals (line 43)
  function: test_lexer_string_interpolation (line 65)
  function: test_lexer_docstrings (line 79)
hypercode\hypercode\tests\unit\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode\hypercode\tests\unit\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode\hypercode\tests\unit\test_intent_blocks.py:
  module: test_intent_blocks (line 0)
  function: test_intent_block (line 13)
hypercode\hypercode\tests\unit\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestHyperCodeKnowledgeBase (line 20)
  function: temp_kb (line 24)
  function: sample_documents (line 33)
  function: test_init_empty_kb (line 56)
  function: test_add_document (line 61)
  function: test_add_multiple_documents (line 82)
  function: test_save_and_load (line 92)
  function: test_search_exact_match (line 113)
  function: test_search_tag_matching (line 126)
  function: test_search_related_terms (line 139)
  function: test_search_space_data_boost (line 153)
  function: test_get_context_for_query (line 180)
  function: test_context_length_limit (line 192)
  function: test_list_documents (line 203)
  function: test_empty_search (line 216)
  function: test_search_nonexistent_term (line 221)
  function: test_document_update (line 231)
  class: TestResearchDocument (line 250)
  function: test_document_creation (line 253)
  function: test_document_optional_fields (line 273)
hypercode\hypercode\tests\unit\test_lexer.py:
  module: test_lexer (line 0)
  function: test_lexer (line 12)
  function: run_tests (line 42)
hypercode\hypercode\tests\unit\test_mcp_connection.py:
  function: check_port (line 26)
  function: find_running_servers (line 36)
  function: test_server_connection (line 49)
  function: test_all_servers (line 90)
  function: check_dependencies (line 139)
hypercode\hypercode\tests\unit\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode\hypercode\tests\unit\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode\hypercode\tests\unit\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 185)
hypercode\hypercode\tests\unit\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode\hypercode\tests\unit\test_search_algorithm.py:
  module: test_search_algorithm (line 0)
  class: TestSearchAlgorithm (line 20)
  function: populated_kb (line 24)
  function: test_exact_title_match_highest_score (line 80)
  function: test_space_data_boosting (line 92)
  function: test_related_term_expansion (line 105)
  function: test_tag_matching_scoring (line 126)
  function: test_content_frequency_scoring (line 136)
  function: test_partial_word_matching (line 149)
  function: test_query_word_ordering (line 167)
  function: test_case_insensitive_search (line 179)
  function: test_empty_query_returns_no_results (line 202)
  function: test_limit_parameter_respected (line 210)
  function: test_no_results_for_nonexistent_terms (line 219)
  function: test_special_characters_in_query (line 227)
  function: test_unicode_characters (line 237)
  function: test_search_performance_with_large_kb (line 256)
  function: test_search_result_consistency (line 277)
  class: TestSearchScoringDetails (line 292)
  function: scoring_kb (line 296)
  function: test_title_match_beats_content_match (line 324)
  function: test_space_data_boosting_works (line 332)
  function: test_frequency_scoring (line 340)
hypercode\hypercode_db.py:
  module: hypercode_db (line 0)
  class: CodeEntity (line 12)
  function: __post_init__ (line 25)
  class: HypercodeDB (line 30)
  function: __init__ (line 37)
  function: _load_database (line 48)
  function: get_entities_by_type (line 96)
  function: get_entities_in_file (line 107)
  function: search_entities (line 118)
  function: print_analysis (line 150)
hypercode\knowledge_graph\graph_builder.py:
  module: graph_builder (line 0)
hypercode\knowledge_graph\sparql_query.py:
  module: sparql_query (line 0)
hypercode\knowledge_graph\update_agent.py:
  module: update_agent (line 0)
hypercode\live_research\cli.py:
  function: print_entry (line 10)
  function: search_entries (line 38)
  function: view_entry (line 59)
  function: add_entry (line 71)
  function: import_entries (line 94)
  function: export_entries (line 126)
  function: main (line 150)
hypercode\live_research\database.py:
  class: ResearchDatabase (line 7)
  function: __init__ (line 8)
  function: _get_connection (line 13)
  function: _create_tables (line 17)
  function: add_research_entry (line 68)
  function: get_research_entry (line 128)
  function: search_entries (line 159)
  function: import_from_json (line 220)
  function: setup_database (line 241)
hypercode\live_research\doc_generator.py:
  module: doc_generator (line 0)
hypercode\live_research\github_publisher.py:
  module: github_publisher (line 0)
hypercode\live_research\import_research.py:
  module: import_research (line 0)
  function: import_research_data (line 18)
hypercode\live_research\paper_indexer.py:
  module: paper_indexer (line 0)
hypercode\live_research\research_crawler.py:
  module: research_crawler (line 0)
hypercode\live_research\synthesis_engine.py:
  module: synthesis_engine (line 0)
hypercode\live_research\web\app.py:
  module: app (line 0)
  function: get_db_connection (line 35)
  function: index (line 43)
  function: view_entry (line 79)
  function: search (line 121)
  function: list_tags (line 194)
  function: api_entries (line 219)
  function: page_not_found (line 246)
  function: server_error (line 252)
  function: format_date_filter (line 258)
hypercode\live_research\web\run.py:
  module: run (line 0)
hypercode\mcp\__init__.py:
  module: __init__ (line 0)
hypercode\mcp\servers\__init__.py:
  module: __init__ (line 0)
hypercode\mcp\servers\aws_cli.py:
  function: main (line 4)
hypercode\mcp\servers\aws_resource_manager.py:
  function: main (line 4)
hypercode\mcp\servers\code_analysis.py:
  function: main (line 4)
hypercode\mcp\servers\dataset_downloader.py:
  function: main (line 4)
hypercode\mcp\servers\file_system.py:
  function: main (line 4)
hypercode\mcp\servers\human_input.py:
  function: main (line 4)
hypercode\mcp\servers\hypercode_syntax.py:
  module: hypercode_syntax (line 0)
  class: HyperCodeSyntaxServer (line 28)
  function: __init__ (line 31)
  function: handle_request (line 35)
  function: _initialize (line 56)
  function: _document_changed (line 79)
  function: _text_hover (line 98)
  function: _completion (line 121)
  function: _parse_document (line 150)
  function: _validate_neurodiversity (line 179)
  function: _generate_diagnostics (line 216)
  function: _get_annotation_hover_info (line 266)
  function: main (line 294)
hypercode\mcp\servers\path_service.py:
  function: main (line 4)
hypercode\mcp\servers\user_profile_manager.py:
  function: main (line 4)
hypercode\mcp\servers\valkey_service.py:
  function: check_redis_connection (line 37)
  function: health_check (line 50)
  function: set_key (line 57)
  function: get_key (line 69)
  function: hset_key (line 83)
  function: hget_key (line 94)
  function: hgetall_hash (line 107)
  function: main (line 124)
hypercode\mcp\servers\web_search.py:
  function: main (line 4)
hypercode\mcp\setup.py:
  module: setup (line 0)
  function: install_dependencies (line 15)
  function: verify_setup (line 27)
  function: show_next_steps (line 45)
  function: main (line 62)
hypercode\mcp\start_servers.py:
  module: start_servers (line 0)
  function: start_server (line 33)
  function: list_servers (line 55)
  function: main (line 61)
hypercode\mcp\test_mcp.py:
  module: test_mcp (line 0)
  function: test_server_imports (line 14)
  function: main (line 48)
hypercode\scripts\build-hyper-database.py:
  module: build-hyper-database (line 0)
  class: HyperDatabaseBuilder (line 21)
  function: __init__ (line 24)
  function: scan_python_file (line 32)
  function: scan_javascript_file (line 78)
  function: should_skip_directory (line 107)
  function: build (line 131)
  function: generate_markdown_report (line 165)
  function: generate_json_report (line 254)
  function: main (line 269)
hypercode\scripts\build_knowledge_base.py:
  module: build_knowledge_base (line 0)
  class: KnowledgeBaseBuilder (line 35)
  function: __init__ (line 38)
  function: should_skip (line 79)
  function: get_file_type (line 162)
  function: process_file (line 244)
  function: build_index (line 287)
  function: main (line 376)
hypercode\scripts\database_utils\__init__.py:
  module: __init__ (line 0)
hypercode\scripts\database_utils\cli.py:
  module: cli (line 0)
  function: get_database_path (line 13)
  function: load_database (line 30)
  function: cmd_stats (line 46)
  function: cmd_search (line 74)
  function: cmd_info (line 116)
  function: main (line 144)
hypercode\scripts\database_utils\db.py:
  module: db (line 0)
  function: init_database (line 40)
  function: get_db_context (line 52)
  function: get_session (line 66)
  function: check_database_health (line 71)
  function: reset_database (line 90)
  function: get_database_stats (line 102)
hypercode\scripts\database_utils\models.py:
  module: models (line 0)
  class: ResearchAgent (line 17)
  function: __repr__ (line 33)
  class: ResearchTask (line 37)
  function: __repr__ (line 71)
  class: ResearchPaper (line 75)
  function: __repr__ (line 102)
  class: KnowledgeNode (line 110)
  function: __repr__ (line 141)
  class: KnowledgeRelationship (line 145)
  function: __repr__ (line 173)
  class: ConflictRecord (line 177)
  function: __repr__ (line 208)
hypercode\scripts\document_processor.py:
  module: document_processor (line 0)
  class: DocumentProcessor (line 15)
  function: get_file_hash (line 19)
  function: extract_metadata (line 29)
  function: extract_pdf_content (line 43)
  function: extract_markdown_content (line 74)
  function: extract_docx_content (line 99)
  function: extract_csv_content (line 133)
  function: extract_text_content (line 154)
  function: process_document (line 167)
hypercode\scripts\enhanced_database_builder.py:
  module: enhanced_database_builder (line 0)
  class: Entity (line 35)
  class: EnhancedHyperDatabaseBuilder (line 51)
  function: __init__ (line 66)
  function: _setup_output_dir (line 82)
  function: should_skip_directory (line 86)
  function: scan_python_file (line 100)
  function: _calculate_complexity (line 163)
  function: build (line 185)
  function: _generate_reports (line 207)
  function: _generate_markdown_report (line 221)
  function: _generate_json_report (line 251)
  function: _generate_metrics_report (line 272)
  function: _generate_health_snapshot (line 309)
  function: _generate_project_structure (line 326)
  function: _generate_doc_coverage (line 342)
  function: _generate_entities_list (line 374)
  function: _generate_recommendations (line 393)
  function: main (line 443)
hypercode\scripts\extract-manifests.py:
  module: extract-manifests (line 0)
  class: ManifestEntry (line 51)
  function: load_schema (line 57)
  function: iter_hc_files (line 62)
  function: parse_front_matter (line 87)
  function: validate_manifest (line 121)
  function: collect_manifests (line 133)
  function: update_database (line 150)
  function: write_report (line 183)
  function: main (line 198)
hypercode\scripts\generate_directory_readmes.py:
  module: generate_directory_readmes (line 0)
  function: create_readme (line 9)
  function: main (line 20)
hypercode\scripts\hc-manifest-lint.py:
  module: hc-manifest-lint (line 0)
  function: iter_hc_files (line 47)
  function: parse_front_matter (line 71)
  function: validate_schema (line 95)
  function: apply_rules (line 108)
  function: main (line 137)
hypercode\scripts\organize_docs.py:
  module: organize_docs (line 0)
  function: setup_directories (line 131)
  function: move_files (line 138)
  function: generate_report (line 172)
  function: main (line 204)
hypercode\scripts\reorganize_repo.py:
  module: reorganize_repo (line 0)
  function: create_directories (line 29)
  function: move_files (line 37)
  function: update_gitignore (line 71)
  function: main (line 83)
hypercode\scripts\run_lexer.py:
  module: run_lexer (line 0)
  class: TestLexer (line 18)
  function: setUp (line 21)
  function: test_empty_source (line 25)
  function: test_basic_tokens (line 31)
  function: test_string_literals (line 44)
  function: test_numbers (line 58)
  function: test_arithmetic_expressions (line 83)
  function: test_comments (line 107)
  function: test_error_handling (line 121)
  function: test_error_recovery (line 153)
  function: _assert_token_types (line 179)
  function: test_lexer_error_class (line 201)
hypercode\scripts\run_tests.py:
  module: run_tests (line 0)
  function: run_tests (line 16)
  function: main (line 49)
hypercode\scripts\style_guide_collector.py:
  module: style_guide_collector (line 0)
  class: StyleGuideCollector (line 17)
  function: __init__ (line 20)
  function: _load_feedback (line 31)
  function: _save_feedback (line 50)
  function: add_feedback (line 59)
  function: _update_analysis (line 101)
  function: analyze_feedback (line 150)
  function: _get_top_items (line 176)
  function: _calculate_consensus (line 201)
  function: _generate_recommendations (line 230)
  function: import_github_issues (line 288)
  function: generate_report (line 309)
  function: interactive_feedback (line 370)
  function: main (line 469)
hypercode\scripts\sync-space-to-main.py:
  module: sync-space-to-main (line 0)
  function: log_error (line 25)
  class: Colors (line 37)
  function: log_info (line 46)
  function: log_success (line 51)
  function: log_warning (line 56)
  function: deep_merge (line 61)
  function: load_config (line 72)
  function: should_skip_file (line 112)
  function: get_all_files (line 135)
  function: copy_file (line 145)
  function: remove_file (line 157)
  function: sync_folder (line 168)
  function: delete_orphans (line 212)
  function: sync_all_mappings (line 229)
  function: write_log (line 281)
  function: print_summary (line 303)
  function: main (line 327)
hypercode\scripts\test_mcp_connection.py:
  function: check_port (line 25)
  function: find_running_servers (line 34)
  function: test_server_connection (line 46)
  function: test_all_servers (line 82)
  function: check_dependencies (line 124)
hypercode\scripts\test_perplexity_api.py:
  module: test_perplexity_api (line 0)
  function: main (line 17)
hypercode\scripts\update_doc_links.py:
  module: update_doc_links (line 0)
  function: update_links_in_file (line 27)
  function: replace_link (line 39)
  function: main (line 63)
hypercode\scripts\web_interface.py:
  function: load_index (line 18)
  function: search_documents (line 24)
  function: index (line 58)
  function: search (line 63)
  function: get_document (line 71)
  function: serve_static (line 80)
  function: create_template_if_not_exists (line 84)
hypercode\src\hypercode\DuelCode\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode\src\hypercode\DuelCode\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode\src\hypercode\DuelCode\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode\src\hypercode\DuelCode\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode\src\hypercode\DuelCode\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode\src\hypercode\DuelCode\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode\src\hypercode\accessibility\adhd_optimizer.py:
  module: adhd_optimizer (line 0)
hypercode\src\hypercode\accessibility\autism_preset.py:
  module: autism_preset (line 0)
hypercode\src\hypercode\accessibility\dyslexia_formatter.py:
  module: dyslexia_formatter (line 0)
hypercode\src\hypercode\accessibility\sensory_customizer.py:
  module: sensory_customizer (line 0)
hypercode\src\hypercode\accessibility\wcag_auditor.py:
  module: wcag_auditor (line 0)
hypercode\src\hypercode\ai_gateway\base_gateway.py:
  module: base_gateway (line 0)
hypercode\src\hypercode\ai_gateway\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\src\hypercode\ai_gateway\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\src\hypercode\ai_gateway\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\src\hypercode\ai_gateway\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode\src\hypercode\ai_gateway\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode\src\hypercode\ai_gateway\rag_engine.py:
  module: rag_engine (line 0)
hypercode\src\hypercode\code_analyzer_ai.py:
  module: code_analyzer_ai (line 0)
  class: CodeAnalyzerAI (line 20)
  function: __init__ (line 23)
  function: analyze_file (line 26)
  function: _analyze_complexity (line 62)
  function: _check_docstrings (line 99)
  function: _get_ai_code_analysis (line 135)
  function: analyze_project (line 163)
  function: _get_project_ai_insights (line 207)
  function: save_analysis (line 239)
  function: print_summary (line 245)
  function: main (line 263)
hypercode\src\hypercode\debug_search.py:
  module: debug_search (line 0)
  function: debug_search (line 15)
hypercode\src\hypercode\demo_ai_research.py:
  module: demo_ai_research (line 0)
  function: demo_ai_research_queries (line 16)
  function: test_document_specific_queries (line 90)
hypercode\src\hypercode\demo_enhanced_client.py:
  module: demo_enhanced_client (line 0)
  function: demo_knowledge_base_integration (line 16)
  function: demonstrate_memory_persistence (line 131)
hypercode\src\hypercode\final_integration_test.py:
  module: final_integration_test (line 0)
  function: final_integration_test (line 15)
hypercode\src\hypercode\health_scanner_ai.py:
  module: health_scanner_ai (line 0)
  class: HealthScannerAI (line 19)
  function: __init__ (line 22)
  function: analyze_project_structure (line 26)
  function: analyze_dependencies (line 65)
  function: analyze_security (line 101)
  function: get_ai_recommendations (line 138)
  function: run_full_scan (line 165)
  function: save_report (line 216)
  function: print_summary (line 222)
  function: main (line 242)
hypercode\src\hypercode\import-helper.py:
  module: import-helper (line 0)
  class: SpaceImportHelper (line 13)
  function: __init__ (line 16)
  function: validate_document (line 21)
  function: load_template (line 63)
  function: validate_all (line 83)
  function: generate_report (line 95)
  function: create_import_script (line 141)
  function: create_template_instructions (line 193)
  function: main (line 264)
hypercode\src\hypercode\import_all_space_data.py:
  module: import_all_space_data (line 0)
  function: format_content (line 16)
  function: import_all_hypercode_data (line 41)
hypercode\src\hypercode\import_hypercode_data.py:
  module: import_hypercode_data (line 0)
  function: import_hypercode_space_data (line 16)
hypercode\src\hypercode\import_perplexity_space.py:
  module: import_perplexity_space (line 0)
  function: create_manual_import_script (line 17)
  function: create_json_import_template (line 86)
  function: import_from_json (line 115)
  function: test_imported_data (line 153)
  function: show_import_menu (line 188)
hypercode\src\hypercode\knowledge_graph\graph_builder.py:
  module: graph_builder (line 0)
hypercode\src\hypercode\knowledge_graph\sparql_query.py:
  module: sparql_query (line 0)
hypercode\src\hypercode\knowledge_graph\update_agent.py:
  module: update_agent (line 0)
hypercode\src\hypercode\live_research\doc_generator.py:
  module: doc_generator (line 0)
hypercode\src\hypercode\live_research\github_publisher.py:
  module: github_publisher (line 0)
hypercode\src\hypercode\live_research\paper_indexer.py:
  module: paper_indexer (line 0)
hypercode\src\hypercode\live_research\research_crawler.py:
  module: research_crawler (line 0)
hypercode\src\hypercode\live_research\synthesis_engine.py:
  module: synthesis_engine (line 0)
hypercode\src\hypercode\mcp\servers\aws_cli.py:
  function: main (line 4)
hypercode\src\hypercode\mcp\servers\aws_resource_manager.py:
  function: main (line 4)
hypercode\src\hypercode\mcp\servers\code_analysis.py:
  function: main (line 4)
hypercode\src\hypercode\mcp\servers\dataset_downloader.py:
  function: main (line 4)
hypercode\src\hypercode\mcp\servers\file_system.py:
  function: main (line 4)
hypercode\src\hypercode\mcp\servers\human_input.py:
  function: main (line 4)
hypercode\src\hypercode\mcp\servers\hypercode_syntax.py:
  module: hypercode_syntax (line 0)
  class: HyperCodeSyntaxServer (line 28)
  function: __init__ (line 31)
  function: handle_request (line 35)
  function: _initialize (line 56)
  function: _document_changed (line 79)
  function: _text_hover (line 98)
  function: _completion (line 121)
  function: _parse_document (line 150)
  function: _validate_neurodiversity (line 179)
  function: _generate_diagnostics (line 216)
  function: _get_annotation_hover_info (line 266)
  function: main (line 294)
hypercode\src\hypercode\mcp\servers\path_service.py:
  function: main (line 4)
hypercode\src\hypercode\mcp\servers\user_profile_manager.py:
  function: main (line 4)
hypercode\src\hypercode\mcp\servers\valkey_service.py:
  function: main (line 4)
hypercode\src\hypercode\mcp\servers\web_search.py:
  function: main (line 4)
hypercode\src\hypercode\perplexity_space_collector.py:
  module: perplexity_space_collector (line 0)
  function: quick_copy_paste_collector (line 18)
  function: create_structured_template (line 117)
  function: show_bro_hacks (line 167)
  function: main_menu (line 207)
hypercode\src\hypercode\perplexity_space_integration.py:
  module: perplexity_space_integration (line 0)
  function: main (line 16)
hypercode\src\hypercode\scripts\test_perplexity_api.py:
  module: test_perplexity_api (line 0)
  function: main (line 17)
hypercode\src\hypercode\src\build.py:
  module: build (line 0)
  function: build (line 34)
hypercode\src\hypercode\src\core\ast_nodes.py:
  module: ast_nodes (line 0)
  class: Node (line 24)
  class: Expression (line 31)
  class: Statement (line 38)
  class: Program (line 45)
  class: Identifier (line 52)
  class: Literal (line 59)
  class: VariableDeclaration (line 66)
  class: BinaryOperation (line 75)
hypercode\src\hypercode\src\core\lexer.py:
  class: LexerError (line 8)
  class: Lexer (line 15)
  function: __init__ (line 32)
  function: tokenize (line 87)
  function: is_at_end (line 111)
  function: scan_token (line 114)
  function: advance (line 205)
  function: add_token (line 210)
  function: error (line 223)
  function: synchronize (line 239)
  function: previous (line 251)
  function: peek_next (line 257)
  function: match (line 263)
  function: peek (line 272)
  function: peek_next (line 277)
  function: string (line 282)
  function: is_digit (line 344)
  function: number (line 348)
  function: is_alpha (line 403)
  function: is_alphanumeric (line 407)
  function: is_hex_digit (line 411)
  function: identifier (line 415)
hypercode\src\hypercode\src\core\optimizer.py:
  module: optimizer (line 0)
hypercode\src\hypercode\src\core\parser.py:
  class: ParseError (line 8)
  class: Parser (line 12)
  function: __init__ (line 13)
  function: parse (line 17)
  function: declaration (line 26)
  function: var_declaration (line 39)
  function: statement (line 64)
  function: print_statement (line 71)
  function: expression_statement (line 76)
  function: block (line 81)
  function: expression (line 88)
  function: assignment (line 91)
  function: equality (line 106)
  function: comparison (line 116)
  function: term (line 129)
  function: factor (line 137)
  function: unary (line 145)
  function: primary (line 152)
  function: match (line 184)
  function: consume (line 191)
  function: error (line 201)
  function: synchronize (line 207)
  function: check (line 227)
  function: advance (line 232)
  function: is_at_end (line 237)
  function: peek (line 240)
  function: previous (line 243)
hypercode\src\hypercode\src\hypercode-backend-js-COMPLETE.py:
  module: hypercode-backend-js-COMPLETE (line 0)
  class: JSCompiler (line 19)
  function: __init__ (line 30)
  function: compile (line 42)
  function: _generate_header (line 65)
  function: _generate_setup (line 74)
  function: _generate_main (line 110)
  function: _generate_footer (line 162)
  function: _indent (line 179)
  function: optimize_ast (line 183)
  function: main (line 200)
hypercode\src\hypercode\src\hypercode-idea-generator-WEB.py:
  module: hypercode-idea-generator-WEB (line 0)
hypercode\src\hypercode\src\hypercode-launch-kit.py:
  module: hypercode-launch-kit (line 0)
  class: HyperCodeLaunchKit (line 23)
  function: __init__ (line 26)
  function: create_readme (line 30)
  function: create_launch_checklist (line 367)
  function: create_launch_script (line 620)
  function: create_first_30_days (line 718)
  function: print_summary (line 974)
  function: main (line 1007)
hypercode\src\hypercode\src\hypercode-lexer-COMPLETE.py:
  module: hypercode-lexer-COMPLETE (line 0)
  class: TokenType (line 21)
  class: Token (line 45)
  function: __repr__ (line 54)
  class: LexerError (line 59)
  function: __init__ (line 62)
  class: HyperCodeLexer (line 69)
  function: __init__ (line 95)
  function: tokenize (line 110)
  function: _advance_position (line 169)
  function: _skip_comment (line 179)
  function: get_tokens (line 184)
  function: filter_tokens (line 188)
  function: print_tokens (line 205)
  function: get_statistics (line 236)
  function: main (line 250)
hypercode\src\hypercode\src\hypercode-parser-COMPLETE.py:
  module: hypercode-parser-COMPLETE (line 0)
  class: NodeType (line 22)
  class: ASTNode (line 38)
  function: __repr__ (line 51)
  class: ParserError (line 68)
  function: __init__ (line 71)
  class: HyperCodeParser (line 80)
  function: __init__ (line 94)
  function: parse (line 105)
  function: _parse_statement (line 127)
  function: _parse_loop (line 174)
  function: _advance (line 209)
  function: _is_at_end (line 215)
  function: validate (line 222)
  function: print_ast (line 237)
  function: main (line 251)
hypercode\src\hypercode\src\hypercode\__init__.py:
  module: __init__ (line 0)
hypercode\src\hypercode\src\hypercode\__main__.py:
  function: main (line 6)
hypercode\src\hypercode\src\hypercode\config.py:
  module: config (line 0)
  class: Config (line 16)
  function: get_headers (line 27)
hypercode\src\hypercode\src\hypercode\core\__init__.py:
  module: __init__ (line 0)
hypercode\src\hypercode\src\hypercode\core\ast.py:
  class: Node (line 9)
  function: accept (line 10)
  class: Expr (line 20)
  class: Literal (line 25)
  class: Variable (line 30)
  class: Assign (line 35)
  class: Binary (line 41)
  class: Unary (line 48)
  class: Grouping (line 54)
  class: Stmt (line 60)
  class: Expression (line 65)
  class: Print (line 70)
  class: Var (line 75)
  class: Block (line 81)
  class: Program (line 87)
hypercode\src\hypercode\src\hypercode\core\cli.py:
  module: cli (line 0)
hypercode\src\hypercode\src\hypercode\core\error_handler.py:
  function: report_parse_error (line 5)
  function: report (line 12)
hypercode\src\hypercode\src\hypercode\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 32)
  function: __init__ (line 35)
  class: Lexer (line 42)
  function: __init__ (line 108)
  function: tokenize (line 125)
  function: _match_patterns (line 160)
  function: _update_position (line 186)
  function: _add_token (line 205)
  function: _handle_unknown (line 269)
hypercode\src\hypercode\src\hypercode\core\optimizer.py:
  module: optimizer (line 0)
hypercode\src\hypercode\src\hypercode\core\parser.py:
  class: ParseError (line 8)
  class: Parser (line 12)
  function: __init__ (line 13)
  function: parse (line 17)
  function: declaration (line 26)
  function: var_declaration (line 39)
  function: statement (line 64)
  function: print_statement (line 71)
  function: expression_statement (line 76)
  function: block (line 81)
  function: expression (line 88)
  function: assignment (line 91)
  function: equality (line 106)
  function: comparison (line 116)
  function: term (line 129)
  function: factor (line 137)
  function: unary (line 145)
  function: primary (line 152)
  function: match (line 184)
  function: consume (line 191)
  function: error (line 201)
  function: synchronize (line 207)
  function: check (line 227)
  function: advance (line 232)
  function: is_at_end (line 237)
  function: peek (line 240)
  function: previous (line 243)
hypercode\src\hypercode\src\hypercode\core\semantic_analyzer.py:
  module: semantic_analyzer (line 0)
hypercode\src\hypercode\src\hypercode\core\tokens.py:
  class: TokenType (line 6)
  class: Token (line 60)
  function: __str__ (line 67)
hypercode\src\hypercode\src\hypercode\enhanced_perplexity_client.py:
  module: enhanced_perplexity_client (line 0)
  class: EnhancedPerplexityClient (line 18)
  function: __init__ (line 21)
  function: query_with_context (line 25)
  function: add_research_data (line 61)
  function: search_research_data (line 71)
  function: list_research_documents (line 75)
  function: get_document (line 79)
  function: delete_document (line 83)
  function: import_from_perplexity_space (line 87)
  function: test_context_integration (line 123)
  function: create_perplexity_space_import_template (line 175)
hypercode\src\hypercode\src\hypercode\knowledge_base.py:
  module: knowledge_base (line 0)
  class: ResearchDocument (line 17)
  function: __post_init__ (line 28)
  function: generate_id (line 36)
  function: validate (line 41)
  function: update_timestamp (line 53)
  class: HyperCodeKnowledgeBase (line 100)
  function: __init__ (line 103)
  function: load (line 109)
  function: save (line 125)
  function: add_document (line 135)
  function: search_documents (line 163)
  function: get_context_for_query (line 227)
  function: list_documents (line 257)
  function: get_document (line 261)
  function: delete_document (line 265)
  function: update_document (line 273)
  function: search_by_tags (line 287)
  function: get_document_statistics (line 306)
  function: export_format (line 331)
  function: validate_all_documents (line 353)
  function: cleanup_duplicates (line 363)
  function: initialize_sample_data (line 384)
hypercode\src\hypercode\src\hypercode\perplexity_client.py:
  module: perplexity_client (line 0)
  class: PerplexityClient (line 12)
  function: __init__ (line 15)
  function: query (line 30)
  function: test_connection (line 72)
hypercode\src\hypercode\src\hypercode\repl.py:
  function: run_repl (line 7)
  function: run (line 22)
hypercode\src\hypercode\src\hypercode_idea_generator.py:
  module: hypercode_idea_generator (line 0)
  class: HyperCodeIdeaGenerator (line 431)
  function: __init__ (line 439)
  function: get_ideas_by_category (line 443)
  function: get_top_ideas (line 468)
  function: vote_for_idea (line 487)
  function: get_trending_ideas (line 497)
  function: format_idea_card (line 502)
  function: main (line 528)
hypercode\src\hypercode\src\hypercode_lexer_fixed.py:
  module: hypercode_lexer_fixed (line 0)
  class: TokenType (line 19)
  class: Token (line 44)
  function: __repr__ (line 54)
  class: LexerError (line 68)
  function: __init__ (line 71)
  class: HyperCodeLexerFixed (line 84)
  function: __init__ (line 125)
  function: tokenize (line 145)
  function: _parse_string (line 217)
  function: _skip_comment (line 300)
  function: _advance (line 305)
  function: print_tokens (line 315)
  function: run_tests (line 329)
  function: main (line 446)
hypercode\src\hypercode\src\hypercode_poc.py:
  module: hypercode_poc (line 0)
  class: TokenType (line 18)
  class: Token (line 34)
  class: UserConfidenceLevel (line 41)
  class: EnhancedLexer (line 48)
  function: __init__ (line 51)
  function: tokenize (line 74)
  function: handle_string (line 115)
  function: handle_number (line 141)
  function: handle_identifier (line 149)
  function: advance (line 171)
  class: ContextAwareErrorMessenger (line 176)
  function: __init__ (line 179)
  function: format_error (line 182)
  class: SemanticContextStreamer (line 189)
  function: analyze (line 192)
  class: ConfidenceTracker (line 209)
  function: __init__ (line 212)
  function: record (line 216)
  class: HyperCodePOC (line 222)
  function: __init__ (line 225)
  function: compile (line 232)
hypercode\src\hypercode\src\parser\debug_ascii.py:
  module: debug_ascii (line 0)
  function: test_regex_patterns (line 14)
hypercode\src\hypercode\src\parser\debug_full.py:
  module: debug_full (line 0)
  function: debug_full_parsing (line 14)
hypercode\src\hypercode\src\parser\debug_parser.py:
  module: debug_parser (line 0)
  function: debug_annotation_detection (line 14)
hypercode\src\hypercode\src\parser\debug_simple.py:
  module: debug_simple (line 0)
  function: debug_simple (line 14)
hypercode\src\hypercode\src\parser\test_parser.py:
  module: test_parser (line 0)
  function: test_first_click_moment (line 14)
hypercode\src\hypercode\src\parser\visual_syntax_parser.py:
  module: visual_syntax_parser (line 0)
  class: SemanticMarker (line 18)
  class: SemanticAnnotation (line 37)
  function: __str__ (line 46)
  class: ParsedFunction (line 51)
  function: get_annotations_by_type (line 62)
  class: VisualSyntaxParser (line 69)
  function: __init__ (line 72)
  function: _build_semantic_patterns (line 76)
  function: _build_color_scheme (line 105)
  function: parse_file (line 123)
  function: parse_content (line 130)
  function: _is_function_definition (line 170)
  function: _start_new_function (line 179)
  function: _parse_line_annotations (line 202)
  function: _parse_annotation_params (line 223)
  function: generate_syntax_highlighting (line 265)
  function: extract_semantic_summary (line 277)
  function: validate_neurodiversity_compliance (line 311)
hypercode\src\hypercode\src\scaffold (1).py:
  module: scaffold (1) (line 0)
  function: create_directories (line 141)
  function: create_python_files (line 151)
  function: create_example_files (line 165)
  function: create_root_files (line 202)
  function: create_healthcheck (line 213)
  function: print_summary (line 234)
  function: main (line 259)
hypercode\src\hypercode\src\scaffold.py:
  module: scaffold (line 0)
  function: create_directories (line 153)
  function: create_python_files (line 184)
  function: create_example_files (line 254)
  function: create_root_files (line 291)
  function: create_healthcheck (line 541)
  function: print_summary (line 583)
  function: main (line 621)
hypercode\src\hypercode\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode\src\hypercode\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode\src\hypercode\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode\src\hypercode\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode\src\hypercode\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 183)
hypercode\src\hypercode\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode\src\hypercode\tests\benchmark_knowledge_base.py:
  module: benchmark_knowledge_base (line 0)
  class: BenchmarkSuite (line 24)
  function: __init__ (line 27)
  function: _get_system_info (line 34)
  function: generate_test_data (line 43)
  function: benchmark_operation (line 93)
  function: run_benchmark_suite (line 118)
  function: _calculate_summary (line 274)
  function: _generate_recommendations (line 296)
  function: generate_markdown_report (line 338)
  function: save_json_results (line 467)
  function: main (line 474)
hypercode\src\hypercode\tests\test_accessibility.py:
  module: test_accessibility (line 0)
hypercode\src\hypercode\tests\test_ai_gateway.py:
  module: test_ai_gateway (line 0)
hypercode\src\hypercode\tests\test_backends.py:
  module: test_backends (line 0)
hypercode\src\hypercode\tests\test_core.py:
  module: test_core (line 0)
  function: run_test (line 29)
hypercode\src\hypercode\tests\test_integration.py:
  module: test_integration (line 0)
hypercode\src\hypercode\tests\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestKnowledgeBaseSearch (line 12)
  function: sample_documents (line 16)
  function: knowledge_base (line 40)
  function: test_basic_search (line 48)
  function: test_search_with_exact_match (line 54)
  function: test_search_case_insensitive (line 59)
  function: test_search_empty_query (line 65)
  function: test_search_no_matches (line 71)
  function: test_search_ranking (line 77)
  function: test_query_normalization (line 88)
  function: test_multi_word_query (line 96)
  function: test_tag_based_search (line 101)
  class: TestEdgeCases (line 110)
  function: knowledge_base (line 114)
  function: test_very_short_query (line 119)
  function: test_very_long_query (line 124)
  function: test_special_characters_in_query (line 134)
  function: test_unicode_in_query (line 139)
  function: test_sql_injection_attempt (line 144)
  function: test_repeated_queries (line 149)
  class: TestPerformance (line 157)
  function: large_knowledge_base (line 161)
  function: test_search_response_time (line 177)
  function: test_concurrent_searches (line 187)
  function: test_memory_usage (line 205)
  class: TestIntegrationWithPerplexity (line 211)
  function: mock_perplexity_client (line 215)
  function: mock_knowledge_base (line 227)
  function: test_enhanced_query_with_context (line 241)
  function: test_fallback_to_perplexity_api (line 255)
  function: test_context_ranking_and_selection (line 267)
  class: TestDocumentManagement (line 282)
  function: knowledge_base (line 286)
  function: test_add_document (line 294)
  function: test_update_document (line 304)
  function: test_remove_document (line 309)
hypercode\src\hypercode\tests\test_knowledge_base_comprehensive.py:
  module: test_knowledge_base_comprehensive (line 0)
  class: TestKnowledgeBaseUnit (line 20)
  function: temp_kb (line 24)
  function: sample_docs (line 36)
  function: test_init_empty_kb (line 59)
  function: test_add_single_document (line 65)
  function: test_add_multiple_documents (line 74)
  function: test_save_and_load (line 84)
  function: test_search_exact_match (line 102)
  function: test_search_partial_match (line 113)
  function: test_search_tag_matching (line 124)
  function: test_search_case_insensitive (line 135)
  function: test_empty_search (line 147)
  function: test_nonexistent_search (line 155)
  function: test_get_context_for_query (line 165)
  function: test_context_length_limit (line 176)
  function: test_document_update (line 186)
  function: test_list_documents (line 202)
  function: test_delete_document (line 213)
  class: TestKnowledgeBaseIntegration (line 229)
  function: populated_kb (line 233)
  function: test_complex_search_queries (line 277)
  function: test_search_ranking_quality (line 291)
  function: test_related_term_expansion (line 301)
  function: test_performance_with_large_dataset (line 313)
  function: test_concurrent_access_simulation (line 332)
  class: TestKnowledgeBasePerformance (line 356)
  function: large_kb (line 360)
  function: test_search_performance_large_dataset (line 382)
  function: test_save_performance_large_dataset (line 396)
  function: test_load_performance_large_dataset (line 409)
  function: test_memory_usage_large_dataset (line 423)
  class: TestKnowledgeBaseEdgeCases (line 446)
  function: edge_case_kb (line 450)
  function: test_empty_title_handling (line 494)
  function: test_special_characters_handling (line 499)
  function: test_very_long_titles (line 507)
  function: test_empty_content_handling (line 512)
  function: test_none_tags_handling (line 517)
  function: test_malformed_json_handling (line 531)
  function: test_file_permission_handling (line 544)
hypercode\src\hypercode\tests\test_lexer.py:
  function: test_lexer_basic_tokens (line 5)
  function: test_lexer_strings (line 23)
  function: test_lexer_operators (line 48)
hypercode\src\hypercode\tests\test_lexer_extended.py:
  function: test_lexer_escaped_strings (line 5)
  function: test_lexer_numbers (line 18)
  function: test_lexer_operators (line 39)
  function: test_lexer_comments (line 86)
  function: test_lexer_whitespace (line 115)
  function: test_lexer_error_handling (line 130)
  function: test_lexer_hex_numbers (line 139)
  function: test_lexer_binary_numbers (line 157)
  function: test_lexer_scientific_notation (line 169)
  function: test_lexer_string_escapes (line 180)
  function: test_lexer_keywords (line 197)
  function: test_lexer_position_tracking (line 223)
  function: test_lexer_error_recovery (line 243)
  function: test_lexer_error_messages (line 252)
hypercode\src\hypercode\tests\test_parser.py:
  function: test_parse_literal (line 12)
  function: test_parse_variable_declaration (line 24)
  function: test_parse_binary_expression (line 37)
hypercode\src\hypercode\tests\unit\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestHyperCodeKnowledgeBase (line 20)
  function: temp_kb (line 24)
  function: sample_documents (line 33)
  function: test_init_empty_kb (line 56)
  function: test_add_document (line 61)
  function: test_add_multiple_documents (line 82)
  function: test_save_and_load (line 92)
  function: test_search_exact_match (line 113)
  function: test_search_tag_matching (line 126)
  function: test_search_related_terms (line 139)
  function: test_search_space_data_boost (line 153)
  function: test_get_context_for_query (line 180)
  function: test_context_length_limit (line 192)
  function: test_list_documents (line 203)
  function: test_empty_search (line 216)
  function: test_search_nonexistent_term (line 221)
  function: test_document_update (line 231)
  class: TestResearchDocument (line 250)
  function: test_document_creation (line 253)
  function: test_document_optional_fields (line 273)
hypercode\src\hypercode\tests\unit\test_search_algorithm.py:
  module: test_search_algorithm (line 0)
  class: TestSearchAlgorithm (line 20)
  function: populated_kb (line 24)
  function: test_exact_title_match_highest_score (line 80)
  function: test_space_data_boosting (line 92)
  function: test_related_term_expansion (line 105)
  function: test_tag_matching_scoring (line 126)
  function: test_content_frequency_scoring (line 136)
  function: test_partial_word_matching (line 149)
  function: test_query_word_ordering (line 167)
  function: test_case_insensitive_search (line 179)
  function: test_empty_query_returns_no_results (line 202)
  function: test_limit_parameter_respected (line 210)
  function: test_no_results_for_nonexistent_terms (line 219)
  function: test_special_characters_in_query (line 227)
  function: test_unicode_characters (line 237)
  function: test_search_performance_with_large_kb (line 256)
  function: test_search_result_consistency (line 277)
  class: TestSearchScoringDetails (line 292)
  function: scoring_kb (line 296)
  function: test_title_match_beats_content_match (line 324)
  function: test_space_data_boosting_works (line 332)
  function: test_frequency_scoring (line 340)
hypercode\tag_channels.py:
  module: tag_channels (line 0)
  function: _coerce_value (line 28)
  function: parse_tag_line (line 51)
  function: parse_tags (line 80)
  function: get_tag (line 95)
  function: group_entities_by_tag (line 103)
hypercode\test_database.py:
  module: test_database (line 0)
  function: test_database_loading (line 10)
hypercode\tests\test_tag_channels.py:
  function: test_parse_tag_line_basic (line 12)
  function: test_parse_tags_multi (line 20)
  function: test_group_entities_by_tag (line 33)
hypercode\tests\test_v01_core.py:
  function: lex_types (line 16)
  function: run_program (line 22)
  function: test_lexer_tokenization_basic (line 38)
  function: test_parser_builds_pipe_and_list (line 54)
  function: test_interpreter_pipeline_math (line 70)
  function: test_interpreter_var_and_print (line 76)
  function: test_interpreter_error_pipeline_non_callable (line 81)
hypercode_backup_20251205_183301\accessibility\adhd_optimizer.py:
  module: adhd_optimizer (line 0)
hypercode_backup_20251205_183301\accessibility\autism_preset.py:
  module: autism_preset (line 0)
hypercode_backup_20251205_183301\accessibility\dyslexia_formatter.py:
  module: dyslexia_formatter (line 0)
hypercode_backup_20251205_183301\accessibility\sensory_customizer.py:
  module: sensory_customizer (line 0)
hypercode_backup_20251205_183301\accessibility\wcag_auditor.py:
  module: wcag_auditor (line 0)
hypercode_backup_20251205_183301\archive\new-files-to-check\backend\research\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\archive\new-files-to-check\backend\research\db.py:
  module: db (line 0)
  function: _get_database_url (line 35)
hypercode_backup_20251205_183301\archive\new-files-to-check\backend\research\models.py:
  module: models (line 0)
  class: Study (line 32)
  function: __repr__ (line 52)
  class: Source (line 56)
  function: __repr__ (line 81)
  class: LanguageVersion (line 85)
  function: __repr__ (line 102)
  class: Task (line 106)
  function: __repr__ (line 124)
  class: Participant (line 128)
  function: __repr__ (line 144)
  class: Session (line 148)
  function: __repr__ (line 169)
  class: Event (line 176)
  function: __repr__ (line 193)
  class: Feedback (line 197)
  function: __repr__ (line 219)
hypercode_backup_20251205_183301\archive\new-files-to-check\backend\research\scripts\import_sources_from_folder.py:
  module: import_sources_from_folder (line 0)
  function: infer_kind (line 25)
  function: main (line 36)
hypercode_backup_20251205_183301\archive\new-files-to-check\backend\research\scripts\seed_basic_data.py:
  module: seed_basic_data (line 0)
  function: main (line 25)
hypercode_backup_20251205_183301\code_insights.py:
  function: analyze_code_patterns (line 8)
  function: find_undocumented_code (line 29)
  function: analyze_test_coverage (line 45)
hypercode_backup_20251205_183301\code_quality_report.py:
  module: code_quality_report (line 0)
  function: get_undocumented_classes_priority (line 15)
  function: get_least_tested_files (line 33)
  function: find_getter_methods (line 69)
  function: generate_code_quality_report (line 103)
hypercode_backup_20251205_183301\core\benchmarks\__init__.py:
  function: benchmark_lexer (line 12)
  function: print_benchmark_results (line 36)
hypercode_backup_20251205_183301\core\benchmarks\benchmarks_lexer.py:
  function: benchmark_lexer (line 6)
  function: print_benchmark_results (line 30)
hypercode_backup_20251205_183301\core\src\ai_gateway\base_gateway.py:
  module: base_gateway (line 0)
hypercode_backup_20251205_183301\core\src\ai_gateway\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\ai_gateway\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\ai_gateway\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\ai_gateway\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\ai_gateway\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode_backup_20251205_183301\core\src\ai_gateway\rag_engine.py:
  module: rag_engine (line 0)
hypercode_backup_20251205_183301\core\src\base_gateway.py:
  module: base_gateway (line 0)
hypercode_backup_20251205_183301\core\src\build.py:
  module: build (line 0)
  function: build (line 34)
hypercode_backup_20251205_183301\core\src\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\core\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\core\src\core\ast.py:
  module: ast (line 0)
  class: Node (line 11)
  class: Program (line 18)
  class: Function (line 25)
  class: VariableDeclaration (line 34)
  class: Literal (line 42)
  class: BinaryOp (line 50)
  class: UnaryOp (line 59)
  class: Variable (line 67)
  class: Call (line 74)
  class: Return (line 82)
  class: Block (line 89)
  class: If (line 96)
  class: While (line 105)
  class: For (line 113)
  class: Assign (line 123)
  class: Logical (line 131)
hypercode_backup_20251205_183301\core\src\core\ast_nodes.py:
  module: ast_nodes (line 0)
  class: Node (line 24)
  class: Expression (line 31)
  class: Statement (line 38)
  class: Program (line 45)
  class: Identifier (line 52)
  class: Literal (line 59)
  class: VariableDeclaration (line 66)
  class: BinaryOperation (line 75)
hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode_backup_20251205_183301\core\src\core\hypercode-\accessibility\adhd_optimizer.py:
  module: adhd_optimizer (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\accessibility\autism_preset.py:
  module: autism_preset (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\accessibility\dyslexia_formatter.py:
  module: dyslexia_formatter (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\accessibility\sensory_customizer.py:
  module: sensory_customizer (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\accessibility\wcag_auditor.py:
  module: wcag_auditor (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\base_gateway.py:
  module: base_gateway (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\rag_engine.py:
  module: rag_engine (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\code_analyzer_ai.py:
  module: code_analyzer_ai (line 0)
  class: CodeAnalyzerAI (line 20)
  function: __init__ (line 23)
  function: analyze_file (line 26)
  function: _analyze_complexity (line 73)
  function: _check_docstrings (line 114)
  function: _get_ai_code_analysis (line 156)
  function: analyze_project (line 184)
  function: _get_project_ai_insights (line 231)
  function: save_analysis (line 263)
  function: print_summary (line 271)
  function: main (line 289)
hypercode_backup_20251205_183301\core\src\core\hypercode-\debug_search.py:
  module: debug_search (line 0)
  function: debug_search (line 15)
hypercode_backup_20251205_183301\core\src\core\hypercode-\demo_ai_research.py:
  module: demo_ai_research (line 0)
  function: demo_ai_research_queries (line 16)
  function: test_document_specific_queries (line 90)
hypercode_backup_20251205_183301\core\src\core\hypercode-\demo_enhanced_client.py:
  module: demo_enhanced_client (line 0)
  function: demo_knowledge_base_integration (line 16)
  function: demonstrate_memory_persistence (line 131)
hypercode_backup_20251205_183301\core\src\core\hypercode-\final_integration_test.py:
  module: final_integration_test (line 0)
  function: final_integration_test (line 15)
hypercode_backup_20251205_183301\core\src\core\hypercode-\health_scanner_ai.py:
  module: health_scanner_ai (line 0)
  class: HealthScannerAI (line 19)
  function: __init__ (line 22)
  function: analyze_project_structure (line 26)
  function: analyze_dependencies (line 69)
  function: analyze_security (line 111)
  function: get_ai_recommendations (line 144)
  function: run_full_scan (line 171)
  function: save_report (line 222)
  function: print_summary (line 228)
  function: main (line 248)
hypercode_backup_20251205_183301\core\src\core\hypercode-\import-helper.py:
  module: import-helper (line 0)
  class: SpaceImportHelper (line 13)
  function: __init__ (line 16)
  function: validate_document (line 21)
  function: load_template (line 63)
  function: validate_all (line 83)
  function: generate_report (line 95)
  function: create_import_script (line 141)
  function: create_template_instructions (line 193)
  function: main (line 264)
hypercode_backup_20251205_183301\core\src\core\hypercode-\import_all_space_data.py:
  module: import_all_space_data (line 0)
  function: format_content (line 16)
  function: import_all_hypercode_data (line 41)
hypercode_backup_20251205_183301\core\src\core\hypercode-\import_hypercode_data.py:
  module: import_hypercode_data (line 0)
  function: import_hypercode_space_data (line 16)
hypercode_backup_20251205_183301\core\src\core\hypercode-\import_perplexity_space.py:
  module: import_perplexity_space (line 0)
  function: create_manual_import_script (line 17)
  function: create_json_import_template (line 86)
  function: import_from_json (line 115)
  function: test_imported_data (line 153)
  function: show_import_menu (line 188)
hypercode_backup_20251205_183301\core\src\core\hypercode-\knowledge_graph\graph_builder.py:
  module: graph_builder (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\knowledge_graph\sparql_query.py:
  module: sparql_query (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\knowledge_graph\update_agent.py:
  module: update_agent (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\live_research\doc_generator.py:
  module: doc_generator (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\live_research\github_publisher.py:
  module: github_publisher (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\live_research\paper_indexer.py:
  module: paper_indexer (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\live_research\research_crawler.py:
  module: research_crawler (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\live_research\synthesis_engine.py:
  module: synthesis_engine (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\aws_cli.py:
  function: main (line 4)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\aws_resource_manager.py:
  function: main (line 4)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\code_analysis.py:
  function: main (line 4)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\dataset_downloader.py:
  function: main (line 4)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\file_system.py:
  function: main (line 4)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\human_input.py:
  function: main (line 4)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\hypercode_syntax.py:
  module: hypercode_syntax (line 0)
  class: HyperCodeSyntaxServer (line 28)
  function: __init__ (line 31)
  function: handle_request (line 35)
  function: _initialize (line 56)
  function: _document_changed (line 79)
  function: _text_hover (line 98)
  function: _completion (line 121)
  function: _parse_document (line 150)
  function: _validate_neurodiversity (line 179)
  function: _generate_diagnostics (line 216)
  function: _get_annotation_hover_info (line 266)
  function: main (line 294)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\path_service.py:
  function: main (line 4)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\user_profile_manager.py:
  function: main (line 4)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\valkey_service.py:
  function: check_redis_connection (line 40)
  function: health_check (line 59)
  function: set_key (line 67)
  function: get_key (line 80)
  function: hset_key (line 95)
  function: hget_key (line 107)
  function: hgetall_hash (line 126)
  function: main (line 144)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\web_search.py:
  function: main (line 4)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\setup.py:
  module: setup (line 0)
  function: install_dependencies (line 16)
  function: verify_setup (line 31)
  function: show_next_steps (line 54)
  function: main (line 72)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\start_servers.py:
  module: start_servers (line 0)
  function: start_server (line 34)
  function: list_servers (line 59)
  function: main (line 66)
hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\test_mcp.py:
  module: test_mcp (line 0)
  function: test_server_imports (line 15)
  function: main (line 47)
hypercode_backup_20251205_183301\core\src\core\hypercode-\perplexity_space_collector.py:
  module: perplexity_space_collector (line 0)
  function: quick_copy_paste_collector (line 18)
  function: create_structured_template (line 117)
  function: show_bro_hacks (line 167)
  function: main_menu (line 207)
hypercode_backup_20251205_183301\core\src\core\hypercode-\perplexity_space_integration.py:
  module: perplexity_space_integration (line 0)
  function: main (line 16)
hypercode_backup_20251205_183301\core\src\core\hypercode-\scripts\style_guide_collector.py:
  module: style_guide_collector (line 0)
  class: StyleGuideCollector (line 16)
  function: __init__ (line 19)
  function: _load_feedback (line 30)
  function: _save_feedback (line 49)
  function: add_feedback (line 58)
  function: _update_analysis (line 100)
  function: analyze_feedback (line 149)
  function: _get_top_items (line 187)
  function: _calculate_consensus (line 210)
  function: _generate_recommendations (line 243)
  function: import_github_issues (line 323)
  function: generate_report (line 346)
  function: interactive_feedback (line 413)
  function: main (line 521)
hypercode_backup_20251205_183301\core\src\core\hypercode-\scripts\test_perplexity_api.py:
  module: test_perplexity_api (line 0)
  function: main (line 17)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\build.py:
  module: build (line 0)
  function: build (line 34)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\core\ast_nodes.py:
  module: ast_nodes (line 0)
  class: Node (line 24)
  class: Expression (line 31)
  class: Statement (line 38)
  class: Program (line 45)
  class: Identifier (line 52)
  class: Literal (line 59)
  class: VariableDeclaration (line 66)
  class: BinaryOperation (line 75)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 15)
  class: Lexer (line 32)
  function: __init__ (line 49)
  function: tokenize (line 110)
  function: is_at_end (line 134)
  function: scan_token (line 137)
  function: advance (line 228)
  function: add_token (line 233)
  function: error (line 246)
  function: synchronize (line 262)
  function: previous (line 274)
  function: peek_next (line 280)
  function: match (line 286)
  function: peek (line 295)
  function: string (line 300)
  function: is_digit (line 362)
  function: number (line 366)
  function: is_alpha (line 421)
  function: is_alphanumeric (line 425)
  function: is_hex_digit (line 429)
  function: identifier (line 433)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\core\optimizer.py:
  module: optimizer (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\core\parser.py:
  class: ParseError (line 8)
  class: Parser (line 12)
  function: __init__ (line 13)
  function: parse (line 17)
  function: declaration (line 26)
  function: var_declaration (line 39)
  function: statement (line 64)
  function: print_statement (line 71)
  function: expression_statement (line 76)
  function: block (line 81)
  function: expression (line 88)
  function: assignment (line 91)
  function: equality (line 106)
  function: comparison (line 116)
  function: term (line 129)
  function: factor (line 137)
  function: unary (line 145)
  function: primary (line 152)
  function: match (line 184)
  function: consume (line 191)
  function: error (line 201)
  function: synchronize (line 207)
  function: check (line 227)
  function: advance (line 232)
  function: is_at_end (line 237)
  function: peek (line 240)
  function: previous (line 243)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode-backend-js-COMPLETE.py:
  module: hypercode-backend-js-COMPLETE (line 0)
  class: JSCompiler (line 19)
  function: __init__ (line 30)
  function: compile (line 42)
  function: _generate_header (line 65)
  function: _generate_setup (line 74)
  function: _generate_main (line 110)
  function: _generate_footer (line 162)
  function: _indent (line 179)
  function: optimize_ast (line 183)
  function: main (line 200)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode-idea-generator-WEB.py:
  module: hypercode-idea-generator-WEB (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode-launch-kit.py:
  module: hypercode-launch-kit (line 0)
  class: HyperCodeLaunchKit (line 23)
  function: __init__ (line 26)
  function: create_readme (line 30)
  function: create_launch_checklist (line 367)
  function: create_launch_script (line 620)
  function: create_first_30_days (line 718)
  function: print_summary (line 974)
  function: main (line 1007)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode-lexer-COMPLETE.py:
  module: hypercode-lexer-COMPLETE (line 0)
  class: TokenType (line 21)
  class: Token (line 45)
  function: __repr__ (line 54)
  class: LexerError (line 59)
  function: __init__ (line 62)
  class: HyperCodeLexer (line 69)
  function: __init__ (line 95)
  function: tokenize (line 110)
  function: _advance_position (line 169)
  function: _skip_comment (line 179)
  function: get_tokens (line 184)
  function: filter_tokens (line 188)
  function: print_tokens (line 205)
  function: get_statistics (line 236)
  function: main (line 250)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode-parser-COMPLETE.py:
  module: hypercode-parser-COMPLETE (line 0)
  class: NodeType (line 22)
  class: ASTNode (line 38)
  function: __repr__ (line 51)
  class: ParserError (line 68)
  function: __init__ (line 71)
  class: HyperCodeParser (line 80)
  function: __init__ (line 94)
  function: parse (line 105)
  function: _parse_statement (line 127)
  function: _parse_loop (line 174)
  function: _advance (line 209)
  function: _is_at_end (line 215)
  function: validate (line 222)
  function: print_ast (line 237)
  function: main (line 251)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\__main__.py:
  function: main (line 6)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\config.py:
  module: config (line 0)
  class: Config (line 16)
  function: get_headers (line 27)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\ast.py:
  class: Node (line 9)
  function: accept (line 10)
  class: Expr (line 20)
  class: Literal (line 25)
  class: Variable (line 30)
  class: Assign (line 35)
  class: Binary (line 41)
  class: Unary (line 48)
  class: Grouping (line 54)
  class: Call (line 59)
  class: Get (line 66)
  class: Stmt (line 73)
  class: Expression (line 78)
  class: Print (line 83)
  class: Var (line 88)
  class: Block (line 94)
  class: Intent (line 99)
  class: Program (line 106)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\cli.py:
  module: cli (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\error_handler.py:
  function: report_parse_error (line 5)
  function: report (line 12)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 32)
  function: __init__ (line 35)
  class: Lexer (line 42)
  function: __init__ (line 109)
  function: tokenize (line 126)
  function: _match_patterns (line 161)
  function: _update_position (line 187)
  function: _add_token (line 206)
  function: _handle_unknown (line 270)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\optimizer.py:
  module: optimizer (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\parser.py:
  class: ParseError (line 24)
  class: Parser (line 28)
  function: __init__ (line 29)
  function: parse (line 33)
  function: declaration (line 42)
  function: var_declaration (line 51)
  function: statement (line 67)
  function: print_statement (line 76)
  function: intent_statement (line 81)
  function: expression_statement (line 96)
  function: block (line 101)
  function: expression (line 108)
  function: assignment (line 111)
  function: equality (line 126)
  function: comparison (line 136)
  function: term (line 149)
  function: factor (line 157)
  function: unary (line 165)
  function: primary (line 172)
  function: _primary (line 189)
  function: finish_call (line 220)
  function: match (line 233)
  function: consume (line 240)
  function: error (line 247)
  function: synchronize (line 253)
  function: check (line 273)
  function: advance (line 278)
  function: is_at_end (line 283)
  function: peek (line 286)
  function: previous (line 289)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\semantic_analyzer.py:
  module: semantic_analyzer (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\tokens.py:
  class: TokenType (line 6)
  class: Token (line 61)
  function: __str__ (line 68)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\enhanced_perplexity_client.py:
  module: enhanced_perplexity_client (line 0)
  class: EnhancedPerplexityClient (line 18)
  function: __init__ (line 21)
  function: query_with_context (line 25)
  function: add_research_data (line 61)
  function: search_research_data (line 71)
  function: list_research_documents (line 75)
  function: get_document (line 79)
  function: delete_document (line 83)
  function: import_from_perplexity_space (line 87)
  function: test_context_integration (line 123)
  function: create_perplexity_space_import_template (line 175)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\knowledge_base.py:
  module: knowledge_base (line 0)
  class: ResearchDocument (line 17)
  function: __post_init__ (line 28)
  function: generate_id (line 36)
  function: validate (line 41)
  function: update_timestamp (line 53)
  class: HyperCodeKnowledgeBase (line 100)
  function: __init__ (line 103)
  function: load (line 109)
  function: save (line 125)
  function: add_document (line 135)
  function: search_documents (line 163)
  function: get_context_for_query (line 226)
  function: list_documents (line 256)
  function: get_document (line 260)
  function: delete_document (line 264)
  function: update_document (line 272)
  function: search_by_tags (line 286)
  function: get_document_statistics (line 305)
  function: export_format (line 330)
  function: validate_all_documents (line 352)
  function: cleanup_duplicates (line 362)
  function: initialize_sample_data (line 383)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\perplexity_client.py:
  module: perplexity_client (line 0)
  class: PerplexityClient (line 12)
  function: __init__ (line 15)
  function: query (line 30)
  function: test_connection (line 72)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\repl.py:
  function: run_repl (line 7)
  function: run (line 22)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode_idea_generator.py:
  module: hypercode_idea_generator (line 0)
  class: HyperCodeIdeaGenerator (line 431)
  function: __init__ (line 439)
  function: get_ideas_by_category (line 443)
  function: get_top_ideas (line 468)
  function: vote_for_idea (line 487)
  function: get_trending_ideas (line 497)
  function: format_idea_card (line 502)
  function: main (line 528)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode_lexer_fixed.py:
  module: hypercode_lexer_fixed (line 0)
  class: TokenType (line 19)
  class: Token (line 44)
  function: __repr__ (line 54)
  class: LexerError (line 68)
  function: __init__ (line 71)
  class: HyperCodeLexerFixed (line 84)
  function: __init__ (line 125)
  function: tokenize (line 145)
  function: _parse_string (line 217)
  function: _skip_comment (line 300)
  function: _advance (line 305)
  function: print_tokens (line 315)
  function: run_tests (line 329)
  function: main (line 446)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode_poc.py:
  module: hypercode_poc (line 0)
  class: TokenType (line 18)
  class: Token (line 34)
  class: UserConfidenceLevel (line 41)
  class: EnhancedLexer (line 48)
  function: __init__ (line 51)
  function: tokenize (line 74)
  function: handle_string (line 115)
  function: handle_number (line 141)
  function: handle_identifier (line 149)
  function: advance (line 171)
  class: ContextAwareErrorMessenger (line 176)
  function: __init__ (line 179)
  function: format_error (line 182)
  class: SemanticContextStreamer (line 189)
  function: analyze (line 192)
  class: ConfidenceTracker (line 209)
  function: __init__ (line 212)
  function: record (line 216)
  class: HyperCodePOC (line 222)
  function: __init__ (line 225)
  function: compile (line 232)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\debug_ascii.py:
  module: debug_ascii (line 0)
  function: test_regex_patterns (line 14)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\debug_full.py:
  module: debug_full (line 0)
  function: debug_full_parsing (line 14)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\debug_parser.py:
  module: debug_parser (line 0)
  function: debug_annotation_detection (line 14)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\debug_simple.py:
  module: debug_simple (line 0)
  function: debug_simple (line 14)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\test_parser.py:
  module: test_parser (line 0)
  function: test_first_click_moment (line 14)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\visual_syntax_parser.py:
  module: visual_syntax_parser (line 0)
  class: SemanticMarker (line 18)
  class: SemanticAnnotation (line 37)
  function: __str__ (line 46)
  class: ParsedFunction (line 51)
  function: get_annotations_by_type (line 62)
  class: VisualSyntaxParser (line 69)
  function: __init__ (line 72)
  function: _build_semantic_patterns (line 76)
  function: _build_color_scheme (line 105)
  function: parse_file (line 123)
  function: parse_content (line 130)
  function: _is_function_definition (line 170)
  function: _start_new_function (line 179)
  function: _parse_line_annotations (line 202)
  function: _parse_annotation_params (line 223)
  function: generate_syntax_highlighting (line 265)
  function: extract_semantic_summary (line 277)
  function: validate_neurodiversity_compliance (line 311)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\scaffold (1).py:
  module: scaffold (1) (line 0)
  function: create_directories (line 141)
  function: create_python_files (line 151)
  function: create_example_files (line 165)
  function: create_root_files (line 202)
  function: create_healthcheck (line 213)
  function: print_summary (line 234)
  function: main (line 259)
hypercode_backup_20251205_183301\core\src\core\hypercode-\src\scaffold.py:
  module: scaffold (line 0)
  function: create_directories (line 153)
  function: create_python_files (line 184)
  function: create_example_files (line 254)
  function: create_root_files (line 291)
  function: create_healthcheck (line 541)
  function: print_summary (line 583)
  function: main (line 621)
hypercode_backup_20251205_183301\core\src\core\hypercode-\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode_backup_20251205_183301\core\src\core\hypercode-\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode_backup_20251205_183301\core\src\core\hypercode-\test_intent_blocks.py:
  module: test_intent_blocks (line 0)
  function: test_intent_block (line 13)
hypercode_backup_20251205_183301\core\src\core\hypercode-\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode_backup_20251205_183301\core\src\core\hypercode-\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode_backup_20251205_183301\core\src\core\hypercode-\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 183)
hypercode_backup_20251205_183301\core\src\core\hypercode-\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\benchmark_knowledge_base.py:
  module: benchmark_knowledge_base (line 0)
  class: BenchmarkSuite (line 24)
  function: __init__ (line 27)
  function: _get_system_info (line 34)
  function: generate_test_data (line 43)
  function: benchmark_operation (line 93)
  function: run_benchmark_suite (line 118)
  function: _calculate_summary (line 274)
  function: _generate_recommendations (line 296)
  function: generate_markdown_report (line 338)
  function: save_json_results (line 467)
  function: main (line 474)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_accessibility.py:
  module: test_accessibility (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_ai_gateway.py:
  module: test_ai_gateway (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_backends.py:
  module: test_backends (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_core.py:
  module: test_core (line 0)
  function: run_test (line 29)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_integration.py:
  module: test_integration (line 0)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestKnowledgeBaseSearch (line 12)
  function: sample_documents (line 16)
  function: knowledge_base (line 40)
  function: test_basic_search (line 48)
  function: test_search_with_exact_match (line 54)
  function: test_search_case_insensitive (line 59)
  function: test_search_empty_query (line 65)
  function: test_search_no_matches (line 71)
  function: test_search_ranking (line 77)
  function: test_query_normalization (line 90)
  function: test_multi_word_query (line 98)
  function: test_tag_based_search (line 103)
  class: TestEdgeCases (line 112)
  function: knowledge_base (line 116)
  function: test_very_short_query (line 121)
  function: test_very_long_query (line 126)
  function: test_special_characters_in_query (line 136)
  function: test_unicode_in_query (line 141)
  function: test_sql_injection_attempt (line 146)
  function: test_repeated_queries (line 151)
  class: TestPerformance (line 159)
  function: large_knowledge_base (line 163)
  function: test_search_response_time (line 179)
  function: test_concurrent_searches (line 189)
  function: test_memory_usage (line 207)
  class: TestIntegrationWithPerplexity (line 213)
  function: mock_perplexity_client (line 217)
  function: mock_knowledge_base (line 229)
  function: test_enhanced_query_with_context (line 243)
  function: test_fallback_to_perplexity_api (line 259)
  function: test_context_ranking_and_selection (line 273)
  class: TestDocumentManagement (line 288)
  function: knowledge_base (line 292)
  function: test_add_document (line 300)
  function: test_update_document (line 310)
  function: test_remove_document (line 315)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_knowledge_base_comprehensive.py:
  module: test_knowledge_base_comprehensive (line 0)
  class: TestKnowledgeBaseUnit (line 20)
  function: temp_kb (line 24)
  function: sample_docs (line 36)
  function: test_init_empty_kb (line 59)
  function: test_add_single_document (line 65)
  function: test_add_multiple_documents (line 74)
  function: test_save_and_load (line 84)
  function: test_search_exact_match (line 102)
  function: test_search_partial_match (line 113)
  function: test_search_tag_matching (line 124)
  function: test_search_case_insensitive (line 135)
  function: test_empty_search (line 147)
  function: test_nonexistent_search (line 155)
  function: test_get_context_for_query (line 165)
  function: test_context_length_limit (line 176)
  function: test_document_update (line 186)
  function: test_list_documents (line 202)
  function: test_delete_document (line 213)
  class: TestKnowledgeBaseIntegration (line 229)
  function: populated_kb (line 233)
  function: test_complex_search_queries (line 277)
  function: test_search_ranking_quality (line 291)
  function: test_related_term_expansion (line 301)
  function: test_performance_with_large_dataset (line 313)
  function: test_concurrent_access_simulation (line 332)
  class: TestKnowledgeBasePerformance (line 356)
  function: large_kb (line 360)
  function: test_search_performance_large_dataset (line 382)
  function: test_save_performance_large_dataset (line 396)
  function: test_load_performance_large_dataset (line 409)
  function: test_memory_usage_large_dataset (line 423)
  class: TestKnowledgeBaseEdgeCases (line 446)
  function: edge_case_kb (line 450)
  function: test_empty_title_handling (line 494)
  function: test_special_characters_handling (line 499)
  function: test_very_long_titles (line 507)
  function: test_empty_content_handling (line 512)
  function: test_none_tags_handling (line 517)
  function: test_malformed_json_handling (line 531)
  function: test_file_permission_handling (line 544)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_lexer.py:
  function: test_lexer_basic_tokens (line 5)
  function: test_lexer_strings (line 23)
  function: test_lexer_operators (line 48)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_lexer_extended.py:
  function: test_lexer_escaped_strings (line 5)
  function: test_lexer_numbers (line 18)
  function: test_lexer_operators (line 39)
  function: test_lexer_comments (line 86)
  function: test_lexer_whitespace (line 115)
  function: test_lexer_error_handling (line 130)
  function: test_lexer_hex_numbers (line 139)
  function: test_lexer_binary_numbers (line 157)
  function: test_lexer_scientific_notation (line 169)
  function: test_lexer_string_escapes (line 180)
  function: test_lexer_keywords (line 197)
  function: test_lexer_position_tracking (line 223)
  function: test_lexer_error_recovery (line 243)
  function: test_lexer_error_messages (line 252)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_parser.py:
  function: test_parse_literal (line 12)
  function: test_parse_variable_declaration (line 24)
  function: test_parse_binary_expression (line 37)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\unit\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestHyperCodeKnowledgeBase (line 20)
  function: temp_kb (line 24)
  function: sample_documents (line 33)
  function: test_init_empty_kb (line 56)
  function: test_add_document (line 61)
  function: test_add_multiple_documents (line 82)
  function: test_save_and_load (line 92)
  function: test_search_exact_match (line 113)
  function: test_search_tag_matching (line 126)
  function: test_search_related_terms (line 139)
  function: test_search_space_data_boost (line 153)
  function: test_get_context_for_query (line 180)
  function: test_context_length_limit (line 192)
  function: test_list_documents (line 203)
  function: test_empty_search (line 216)
  function: test_search_nonexistent_term (line 221)
  function: test_document_update (line 231)
  class: TestResearchDocument (line 250)
  function: test_document_creation (line 253)
  function: test_document_optional_fields (line 273)
hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\unit\test_search_algorithm.py:
  module: test_search_algorithm (line 0)
  class: TestSearchAlgorithm (line 20)
  function: populated_kb (line 24)
  function: test_exact_title_match_highest_score (line 80)
  function: test_space_data_boosting (line 92)
  function: test_related_term_expansion (line 105)
  function: test_tag_matching_scoring (line 126)
  function: test_content_frequency_scoring (line 136)
  function: test_partial_word_matching (line 149)
  function: test_query_word_ordering (line 167)
  function: test_case_insensitive_search (line 179)
  function: test_empty_query_returns_no_results (line 202)
  function: test_limit_parameter_respected (line 210)
  function: test_no_results_for_nonexistent_terms (line 219)
  function: test_special_characters_in_query (line 227)
  function: test_unicode_characters (line 237)
  function: test_search_performance_with_large_kb (line 256)
  function: test_search_result_consistency (line 277)
  class: TestSearchScoringDetails (line 292)
  function: scoring_kb (line 296)
  function: test_title_match_beats_content_match (line 324)
  function: test_space_data_boosting_works (line 332)
  function: test_frequency_scoring (line 340)
hypercode_backup_20251205_183301\core\src\core\interpreter.py:
  class: RuntimeError (line 8)
  function: __init__ (line 9)
  class: Environment (line 15)
  function: __init__ (line 16)
  function: define (line 20)
  function: get (line 23)
  function: assign (line 30)
  class: Callable (line 40)
  function: arity (line 41)
  function: call (line 44)
  class: HyperCodeFunction (line 48)
  function: __init__ (line 49)
  function: call (line 53)
  function: arity (line 65)
  class: ReturnException (line 69)
  function: __init__ (line 70)
  class: Interpreter (line 74)
  function: __init__ (line 75)
  class: Clock (line 82)
  function: arity (line 83)
  function: call (line 86)
  function: __str__ (line 89)
  class: Double (line 92)
  function: arity (line 93)
  function: call (line 96)
  function: __str__ (line 101)
  class: Square (line 104)
  function: arity (line 105)
  function: call (line 108)
  function: __str__ (line 113)
  function: execute_block (line 120)
  function: interpret (line 129)
  function: execute (line 141)
  function: evaluate (line 144)
  function: visit_Expression (line 147)
  function: visit_Print (line 151)
  function: visit_Let (line 158)
  function: visit_Block (line 165)
  function: visit_BlockDecl (line 169)
  function: visit_Intent (line 175)
  function: visit_Function (line 180)
  function: visit_Return (line 185)
  function: visit_Literal (line 191)
  function: visit_Grouping (line 194)
  function: visit_Variable (line 197)
  function: visit_Assign (line 200)
  function: visit_Pipe (line 205)
  function: visit_State (line 234)
  function: visit_Call (line 244)
  function: visit_Binary (line 262)
  function: visit_Unary (line 293)
  function: is_truthy (line 301)
  function: stringify (line 308)
  function: get_output (line 322)
hypercode_backup_20251205_183301\core\src\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 17)
  class: Lexer (line 33)
  function: __init__ (line 41)
  function: scan_tokens (line 77)
  function: scan_token (line 87)
  function: number (line 164)
  function: string (line 197)
  function: docstring (line 242)
  function: identifier (line 268)
  function: error (line 278)
  function: is_at_end (line 294)
  function: advance (line 298)
  function: match (line 307)
  function: peek (line 317)
  function: peek_next (line 323)
  function: add_token (line 329)
hypercode_backup_20251205_183301\core\src\core\optimizer.py:
  module: optimizer (line 0)
hypercode_backup_20251205_183301\core\src\core\parser.py:
  class: ParseError (line 7)
  class: Parser (line 11)
  function: __init__ (line 12)
  function: parse (line 16)
  function: declaration (line 25)
  function: let_declaration (line 38)
  function: block_declaration (line 48)
  function: statement (line 54)
  function: print_statement (line 65)
  function: expression_statement (line 70)
  function: block (line 75)
  function: expression (line 84)
  function: pipe (line 87)
  function: assignment (line 103)
  function: equality (line 118)
  function: comparison (line 128)
  function: term (line 141)
  function: factor (line 149)
  function: unary (line 157)
  function: primary (line 164)
  function: function (line 194)
  function: if_statement (line 215)
  function: return_statement (line 227)
  function: match (line 237)
  function: consume (line 244)
  function: error (line 249)
  function: synchronize (line 255)
  function: check (line 276)
  function: advance (line 281)
  function: is_at_end (line 286)
  function: peek (line 289)
  function: previous (line 292)
hypercode_backup_20251205_183301\core\src\core\tokens.py:
  module: tokens (line 0)
  class: TokenType (line 12)
  class: Token (line 74)
  function: __init__ (line 86)
  function: __str__ (line 95)
  function: __repr__ (line 98)
hypercode_backup_20251205_183301\core\src\duelcode\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode_backup_20251205_183301\core\src\duelcode\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode_backup_20251205_183301\core\src\duelcode\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode_backup_20251205_183301\core\src\duelcode\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode_backup_20251205_183301\core\src\duelcode\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode_backup_20251205_183301\core\src\duelcode\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode_backup_20251205_183301\core\src\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode_backup_20251205_183301\core\src\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode_backup_20251205_183301\core\src\hypercode-backend-js-COMPLETE.py:
  module: hypercode-backend-js-COMPLETE (line 0)
  class: JSCompiler (line 19)
  function: __init__ (line 30)
  function: compile (line 42)
  function: _generate_header (line 65)
  function: _generate_setup (line 74)
  function: _generate_main (line 110)
  function: _generate_footer (line 162)
  function: _indent (line 179)
  function: optimize_ast (line 183)
  function: main (line 200)
hypercode_backup_20251205_183301\core\src\hypercode-idea-generator-WEB.py:
  module: hypercode-idea-generator-WEB (line 0)
hypercode_backup_20251205_183301\core\src\hypercode-launch-kit.py:
  module: hypercode-launch-kit (line 0)
  class: HyperCodeLaunchKit (line 23)
  function: __init__ (line 26)
  function: create_readme (line 30)
  function: create_launch_checklist (line 367)
  function: create_launch_script (line 620)
  function: create_first_30_days (line 718)
  function: print_summary (line 974)
  function: main (line 1007)
hypercode_backup_20251205_183301\core\src\hypercode-lexer-COMPLETE.py:
  module: hypercode-lexer-COMPLETE (line 0)
  class: TokenType (line 21)
  class: Token (line 45)
  function: __repr__ (line 54)
  class: LexerError (line 59)
  function: __init__ (line 62)
  class: HyperCodeLexer (line 69)
  function: __init__ (line 95)
  function: tokenize (line 110)
  function: _advance_position (line 169)
  function: _skip_comment (line 179)
  function: get_tokens (line 184)
  function: filter_tokens (line 188)
  function: print_tokens (line 205)
  function: get_statistics (line 236)
  function: main (line 250)
hypercode_backup_20251205_183301\core\src\hypercode-parser-COMPLETE.py:
  module: hypercode-parser-COMPLETE (line 0)
  class: NodeType (line 22)
  class: ASTNode (line 38)
  function: __repr__ (line 51)
  class: ParserError (line 68)
  function: __init__ (line 71)
  class: HyperCodeParser (line 80)
  function: __init__ (line 94)
  function: parse (line 105)
  function: _parse_statement (line 127)
  function: _parse_loop (line 174)
  function: _advance (line 209)
  function: _is_at_end (line 215)
  function: validate (line 222)
  function: print_ast (line 237)
  function: main (line 251)
hypercode_backup_20251205_183301\core\src\hypercode\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\core\src\hypercode\__main__.py:
  function: main (line 6)
hypercode_backup_20251205_183301\core\src\hypercode\cli\__init__.py:
  module: __init__ (line 0)
  function: main (line 14)
hypercode_backup_20251205_183301\core\src\hypercode\config.py:
  module: config (line 0)
  class: Config (line 16)
  function: get_headers (line 27)
hypercode_backup_20251205_183301\core\src\hypercode\core\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\core\src\hypercode\core\cli.py:
  module: cli (line 0)
hypercode_backup_20251205_183301\core\src\hypercode\core\error_handler.py:
  function: report_parse_error (line 5)
  function: report (line 12)
hypercode_backup_20251205_183301\core\src\hypercode\core\hypercode_ast.py:
  class: Node (line 9)
  function: accept (line 10)
  class: Expr (line 20)
  class: Literal (line 25)
  class: Variable (line 30)
  class: Assign (line 35)
  class: Binary (line 41)
  class: Unary (line 48)
  class: Grouping (line 54)
  class: Call (line 59)
  class: Get (line 66)
  class: Stmt (line 73)
  class: Expression (line 78)
  class: Print (line 83)
  class: Var (line 88)
  class: Block (line 94)
  class: If (line 99)
  class: Fun (line 106)
  class: Return (line 113)
  class: Intent (line 119)
  class: Program (line 126)
hypercode_backup_20251205_183301\core\src\hypercode\core\interpreter.py:
  class: Return (line 6)
  function: __init__ (line 7)
  class: HyperCodeFunction (line 11)
  function: __init__ (line 12)
  function: __str__ (line 16)
  function: arity (line 19)
  function: call (line 22)
  class: Environment (line 35)
  function: __init__ (line 36)
  function: define (line 40)
  function: get (line 43)
  function: assign (line 50)
  class: Interpreter (line 60)
  function: __init__ (line 61)
  function: interpret (line 65)
  function: execute (line 72)
  function: execute_block (line 75)
  function: evaluate (line 84)
  function: visit_Expression (line 87)
  function: visit_Print (line 90)
  function: visit_Var (line 94)
  function: visit_Block (line 100)
  function: visit_Assign (line 103)
  function: visit_Binary (line 108)
  function: visit_Grouping (line 151)
  function: visit_Literal (line 154)
  function: visit_Unary (line 157)
  function: visit_Variable (line 170)
  function: visit_If (line 173)
  function: is_truthy (line 179)
  function: visit_Fun (line 186)
  function: visit_Return (line 190)
  function: visit_Call (line 196)
  function: is_callable (line 214)
  class: Visitor (line 219)
  function: visit_Expression (line 220)
  function: visit_Print (line 223)
  function: visit_Var (line 226)
  function: visit_Block (line 229)
  function: visit_If (line 232)
  function: visit_Fun (line 235)
  function: visit_Return (line 238)
  function: visit_Assign (line 241)
  function: visit_Binary (line 244)
  function: visit_Grouping (line 247)
  function: visit_Literal (line 250)
  function: visit_Unary (line 253)
  function: visit_Variable (line 256)
  function: visit_Call (line 259)
hypercode_backup_20251205_183301\core\src\hypercode\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 28)
  function: __init__ (line 35)
  class: Lexer (line 42)
  function: __init__ (line 45)
  function: tokenize (line 59)
  function: is_at_end (line 89)
  class: LexerError (line 102)
  function: __init__ (line 105)
  class: Lexer (line 112)
  function: __init__ (line 122)
  function: tokenize (line 136)
  function: scan_token (line 164)
  function: string (line 251)
  function: number (line 273)
  function: identifier (line 306)
  function: match (line 316)
  function: peek (line 327)
  function: peek_next (line 333)
  function: advance (line 339)
  function: add_token (line 349)
  function: error (line 357)
  function: is_at_end (line 371)
hypercode_backup_20251205_183301\core\src\hypercode\core\optimizer.py:
  module: optimizer (line 0)
hypercode_backup_20251205_183301\core\src\hypercode\core\parser.py:
  class: ParseError (line 8)
  class: Parser (line 12)
  function: __init__ (line 13)
  function: parse (line 17)
  function: declaration (line 26)
  function: var_declaration (line 37)
  function: statement (line 53)
  function: print_statement (line 66)
  function: return_statement (line 71)
  function: intent_statement (line 79)
  function: expression_statement (line 92)
  function: if_statement (line 97)
  function: function (line 109)
  function: block (line 128)
  function: expression (line 135)
  function: assignment (line 138)
  function: equality (line 153)
  function: comparison (line 163)
  function: term (line 176)
  function: factor (line 184)
  function: unary (line 192)
  function: primary (line 199)
  function: _primary (line 214)
  function: finish_call (line 245)
  function: match (line 258)
  function: consume (line 265)
  function: error (line 272)
  function: synchronize (line 278)
  function: check (line 298)
  function: advance (line 303)
  function: is_at_end (line 308)
  function: peek (line 311)
  function: previous (line 314)
hypercode_backup_20251205_183301\core\src\hypercode\core\semantic_analyzer.py:
  module: semantic_analyzer (line 0)
hypercode_backup_20251205_183301\core\src\hypercode\core\sensory_profile.py:
  module: sensory_profile (line 0)
  class: VisualNoiseLevel (line 15)
  class: AnimationSpeed (line 22)
  class: VisualSettings (line 29)
  class: AudioSettings (line 43)
  class: AnimationSettings (line 58)
  class: SensoryProfile (line 68)
  function: to_dict (line 77)
  function: from_dict (line 93)
  function: save (line 115)
  function: load (line 121)
  class: ProfileManager (line 128)
  function: __init__ (line 131)
  function: _ensure_default_profiles (line 141)
  function: _create_minimal_profile (line 154)
  function: _create_enhanced_profile (line 171)
  function: _create_high_contrast_profile (line 198)
  function: list_profiles (line 224)
  function: get_profile (line 228)
  function: save_profile (line 235)
  function: delete_profile (line 240)
  function: get_profile (line 251)
  function: list_profiles (line 263)
hypercode_backup_20251205_183301\core\src\hypercode\core\tokens.py:
  class: TokenType (line 6)
  class: Token (line 96)
  function: __str__ (line 103)
hypercode_backup_20251205_183301\core\src\hypercode\enhanced_perplexity_client.py:
  module: enhanced_perplexity_client (line 0)
  class: EnhancedPerplexityClient (line 18)
  function: __init__ (line 21)
  function: query_with_context (line 25)
  function: add_research_data (line 61)
  function: search_research_data (line 71)
  function: list_research_documents (line 75)
  function: get_document (line 79)
  function: delete_document (line 83)
  function: import_from_perplexity_space (line 87)
  function: test_context_integration (line 123)
  function: create_perplexity_space_import_template (line 175)
hypercode_backup_20251205_183301\core\src\hypercode\knowledge_base.py:
  module: knowledge_base (line 0)
  class: ResearchDocument (line 17)
  function: __post_init__ (line 28)
  function: generate_id (line 36)
  function: validate (line 41)
  function: update_timestamp (line 53)
  class: HyperCodeKnowledgeBase (line 100)
  function: __init__ (line 103)
  function: load (line 109)
  function: save (line 125)
  function: add_document (line 135)
  function: search_documents (line 163)
  function: get_context_for_query (line 227)
  function: list_documents (line 257)
  function: get_document (line 261)
  function: delete_document (line 265)
  function: update_document (line 273)
  function: search_by_tags (line 287)
  function: get_document_statistics (line 306)
  function: export_format (line 331)
  function: validate_all_documents (line 353)
  function: cleanup_duplicates (line 363)
  function: initialize_sample_data (line 384)
hypercode_backup_20251205_183301\core\src\hypercode\perplexity_client.py:
  module: perplexity_client (line 0)
  class: PerplexityClient (line 12)
  function: __init__ (line 15)
  function: query (line 30)
  function: test_connection (line 72)
hypercode_backup_20251205_183301\core\src\hypercode\repl.py:
  function: run_repl (line 11)
  function: run (line 32)
  function: show_help (line 51)
hypercode_backup_20251205_183301\core\src\hypercode_idea_generator.py:
  module: hypercode_idea_generator (line 0)
  class: HyperCodeIdeaGenerator (line 431)
  function: __init__ (line 439)
  function: get_ideas_by_category (line 443)
  function: get_top_ideas (line 468)
  function: vote_for_idea (line 487)
  function: get_trending_ideas (line 497)
  function: format_idea_card (line 502)
  function: main (line 528)
hypercode_backup_20251205_183301\core\src\hypercode_poc.py:
  module: hypercode_poc (line 0)
  class: TokenType (line 18)
  class: Token (line 34)
  class: UserConfidenceLevel (line 41)
  class: EnhancedLexer (line 48)
  function: __init__ (line 51)
  function: tokenize (line 74)
  function: handle_string (line 115)
  function: handle_number (line 141)
  function: handle_identifier (line 149)
  function: advance (line 171)
  class: ContextAwareErrorMessenger (line 176)
  function: __init__ (line 179)
  function: format_error (line 182)
  class: SemanticContextStreamer (line 189)
  function: analyze (line 192)
  class: ConfidenceTracker (line 209)
  function: __init__ (line 212)
  function: record (line 216)
  class: HyperCodePOC (line 222)
  function: __init__ (line 225)
  function: compile (line 232)
hypercode_backup_20251205_183301\core\src\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\core\src\parser\debug_ascii.py:
  module: debug_ascii (line 0)
  function: test_regex_patterns (line 14)
hypercode_backup_20251205_183301\core\src\parser\debug_full.py:
  module: debug_full (line 0)
  function: debug_full_parsing (line 14)
hypercode_backup_20251205_183301\core\src\parser\debug_parser.py:
  module: debug_parser (line 0)
  function: debug_annotation_detection (line 14)
hypercode_backup_20251205_183301\core\src\parser\debug_simple.py:
  module: debug_simple (line 0)
  function: debug_simple (line 14)
hypercode_backup_20251205_183301\core\src\parser\test_parser.py:
  module: test_parser (line 0)
  function: test_first_click_moment (line 14)
hypercode_backup_20251205_183301\core\src\parser\visual_syntax_parser.py:
  module: visual_syntax_parser (line 0)
  class: SemanticMarker (line 18)
  class: SemanticAnnotation (line 37)
  function: __str__ (line 46)
  class: ParsedFunction (line 51)
  function: get_annotations_by_type (line 62)
  class: VisualSyntaxParser (line 69)
  function: __init__ (line 72)
  function: _build_semantic_patterns (line 76)
  function: _build_color_scheme (line 105)
  function: parse_file (line 123)
  function: parse_content (line 130)
  function: _is_function_definition (line 170)
  function: _start_new_function (line 179)
  function: _parse_line_annotations (line 202)
  function: _parse_annotation_params (line 223)
  function: generate_syntax_highlighting (line 265)
  function: extract_semantic_summary (line 277)
  function: validate_neurodiversity_compliance (line 311)
hypercode_backup_20251205_183301\core\src\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode_backup_20251205_183301\core\src\rag_engine.py:
  module: rag_engine (line 0)
hypercode_backup_20251205_183301\core\src\scaffold (1).py:
  module: scaffold (1) (line 0)
  function: create_directories (line 141)
  function: create_python_files (line 151)
  function: create_example_files (line 165)
  function: create_root_files (line 202)
  function: create_healthcheck (line 213)
  function: print_summary (line 234)
  function: main (line 259)
hypercode_backup_20251205_183301\core\src\scaffold.py:
  module: scaffold (line 0)
  function: create_directories (line 153)
  function: create_python_files (line 184)
  function: create_example_files (line 254)
  function: create_root_files (line 291)
  function: create_healthcheck (line 541)
  function: print_summary (line 583)
  function: main (line 621)
hypercode_backup_20251205_183301\core\src\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode_backup_20251205_183301\core\src\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode_backup_20251205_183301\core\src\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode_backup_20251205_183301\core\src\utils\code_analyzer_ai.py:
  module: code_analyzer_ai (line 0)
  class: CodeAnalyzerAI (line 19)
  function: __init__ (line 22)
  function: analyze_file (line 25)
  function: _analyze_complexity (line 61)
  function: _check_docstrings (line 98)
  function: _get_ai_code_analysis (line 134)
  function: analyze_project (line 162)
  function: _get_project_ai_insights (line 206)
  function: save_analysis (line 238)
  function: print_summary (line 244)
  function: main (line 262)
hypercode_backup_20251205_183301\core\src\utils\debug_search.py:
  module: debug_search (line 0)
  function: debug_search (line 15)
hypercode_backup_20251205_183301\core\src\utils\demo_ai_research.py:
  module: demo_ai_research (line 0)
  function: demo_ai_research_queries (line 16)
  function: test_document_specific_queries (line 90)
hypercode_backup_20251205_183301\core\src\utils\demo_enhanced_client.py:
  module: demo_enhanced_client (line 0)
  function: demo_knowledge_base_integration (line 16)
  function: demonstrate_memory_persistence (line 131)
hypercode_backup_20251205_183301\core\src\utils\final_integration_test.py:
  module: final_integration_test (line 0)
  function: final_integration_test (line 15)
hypercode_backup_20251205_183301\core\src\utils\health_scanner_ai.py:
  module: health_scanner_ai (line 0)
  class: HealthScannerAI (line 18)
  function: __init__ (line 21)
  function: analyze_project_structure (line 25)
  function: analyze_dependencies (line 64)
  function: analyze_security (line 100)
  function: get_ai_recommendations (line 137)
  function: run_full_scan (line 164)
  function: save_report (line 215)
  function: print_summary (line 221)
  function: main (line 241)
hypercode_backup_20251205_183301\core\src\utils\import-helper.py:
  module: import-helper (line 0)
  class: SpaceImportHelper (line 13)
  function: __init__ (line 16)
  function: validate_document (line 21)
  function: load_template (line 63)
  function: validate_all (line 83)
  function: generate_report (line 95)
  function: create_import_script (line 141)
  function: create_template_instructions (line 193)
  function: main (line 264)
hypercode_backup_20251205_183301\core\src\utils\import_all_space_data.py:
  module: import_all_space_data (line 0)
  function: format_content (line 16)
  function: import_all_hypercode_data (line 41)
hypercode_backup_20251205_183301\core\src\utils\import_hypercode_data.py:
  module: import_hypercode_data (line 0)
  function: import_hypercode_space_data (line 16)
hypercode_backup_20251205_183301\core\src\utils\import_perplexity_space.py:
  module: import_perplexity_space (line 0)
  function: create_manual_import_script (line 17)
  function: create_json_import_template (line 86)
  function: import_from_json (line 115)
  function: test_imported_data (line 153)
  function: show_import_menu (line 188)
hypercode_backup_20251205_183301\core\src\utils\local_health_scanner.py:
  module: local_health_scanner (line 0)
  class: ProjectScanner (line 19)
  function: __init__ (line 22)
  function: scan_project (line 34)
  function: _scan_directory (line 42)
  function: _analyze_file (line 51)
  function: _analyze_ast (line 74)
  function: _check_documentation (line 94)
  function: _check_tests (line 106)
  function: _calculate_metrics (line 117)
  function: print_health_report (line 128)
  function: main (line 158)
hypercode_backup_20251205_183301\core\src\utils\perplexity_space_collector.py:
  module: perplexity_space_collector (line 0)
  function: quick_copy_paste_collector (line 18)
  function: create_structured_template (line 117)
  function: show_bro_hacks (line 167)
  function: main_menu (line 207)
hypercode_backup_20251205_183301\core\src\utils\perplexity_space_integration.py:
  module: perplexity_space_integration (line 0)
  function: main (line 16)
hypercode_backup_20251205_183301\core\src\utils\run_lexer.py:
  function: run_lexer (line 12)
hypercode_backup_20251205_183301\core\src\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode_backup_20251205_183301\core\tests\benchmark_knowledge_base.py:
  module: benchmark_knowledge_base (line 0)
  class: BenchmarkSuite (line 24)
  function: __init__ (line 27)
  function: _get_system_info (line 34)
  function: generate_test_data (line 43)
  function: benchmark_operation (line 93)
  function: run_benchmark_suite (line 118)
  function: _calculate_summary (line 274)
  function: _generate_recommendations (line 296)
  function: generate_markdown_report (line 338)
  function: save_json_results (line 467)
  function: main (line 474)
hypercode_backup_20251205_183301\core\tests\conftest.py:
  function: sample_hypercode (line 16)
  function: sample_lexer_tokens (line 27)
hypercode_backup_20251205_183301\core\tests\test_accessibility.py:
  module: test_accessibility (line 0)
hypercode_backup_20251205_183301\core\tests\test_ai_gateway.py:
  module: test_ai_gateway (line 0)
hypercode_backup_20251205_183301\core\tests\test_backends.py:
  module: test_backends (line 0)
hypercode_backup_20251205_183301\core\tests\test_core.py:
  module: test_core (line 0)
  function: run_test (line 30)
hypercode_backup_20251205_183301\core\tests\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode_backup_20251205_183301\core\tests\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode_backup_20251205_183301\core\tests\test_integration.py:
  module: test_integration (line 0)
hypercode_backup_20251205_183301\core\tests\test_intent_blocks.py:
  module: test_intent_blocks (line 0)
  function: test_intent_block (line 13)
hypercode_backup_20251205_183301\core\tests\test_interpreter.py:
  function: run_code (line 10)
  class: TestInterpreter (line 28)
  function: test_if_statement_then (line 30)
  function: test_if_statement_else (line 42)
  function: test_function_call (line 54)
  function: test_function_with_parameters (line 64)
  function: test_function_with_return (line 74)
  function: test_recursive_function_call (line 85)
  function: test_scoping (line 99)
hypercode_backup_20251205_183301\core\tests\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestKnowledgeBaseSearch (line 12)
  function: sample_documents (line 16)
  function: knowledge_base (line 40)
  function: test_basic_search (line 48)
  function: test_search_with_exact_match (line 54)
  function: test_search_case_insensitive (line 59)
  function: test_search_empty_query (line 65)
  function: test_search_no_matches (line 71)
  function: test_search_ranking (line 77)
  function: test_query_normalization (line 90)
  function: test_multi_word_query (line 98)
  function: test_tag_based_search (line 103)
  class: TestEdgeCases (line 112)
  function: knowledge_base (line 116)
  function: test_very_short_query (line 121)
  function: test_very_long_query (line 126)
  function: test_special_characters_in_query (line 136)
  function: test_unicode_in_query (line 141)
  function: test_sql_injection_attempt (line 146)
  function: test_repeated_queries (line 151)
  class: TestPerformance (line 159)
  function: large_knowledge_base (line 163)
  function: test_search_response_time (line 179)
  function: test_concurrent_searches (line 189)
  function: test_memory_usage (line 207)
  class: TestIntegrationWithPerplexity (line 213)
  function: mock_perplexity_client (line 217)
  function: mock_knowledge_base (line 229)
  function: test_enhanced_query_with_context (line 243)
  function: test_fallback_to_perplexity_api (line 259)
  function: test_context_ranking_and_selection (line 273)
  class: TestDocumentManagement (line 288)
  function: knowledge_base (line 292)
  function: test_add_document (line 300)
  function: test_update_document (line 310)
  function: test_remove_document (line 315)
hypercode_backup_20251205_183301\core\tests\test_knowledge_base_comprehensive.py:
  module: test_knowledge_base_comprehensive (line 0)
  class: TestKnowledgeBaseUnit (line 20)
  function: temp_kb (line 24)
  function: sample_docs (line 36)
  function: test_init_empty_kb (line 59)
  function: test_add_single_document (line 65)
  function: test_add_multiple_documents (line 74)
  function: test_save_and_load (line 84)
  function: test_search_exact_match (line 102)
  function: test_search_partial_match (line 113)
  function: test_search_tag_matching (line 124)
  function: test_search_case_insensitive (line 135)
  function: test_empty_search (line 147)
  function: test_nonexistent_search (line 155)
  function: test_get_context_for_query (line 165)
  function: test_context_length_limit (line 176)
  function: test_document_update (line 186)
  function: test_list_documents (line 202)
  function: test_delete_document (line 213)
  class: TestKnowledgeBaseIntegration (line 229)
  function: populated_kb (line 233)
  function: test_complex_search_queries (line 277)
  function: test_search_ranking_quality (line 291)
  function: test_related_term_expansion (line 301)
  function: test_performance_with_large_dataset (line 313)
  function: test_concurrent_access_simulation (line 332)
  class: TestKnowledgeBasePerformance (line 356)
  function: large_kb (line 360)
  function: test_search_performance_large_dataset (line 382)
  function: test_save_performance_large_dataset (line 396)
  function: test_load_performance_large_dataset (line 409)
  function: test_memory_usage_large_dataset (line 423)
  class: TestKnowledgeBaseEdgeCases (line 446)
  function: edge_case_kb (line 450)
  function: test_empty_title_handling (line 494)
  function: test_special_characters_handling (line 499)
  function: test_very_long_titles (line 507)
  function: test_empty_content_handling (line 512)
  function: test_none_tags_handling (line 517)
  function: test_malformed_json_handling (line 531)
  function: test_file_permission_handling (line 544)
hypercode_backup_20251205_183301\core\tests\test_lexer.py:
  function: test_lexer_basic_tokens (line 5)
  function: test_lexer_strings (line 23)
  function: test_lexer_operators (line 48)
hypercode_backup_20251205_183301\core\tests\test_lexer_extended.py:
  function: test_lexer_escaped_strings (line 5)
  function: test_lexer_numbers (line 18)
  function: test_lexer_operators (line 39)
  function: test_lexer_comments (line 86)
  function: test_lexer_whitespace (line 115)
  function: test_lexer_error_handling (line 130)
  function: test_lexer_hex_numbers (line 139)
  function: test_lexer_binary_numbers (line 157)
  function: test_lexer_scientific_notation (line 169)
  function: test_lexer_string_escapes (line 180)
  function: test_lexer_keywords (line 197)
  function: test_lexer_position_tracking (line 223)
  function: test_lexer_error_recovery (line 243)
  function: test_lexer_error_messages (line 252)
hypercode_backup_20251205_183301\core\tests\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode_backup_20251205_183301\core\tests\test_parser.py:
  function: test_parse_literal (line 12)
  function: test_parse_variable_declaration (line 24)
  function: test_parse_binary_expression (line 37)
hypercode_backup_20251205_183301\core\tests\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode_backup_20251205_183301\core\tests\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 185)
hypercode_backup_20251205_183301\core\tests\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode_backup_20251205_183301\core\tests\test_sensory_profiles.py:
  module: test_sensory_profiles (line 0)
  function: test_visual_settings_creation (line 21)
  function: test_audio_settings_creation (line 35)
  function: test_animation_settings_creation (line 44)
  function: test_sensory_profile_creation (line 55)
  function: test_profile_serialization (line 71)
  function: test_profile_file_io (line 92)
  function: test_profile_manager_initialization (line 115)
  function: test_profile_manager_get_profile (line 129)
  function: test_profile_manager_save_custom_profile (line 142)
  function: test_profile_manager_delete_profile (line 169)
hypercode_backup_20251205_183301\core\tests\test_syntax.py:
  module: test_syntax (line 0)
  function: test_program_structure (line 8)
  function: test_function_definition (line 26)
  function: test_io_operations (line 49)
  function: test_variables (line 73)
  function: test_loops (line 96)
  function: test_conditionals (line 117)
  function: test_goto (line 142)
  function: test_comments (line 167)
hypercode_backup_20251205_183301\core\tests\tests\test_lexer_enhanced.py:
  function: test_lexer_edge_cases (line 7)
  function: test_lexer_error_handling (line 28)
  function: test_lexer_number_literals (line 43)
  function: test_lexer_string_interpolation (line 65)
  function: test_lexer_docstrings (line 79)
hypercode_backup_20251205_183301\core\tests\unit\lexer\test_lexer_basic.py:
  module: test_lexer_basic (line 0)
  class: TestLexerBasic (line 9)
  function: test_empty_source (line 12)
  function: test_whitespace_handling (line 19)
  function: test_single_character_tokens (line 27)
  function: test_comments_are_ignored (line 52)
  function: test_string_literals (line 72)
  function: test_number_literals (line 87)
  function: test_identifiers_and_keywords (line 103)
  function: test_error_handling (line 139)
hypercode_backup_20251205_183301\core\tests\unit\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode_backup_20251205_183301\core\tests\unit\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode_backup_20251205_183301\core\tests\unit\test_intent_blocks.py:
  module: test_intent_blocks (line 0)
  function: test_intent_block (line 13)
hypercode_backup_20251205_183301\core\tests\unit\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestHyperCodeKnowledgeBase (line 20)
  function: temp_kb (line 24)
  function: sample_documents (line 33)
  function: test_init_empty_kb (line 56)
  function: test_add_document (line 61)
  function: test_add_multiple_documents (line 82)
  function: test_save_and_load (line 92)
  function: test_search_exact_match (line 113)
  function: test_search_tag_matching (line 126)
  function: test_search_related_terms (line 139)
  function: test_search_space_data_boost (line 153)
  function: test_get_context_for_query (line 180)
  function: test_context_length_limit (line 192)
  function: test_list_documents (line 203)
  function: test_empty_search (line 216)
  function: test_search_nonexistent_term (line 221)
  function: test_document_update (line 231)
  class: TestResearchDocument (line 250)
  function: test_document_creation (line 253)
  function: test_document_optional_fields (line 273)
hypercode_backup_20251205_183301\core\tests\unit\test_lexer.py:
  module: test_lexer (line 0)
  function: test_lexer (line 12)
  function: run_tests (line 42)
hypercode_backup_20251205_183301\core\tests\unit\test_lexer_pytest.py:
  module: test_lexer_pytest (line 0)
  function: test_basic_arithmetic (line 9)
  function: test_variable_declaration (line 25)
  function: test_string_literals (line 40)
hypercode_backup_20251205_183301\core\tests\unit\test_mcp_connection.py:
  function: check_port (line 26)
  function: find_running_servers (line 36)
  function: test_server_connection (line 49)
  function: test_all_servers (line 90)
  function: check_dependencies (line 139)
hypercode_backup_20251205_183301\core\tests\unit\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode_backup_20251205_183301\core\tests\unit\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode_backup_20251205_183301\core\tests\unit\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 185)
hypercode_backup_20251205_183301\core\tests\unit\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode_backup_20251205_183301\core\tests\unit\test_search_algorithm.py:
  module: test_search_algorithm (line 0)
  class: TestSearchAlgorithm (line 20)
  function: populated_kb (line 24)
  function: test_exact_title_match_highest_score (line 80)
  function: test_space_data_boosting (line 92)
  function: test_related_term_expansion (line 105)
  function: test_tag_matching_scoring (line 126)
  function: test_content_frequency_scoring (line 136)
  function: test_partial_word_matching (line 149)
  function: test_query_word_ordering (line 167)
  function: test_case_insensitive_search (line 179)
  function: test_empty_query_returns_no_results (line 202)
  function: test_limit_parameter_respected (line 210)
  function: test_no_results_for_nonexistent_terms (line 219)
  function: test_special_characters_in_query (line 227)
  function: test_unicode_characters (line 237)
  function: test_search_performance_with_large_kb (line 256)
  function: test_search_result_consistency (line 277)
  class: TestSearchScoringDetails (line 292)
  function: scoring_kb (line 296)
  function: test_title_match_beats_content_match (line 324)
  function: test_space_data_boosting_works (line 332)
  function: test_frequency_scoring (line 340)
hypercode_backup_20251205_183301\database_analyzer.py:
  module: database_analyzer (line 0)
  class: EntityMetrics (line 15)
  class: DocstringStats (line 21)
  class: DatabaseAnalyzer (line 28)
  function: __init__ (line 29)
  function: load_database (line 48)
  function: analyze_documentation (line 64)
  function: analyze_test_coverage (line 96)
  function: analyze_code_structure (line 112)
  function: generate_report (line 135)
  function: get_entities_needing_docs (line 185)
  function: get_untested_entities (line 191)
  function: main (line 196)
hypercode_backup_20251205_183301\fix_database_issues.py:
  module: fix_database_issues (line 0)
  class: FixedCodeEntity (line 18)
  function: __post_init__ (line 45)
  function: _validate_required_fields (line 58)
  function: _validate_field_types (line 65)
  function: _normalize_fields (line 78)
  function: _clean_docstring (line 104)
  function: to_dict (line 118)
  class: DatabaseFixer (line 136)
  function: __init__ (line 139)
  function: load_database (line 153)
  function: _check_for_issues (line 190)
  function: fix_issues (line 217)
  function: save_database (line 245)
  function: generate_report (line 271)
  function: main (line 312)
hypercode_backup_20251205_183301\hypercode\accessibility\adhd_optimizer.py:
  module: adhd_optimizer (line 0)
hypercode_backup_20251205_183301\hypercode\accessibility\autism_preset.py:
  module: autism_preset (line 0)
hypercode_backup_20251205_183301\hypercode\accessibility\dyslexia_formatter.py:
  module: dyslexia_formatter (line 0)
hypercode_backup_20251205_183301\hypercode\accessibility\sensory_customizer.py:
  module: sensory_customizer (line 0)
hypercode_backup_20251205_183301\hypercode\accessibility\wcag_auditor.py:
  module: wcag_auditor (line 0)
hypercode_backup_20251205_183301\hypercode\benchmarks\__init__.py:
  function: benchmark_lexer (line 13)
  function: print_benchmark_results (line 38)
hypercode_backup_20251205_183301\hypercode\benchmarks\benchmarks_lexer.py:
  function: benchmark_lexer (line 7)
  function: print_benchmark_results (line 32)
hypercode_backup_20251205_183301\hypercode\build-hyper-database.py:
  module: build-hyper-database (line 0)
  class: HyperDatabaseBuilder (line 21)
  function: __init__ (line 24)
  function: scan_python_file (line 32)
  function: scan_javascript_file (line 78)
  function: should_skip_directory (line 107)
  function: build (line 127)
  function: generate_markdown_report (line 161)
  function: generate_json_report (line 248)
  function: main (line 263)
hypercode_backup_20251205_183301\hypercode\knowledge_graph\graph_builder.py:
  module: graph_builder (line 0)
hypercode_backup_20251205_183301\hypercode\knowledge_graph\sparql_query.py:
  module: sparql_query (line 0)
hypercode_backup_20251205_183301\hypercode\knowledge_graph\update_agent.py:
  module: update_agent (line 0)
hypercode_backup_20251205_183301\hypercode\live_research\doc_generator.py:
  module: doc_generator (line 0)
hypercode_backup_20251205_183301\hypercode\live_research\github_publisher.py:
  module: github_publisher (line 0)
hypercode_backup_20251205_183301\hypercode\live_research\paper_indexer.py:
  module: paper_indexer (line 0)
hypercode_backup_20251205_183301\hypercode\live_research\research_crawler.py:
  module: research_crawler (line 0)
hypercode_backup_20251205_183301\hypercode\live_research\synthesis_engine.py:
  module: synthesis_engine (line 0)
hypercode_backup_20251205_183301\hypercode\mcp\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\hypercode\mcp\servers\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\hypercode\mcp\servers\aws_cli.py:
  function: main (line 4)
hypercode_backup_20251205_183301\hypercode\mcp\servers\aws_resource_manager.py:
  function: main (line 4)
hypercode_backup_20251205_183301\hypercode\mcp\servers\code_analysis.py:
  function: main (line 4)
hypercode_backup_20251205_183301\hypercode\mcp\servers\dataset_downloader.py:
  function: main (line 4)
hypercode_backup_20251205_183301\hypercode\mcp\servers\file_system.py:
  function: main (line 4)
hypercode_backup_20251205_183301\hypercode\mcp\servers\human_input.py:
  function: main (line 4)
hypercode_backup_20251205_183301\hypercode\mcp\servers\hypercode_syntax.py:
  module: hypercode_syntax (line 0)
  class: HyperCodeSyntaxServer (line 28)
  function: __init__ (line 31)
  function: handle_request (line 35)
  function: _initialize (line 56)
  function: _document_changed (line 79)
  function: _text_hover (line 98)
  function: _completion (line 121)
  function: _parse_document (line 150)
  function: _validate_neurodiversity (line 179)
  function: _generate_diagnostics (line 216)
  function: _get_annotation_hover_info (line 266)
  function: main (line 294)
hypercode_backup_20251205_183301\hypercode\mcp\servers\path_service.py:
  function: main (line 4)
hypercode_backup_20251205_183301\hypercode\mcp\servers\user_profile_manager.py:
  function: main (line 4)
hypercode_backup_20251205_183301\hypercode\mcp\servers\valkey_service.py:
  function: check_redis_connection (line 40)
  function: health_check (line 59)
  function: set_key (line 67)
  function: get_key (line 80)
  function: hset_key (line 95)
  function: hget_key (line 107)
  function: hgetall_hash (line 126)
  function: main (line 144)
hypercode_backup_20251205_183301\hypercode\mcp\servers\web_search.py:
  function: main (line 4)
hypercode_backup_20251205_183301\hypercode\mcp\setup.py:
  module: setup (line 0)
  function: install_dependencies (line 16)
  function: verify_setup (line 31)
  function: show_next_steps (line 54)
  function: main (line 72)
hypercode_backup_20251205_183301\hypercode\mcp\start_servers.py:
  module: start_servers (line 0)
  function: start_server (line 34)
  function: list_servers (line 59)
  function: main (line 66)
hypercode_backup_20251205_183301\hypercode\mcp\test_mcp.py:
  module: test_mcp (line 0)
  function: test_server_imports (line 15)
  function: main (line 47)
hypercode_backup_20251205_183301\hypercode\new files to check\backend\research\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\hypercode\new files to check\backend\research\db.py:
  module: db (line 0)
  function: _get_database_url (line 35)
hypercode_backup_20251205_183301\hypercode\new files to check\backend\research\models.py:
  module: models (line 0)
  class: Study (line 32)
  function: __repr__ (line 52)
  class: Source (line 56)
  function: __repr__ (line 81)
  class: LanguageVersion (line 85)
  function: __repr__ (line 102)
  class: Task (line 106)
  function: __repr__ (line 124)
  class: Participant (line 128)
  function: __repr__ (line 144)
  class: Session (line 148)
  function: __repr__ (line 169)
  class: Event (line 176)
  function: __repr__ (line 193)
  class: Feedback (line 199)
  function: __repr__ (line 221)
hypercode_backup_20251205_183301\hypercode\new files to check\backend\research\scripts\import_sources_from_folder.py:
  module: import_sources_from_folder (line 0)
  function: infer_kind (line 25)
  function: main (line 36)
hypercode_backup_20251205_183301\hypercode\new files to check\backend\research\scripts\seed_basic_data.py:
  module: seed_basic_data (line 0)
  function: main (line 25)
hypercode_backup_20251205_183301\hypercode\run_lexer.py:
  function: run_lexer (line 13)
hypercode_backup_20251205_183301\hypercode\scripts\style_guide_collector.py:
  module: style_guide_collector (line 0)
  class: StyleGuideCollector (line 18)
  function: __init__ (line 21)
  function: _load_feedback (line 32)
  function: _save_feedback (line 51)
  function: add_feedback (line 60)
  function: _update_analysis (line 102)
  function: analyze_feedback (line 151)
  function: _get_top_items (line 189)
  function: _calculate_consensus (line 212)
  function: _generate_recommendations (line 247)
  function: import_github_issues (line 331)
  function: generate_report (line 354)
  function: interactive_feedback (line 419)
  function: main (line 527)
hypercode_backup_20251205_183301\hypercode\scripts\test_perplexity_api.py:
  module: test_perplexity_api (line 0)
  function: main (line 17)
hypercode_backup_20251205_183301\hypercode\src\ai_gateway\base_gateway.py:
  module: base_gateway (line 0)
hypercode_backup_20251205_183301\hypercode\src\ai_gateway\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\hypercode\src\ai_gateway\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\hypercode\src\ai_gateway\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\hypercode\src\ai_gateway\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\hypercode\src\ai_gateway\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode_backup_20251205_183301\hypercode\src\ai_gateway\rag_engine.py:
  module: rag_engine (line 0)
hypercode_backup_20251205_183301\hypercode\src\base_gateway.py:
  module: base_gateway (line 0)
hypercode_backup_20251205_183301\hypercode\src\build.py:
  module: build (line 0)
  function: build (line 34)
hypercode_backup_20251205_183301\hypercode\src\claude_adapter.py:
  module: claude_adapter (line 0)
  class: ClaudeAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\hypercode\src\core\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\hypercode\src\core\ast.py:
  class: Node (line 9)
  function: accept (line 10)
  class: Expr (line 20)
  class: Literal (line 25)
  class: Variable (line 30)
  class: Assign (line 35)
  class: Binary (line 41)
  class: Unary (line 48)
  class: Grouping (line 54)
  class: Call (line 59)
  class: Get (line 66)
  class: Stmt (line 73)
  class: Expression (line 78)
  class: Print (line 83)
  class: Var (line 88)
  class: Block (line 94)
  class: Intent (line 99)
  class: Function (line 104)
  class: If (line 111)
  class: Return (line 118)
  class: Program (line 125)
hypercode_backup_20251205_183301\hypercode\src\core\ast_nodes.py:
  module: ast_nodes (line 0)
  class: Node (line 24)
  class: Expression (line 31)
  class: Statement (line 38)
  class: Program (line 45)
  class: Identifier (line 52)
  class: Literal (line 59)
  class: VariableDeclaration (line 66)
  class: BinaryOperation (line 75)
hypercode_backup_20251205_183301\hypercode\src\core\interpreter.py:
  class: RuntimeError (line 8)
  function: __init__ (line 9)
  class: Environment (line 15)
  function: __init__ (line 16)
  function: define (line 20)
  function: get (line 23)
  function: assign (line 30)
  class: Callable (line 40)
  function: arity (line 41)
  function: call (line 44)
  class: Function (line 48)
  function: __init__ (line 49)
  function: call (line 53)
  function: arity (line 65)
  class: ReturnException (line 69)
  function: __init__ (line 70)
  class: Interpreter (line 74)
  function: __init__ (line 75)
  class: Clock (line 82)
  function: arity (line 83)
  function: call (line 86)
  function: __str__ (line 89)
  function: execute_block (line 94)
  function: interpret (line 103)
  function: execute (line 112)
  function: evaluate (line 115)
  function: visit_Expression (line 118)
  function: visit_Print (line 122)
  function: visit_Var (line 129)
  function: visit_Block (line 136)
  function: visit_Expression (line 140)
  function: visit_Print (line 144)
  function: visit_Intent (line 150)
  function: visit_Function (line 155)
  function: visit_Return (line 160)
  function: visit_Literal (line 166)
  function: visit_Grouping (line 169)
  function: visit_Variable (line 172)
  function: visit_Assign (line 175)
  function: visit_Call (line 180)
  function: visit_Binary (line 198)
  function: visit_Unary (line 229)
  function: is_truthy (line 237)
  function: stringify (line 244)
  function: get_output (line 256)
hypercode_backup_20251205_183301\hypercode\src\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 17)
  class: Lexer (line 34)
  function: __init__ (line 42)
  function: scan_tokens (line 99)
  function: scan_token (line 109)
  function: number (line 168)
  function: string (line 203)
  function: docstring (line 252)
  function: identifier (line 278)
  function: error (line 288)
  function: is_at_end (line 312)
  function: advance (line 316)
  function: match (line 325)
  function: peek (line 335)
  function: peek_next (line 341)
  function: add_token (line 347)
hypercode_backup_20251205_183301\hypercode\src\core\optimizer.py:
  module: optimizer (line 0)
hypercode_backup_20251205_183301\hypercode\src\core\parser.py:
  class: ParseError (line 7)
  class: Parser (line 11)
  function: __init__ (line 12)
  function: parse (line 16)
  function: declaration (line 25)
  function: var_declaration (line 36)
  function: statement (line 61)
  function: print_statement (line 72)
  function: expression_statement (line 77)
  function: block (line 82)
  function: expression (line 91)
  function: assignment (line 94)
  function: equality (line 109)
  function: comparison (line 119)
  function: term (line 132)
  function: factor (line 140)
  function: unary (line 148)
  function: primary (line 155)
  function: function (line 177)
  function: if_statement (line 200)
  function: return_statement (line 212)
  function: match (line 222)
  function: consume (line 229)
  function: error (line 239)
  function: synchronize (line 245)
  function: check (line 265)
  function: advance (line 270)
  function: is_at_end (line 275)
  function: peek (line 278)
  function: previous (line 281)
hypercode_backup_20251205_183301\hypercode\src\core\tokens.py:
  module: tokens (line 0)
  class: TokenType (line 11)
  class: Token (line 71)
  function: __init__ (line 83)
  function: __str__ (line 92)
  function: __repr__ (line 95)
hypercode_backup_20251205_183301\hypercode\src\duelcode\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode_backup_20251205_183301\hypercode\src\duelcode\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode_backup_20251205_183301\hypercode\src\duelcode\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode_backup_20251205_183301\hypercode\src\duelcode\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode_backup_20251205_183301\hypercode\src\duelcode\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode_backup_20251205_183301\hypercode\src\duelcode\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode_backup_20251205_183301\hypercode\src\duelcode_validator.py:
  module: duelcode_validator (line 0)
  class: Severity (line 16)
  class: ValidationResult (line 23)
  class: DuelCodeValidator (line 30)
  function: __init__ (line 51)
  function: _add_result (line 58)
  function: _find_lines (line 71)
  function: validate (line 81)
  function: validate_structure (line 93)
  function: validate_headings (line 129)
  function: validate_code_blocks (line 171)
  function: validate_checklists (line 210)
  function: validate_visual_elements (line 245)
  function: validate_links (line 263)
  function: print_validation_results (line 283)
  function: main (line 316)
hypercode_backup_20251205_183301\hypercode\src\enhanced_validator.py:
  module: enhanced_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 19)
  class: DuelCodeEnhancedValidator (line 26)
  function: __init__ (line 83)
  function: _add_result (line 90)
  function: _find_lines (line 103)
  function: validate_code_blocks_have_language (line 115)
  function: validate_has_visual_representation (line 128)
  function: validate_has_practical_exercise (line 140)
  function: validate_has_learning_objectives (line 152)
  function: validate_has_checklist (line 174)
  function: validate_has_conclusion (line 195)
  function: validate_has_whats_next (line 204)
  function: validate_code_quality (line 213)
  function: _analyze_code_block (line 234)
  function: _analyze_python_code (line 256)
  function: _analyze_javascript_code (line 277)
  function: validate_has_glossary (line 291)
  function: validate_has_see_also (line 325)
  function: validate_has_faq (line 334)
  function: validate_has_acknowledgments (line 344)
  function: validate_all (line 353)
  function: print_validation_results (line 376)
  function: main (line 407)
hypercode_backup_20251205_183301\hypercode\src\hypercode-backend-js-COMPLETE.py:
  module: hypercode-backend-js-COMPLETE (line 0)
  class: JSCompiler (line 19)
  function: __init__ (line 30)
  function: compile (line 42)
  function: _generate_header (line 65)
  function: _generate_setup (line 74)
  function: _generate_main (line 110)
  function: _generate_footer (line 162)
  function: _indent (line 179)
  function: optimize_ast (line 183)
  function: main (line 200)
hypercode_backup_20251205_183301\hypercode\src\hypercode-idea-generator-WEB.py:
  module: hypercode-idea-generator-WEB (line 0)
hypercode_backup_20251205_183301\hypercode\src\hypercode-launch-kit.py:
  module: hypercode-launch-kit (line 0)
  class: HyperCodeLaunchKit (line 23)
  function: __init__ (line 26)
  function: create_readme (line 30)
  function: create_launch_checklist (line 367)
  function: create_launch_script (line 620)
  function: create_first_30_days (line 718)
  function: print_summary (line 974)
  function: main (line 1007)
hypercode_backup_20251205_183301\hypercode\src\hypercode-lexer-COMPLETE.py:
  module: hypercode-lexer-COMPLETE (line 0)
  class: TokenType (line 21)
  class: Token (line 45)
  function: __repr__ (line 54)
  class: LexerError (line 59)
  function: __init__ (line 62)
  class: HyperCodeLexer (line 69)
  function: __init__ (line 95)
  function: tokenize (line 110)
  function: _advance_position (line 169)
  function: _skip_comment (line 179)
  function: get_tokens (line 184)
  function: filter_tokens (line 188)
  function: print_tokens (line 205)
  function: get_statistics (line 236)
  function: main (line 250)
hypercode_backup_20251205_183301\hypercode\src\hypercode-parser-COMPLETE.py:
  module: hypercode-parser-COMPLETE (line 0)
  class: NodeType (line 22)
  class: ASTNode (line 38)
  function: __repr__ (line 51)
  class: ParserError (line 68)
  function: __init__ (line 71)
  class: HyperCodeParser (line 80)
  function: __init__ (line 94)
  function: parse (line 105)
  function: _parse_statement (line 127)
  function: _parse_loop (line 174)
  function: _advance (line 209)
  function: _is_at_end (line 215)
  function: validate (line 222)
  function: print_ast (line 237)
  function: main (line 251)
hypercode_backup_20251205_183301\hypercode\src\hypercode\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\hypercode\src\hypercode\__main__.py:
  function: main (line 6)
hypercode_backup_20251205_183301\hypercode\src\hypercode\config.py:
  module: config (line 0)
  class: Config (line 16)
  function: get_headers (line 27)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\ast.py:
  class: Node (line 9)
  function: accept (line 10)
  class: Expr (line 20)
  class: Literal (line 25)
  class: Variable (line 30)
  class: Assign (line 35)
  class: Binary (line 41)
  class: Unary (line 48)
  class: Grouping (line 54)
  class: Call (line 59)
  class: Get (line 66)
  class: Stmt (line 73)
  class: Expression (line 78)
  class: Print (line 83)
  class: Var (line 88)
  class: Block (line 94)
  class: If (line 99)
  class: Fun (line 106)
  class: Return (line 113)
  class: Intent (line 119)
  class: Program (line 126)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\cli.py:
  module: cli (line 0)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\error_handler.py:
  function: report_parse_error (line 5)
  function: report (line 12)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\interpreter.py:
  class: Return (line 8)
  function: __init__ (line 9)
  class: HyperCodeFunction (line 13)
  function: __init__ (line 14)
  function: __str__ (line 18)
  function: arity (line 21)
  function: call (line 24)
  class: Environment (line 37)
  function: __init__ (line 38)
  function: define (line 42)
  function: get (line 45)
  function: assign (line 52)
  class: Interpreter (line 62)
  function: __init__ (line 63)
  function: interpret (line 67)
  function: execute (line 74)
  function: execute_block (line 77)
  function: evaluate (line 86)
  function: visit_Expression (line 89)
  function: visit_Print (line 92)
  function: visit_Var (line 96)
  function: visit_Block (line 102)
  function: visit_Assign (line 105)
  function: visit_Binary (line 110)
  function: visit_Grouping (line 153)
  function: visit_Literal (line 156)
  function: visit_Unary (line 159)
  function: visit_Variable (line 172)
  function: visit_If (line 175)
  function: is_truthy (line 181)
  function: visit_Fun (line 188)
  function: visit_Return (line 192)
  function: visit_Call (line 198)
  function: is_callable (line 216)
  class: Visitor (line 221)
  function: visit_Expression (line 222)
  function: visit_Print (line 225)
  function: visit_Var (line 228)
  function: visit_Block (line 231)
  function: visit_If (line 234)
  function: visit_Fun (line 237)
  function: visit_Return (line 240)
  function: visit_Assign (line 243)
  function: visit_Binary (line 246)
  function: visit_Grouping (line 249)
  function: visit_Literal (line 252)
  function: visit_Unary (line 255)
  function: visit_Variable (line 258)
  function: visit_Call (line 261)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\lexer.py:
  module: lexer (line 0)
  class: LexerError (line 32)
  function: __init__ (line 35)
  class: Lexer (line 42)
  function: __init__ (line 109)
  function: tokenize (line 126)
  function: _match_patterns (line 161)
  function: _update_position (line 187)
  function: _add_token (line 206)
  function: _handle_unknown (line 270)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\optimizer.py:
  module: optimizer (line 0)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\parser.py:
  class: ParseError (line 8)
  class: Parser (line 12)
  function: __init__ (line 13)
  function: parse (line 17)
  function: declaration (line 26)
  function: var_declaration (line 37)
  function: statement (line 53)
  function: print_statement (line 66)
  function: return_statement (line 71)
  function: intent_statement (line 79)
  function: expression_statement (line 94)
  function: if_statement (line 99)
  function: function (line 111)
  function: block (line 130)
  function: expression (line 137)
  function: assignment (line 140)
  function: equality (line 155)
  function: comparison (line 165)
  function: term (line 178)
  function: factor (line 186)
  function: unary (line 194)
  function: primary (line 201)
  function: _primary (line 218)
  function: finish_call (line 249)
  function: match (line 262)
  function: consume (line 269)
  function: error (line 276)
  function: synchronize (line 282)
  function: check (line 302)
  function: advance (line 307)
  function: is_at_end (line 312)
  function: peek (line 315)
  function: previous (line 318)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\semantic_analyzer.py:
  module: semantic_analyzer (line 0)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\sensory_profile.py:
  module: sensory_profile (line 0)
  class: VisualNoiseLevel (line 15)
  class: AnimationSpeed (line 22)
  class: VisualSettings (line 29)
  class: AudioSettings (line 43)
  class: AnimationSettings (line 58)
  class: SensoryProfile (line 68)
  function: to_dict (line 77)
  function: from_dict (line 85)
  function: save (line 107)
  function: load (line 113)
  class: ProfileManager (line 120)
  function: __init__ (line 123)
  function: _ensure_default_profiles (line 133)
  function: _create_minimal_profile (line 146)
  function: _create_enhanced_profile (line 163)
  function: _create_high_contrast_profile (line 190)
  function: list_profiles (line 216)
  function: get_profile (line 220)
  function: save_profile (line 227)
  function: delete_profile (line 232)
  function: get_profile (line 243)
  function: list_profiles (line 248)
hypercode_backup_20251205_183301\hypercode\src\hypercode\core\tokens.py:
  class: TokenType (line 6)
  class: Token (line 61)
  function: __str__ (line 68)
hypercode_backup_20251205_183301\hypercode\src\hypercode\enhanced_perplexity_client.py:
  module: enhanced_perplexity_client (line 0)
  class: EnhancedPerplexityClient (line 18)
  function: __init__ (line 21)
  function: query_with_context (line 25)
  function: add_research_data (line 61)
  function: search_research_data (line 71)
  function: list_research_documents (line 75)
  function: get_document (line 79)
  function: delete_document (line 83)
  function: import_from_perplexity_space (line 87)
  function: test_context_integration (line 123)
  function: create_perplexity_space_import_template (line 175)
hypercode_backup_20251205_183301\hypercode\src\hypercode\knowledge_base.py:
  module: knowledge_base (line 0)
  class: ResearchDocument (line 17)
  function: __post_init__ (line 28)
  function: generate_id (line 36)
  function: validate (line 41)
  function: update_timestamp (line 53)
  class: HyperCodeKnowledgeBase (line 100)
  function: __init__ (line 103)
  function: load (line 109)
  function: save (line 125)
  function: add_document (line 135)
  function: search_documents (line 163)
  function: get_context_for_query (line 227)
  function: list_documents (line 257)
  function: get_document (line 261)
  function: delete_document (line 265)
  function: update_document (line 273)
  function: search_by_tags (line 287)
  function: get_document_statistics (line 306)
  function: export_format (line 331)
  function: validate_all_documents (line 353)
  function: cleanup_duplicates (line 363)
  function: initialize_sample_data (line 384)
hypercode_backup_20251205_183301\hypercode\src\hypercode\perplexity_client.py:
  module: perplexity_client (line 0)
  class: PerplexityClient (line 12)
  function: __init__ (line 15)
  function: query (line 30)
  function: test_connection (line 72)
hypercode_backup_20251205_183301\hypercode\src\hypercode\repl.py:
  function: run_repl (line 12)
  function: run (line 33)
  function: show_help (line 54)
hypercode_backup_20251205_183301\hypercode\src\hypercode_idea_generator.py:
  module: hypercode_idea_generator (line 0)
  class: HyperCodeIdeaGenerator (line 431)
  function: __init__ (line 439)
  function: get_ideas_by_category (line 443)
  function: get_top_ideas (line 468)
  function: vote_for_idea (line 487)
  function: get_trending_ideas (line 497)
  function: format_idea_card (line 502)
  function: main (line 528)
hypercode_backup_20251205_183301\hypercode\src\hypercode_poc.py:
  module: hypercode_poc (line 0)
  class: TokenType (line 18)
  class: Token (line 34)
  class: UserConfidenceLevel (line 41)
  class: EnhancedLexer (line 48)
  function: __init__ (line 51)
  function: tokenize (line 74)
  function: handle_string (line 115)
  function: handle_number (line 141)
  function: handle_identifier (line 149)
  function: advance (line 171)
  class: ContextAwareErrorMessenger (line 176)
  function: __init__ (line 179)
  function: format_error (line 182)
  class: SemanticContextStreamer (line 189)
  function: analyze (line 192)
  class: ConfidenceTracker (line 209)
  function: __init__ (line 212)
  function: record (line 216)
  class: HyperCodePOC (line 222)
  function: __init__ (line 225)
  function: compile (line 232)
hypercode_backup_20251205_183301\hypercode\src\mistral_adapter.py:
  module: mistral_adapter (line 0)
  class: MistralAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\hypercode\src\ollama_adapter.py:
  module: ollama_adapter (line 0)
  class: OllamaAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\hypercode\src\openai_adapter.py:
  module: openai_adapter (line 0)
  class: OpenaiAdapterAdapter (line 22)
  function: __init__ (line 25)
hypercode_backup_20251205_183301\hypercode\src\parser\debug_ascii.py:
  module: debug_ascii (line 0)
  function: test_regex_patterns (line 14)
hypercode_backup_20251205_183301\hypercode\src\parser\debug_full.py:
  module: debug_full (line 0)
  function: debug_full_parsing (line 14)
hypercode_backup_20251205_183301\hypercode\src\parser\debug_parser.py:
  module: debug_parser (line 0)
  function: debug_annotation_detection (line 14)
hypercode_backup_20251205_183301\hypercode\src\parser\debug_simple.py:
  module: debug_simple (line 0)
  function: debug_simple (line 14)
hypercode_backup_20251205_183301\hypercode\src\parser\test_parser.py:
  module: test_parser (line 0)
  function: test_first_click_moment (line 14)
hypercode_backup_20251205_183301\hypercode\src\parser\visual_syntax_parser.py:
  module: visual_syntax_parser (line 0)
  class: SemanticMarker (line 18)
  class: SemanticAnnotation (line 37)
  function: __str__ (line 46)
  class: ParsedFunction (line 51)
  function: get_annotations_by_type (line 62)
  class: VisualSyntaxParser (line 69)
  function: __init__ (line 72)
  function: _build_semantic_patterns (line 76)
  function: _build_color_scheme (line 105)
  function: parse_file (line 123)
  function: parse_content (line 130)
  function: _is_function_definition (line 170)
  function: _start_new_function (line 179)
  function: _parse_line_annotations (line 202)
  function: _parse_annotation_params (line 223)
  function: generate_syntax_highlighting (line 265)
  function: extract_semantic_summary (line 277)
  function: validate_neurodiversity_compliance (line 311)
hypercode_backup_20251205_183301\hypercode\src\prompt_normalizer.py:
  module: prompt_normalizer (line 0)
hypercode_backup_20251205_183301\hypercode\src\rag_engine.py:
  module: rag_engine (line 0)
hypercode_backup_20251205_183301\hypercode\src\scaffold (1).py:
  module: scaffold (1) (line 0)
  function: create_directories (line 141)
  function: create_python_files (line 151)
  function: create_example_files (line 165)
  function: create_root_files (line 202)
  function: create_healthcheck (line 213)
  function: print_summary (line 234)
  function: main (line 259)
hypercode_backup_20251205_183301\hypercode\src\scaffold.py:
  module: scaffold (line 0)
  function: create_directories (line 153)
  function: create_python_files (line 184)
  function: create_example_files (line 254)
  function: create_root_files (line 291)
  function: create_healthcheck (line 541)
  function: print_summary (line 583)
  function: main (line 621)
hypercode_backup_20251205_183301\hypercode\src\test_framework.py:
  module: test_framework (line 0)
  class: TestResult (line 17)
  class: TestCase (line 24)
  class: TestRun (line 34)
  class: DuelCodeTestSuite (line 44)
  function: __init__ (line 45)
  function: discover_tutorials (line 49)
  function: run_validator (line 56)
  function: parse_validator_output (line 71)
  function: test_tutorial (line 99)
  function: test_validator_integrity (line 135)
  function: test_template_validity (line 176)
  function: run_all_tests (line 221)
  function: generate_report (line 248)
  function: main (line 295)
hypercode_backup_20251205_183301\hypercode\src\test_validator.py:
  module: test_validator (line 0)
  function: test_valid_file (line 11)
  function: test_invalid_file (line 65)
  function: main (line 90)
hypercode_backup_20251205_183301\hypercode\src\ultra_validator.py:
  module: ultra_validator (line 0)
  class: Severity (line 12)
  class: ValidationResult (line 20)
  class: DuelCodeUltraValidator (line 28)
  function: __init__ (line 88)
  function: _add_result (line 95)
  function: _find_lines (line 106)
  function: validate_code_blocks_have_language (line 118)
  function: validate_has_visual_representation (line 152)
  function: validate_has_practical_exercise (line 171)
  function: validate_has_learning_objectives (line 192)
  function: validate_has_checklist (line 215)
  function: validate_has_conclusion (line 234)
  function: validate_has_whats_next (line 257)
  function: validate_code_quality (line 278)
  function: _validate_code_block_content (line 305)
  function: validate_has_glossary (line 340)
  function: validate_has_see_also (line 360)
  function: validate_has_faq (line 380)
  function: validate_has_acknowledgments (line 402)
  function: validate_accessibility (line 422)
  function: validate_interactive_elements (line 443)
  function: validate_all (line 463)
  function: print_results (line 487)
  function: main (line 537)
hypercode_backup_20251205_183301\hypercode\src\utils\code_analyzer_ai.py:
  module: code_analyzer_ai (line 0)
  class: CodeAnalyzerAI (line 19)
  function: __init__ (line 22)
  function: analyze_file (line 25)
  function: _analyze_complexity (line 72)
  function: _check_docstrings (line 113)
  function: _get_ai_code_analysis (line 155)
  function: analyze_project (line 183)
  function: _get_project_ai_insights (line 230)
  function: save_analysis (line 262)
  function: print_summary (line 270)
  function: main (line 288)
hypercode_backup_20251205_183301\hypercode\src\utils\debug_search.py:
  module: debug_search (line 0)
  function: debug_search (line 15)
hypercode_backup_20251205_183301\hypercode\src\utils\demo_ai_research.py:
  module: demo_ai_research (line 0)
  function: demo_ai_research_queries (line 16)
  function: test_document_specific_queries (line 90)
hypercode_backup_20251205_183301\hypercode\src\utils\demo_enhanced_client.py:
  module: demo_enhanced_client (line 0)
  function: demo_knowledge_base_integration (line 16)
  function: demonstrate_memory_persistence (line 131)
hypercode_backup_20251205_183301\hypercode\src\utils\final_integration_test.py:
  module: final_integration_test (line 0)
  function: final_integration_test (line 15)
hypercode_backup_20251205_183301\hypercode\src\utils\health_scanner_ai.py:
  module: health_scanner_ai (line 0)
  class: HealthScannerAI (line 18)
  function: __init__ (line 21)
  function: analyze_project_structure (line 25)
  function: analyze_dependencies (line 68)
  function: analyze_security (line 110)
  function: get_ai_recommendations (line 143)
  function: run_full_scan (line 170)
  function: save_report (line 221)
  function: print_summary (line 227)
  function: main (line 247)
hypercode_backup_20251205_183301\hypercode\src\utils\import-helper.py:
  module: import-helper (line 0)
  class: SpaceImportHelper (line 13)
  function: __init__ (line 16)
  function: validate_document (line 21)
  function: load_template (line 63)
  function: validate_all (line 83)
  function: generate_report (line 95)
  function: create_import_script (line 141)
  function: create_template_instructions (line 193)
  function: main (line 264)
hypercode_backup_20251205_183301\hypercode\src\utils\import_all_space_data.py:
  module: import_all_space_data (line 0)
  function: format_content (line 16)
  function: import_all_hypercode_data (line 41)
hypercode_backup_20251205_183301\hypercode\src\utils\import_hypercode_data.py:
  module: import_hypercode_data (line 0)
  function: import_hypercode_space_data (line 16)
hypercode_backup_20251205_183301\hypercode\src\utils\import_perplexity_space.py:
  module: import_perplexity_space (line 0)
  function: create_manual_import_script (line 17)
  function: create_json_import_template (line 86)
  function: import_from_json (line 115)
  function: test_imported_data (line 153)
  function: show_import_menu (line 188)
hypercode_backup_20251205_183301\hypercode\src\utils\local_health_scanner.py:
  module: local_health_scanner (line 0)
  class: ProjectScanner (line 20)
  function: __init__ (line 23)
  function: scan_project (line 35)
  function: _scan_directory (line 43)
  function: _analyze_file (line 52)
  function: _analyze_ast (line 77)
  function: _check_documentation (line 97)
  function: _check_tests (line 109)
  function: _calculate_metrics (line 120)
  function: print_health_report (line 132)
  function: main (line 163)
hypercode_backup_20251205_183301\hypercode\src\utils\perplexity_space_collector.py:
  module: perplexity_space_collector (line 0)
  function: quick_copy_paste_collector (line 18)
  function: create_structured_template (line 117)
  function: show_bro_hacks (line 167)
  function: main_menu (line 207)
hypercode_backup_20251205_183301\hypercode\src\utils\perplexity_space_integration.py:
  module: perplexity_space_integration (line 0)
  function: main (line 16)
hypercode_backup_20251205_183301\hypercode\src\utils\run_lexer.py:
  function: run_lexer (line 13)
hypercode_backup_20251205_183301\hypercode\src\validate_duelcode.py:
  module: validate_duelcode (line 0)
  class: DuelCodeValidator (line 23)
  function: __init__ (line 24)
  function: validate_sections (line 30)
  function: check_formatting (line 39)
  function: check_visual_aids (line 55)
  function: validate (line 60)
  function: main (line 68)
hypercode_backup_20251205_183301\hypercode\test_mcp_connection.py:
  function: check_port (line 26)
  function: find_running_servers (line 36)
  function: test_server_connection (line 49)
  function: test_all_servers (line 90)
  function: check_dependencies (line 139)
hypercode_backup_20251205_183301\hypercode\tests\benchmark_knowledge_base.py:
  module: benchmark_knowledge_base (line 0)
  class: BenchmarkSuite (line 24)
  function: __init__ (line 27)
  function: _get_system_info (line 34)
  function: generate_test_data (line 43)
  function: benchmark_operation (line 93)
  function: run_benchmark_suite (line 118)
  function: _calculate_summary (line 274)
  function: _generate_recommendations (line 296)
  function: generate_markdown_report (line 338)
  function: save_json_results (line 467)
  function: main (line 474)
hypercode_backup_20251205_183301\hypercode\tests\test_accessibility.py:
  module: test_accessibility (line 0)
hypercode_backup_20251205_183301\hypercode\tests\test_ai_gateway.py:
  module: test_ai_gateway (line 0)
hypercode_backup_20251205_183301\hypercode\tests\test_backends.py:
  module: test_backends (line 0)
hypercode_backup_20251205_183301\hypercode\tests\test_core.py:
  module: test_core (line 0)
  function: run_test (line 30)
hypercode_backup_20251205_183301\hypercode\tests\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode_backup_20251205_183301\hypercode\tests\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode_backup_20251205_183301\hypercode\tests\test_integration.py:
  module: test_integration (line 0)
hypercode_backup_20251205_183301\hypercode\tests\test_intent_blocks.py:
  module: test_intent_blocks (line 0)
  function: test_intent_block (line 13)
hypercode_backup_20251205_183301\hypercode\tests\test_interpreter.py:
  function: run_code (line 10)
  class: TestInterpreter (line 28)
  function: test_if_statement_then (line 30)
  function: test_if_statement_else (line 42)
  function: test_function_call (line 54)
  function: test_function_with_parameters (line 64)
  function: test_function_with_return (line 74)
  function: test_recursive_function_call (line 85)
  function: test_scoping (line 99)
hypercode_backup_20251205_183301\hypercode\tests\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestKnowledgeBaseSearch (line 12)
  function: sample_documents (line 16)
  function: knowledge_base (line 40)
  function: test_basic_search (line 48)
  function: test_search_with_exact_match (line 54)
  function: test_search_case_insensitive (line 59)
  function: test_search_empty_query (line 65)
  function: test_search_no_matches (line 71)
  function: test_search_ranking (line 77)
  function: test_query_normalization (line 90)
  function: test_multi_word_query (line 98)
  function: test_tag_based_search (line 103)
  class: TestEdgeCases (line 112)
  function: knowledge_base (line 116)
  function: test_very_short_query (line 121)
  function: test_very_long_query (line 126)
  function: test_special_characters_in_query (line 136)
  function: test_unicode_in_query (line 141)
  function: test_sql_injection_attempt (line 146)
  function: test_repeated_queries (line 151)
  class: TestPerformance (line 159)
  function: large_knowledge_base (line 163)
  function: test_search_response_time (line 179)
  function: test_concurrent_searches (line 189)
  function: test_memory_usage (line 207)
  class: TestIntegrationWithPerplexity (line 213)
  function: mock_perplexity_client (line 217)
  function: mock_knowledge_base (line 229)
  function: test_enhanced_query_with_context (line 243)
  function: test_fallback_to_perplexity_api (line 259)
  function: test_context_ranking_and_selection (line 273)
  class: TestDocumentManagement (line 288)
  function: knowledge_base (line 292)
  function: test_add_document (line 300)
  function: test_update_document (line 310)
  function: test_remove_document (line 315)
hypercode_backup_20251205_183301\hypercode\tests\test_knowledge_base_comprehensive.py:
  module: test_knowledge_base_comprehensive (line 0)
  class: TestKnowledgeBaseUnit (line 20)
  function: temp_kb (line 24)
  function: sample_docs (line 36)
  function: test_init_empty_kb (line 59)
  function: test_add_single_document (line 65)
  function: test_add_multiple_documents (line 74)
  function: test_save_and_load (line 84)
  function: test_search_exact_match (line 102)
  function: test_search_partial_match (line 113)
  function: test_search_tag_matching (line 124)
  function: test_search_case_insensitive (line 135)
  function: test_empty_search (line 147)
  function: test_nonexistent_search (line 155)
  function: test_get_context_for_query (line 165)
  function: test_context_length_limit (line 176)
  function: test_document_update (line 186)
  function: test_list_documents (line 202)
  function: test_delete_document (line 213)
  class: TestKnowledgeBaseIntegration (line 229)
  function: populated_kb (line 233)
  function: test_complex_search_queries (line 277)
  function: test_search_ranking_quality (line 291)
  function: test_related_term_expansion (line 301)
  function: test_performance_with_large_dataset (line 313)
  function: test_concurrent_access_simulation (line 332)
  class: TestKnowledgeBasePerformance (line 356)
  function: large_kb (line 360)
  function: test_search_performance_large_dataset (line 382)
  function: test_save_performance_large_dataset (line 396)
  function: test_load_performance_large_dataset (line 409)
  function: test_memory_usage_large_dataset (line 423)
  class: TestKnowledgeBaseEdgeCases (line 446)
  function: edge_case_kb (line 450)
  function: test_empty_title_handling (line 494)
  function: test_special_characters_handling (line 499)
  function: test_very_long_titles (line 507)
  function: test_empty_content_handling (line 512)
  function: test_none_tags_handling (line 517)
  function: test_malformed_json_handling (line 531)
  function: test_file_permission_handling (line 544)
hypercode_backup_20251205_183301\hypercode\tests\test_lexer.py:
  function: test_lexer_basic_tokens (line 5)
  function: test_lexer_strings (line 23)
  function: test_lexer_operators (line 48)
hypercode_backup_20251205_183301\hypercode\tests\test_lexer_extended.py:
  function: test_lexer_escaped_strings (line 5)
  function: test_lexer_numbers (line 18)
  function: test_lexer_operators (line 39)
  function: test_lexer_comments (line 86)
  function: test_lexer_whitespace (line 115)
  function: test_lexer_error_handling (line 130)
  function: test_lexer_hex_numbers (line 139)
  function: test_lexer_binary_numbers (line 157)
  function: test_lexer_scientific_notation (line 169)
  function: test_lexer_string_escapes (line 180)
  function: test_lexer_keywords (line 197)
  function: test_lexer_position_tracking (line 223)
  function: test_lexer_error_recovery (line 243)
  function: test_lexer_error_messages (line 252)
hypercode_backup_20251205_183301\hypercode\tests\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode_backup_20251205_183301\hypercode\tests\test_parser.py:
  function: test_parse_literal (line 12)
  function: test_parse_variable_declaration (line 24)
  function: test_parse_binary_expression (line 37)
hypercode_backup_20251205_183301\hypercode\tests\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode_backup_20251205_183301\hypercode\tests\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 185)
hypercode_backup_20251205_183301\hypercode\tests\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode_backup_20251205_183301\hypercode\tests\test_sensory_profiles.py:
  module: test_sensory_profiles (line 0)
  function: test_visual_settings_creation (line 21)
  function: test_audio_settings_creation (line 35)
  function: test_animation_settings_creation (line 44)
  function: test_sensory_profile_creation (line 55)
  function: test_profile_serialization (line 71)
  function: test_profile_file_io (line 92)
  function: test_profile_manager_initialization (line 115)
  function: test_profile_manager_get_profile (line 129)
  function: test_profile_manager_save_custom_profile (line 142)
  function: test_profile_manager_delete_profile (line 169)
hypercode_backup_20251205_183301\hypercode\tests\tests\test_lexer_enhanced.py:
  function: test_lexer_edge_cases (line 7)
  function: test_lexer_error_handling (line 28)
  function: test_lexer_number_literals (line 43)
  function: test_lexer_string_interpolation (line 65)
  function: test_lexer_docstrings (line 79)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_direct_access.py:
  module: test_direct_access (line 0)
  function: test_direct_implementation_access (line 15)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_implementation_guide.py:
  module: test_implementation_guide (line 0)
  function: test_search_functionality (line 15)
  function: test_implementation_guide_content (line 37)
  function: test_context_queries (line 82)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_intent_blocks.py:
  module: test_intent_blocks (line 0)
  function: test_intent_block (line 13)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_knowledge_base.py:
  module: test_knowledge_base (line 0)
  class: TestHyperCodeKnowledgeBase (line 20)
  function: temp_kb (line 24)
  function: sample_documents (line 33)
  function: test_init_empty_kb (line 56)
  function: test_add_document (line 61)
  function: test_add_multiple_documents (line 82)
  function: test_save_and_load (line 92)
  function: test_search_exact_match (line 113)
  function: test_search_tag_matching (line 126)
  function: test_search_related_terms (line 139)
  function: test_search_space_data_boost (line 153)
  function: test_get_context_for_query (line 180)
  function: test_context_length_limit (line 192)
  function: test_list_documents (line 203)
  function: test_empty_search (line 216)
  function: test_search_nonexistent_term (line 221)
  function: test_document_update (line 231)
  class: TestResearchDocument (line 250)
  function: test_document_creation (line 253)
  function: test_document_optional_fields (line 273)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_lexer.py:
  module: test_lexer (line 0)
  function: test_lexer (line 12)
  function: run_tests (line 42)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_mcp_connection.py:
  function: check_port (line 26)
  function: find_running_servers (line 36)
  function: test_server_connection (line 49)
  function: test_all_servers (line 90)
  function: check_dependencies (line 139)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_mcp_integration.py:
  module: test_mcp_integration (line 0)
  function: test_mcp_server (line 15)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_perplexity.py:
  module: test_perplexity (line 0)
  function: test_perplexity_connection (line 16)
  function: test_ai_research_integration (line 66)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_real_data.py:
  module: test_real_data (line 0)
  function: test_enhanced_knowledge_base (line 16)
  function: test_real_perplexity_data_simulation (line 185)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_real_space_data.py:
  module: test_real_space_data (line 0)
  function: test_real_space_data (line 15)
hypercode_backup_20251205_183301\hypercode\tests\unit\test_search_algorithm.py:
  module: test_search_algorithm (line 0)
  class: TestSearchAlgorithm (line 20)
  function: populated_kb (line 24)
  function: test_exact_title_match_highest_score (line 80)
  function: test_space_data_boosting (line 92)
  function: test_related_term_expansion (line 105)
  function: test_tag_matching_scoring (line 126)
  function: test_content_frequency_scoring (line 136)
  function: test_partial_word_matching (line 149)
  function: test_query_word_ordering (line 167)
  function: test_case_insensitive_search (line 179)
  function: test_empty_query_returns_no_results (line 202)
  function: test_limit_parameter_respected (line 210)
  function: test_no_results_for_nonexistent_terms (line 219)
  function: test_special_characters_in_query (line 227)
  function: test_unicode_characters (line 237)
  function: test_search_performance_with_large_kb (line 256)
  function: test_search_result_consistency (line 277)
  class: TestSearchScoringDetails (line 292)
  function: scoring_kb (line 296)
  function: test_title_match_beats_content_match (line 324)
  function: test_space_data_boosting_works (line 332)
  function: test_frequency_scoring (line 340)
hypercode_backup_20251205_183301\hypercode_db.py:
  module: hypercode_db (line 0)
  class: CodeEntity (line 12)
  function: __post_init__ (line 23)
  class: HypercodeDB (line 28)
  function: __init__ (line 35)
  function: _load_database (line 46)
  function: get_entities_by_type (line 93)
  function: get_entities_in_file (line 104)
  function: print_analysis (line 116)
hypercode_backup_20251205_183301\knowledge_graph\graph_builder.py:
  module: graph_builder (line 0)
hypercode_backup_20251205_183301\knowledge_graph\sparql_query.py:
  module: sparql_query (line 0)
hypercode_backup_20251205_183301\knowledge_graph\update_agent.py:
  module: update_agent (line 0)
hypercode_backup_20251205_183301\live_research\cli.py:
  function: print_entry (line 10)
  function: search_entries (line 38)
  function: view_entry (line 59)
  function: add_entry (line 71)
  function: import_entries (line 94)
  function: export_entries (line 126)
  function: main (line 150)
hypercode_backup_20251205_183301\live_research\database.py:
  class: ResearchDatabase (line 7)
  function: __init__ (line 8)
  function: _get_connection (line 13)
  function: _create_tables (line 17)
  function: add_research_entry (line 68)
  function: get_research_entry (line 128)
  function: search_entries (line 159)
  function: import_from_json (line 220)
  function: setup_database (line 241)
hypercode_backup_20251205_183301\live_research\doc_generator.py:
  module: doc_generator (line 0)
hypercode_backup_20251205_183301\live_research\github_publisher.py:
  module: github_publisher (line 0)
hypercode_backup_20251205_183301\live_research\import_research.py:
  module: import_research (line 0)
  function: import_research_data (line 18)
hypercode_backup_20251205_183301\live_research\paper_indexer.py:
  module: paper_indexer (line 0)
hypercode_backup_20251205_183301\live_research\research_crawler.py:
  module: research_crawler (line 0)
hypercode_backup_20251205_183301\live_research\synthesis_engine.py:
  module: synthesis_engine (line 0)
hypercode_backup_20251205_183301\live_research\web\app.py:
  module: app (line 0)
  function: get_db_connection (line 35)
  function: index (line 43)
  function: view_entry (line 79)
  function: search (line 121)
  function: list_tags (line 194)
  function: api_entries (line 219)
  function: page_not_found (line 246)
  function: server_error (line 252)
  function: format_date_filter (line 258)
hypercode_backup_20251205_183301\live_research\web\run.py:
  module: run (line 0)
hypercode_backup_20251205_183301\mcp\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\mcp\servers\__init__.py:
  module: __init__ (line 0)
hypercode_backup_20251205_183301\mcp\servers\aws_cli.py:
  function: main (line 4)
hypercode_backup_20251205_183301\mcp\servers\aws_resource_manager.py:
  function: main (line 4)
hypercode_backup_20251205_183301\mcp\servers\code_analysis.py:
  function: main (line 4)
hypercode_backup_20251205_183301\mcp\servers\dataset_downloader.py:
  function: main (line 4)
hypercode_backup_20251205_183301\mcp\servers\file_system.py:
  function: main (line 4)
hypercode_backup_20251205_183301\mcp\servers\human_input.py:
  function: main (line 4)
hypercode_backup_20251205_183301\mcp\servers\hypercode_syntax.py:
  module: hypercode_syntax (line 0)
  class: HyperCodeSyntaxServer (line 28)
  function: __init__ (line 31)
  function: handle_request (line 35)
  function: _initialize (line 56)
  function: _document_changed (line 79)
  function: _text_hover (line 98)
  function: _completion (line 121)
  function: _parse_document (line 150)
  function: _validate_neurodiversity (line 179)
  function: _generate_diagnostics (line 216)
  function: _get_annotation_hover_info (line 266)
  function: main (line 294)
hypercode_backup_20251205_183301\mcp\servers\path_service.py:
  function: main (line 4)
hypercode_backup_20251205_183301\mcp\servers\user_profile_manager.py:
  function: main (line 4)
hypercode_backup_20251205_183301\mcp\servers\valkey_service.py:
  function: check_redis_connection (line 37)
  function: health_check (line 50)
  function: set_key (line 57)
  function: get_key (line 69)
  function: hset_key (line 83)
  function: hget_key (line 94)
  function: hgetall_hash (line 107)
  function: main (line 124)
hypercode_backup_20251205_183301\mcp\servers\web_search.py:
  function: main (line 4)
hypercode_backup_20251205_183301\mcp\setup.py:
  module: setup (line 0)
  function: install_dependencies (line 15)
  function: verify_setup (line 27)
  function: show_next_steps (line 45)
  function: main (line 62)
hypercode_backup_20251205_183301\mcp\start_servers.py:
  module: start_servers (line 0)
  function: start_server (line 33)
  function: list_servers (line 55)
  function: main (line 61)
hypercode_backup_20251205_183301\mcp\test_mcp.py:
  module: test_mcp (line 0)
  function: test_server_imports (line 14)
  function: main (line 48)
hypercode_backup_20251205_183301\scripts\build-hyper-database.py:
  module: build-hyper-database (line 0)
  class: HyperDatabaseBuilder (line 21)
  function: __init__ (line 24)
  function: scan_python_file (line 32)
  function: scan_javascript_file (line 78)
  function: should_skip_directory (line 107)
  function: build (line 127)
  function: generate_markdown_report (line 161)
  function: generate_json_report (line 250)
  function: main (line 265)
hypercode_backup_20251205_183301\scripts\build_knowledge_base.py:
  module: build_knowledge_base (line 0)
  class: KnowledgeBaseBuilder (line 35)
  function: __init__ (line 38)
  function: should_skip (line 79)
  function: get_file_type (line 162)
  function: process_file (line 244)
  function: build_index (line 287)
  function: main (line 376)
hypercode_backup_20251205_183301\scripts\document_processor.py:
  module: document_processor (line 0)
  class: DocumentProcessor (line 15)
  function: get_file_hash (line 19)
  function: extract_metadata (line 29)
  function: extract_pdf_content (line 43)
  function: extract_markdown_content (line 74)
  function: extract_docx_content (line 99)
  function: extract_csv_content (line 133)
  function: extract_text_content (line 154)
  function: process_document (line 167)
hypercode_backup_20251205_183301\scripts\generate_directory_readmes.py:
  module: generate_directory_readmes (line 0)
  function: create_readme (line 9)
  function: main (line 20)
hypercode_backup_20251205_183301\scripts\organize_docs.py:
  module: organize_docs (line 0)
  function: setup_directories (line 131)
  function: move_files (line 138)
  function: generate_report (line 172)
  function: main (line 204)
hypercode_backup_20251205_183301\scripts\reorganize_repo.py:
  module: reorganize_repo (line 0)
  function: create_directories (line 29)
  function: move_files (line 37)
  function: update_gitignore (line 71)
  function: main (line 83)
hypercode_backup_20251205_183301\scripts\run_lexer.py:
  module: run_lexer (line 0)
  class: TestLexer (line 18)
  function: setUp (line 21)
  function: test_empty_source (line 25)
  function: test_basic_tokens (line 31)
  function: test_string_literals (line 44)
  function: test_numbers (line 58)
  function: test_arithmetic_expressions (line 83)
  function: test_comments (line 107)
  function: test_error_handling (line 121)
  function: test_error_recovery (line 153)
  function: _assert_token_types (line 179)
  function: test_lexer_error_class (line 201)
hypercode_backup_20251205_183301\scripts\run_tests.py:
  module: run_tests (line 0)
  function: run_tests (line 16)
  function: main (line 49)
hypercode_backup_20251205_183301\scripts\style_guide_collector.py:
  module: style_guide_collector (line 0)
  class: StyleGuideCollector (line 17)
  function: __init__ (line 20)
  function: _load_feedback (line 31)
  function: _save_feedback (line 50)
  function: add_feedback (line 59)
  function: _update_analysis (line 101)
  function: analyze_feedback (line 150)
  function: _get_top_items (line 176)
  function: _calculate_consensus (line 201)
  function: _generate_recommendations (line 230)
  function: import_github_issues (line 288)
  function: generate_report (line 309)
  function: interactive_feedback (line 370)
  function: main (line 469)
hypercode_backup_20251205_183301\scripts\sync-space-to-main.py:
  module: sync-space-to-main (line 0)
  function: log_error (line 25)
  class: Colors (line 37)
  function: log_info (line 46)
  function: log_success (line 51)
  function: log_warning (line 56)
  function: deep_merge (line 61)
  function: load_config (line 72)
  function: should_skip_file (line 112)
  function: get_all_files (line 135)
  function: copy_file (line 145)
  function: remove_file (line 157)
  function: sync_folder (line 168)
  function: delete_orphans (line 212)
  function: sync_all_mappings (line 229)
  function: write_log (line 281)
  function: print_summary (line 303)
  function: main (line 327)
hypercode_backup_20251205_183301\scripts\test_mcp_connection.py:
  function: check_port (line 25)
  function: find_running_servers (line 34)
  function: test_server_connection (line 46)
  function: test_all_servers (line 82)
  function: check_dependencies (line 124)
hypercode_backup_20251205_183301\scripts\test_perplexity_api.py:
  module: test_perplexity_api (line 0)
  function: main (line 17)
hypercode_backup_20251205_183301\scripts\update_doc_links.py:
  module: update_doc_links (line 0)
  function: update_links_in_file (line 27)
  function: replace_link (line 39)
  function: main (line 63)
hypercode_backup_20251205_183301\scripts\web_interface.py:
  function: load_index (line 18)
  function: search_documents (line 24)
  function: index (line 58)
  function: search (line 63)
  function: get_document (line 71)
  function: serve_static (line 80)
  function: create_template_if_not_exists (line 84)
hypercode_backup_20251205_183301\test_database.py:
  module: test_database (line 0)
  function: test_database_loading (line 10)
```

## 📚 Documentation Coverage
| File | Entities | Documented | Coverage |
|------|----------|------------|----------|
| `hypercode\core\src\core\hypercode-\mcp\servers\aws_cli.py` | 1 | 0 | 0.0% |
| `hypercode\core\src\core\hypercode-\mcp\servers\aws_resource_manager.py` | 1 | 0 | 0.0% |
| `hypercode\core\src\core\hypercode-\mcp\servers\code_analysis.py` | 1 | 0 | 0.0% |
| `hypercode\core\src\core\hypercode-\mcp\servers\dataset_downloader.py` | 1 | 0 | 0.0% |
| `hypercode\core\src\core\hypercode-\mcp\servers\file_system.py` | 1 | 0 | 0.0% |
| `hypercode\core\src\core\hypercode-\mcp\servers\human_input.py` | 1 | 0 | 0.0% |
| `hypercode\core\src\core\hypercode-\mcp\servers\path_service.py` | 1 | 0 | 0.0% |
| `hypercode\core\src\core\hypercode-\mcp\servers\user_profile_manager.py` | 1 | 0 | 0.0% |
| `hypercode\core\src\core\hypercode-\mcp\servers\web_search.py` | 1 | 0 | 0.0% |
| `hypercode\core\src\core\hypercode-\src\hypercode\__main__.py` | 1 | 0 | 0.0% |

*Showing 10 of 1021 files with lowest coverage*

## 🧩 All Entities
### 📄 data\cli_main.py

#### Function: `cli`
> 🚀 HyperCode - Programming Language for Neurodivergent Brains & AI Systems
*Line 25*  

#### Function: `database`
> Database management commands.
*Line 42*  

#### Function: `init`
> Initialize database schema.
*Line 48*  

#### Function: `reset`
> Reset database (DESTRUCTIVE - DELETE ALL DATA).
*Line 61*  

#### Function: `status`
> Check database connection and status.
*Line 82*  

#### Function: `research`
> Auto-research mode and knowledge graph management.
*Line 115*  

#### Function: `auto_research`
> Start auto-research mode.
*Line 126*  

#### Function: `run`
*Line 147*  

#### Function: `process_papers`
> Process papers through the research pipeline.
*Line 172*  

#### Function: `process_all`
*Line 199*  

#### Function: `agents`
> List registered research agents.
*Line 227*  

#### Function: `knowledge`
> Knowledge graph management and query.
*Line 260*  

#### Function: `nodes`
> List knowledge graph nodes.
*Line 268*  

#### Function: `relationships`
> List knowledge graph relationships.
*Line 308*  

#### Function: `graph`
> Explore knowledge graph around a node.
*Line 350*  

#### Function: `system`
> System and configuration commands.
*Line 404*  

#### Function: `version`
> Show HyperCode version and system info.
*Line 410*  

#### Function: `health`
> System health check.
*Line 429*  

### 📄 data\db.py

#### Class: `DatabaseConfig`
> Centralized database configuration.
*Line 21*  

#### Function: `create_db_engine`
> Create SQLAlchemy engine with appropriate configuration.
*Line 59*  

#### Function: `set_sqlite_pragma`
*Line 83*  

#### Function: `init_db`
> Initialize database schema.
*Line 108*  

#### Function: `get_db`
> Get a database session.
*Line 124*  

#### Function: `get_db_context`
> Context manager for database sessions.
*Line 130*  

#### Function: `close_db`
> Close database connections.
*Line 151*  

#### Function: `check_db_connection`
> Test database connection.
*Line 161*  

#### Function: `get_db_stats`
> Get database statistics.
*Line 173*  

#### Function: `db_cli`
> Database management commands.
*Line 202*  

#### Function: `init`
> Initialize database.
*Line 208*  

#### Function: `reset`
> Reset database (DANGEROUS).
*Line 216*  

#### Function: `stats`
> Show database statistics.
*Line 225*  

#### Function: `migrate`
> Run Alembic migrations.
*Line 235*  

### 📄 data\models.py

#### Class: `ResearchPaper`
> Core research document storage.
*Line 35*  

#### Class: `ResearchAgent`
> Autonomous research agents for multi-agent system.
*Line 67*  

#### Class: `ResearchTask`
> Task queue for autonomous research operations.
*Line 99*  

#### Class: `KnowledgeNode`
> Knowledge graph nodes representing entities and concepts.
*Line 141*  

#### Class: `KnowledgeRelationship`
> Knowledge graph relationships between nodes.
*Line 187*  

#### Class: `ConflictRecord`
> Track conflicts detected between new research and existing knowledge.
*Line 217*  

#### Class: `ResearchMetrics`
> Track metrics about the research system and auto-research mode.
*Line 243*  

### 📄 data\research_agent.py

#### Class: `AgentType`
> Types of specialized research agents.
*Line 31*  

#### Class: `TaskStatus`
> Research task status.
*Line 45*  

#### Class: `TaskResult`
> Result from a research task execution.
*Line 54*  

#### Class: `BaseResearchAgent`
> Abstract base class for research agents.
*Line 67*  

#### Function: `__init__`
*Line 73*  

#### Function: `execute`
> Execute the agent's specialized task.
*Line 81*  

#### Function: `log_execution`
> Log execution results to database.
*Line 85*  

#### Class: `DocumentRetrievalAgent`
> Agent 1: Document Retrieval
*Line 103*  

#### Function: `execute`
> Retrieve documents from configured sources.
*Line 110*  

#### Class: `FilteringAgent`
> Agent 2: Filtering
*Line 159*  

#### Function: `execute`
> Filter and segment document content.
*Line 166*  

#### Class: `SummarizationAgent`
> Agent 3: Summarization
*Line 203*  

#### Function: `execute`
> Generate summary of document content.
*Line 210*  

#### Class: `EntityExtractionAgent`
> Agent 4: Entity Extraction
*Line 246*  

#### Function: `execute`
> Extract entities from text.
*Line 254*  

#### Class: `RelationshipExtractionAgent`
> Agent 5: Relationship Extraction
*Line 292*  

#### Function: `execute`
> Extract relationships between entities.
*Line 299*  

#### Class: `SchemaAlignmentAgent`
> Agent 6: Schema Alignment
*Line 336*  

#### Function: `execute`
> Align entities and relationships to KG schema.
*Line 344*  

#### Class: `ConflictResolutionAgent`
> Agent 7: Conflict Resolution
*Line 388*  

#### Function: `execute`
> Detect and resolve conflicts in knowledge.
*Line 396*  

#### Class: `EvaluationAgent`
> Agent 8: Evaluation
*Line 438*  

#### Function: `execute`
> Evaluate quality of extracted knowledge.
*Line 449*  

#### Class: `ControllerAgent`
> Agent 9: Central Controller
*Line 491*  

#### Function: `__init__`
*Line 499*  

#### Function: `register_agent`
> Register a specialized agent.
*Line 503*  

#### Function: `execute`
> Orchestrate the research pipeline.
*Line 507*  

#### Class: `AutoResearchManager`
> Manages the auto-research mode system.
*Line 560*  

#### Function: `__init__`
*Line 566*  

#### Function: `initialize_agents`
> Initialize all specialized agents.
*Line 571*  

#### Function: `process_research_task`
> Process a research task through the auto-research pipeline.
*Line 590*  

#### Function: `auto_research_mode`
> Run continuous auto-research mode.
*Line 610*  

### 📄 hypercode-research\scripts\ai-researcher.py

#### Module: `ai-researcher`
> HyperCode AI Research Agent
*Line 0*  

#### Class: `ResearchAgent`
> AI agent for automated research discovery and summarization.
*Line 52*  

#### Function: `__init__`
*Line 55*  

#### Function: `search_topic`
> Search for research on a specific topic.
*Line 60*  

#### Function: `categorize_result`
> Determine which research category a result belongs to.
*Line 85*  

#### Function: `generate_draft_entry`
> Generate a draft research entry from search result.
*Line 105*  

#### Function: `save_draft`
> Save draft research entry to file.
*Line 170*  

#### Function: `run_daily_scan`
> Execute daily research scan across all topics.
*Line 188*  

#### Function: `main`
> Main entry point for research agent.
*Line 244*  

### 📄 hypercode-research\scripts\knowledge-graph.py

#### Module: `knowledge-graph`
> HyperCode Knowledge Graph Generator
*Line 0*  

#### Class: `KnowledgeGraphGenerator`
> Generate visual knowledge graphs from research entries.
*Line 24*  

#### Function: `__init__`
*Line 27*  

#### Function: `extract_frontmatter`
> Extract YAML frontmatter from markdown file.
*Line 39*  

#### Function: `scan_research_entries`
> Scan all research entries and build graph data.
*Line 49*  

#### Function: `generate_json`
> Generate JSON representation for interactive visualization.
*Line 102*  

#### Function: `generate_mermaid`
> Generate Mermaid diagram syntax.
*Line 120*  

#### Function: `generate_ascii_graph`
> Generate simple ASCII representation of the graph.
*Line 159*  

#### Function: `generate_graphviz_dot`
> Generate GraphViz DOT format (requires graphviz to render).
*Line 191*  

#### Function: `main`
> Main entry point for knowledge graph generator.
*Line 224*  

### 📄 hypercode-research\scripts\link-validator.py

#### Module: `link-validator`
> HyperCode Link Validator
*Line 0*  

#### Class: `LinkValidator`
> Validate all links in markdown files.
*Line 20*  

#### Function: `__init__`
*Line 23*  

#### Function: `extract_links`
> Extract all URLs from markdown content.
*Line 32*  

#### Function: `scan_files`
> Scan all markdown files for links.
*Line 44*  

#### Function: `check_url`
> Check if a URL is accessible.
*Line 56*  

#### Function: `validate_links`
> Validate all links concurrently.
*Line 66*  

#### Function: `report`
> Generate validation report.
*Line 89*  

#### Function: `main`
> Main entry point.
*Line 116*  

### 📄 hypercode\accessibility\adhd_optimizer.py

#### Module: `adhd_optimizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\accessibility\autism_preset.py

#### Module: `autism_preset`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\accessibility\dyslexia_formatter.py

#### Module: `dyslexia_formatter`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\accessibility\sensory_customizer.py

#### Module: `sensory_customizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\accessibility\wcag_auditor.py

#### Module: `wcag_auditor`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\archive\new-files-to-check\backend\research\__init__.py

#### Module: `__init__`
> Initialization for the research module.
*Line 0*  

### 📄 hypercode\archive\new-files-to-check\backend\research\db.py

#### Module: `db`
> Database configuration for the HyperCode research module.
*Line 0*  

#### Function: `_get_database_url`
> Return the database URL to connect to.
*Line 35*  

### 📄 hypercode\archive\new-files-to-check\backend\research\models.py

#### Module: `models`
> ORM models for the HyperCode research database.
*Line 0*  

#### Class: `Study`
> Top‑level research study.
*Line 32*  

#### Function: `__repr__`
*Line 52*  

#### Class: `Source`
> External or internal resource used in a study.
*Line 56*  

#### Function: `__repr__`
*Line 81*  

#### Class: `LanguageVersion`
> Version of the HyperCode language.
*Line 85*  

#### Function: `__repr__`
*Line 102*  

#### Class: `Task`
> A coding task or challenge used in experiments.
*Line 106*  

#### Function: `__repr__`
*Line 124*  

#### Class: `Participant`
> An anonymised participant in the study.
*Line 128*  

#### Function: `__repr__`
*Line 144*  

#### Class: `Session`
> A single coding session of a participant performing a task.
*Line 148*  

#### Function: `__repr__`
*Line 169*  

#### Class: `Event`
> Low‑level interaction within a session.
*Line 176*  

#### Function: `__repr__`
*Line 193*  

#### Class: `Feedback`
> Qualitative and quantitative feedback for a session.
*Line 197*  

#### Function: `__repr__`
*Line 219*  

### 📄 hypercode\archive\new-files-to-check\backend\research\scripts\import_sources_from_folder.py

#### Module: `import_sources_from_folder`
> Import research sources from a folder into the database.
*Line 0*  

#### Function: `infer_kind`
*Line 25*  

#### Function: `main`
*Line 36*  

### 📄 hypercode\archive\new-files-to-check\backend\research\scripts\seed_basic_data.py

#### Module: `seed_basic_data`
> Seed the research database with initial data.
*Line 0*  

#### Function: `main`
*Line 25*  

### 📄 hypercode\code_insights.py

#### Function: `analyze_code_patterns`
> Analyze function and class naming patterns.
*Line 8*  

#### Function: `find_undocumented_code`
> Find complex but undocumented code.
*Line 29*  

#### Function: `analyze_test_coverage`
> Analyze test coverage patterns.
*Line 45*  

#### Function: `summarize_manifests`
> Summarize HC Manifest adoption and safety posture.
*Line 92*  

### 📄 hypercode\code_quality_report.py

#### Module: `code_quality_report`
> Code Quality Analysis for Hypercode Project
*Line 0*  

#### Function: `get_undocumented_classes_priority`
> Get undocumented classes sorted by importance (more methods = higher priority).
*Line 15*  

#### Function: `get_least_tested_files`
> Get files with most code but least test coverage.
*Line 33*  

#### Function: `find_getter_methods`
> Find get_ methods that could be converted to properties.
*Line 69*  

#### Function: `generate_code_quality_report`
> Generate a comprehensive code quality report.
*Line 103*  

### 📄 hypercode\core\benchmarks\__init__.py

#### Function: `benchmark_lexer`
> Benchmark the lexer with the given source code.
*Line 12*  

#### Function: `print_benchmark_results`
> Print benchmark results in a readable format.
*Line 36*  

### 📄 hypercode\core\benchmarks\benchmarks_lexer.py

#### Function: `benchmark_lexer`
> Benchmark the lexer with the given source code.
*Line 6*  

#### Function: `print_benchmark_results`
> Print benchmark results in a readable format.
*Line 30*  

### 📄 hypercode\core\src\ai_gateway\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\core\src\ai_gateway\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\ai_gateway\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\ai_gateway\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\ai_gateway\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\ai_gateway\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\core\src\ai_gateway\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\core\src\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\core\src\build.py

#### Module: `build`
> Build script for the HyperCode language.
*Line 0*  

#### Function: `build`
> Builds a HyperCode source file to the target language.
*Line 34*  

### 📄 hypercode\core\src\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\core\__init__.py

#### Module: `__init__`
> HyperCode Core Module
*Line 0*  

### 📄 hypercode\core\src\core\ast.py

#### Module: `ast`
> Abstract Syntax Tree (AST) for HyperCode.
*Line 0*  

#### Class: `Node`
> Base class for all AST nodes.
*Line 11*  

#### Class: `Program`
> Represents a complete HyperCode program.
*Line 18*  

#### Class: `Function`
> Represents a function definition.
*Line 25*  

#### Class: `VariableDeclaration`
> Represents a variable declaration.
*Line 34*  

#### Class: `Literal`
> Represents a literal value (number, string, boolean, etc.).
*Line 42*  

#### Class: `BinaryOp`
> Represents a binary operation (e.g., 1 + 2).
*Line 50*  

#### Class: `UnaryOp`
> Represents a unary operation (e.g., -1 or !true).
*Line 59*  

#### Class: `Variable`
> Represents a variable reference.
*Line 67*  

#### Class: `Call`
> Represents a function call.
*Line 74*  

#### Class: `Return`
> Represents a return statement.
*Line 82*  

#### Class: `Block`
> Represents a block of statements.
*Line 89*  

#### Class: `If`
> Represents an if statement.
*Line 96*  

#### Class: `While`
> Represents a while loop.
*Line 105*  

#### Class: `For`
> Represents a for loop.
*Line 113*  

#### Class: `Assign`
> Represents a variable assignment.
*Line 123*  

#### Class: `Logical`
> Represents a logical operation (and/or).
*Line 131*  

### 📄 hypercode\core\src\core\ast_nodes.py

#### Module: `ast_nodes`
> Abstract Syntax Tree (AST) nodes for the HyperCode language.
*Line 0*  

#### Class: `Node`
> Base class for all AST nodes.
*Line 24*  

#### Class: `Expression`
> Base class for all expression nodes.
*Line 31*  

#### Class: `Statement`
> Base class for all statement nodes.
*Line 38*  

#### Class: `Program`
> Represents the entire program as a list of statements.
*Line 45*  

#### Class: `Identifier`
> Represents an identifier (e.g., a variable name).
*Line 52*  

#### Class: `Literal`
> Represents a literal value (e.g., number, string).
*Line 59*  

#### Class: `VariableDeclaration`
> Represents a variable declaration (let or const).
*Line 66*  

#### Class: `BinaryOperation`
> Represents a binary operation (e.g., a + b).
*Line 75*  

### 📄 hypercode\core\src\core\hypercode-\DuelCode\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode\core\src\core\hypercode-\DuelCode\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode\core\src\core\hypercode-\DuelCode\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode\core\src\core\hypercode-\DuelCode\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode\core\src\core\hypercode-\DuelCode\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode\core\src\core\hypercode-\DuelCode\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode\core\src\core\hypercode-\accessibility\adhd_optimizer.py

#### Module: `adhd_optimizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\accessibility\autism_preset.py

#### Module: `autism_preset`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\accessibility\dyslexia_formatter.py

#### Module: `dyslexia_formatter`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\accessibility\sensory_customizer.py

#### Module: `sensory_customizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\accessibility\wcag_auditor.py

#### Module: `wcag_auditor`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\ai_gateway\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\ai_gateway\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\core\hypercode-\ai_gateway\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\core\hypercode-\ai_gateway\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\core\hypercode-\ai_gateway\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\core\hypercode-\ai_gateway\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\ai_gateway\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\code_analyzer_ai.py

#### Module: `code_analyzer_ai`
> Perplexity AI Code Analyzer for HyperCode
*Line 0*  

#### Class: `CodeAnalyzerAI`
> AI-powered code analyzer for HyperCode
*Line 20*  

#### Function: `__init__`
*Line 23*  

#### Function: `analyze_file`
> Analyze a Python file with AI assistance
*Line 26*  

#### Function: `_analyze_complexity`
> Analyze code complexity indicators
*Line 73*  

#### Function: `_check_docstrings`
> Check for docstring coverage
*Line 114*  

#### Function: `_get_ai_code_analysis`
> Get AI analysis of code from Perplexity
*Line 156*  

#### Function: `analyze_project`
> Analyze entire project
*Line 184*  

#### Function: `_get_project_ai_insights`
> Get AI insights for the entire project
*Line 231*  

#### Function: `save_analysis`
> Save analysis to file
*Line 263*  

#### Function: `print_summary`
> Print analysis summary
*Line 271*  

#### Function: `main`
> Main function
*Line 289*  

### 📄 hypercode\core\src\core\hypercode-\debug_search.py

#### Module: `debug_search`
> Debug search results
*Line 0*  

#### Function: `debug_search`
> Debug why space data isn't being found
*Line 15*  

### 📄 hypercode\core\src\core\hypercode-\demo_ai_research.py

#### Module: `demo_ai_research`
> HyperCode AI Research + Perplexity Integration Demo
*Line 0*  

#### Function: `demo_ai_research_queries`
> Demonstrate AI Research integration with Perplexity
*Line 16*  

#### Function: `test_document_specific_queries`
> Test queries specific to the HyperCode AI Research document
*Line 90*  

### 📄 hypercode\core\src\core\hypercode-\demo_enhanced_client.py

#### Module: `demo_enhanced_client`
> Demo: Enhanced Perplexity Client with Knowledge Base
*Line 0*  

#### Function: `demo_knowledge_base_integration`
> Demonstrate the knowledge base integration
*Line 16*  

#### Function: `demonstrate_memory_persistence`
> Demonstrate that the knowledge base persists between sessions
*Line 131*  

### 📄 hypercode\core\src\core\hypercode-\final_integration_test.py

#### Module: `final_integration_test`
> Final Test: Complete Perplexity Space Integration
*Line 0*  

#### Function: `final_integration_test`
> Complete test of the Perplexity Space integration
*Line 15*  

### 📄 hypercode\core\src\core\hypercode-\health_scanner_ai.py

#### Module: `health_scanner_ai`
> HyperCode Health Scanner with Perplexity AI Integration
*Line 0*  

#### Class: `HealthScannerAI`
> AI-powered health scanner for HyperCode project
*Line 19*  

#### Function: `__init__`
*Line 22*  

#### Function: `analyze_project_structure`
> Analyze project structure and identify health issues
*Line 26*  

#### Function: `analyze_dependencies`
> Analyze dependency management
*Line 69*  

#### Function: `analyze_security`
> Analyze security configuration
*Line 111*  

#### Function: `get_ai_recommendations`
> Get AI-powered recommendations based on health scan
*Line 144*  

#### Function: `run_full_scan`
> Run complete health scan with AI analysis
*Line 171*  

#### Function: `save_report`
> Save health scan report to file
*Line 222*  

#### Function: `print_summary`
> Print a summary of the health scan
*Line 228*  

#### Function: `main`
> Main function to run the health scanner
*Line 248*  

### 📄 hypercode\core\src\core\hypercode-\import-helper.py

#### Module: `import-helper`
> HyperCode Perplexity Space Import Helper
*Line 0*  

#### Class: `SpaceImportHelper`
> Helper class for managing Perplexity Space imports
*Line 13*  

#### Function: `__init__`
*Line 16*  

#### Function: `validate_document`
> Validate a document structure
*Line 21*  

#### Function: `load_template`
> Load documents from JSON template file
*Line 63*  

#### Function: `validate_all`
> Validate all loaded documents
*Line 83*  

#### Function: `generate_report`
> Generate a validation report
*Line 95*  

#### Function: `create_import_script`
> Generate a Python script to import the data
*Line 141*  

#### Function: `create_template_instructions`
> Generate detailed instructions for filling the template
*Line 193*  

#### Function: `main`
> CLI interface for the import helper
*Line 264*  

### 📄 hypercode\core\src\core\hypercode-\import_all_space_data.py

#### Module: `import_all_space_data`
> Complete Import of HyperCode Space Data
*Line 0*  

#### Function: `format_content`
> Recursively format nested data into readable text
*Line 16*  

#### Function: `import_all_hypercode_data`
> Import all sections of your HyperCode Space data
*Line 41*  

### 📄 hypercode\core\src\core\hypercode-\import_hypercode_data.py

#### Module: `import_hypercode_data`
> Import HyperCode Space Data
*Line 0*  

#### Function: `import_hypercode_space_data`
> Import your actual HyperCode Space data
*Line 16*  

### 📄 hypercode\core\src\core\hypercode-\import_perplexity_space.py

#### Module: `import_perplexity_space`
> Perplexity Space Data Importer
*Line 0*  

#### Function: `create_manual_import_script`
> Create a script for manual data entry from Perplexity Space
*Line 17*  

#### Function: `create_json_import_template`
> Create a JSON template for importing data
*Line 86*  

#### Function: `import_from_json`
> Import data from JSON file
*Line 115*  

#### Function: `test_imported_data`
> Test the imported data with context-aware queries
*Line 153*  

#### Function: `show_import_menu`
> Show the import menu
*Line 188*  

### 📄 hypercode\core\src\core\hypercode-\knowledge_graph\graph_builder.py

#### Module: `graph_builder`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\knowledge_graph\sparql_query.py

#### Module: `sparql_query`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\knowledge_graph\update_agent.py

#### Module: `update_agent`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\live_research\doc_generator.py

#### Module: `doc_generator`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\live_research\github_publisher.py

#### Module: `github_publisher`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\live_research\paper_indexer.py

#### Module: `paper_indexer`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\live_research\research_crawler.py

#### Module: `research_crawler`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\live_research\synthesis_engine.py

#### Module: `synthesis_engine`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\mcp\__init__.py

#### Module: `__init__`
> HyperCode MCP (Model Context Protocol) Server Package
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\__init__.py

#### Module: `__init__`
> MCP Servers Package
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\aws_cli.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\aws_resource_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\code_analysis.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\dataset_downloader.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\file_system.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\human_input.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\hypercode_syntax.py

#### Module: `hypercode_syntax`
> HyperCode Syntax MCP Server
*Line 0*  

#### Class: `HyperCodeSyntaxServer`
> 🎨 MCP Server for HyperCode Visual Syntax Integration
*Line 28*  

#### Function: `__init__`
*Line 31*  

#### Function: `handle_request`
> Handle MCP requests from IDE
*Line 35*  

#### Function: `_initialize`
> Initialize the MCP server
*Line 56*  

#### Function: `_document_changed`
> Handle document changes for real-time parsing
*Line 79*  

#### Function: `_text_hover`
> Provide hover information for semantic annotations
*Line 98*  

#### Function: `_completion`
> Provide completion for semantic annotations
*Line 121*  

#### Function: `_parse_document`
> Parse entire document and return semantic structure
*Line 150*  

#### Function: `_validate_neurodiversity`
> Validate neurodiversity compliance and provide suggestions
*Line 179*  

#### Function: `_generate_diagnostics`
> Generate IDE diagnostics from parsed functions
*Line 216*  

#### Function: `_get_annotation_hover_info`
> Generate hover information for semantic annotations
*Line 266*  

#### Function: `main`
> Main MCP server loop
*Line 294*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\path_service.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\user_profile_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\valkey_service.py

#### Function: `check_redis_connection`
*Line 40*  

#### Function: `health_check`
> Health check endpoint to verify that the service is running.
*Line 59*  

#### Function: `set_key`
> Set a value for a given key. The value should be a JSON object.
*Line 67*  

#### Function: `get_key`
> Get the value for a given key.
*Line 80*  

#### Function: `hset_key`
> Set a field (key) in a hash (name). The value should be a JSON object.
*Line 95*  

#### Function: `hget_key`
> Get a field (key) from a hash (name).
*Line 107*  

#### Function: `hgetall_hash`
> Get all fields and values for a given hash name.
*Line 126*  

#### Function: `main`
> Main function to run the Valkey Service MCP Server.
*Line 144*  

### 📄 hypercode\core\src\core\hypercode-\mcp\servers\web_search.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\core\src\core\hypercode-\mcp\setup.py

#### Module: `setup`
> MCP Setup Script
*Line 0*  

#### Function: `install_dependencies`
> Install required dependencies
*Line 16*  

#### Function: `verify_setup`
> Verify that MCP is properly set up
*Line 31*  

#### Function: `show_next_steps`
> Show next steps for using MCP
*Line 54*  

#### Function: `main`
*Line 72*  

### 📄 hypercode\core\src\core\hypercode-\mcp\start_servers.py

#### Module: `start_servers`
> MCP Servers Startup Script
*Line 0*  

#### Function: `start_server`
> Start a specific MCP server
*Line 34*  

#### Function: `list_servers`
> List all available servers
*Line 59*  

#### Function: `main`
*Line 66*  

### 📄 hypercode\core\src\core\hypercode-\mcp\test_mcp.py

#### Module: `test_mcp`
> MCP Servers Test Script
*Line 0*  

#### Function: `test_server_imports`
> Test that all servers can be imported
*Line 15*  

#### Function: `main`
*Line 47*  

### 📄 hypercode\core\src\core\hypercode-\perplexity_space_collector.py

#### Module: `perplexity_space_collector`
> Perplexity Space Data Collector
*Line 0*  

#### Function: `quick_copy_paste_collector`
> Quick collector for copy-paste workflow
*Line 18*  

#### Function: `create_structured_template`
> Create a structured JSON template for bulk import
*Line 117*  

#### Function: `show_bro_hacks`
> Show BROski's pro tips
*Line 167*  

#### Function: `main_menu`
> Main menu for the collector
*Line 207*  

### 📄 hypercode\core\src\core\hypercode-\perplexity_space_integration.py

#### Module: `perplexity_space_integration`
> Perplexity Space Integration Guide
*Line 0*  

#### Function: `main`
*Line 16*  

### 📄 hypercode\core\src\core\hypercode-\scripts\style_guide_collector.py

#### Module: `style_guide_collector`
> 🎨 HyperCode Style Guide Feedback Collector
*Line 0*  

#### Class: `StyleGuideCollector`
> 🎨 Collects and analyzes style guide feedback from the community
*Line 16*  

#### Function: `__init__`
*Line 19*  

#### Function: `_load_feedback`
> 📂 Load existing feedback data
*Line 30*  

#### Function: `_save_feedback`
> 💾 Save feedback data
*Line 49*  

#### Function: `add_feedback`
> 📝 Add new feedback entry
*Line 58*  

#### Function: `_update_analysis`
> 📊 Update analysis based on new feedback
*Line 100*  

#### Function: `analyze_feedback`
> 📊 Generate comprehensive analysis of all feedback
*Line 149*  

#### Function: `_get_top_items`
> 📊 Get top items from a frequency dictionary
*Line 187*  

#### Function: `_calculate_consensus`
> 📊 Calculate consensus for preference categories
*Line 210*  

#### Function: `_generate_recommendations`
> 💡 Generate style guide recommendations based on feedback
*Line 243*  

#### Function: `import_github_issues`
> 📥 Import feedback from GitHub issues
*Line 323*  

#### Function: `generate_report`
> 📊 Generate comprehensive feedback report
*Line 346*  

#### Function: `interactive_feedback`
> 🎯 Interactive feedback collection from command line
*Line 413*  

#### Function: `main`
> 🚀 Main entry point
*Line 521*  

### 📄 hypercode\core\src\core\hypercode-\scripts\test_perplexity_api.py

#### Module: `test_perplexity_api`
> Test script for Perplexity API integration.
*Line 0*  

#### Function: `main`
> Test the Perplexity API connection and make a sample query.
*Line 17*  

### 📄 hypercode\core\src\core\hypercode-\src\build.py

#### Module: `build`
> Build script for the HyperCode language.
*Line 0*  

#### Function: `build`
> Builds a HyperCode source file to the target language.
*Line 34*  

### 📄 hypercode\core\src\core\hypercode-\src\core\ast_nodes.py

#### Module: `ast_nodes`
> Abstract Syntax Tree (AST) nodes for the HyperCode language.
*Line 0*  

#### Class: `Node`
> Base class for all AST nodes.
*Line 24*  

#### Class: `Expression`
> Base class for all expression nodes.
*Line 31*  

#### Class: `Statement`
> Base class for all statement nodes.
*Line 38*  

#### Class: `Program`
> Represents the entire program as a list of statements.
*Line 45*  

#### Class: `Identifier`
> Represents an identifier (e.g., a variable name).
*Line 52*  

#### Class: `Literal`
> Represents a literal value (e.g., number, string).
*Line 59*  

#### Class: `VariableDeclaration`
> Represents a variable declaration (let or const).
*Line 66*  

#### Class: `BinaryOperation`
> Represents a binary operation (e.g., a + b).
*Line 75*  

### 📄 hypercode\core\src\core\hypercode-\src\core\lexer.py

#### Module: `lexer`
> HyperCode Lexer Module
*Line 0*  

#### Class: `LexerError`
> Represents a lexical analysis error.
*Line 15*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode programming language.
*Line 32*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 49*  

#### Function: `tokenize`
> Convert the source code into a list of tokens.
*Line 110*  

#### Function: `is_at_end`
*Line 134*  

#### Function: `scan_token`
> Scan the next token from the source code.
*Line 137*  

#### Function: `advance`
*Line 228*  

#### Function: `add_token`
> Add a new token to the tokens list.
*Line 233*  

#### Function: `error`
> Record a lexing error.
*Line 246*  

#### Function: `synchronize`
> Synchronize after an error by skipping tokens until we find a statement boundary.
*Line 262*  

#### Function: `previous`
> Return the previous character.
*Line 274*  

#### Function: `peek_next`
> Look ahead two characters.
*Line 280*  

#### Function: `match`
*Line 286*  

#### Function: `peek`
*Line 295*  

#### Function: `string`
> Parse a string literal.
*Line 300*  

#### Function: `is_digit`
> Check if a character is a digit (0-9).
*Line 362*  

#### Function: `number`
> Parse a number literal (integer or float).
*Line 366*  

#### Function: `is_alpha`
> Check if a character is alphabetic or underscore.
*Line 421*  

#### Function: `is_alphanumeric`
> Check if a character is alphanumeric or underscore.
*Line 425*  

#### Function: `is_hex_digit`
> Check if a character is a valid hexadecimal digit.
*Line 429*  

#### Function: `identifier`
> Parse an identifier or keyword.
*Line 433*  

### 📄 hypercode\core\src\core\hypercode-\src\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\src\core\parser.py

#### Class: `ParseError`
*Line 8*  

#### Class: `Parser`
*Line 12*  

#### Function: `__init__`
*Line 13*  

#### Function: `parse`
> Parse the entire program.
*Line 17*  

#### Function: `declaration`
*Line 26*  

#### Function: `var_declaration`
*Line 39*  

#### Function: `statement`
*Line 64*  

#### Function: `print_statement`
*Line 71*  

#### Function: `expression_statement`
*Line 76*  

#### Function: `block`
*Line 81*  

#### Function: `expression`
*Line 88*  

#### Function: `assignment`
*Line 91*  

#### Function: `equality`
*Line 106*  

#### Function: `comparison`
*Line 116*  

#### Function: `term`
*Line 129*  

#### Function: `factor`
*Line 137*  

#### Function: `unary`
*Line 145*  

#### Function: `primary`
*Line 152*  

#### Function: `match`
*Line 184*  

#### Function: `consume`
*Line 191*  

#### Function: `error`
*Line 201*  

#### Function: `synchronize`
*Line 207*  

#### Function: `check`
*Line 227*  

#### Function: `advance`
*Line 232*  

#### Function: `is_at_end`
*Line 237*  

#### Function: `peek`
*Line 240*  

#### Function: `previous`
*Line 243*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode-backend-js-COMPLETE.py

#### Module: `hypercode-backend-js-COMPLETE`
> HyperCode JavaScript Backend - Complete Implementation
*Line 0*  

#### Class: `JSCompiler`
> Compiles HyperCode AST to JavaScript.
*Line 19*  

#### Function: `__init__`
> Initialize compiler.
*Line 30*  

#### Function: `compile`
> Compile AST to JavaScript.
*Line 42*  

#### Function: `_generate_header`
> Generate JavaScript header
*Line 65*  

#### Function: `_generate_setup`
> Generate setup code (memory tape, pointer, I/O)
*Line 74*  

#### Function: `_generate_main`
> Generate JavaScript for AST node.
*Line 110*  

#### Function: `_generate_footer`
> Generate JavaScript footer
*Line 162*  

#### Function: `_indent`
> Get current indentation
*Line 179*  

#### Function: `optimize_ast`
> Optimize AST (future: loop unrolling, dead code elimination).
*Line 183*  

#### Function: `main`
> CLI interface for JavaScript backend
*Line 200*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode-idea-generator-WEB.py

#### Module: `hypercode-idea-generator-WEB`
> HyperCode Community Idea Generator - Web Interface (HTML/CSS/JS)
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode-launch-kit.py

#### Module: `hypercode-launch-kit`
> HyperCode Launch Kit - Ultimate System Initialization
*Line 0*  

#### Class: `HyperCodeLaunchKit`
> Complete launch system initialization
*Line 23*  

#### Function: `__init__`
*Line 26*  

#### Function: `create_readme`
> Create the ultimate README.md
*Line 30*  

#### Function: `create_launch_checklist`
> Create launch day checklist
*Line 367*  

#### Function: `create_launch_script`
> Create automated launch script
*Line 620*  

#### Function: `create_first_30_days`
> Create 30-day success roadmap
*Line 718*  

#### Function: `print_summary`
> Print beautiful summary
*Line 974*  

#### Function: `main`
> Run launch kit initialization
*Line 1007*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode-lexer-COMPLETE.py

#### Module: `hypercode-lexer-COMPLETE`
> HyperCode Lexer - Complete Implementation
*Line 0*  

#### Class: `TokenType`
> HyperCode token types - minimal yet powerful
*Line 21*  

#### Class: `Token`
> Represents a single token with position tracking
*Line 45*  

#### Function: `__repr__`
> Neurodivergent-friendly representation
*Line 54*  

#### Class: `LexerError`
> Lexer-specific errors with context
*Line 59*  

#### Function: `__init__`
*Line 62*  

#### Class: `HyperCodeLexer`
> Tokenizes HyperCode programs with accessibility features.
*Line 69*  

#### Function: `__init__`
> Initialize lexer with source code.
*Line 95*  

#### Function: `tokenize`
> Convert HyperCode source to token stream.
*Line 110*  

#### Function: `_advance_position`
> Update position tracking after processing character
*Line 169*  

#### Function: `_skip_comment`
> Skip characters until end of line
*Line 179*  

#### Function: `get_tokens`
> Return current token list
*Line 184*  

#### Function: `filter_tokens`
> Get tokens excluding certain types.
*Line 188*  

#### Function: `print_tokens`
> Print tokens in readable format.
*Line 205*  

#### Function: `get_statistics`
> Get token statistics (useful for analysis).
*Line 236*  

#### Function: `main`
> CLI interface for the lexer
*Line 250*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode-parser-COMPLETE.py

#### Module: `hypercode-parser-COMPLETE`
> HyperCode Parser - Complete Implementation
*Line 0*  

#### Class: `NodeType`
> AST Node types
*Line 22*  

#### Class: `ASTNode`
> Abstract Syntax Tree Node.
*Line 38*  

#### Function: `__repr__`
> Pretty-print AST (neurodivergent-friendly)
*Line 51*  

#### Class: `ParserError`
> Parser-specific errors with context
*Line 68*  

#### Function: `__init__`
*Line 71*  

#### Class: `HyperCodeParser`
> Parses HyperCode token stream into AST.
*Line 80*  

#### Function: `__init__`
> Initialize parser with token stream.
*Line 94*  

#### Function: `parse`
> Parse tokens into AST.
*Line 105*  

#### Function: `_parse_statement`
> Parse a single statement
*Line 127*  

#### Function: `_parse_loop`
> Parse loop structure: [ statements ]
*Line 174*  

#### Function: `_advance`
> Move to next token
*Line 209*  

#### Function: `_is_at_end`
> Check if at end of token stream
*Line 215*  

#### Function: `validate`
> Validate AST structure.
*Line 222*  

#### Function: `print_ast`
> Print AST in readable format.
*Line 237*  

#### Function: `main`
> CLI interface for the parser
*Line 251*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\__init__.py

#### Module: `__init__`
> HyperCode - A neurodivergent-first programming language with AI compatibility.
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\__main__.py

#### Function: `main`
*Line 6*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\config.py

#### Module: `config`
> Configuration module for HyperCode.
*Line 0*  

#### Class: `Config`
> Configuration class for HyperCode
*Line 16*  

#### Function: `get_headers`
> Get headers for API requests
*Line 27*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\core\__init__.py

#### Module: `__init__`
> Core package for the HyperCode language implementation.
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\core\ast.py

#### Class: `Node`
*Line 9*  

#### Function: `accept`
*Line 10*  

#### Class: `Expr`
*Line 20*  

#### Class: `Literal`
*Line 25*  

#### Class: `Variable`
*Line 30*  

#### Class: `Assign`
*Line 35*  

#### Class: `Binary`
*Line 41*  

#### Class: `Unary`
*Line 48*  

#### Class: `Grouping`
*Line 54*  

#### Class: `Call`
*Line 59*  

#### Class: `Get`
*Line 66*  

#### Class: `Stmt`
*Line 73*  

#### Class: `Expression`
*Line 78*  

#### Class: `Print`
*Line 83*  

#### Class: `Var`
*Line 88*  

#### Class: `Block`
*Line 94*  

#### Class: `Intent`
*Line 99*  

#### Class: `Program`
*Line 106*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\core\cli.py

#### Module: `cli`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\core\error_handler.py

#### Function: `report_parse_error`
*Line 5*  

#### Function: `report`
*Line 12*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\core\lexer.py

#### Module: `lexer`
> Core HyperCode language implementation - Lexer
*Line 0*  

#### Class: `LexerError`
> Exception raised for errors in the lexer.
*Line 32*  

#### Function: `__init__`
*Line 35*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode language.
*Line 42*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 109*  

#### Function: `tokenize`
> Convert source code into a list of tokens.
*Line 126*  

#### Function: `_match_patterns`
> Try to match the current position against all token patterns.
*Line 161*  

#### Function: `_update_position`
> Update line and column numbers based on the given text.
*Line 187*  

#### Function: `_add_token`
> Add a token to the token list.
*Line 206*  

#### Function: `_handle_unknown`
> Handle unknown characters in the source.
*Line 270*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\core\parser.py

#### Class: `ParseError`
*Line 24*  

#### Class: `Parser`
*Line 28*  

#### Function: `__init__`
*Line 29*  

#### Function: `parse`
> Parse the entire program.
*Line 33*  

#### Function: `declaration`
*Line 42*  

#### Function: `var_declaration`
*Line 51*  

#### Function: `statement`
*Line 67*  

#### Function: `print_statement`
*Line 76*  

#### Function: `intent_statement`
*Line 81*  

#### Function: `expression_statement`
*Line 96*  

#### Function: `block`
*Line 101*  

#### Function: `expression`
*Line 108*  

#### Function: `assignment`
*Line 111*  

#### Function: `equality`
*Line 126*  

#### Function: `comparison`
*Line 136*  

#### Function: `term`
*Line 149*  

#### Function: `factor`
*Line 157*  

#### Function: `unary`
*Line 165*  

#### Function: `primary`
*Line 172*  

#### Function: `_primary`
*Line 189*  

#### Function: `finish_call`
*Line 220*  

#### Function: `match`
*Line 233*  

#### Function: `consume`
*Line 240*  

#### Function: `error`
*Line 247*  

#### Function: `synchronize`
*Line 253*  

#### Function: `check`
*Line 273*  

#### Function: `advance`
*Line 278*  

#### Function: `is_at_end`
*Line 283*  

#### Function: `peek`
*Line 286*  

#### Function: `previous`
*Line 289*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\core\semantic_analyzer.py

#### Module: `semantic_analyzer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\core\tokens.py

#### Class: `TokenType`
*Line 6*  

#### Class: `Token`
*Line 61*  

#### Function: `__str__`
*Line 68*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\enhanced_perplexity_client.py

#### Module: `enhanced_perplexity_client`
> Enhanced Perplexity Client with Knowledge Base Integration
*Line 0*  

#### Class: `EnhancedPerplexityClient`
> Enhanced Perplexity client with knowledge base integration
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `query_with_context`
> Send a query with relevant knowledge base context
*Line 25*  

#### Function: `add_research_data`
> Add research data to the knowledge base
*Line 61*  

#### Function: `search_research_data`
> Search the knowledge base
*Line 71*  

#### Function: `list_research_documents`
> List all research documents
*Line 75*  

#### Function: `get_document`
> Get a specific document
*Line 79*  

#### Function: `delete_document`
> Delete a document
*Line 83*  

#### Function: `import_from_perplexity_space`
> Import data from Perplexity Space export
*Line 87*  

#### Function: `test_context_integration`
> Test the context integration
*Line 123*  

#### Function: `create_perplexity_space_import_template`
> Create a template for importing Perplexity Space data
*Line 175*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\knowledge_base.py

#### Module: `knowledge_base`
> HyperCode Knowledge Base - Perplexity Space Integration
*Line 0*  

#### Class: `ResearchDocument`
> Represents a research document from Perplexity Space
*Line 17*  

#### Function: `__post_init__`
*Line 28*  

#### Function: `generate_id`
> Generate unique ID from content hash
*Line 36*  

#### Function: `validate`
> Validate document data
*Line 41*  

#### Function: `update_timestamp`
> Update the last_updated timestamp
*Line 53*  

#### Class: `HyperCodeKnowledgeBase`
> Knowledge base for HyperCode research data
*Line 100*  

#### Function: `__init__`
*Line 103*  

#### Function: `load`
> Load knowledge base from file
*Line 109*  

#### Function: `save`
> Save knowledge base to file
*Line 125*  

#### Function: `add_document`
> Add a new research document
*Line 135*  

#### Function: `search_documents`
> Search documents by query
*Line 163*  

#### Function: `get_context_for_query`
> Get relevant context for a query
*Line 226*  

#### Function: `list_documents`
> List all documents
*Line 256*  

#### Function: `get_document`
> Get a specific document by ID
*Line 260*  

#### Function: `delete_document`
> Delete a document
*Line 264*  

#### Function: `update_document`
> Update an existing document
*Line 272*  

#### Function: `search_by_tags`
> Search documents by tags with AND/OR operators
*Line 286*  

#### Function: `get_document_statistics`
> Get statistics about the knowledge base
*Line 305*  

#### Function: `export_format`
> Export knowledge base in different formats
*Line 330*  

#### Function: `validate_all_documents`
> Validate all documents and return list of errors
*Line 352*  

#### Function: `cleanup_duplicates`
> Remove duplicate documents based on content hash
*Line 362*  

#### Function: `initialize_sample_data`
> Initialize with sample HyperCode research data
*Line 383*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\perplexity_client.py

#### Module: `perplexity_client`
> Perplexity AI API client for HyperCode.
*Line 0*  

#### Class: `PerplexityClient`
> Client for interacting with Perplexity AI API
*Line 12*  

#### Function: `__init__`
> Initialize the Perplexity client.
*Line 15*  

#### Function: `query`
> Send a query to the Perplexity API.
*Line 30*  

#### Function: `test_connection`
> Test the connection to the Perplexity API
*Line 72*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode\repl.py

#### Function: `run_repl`
*Line 7*  

#### Function: `run`
*Line 22*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode_idea_generator.py

#### Module: `hypercode_idea_generator`
> HyperCode Idea Generator - AI-Powered Community Input System
*Line 0*  

#### Class: `HyperCodeIdeaGenerator`
> AI-Powered Idea Generator for HyperCode community input.
*Line 431*  

#### Function: `__init__`
*Line 439*  

#### Function: `get_ideas_by_category`
> Get ideas by category and optionally by difficulty level.
*Line 443*  

#### Function: `get_top_ideas`
> Get most-voted ideas across all categories.
*Line 468*  

#### Function: `vote_for_idea`
> Vote for an idea.
*Line 487*  

#### Function: `get_trending_ideas`
> Get trending ideas (high votes + recent activity).
*Line 497*  

#### Function: `format_idea_card`
> Format idea for display.
*Line 502*  

#### Function: `main`
> Interactive idea generator CLI
*Line 528*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode_lexer_fixed.py

#### Module: `hypercode_lexer_fixed`
> HyperCode Lexer - Fixed String Handling with Escape Sequences
*Line 0*  

#### Class: `TokenType`
> HyperCode token types
*Line 19*  

#### Class: `Token`
> Represents a single token with position tracking
*Line 44*  

#### Function: `__repr__`
> Readable representation
*Line 54*  

#### Class: `LexerError`
> Lexer error with context
*Line 68*  

#### Function: `__init__`
*Line 71*  

#### Class: `HyperCodeLexerFixed`
> Fixed lexer with proper string escape sequence handling.
*Line 84*  

#### Function: `__init__`
> Initialize lexer.
*Line 125*  

#### Function: `tokenize`
> Convert source to token stream.
*Line 145*  

#### Function: `_parse_string`
> Parse string literal with escape sequence handling.
*Line 217*  

#### Function: `_skip_comment`
> Skip comment until end of line
*Line 300*  

#### Function: `_advance`
> Update position after processing character
*Line 305*  

#### Function: `print_tokens`
> Print tokens in readable format
*Line 315*  

#### Function: `run_tests`
> Comprehensive test suite
*Line 329*  

#### Function: `main`
> Main entry point
*Line 446*  

### 📄 hypercode\core\src\core\hypercode-\src\hypercode_poc.py

#### Module: `hypercode_poc`
> HyperCode POC - Neurodivergent-First Programming Language
*Line 0*  

#### Class: `TokenType`
> Brainfuck-inspired core + modern aliases
*Line 18*  

#### Class: `Token`
*Line 34*  

#### Class: `UserConfidenceLevel`
*Line 41*  

#### Class: `EnhancedLexer`
> Smart tokenizer with escape handling + accessibility focus
*Line 48*  

#### Function: `__init__`
*Line 51*  

#### Function: `tokenize`
*Line 74*  

#### Function: `handle_string`
*Line 115*  

#### Function: `handle_number`
*Line 141*  

#### Function: `handle_identifier`
*Line 149*  

#### Function: `advance`
*Line 171*  

#### Class: `ContextAwareErrorMessenger`
> Friendly, adaptive error messages
*Line 176*  

#### Function: `__init__`
*Line 179*  

#### Function: `format_error`
*Line 182*  

#### Class: `SemanticContextStreamer`
> Understand programmer intent from tokens
*Line 189*  

#### Function: `analyze`
*Line 192*  

#### Class: `ConfidenceTracker`
> Adapt system guidance to user skill level
*Line 209*  

#### Function: `__init__`
*Line 212*  

#### Function: `record`
*Line 216*  

#### Class: `HyperCodePOC`
> Main system: Lexer + Error Messenger + Semantic Analyzer + Confidence Tracker
*Line 222*  

#### Function: `__init__`
*Line 225*  

#### Function: `compile`
*Line 232*  

### 📄 hypercode\core\src\core\hypercode-\src\parser\debug_ascii.py

#### Module: `debug_ascii`
> ASCII-only debug
*Line 0*  

#### Function: `test_regex_patterns`
> Test regex patterns directly
*Line 14*  

### 📄 hypercode\core\src\core\hypercode-\src\parser\debug_full.py

#### Module: `debug_full`
> Debug the full parsing flow
*Line 0*  

#### Function: `debug_full_parsing`
> Debug the full parsing flow
*Line 14*  

### 📄 hypercode\core\src\core\hypercode-\src\parser\debug_parser.py

#### Module: `debug_parser`
> Debug the Visual Syntax Parser - Find what's wrong with annotation detection
*Line 0*  

#### Function: `debug_annotation_detection`
> Debug why annotations aren't being detected
*Line 14*  

### 📄 hypercode\core\src\core\hypercode-\src\parser\debug_simple.py

#### Module: `debug_simple`
> Simple debug without emoji characters
*Line 0*  

#### Function: `debug_simple`
> Debug without emoji characters
*Line 14*  

### 📄 hypercode\core\src\core\hypercode-\src\parser\test_parser.py

#### Module: `test_parser`
> Test the Visual Syntax Parser - First Click Moment Demo
*Line 0*  

#### Function: `test_first_click_moment`
> Test the parser with the first click moment example
*Line 14*  

### 📄 hypercode\core\src\core\hypercode-\src\parser\visual_syntax_parser.py

#### Module: `visual_syntax_parser`
> 🎨 Visual Syntax Parser for HyperCode V3
*Line 0*  

#### Class: `SemanticMarker`
> 🎨 Semantic marker types with emoji representations
*Line 18*  

#### Class: `SemanticAnnotation`
> 📋 A single semantic annotation with its metadata
*Line 37*  

#### Function: `__str__`
*Line 46*  

#### Class: `ParsedFunction`
> 🔍 A fully parsed HyperCode function
*Line 51*  

#### Function: `get_annotations_by_type`
> Get all annotations of a specific type
*Line 62*  

#### Class: `VisualSyntaxParser`
> 🎨 Main parser for HyperCode's visual semantic syntax
*Line 69*  

#### Function: `__init__`
*Line 72*  

#### Function: `_build_semantic_patterns`
> 🔍 Build regex patterns for all semantic markers
*Line 76*  

#### Function: `_build_color_scheme`
> 🎨 Build semantic color mapping for IDE highlighting
*Line 105*  

#### Function: `parse_file`
> 📄 Parse an entire HyperCode file
*Line 123*  

#### Function: `parse_content`
> 📝 Parse HyperCode content string
*Line 130*  

#### Function: `_is_function_definition`
> 🔍 Check if line is a function definition
*Line 170*  

#### Function: `_start_new_function`
> 🆕 Create new ParsedFunction from definition line
*Line 179*  

#### Function: `_parse_line_annotations`
> � Parse semantic annotations from a line
*Line 202*  

#### Function: `_parse_annotation_params`
> 🔧 Parse annotation parameters from string
*Line 223*  

#### Function: `generate_syntax_highlighting`
> 🎨 Generate HTML with syntax highlighting for visual markers
*Line 265*  

#### Function: `extract_semantic_summary`
> 📊 Extract semantic summary for analysis
*Line 277*  

#### Function: `validate_neurodiversity_compliance`
> 🧠 Validate neurodiversity-first design principles
*Line 311*  

### 📄 hypercode\core\src\core\hypercode-\src\scaffold (1).py

#### Module: `scaffold (1)`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 141*  

#### Function: `create_python_files`
> Create all Python files with proper __init__.py structure.
*Line 151*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 165*  

#### Function: `create_root_files`
> Create root-level configuration files as empty placeholders.
*Line 202*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 213*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 234*  

#### Function: `main`
> Main scaffolding function.
*Line 259*  

### 📄 hypercode\core\src\core\hypercode-\src\scaffold.py

#### Module: `scaffold`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 153*  

#### Function: `create_python_files`
> Create all Python files with proper docstrings and structure.
*Line 184*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 254*  

#### Function: `create_root_files`
> Create root-level configuration files with appropriate content.
*Line 291*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 541*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 583*  

#### Function: `main`
> Main scaffolding function.
*Line 621*  

### 📄 hypercode\core\src\core\hypercode-\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode\core\src\core\hypercode-\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode\core\src\core\hypercode-\test_intent_blocks.py

#### Module: `test_intent_blocks`
> Test script for Intent Blocks implementation
*Line 0*  

#### Function: `test_intent_block`
> Test parsing of intent blocks
*Line 13*  

### 📄 hypercode\core\src\core\hypercode-\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode\core\src\core\hypercode-\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode\core\src\core\hypercode-\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 183*  

### 📄 hypercode\core\src\core\hypercode-\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode\core\src\core\hypercode-\tests\benchmark_knowledge_base.py

#### Module: `benchmark_knowledge_base`
> Performance Benchmark Tool for HyperCode Knowledge Base
*Line 0*  

#### Class: `BenchmarkSuite`
> Comprehensive benchmark suite for Knowledge Base
*Line 24*  

#### Function: `__init__`
*Line 27*  

#### Function: `_get_system_info`
> Get system information for benchmark context
*Line 34*  

#### Function: `generate_test_data`
> Generate test data of specified size
*Line 43*  

#### Function: `benchmark_operation`
> Benchmark a single operation
*Line 93*  

#### Function: `run_benchmark_suite`
> Run complete benchmark suite
*Line 118*  

#### Function: `_calculate_summary`
> Calculate summary statistics
*Line 274*  

#### Function: `_generate_recommendations`
> Generate performance recommendations
*Line 296*  

#### Function: `generate_markdown_report`
> Generate beautiful markdown report
*Line 338*  

#### Function: `save_json_results`
> Save results as JSON
*Line 467*  

#### Function: `main`
> Main benchmark runner
*Line 474*  

### 📄 hypercode\core\src\core\hypercode-\tests\test_accessibility.py

#### Module: `test_accessibility`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\tests\test_ai_gateway.py

#### Module: `test_ai_gateway`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\tests\test_backends.py

#### Module: `test_backends`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\tests\test_core.py

#### Module: `test_core`
> Test harness for core HyperCode components.
*Line 0*  

#### Function: `run_test`
> Test the lexer and parser with the given source code.
*Line 29*  

### 📄 hypercode\core\src\core\hypercode-\tests\test_integration.py

#### Module: `test_integration`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\core\src\core\hypercode-\tests\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Comprehensive test suite for knowledge base search functionality.
*Line 0*  

#### Class: `TestKnowledgeBaseSearch`
> Test suite for knowledge base search functionality.
*Line 12*  

#### Function: `sample_documents`
> Create sample documents for testing.
*Line 16*  

#### Function: `knowledge_base`
> Create a knowledge base instance with sample documents.
*Line 40*  

#### Function: `test_basic_search`
> Test basic search functionality.
*Line 48*  

#### Function: `test_search_with_exact_match`
> Test search with exact phrase matching.
*Line 54*  

#### Function: `test_search_case_insensitive`
> Test that search is case-insensitive.
*Line 59*  

#### Function: `test_search_empty_query`
> Test search with empty query returns all or no documents.
*Line 65*  

#### Function: `test_search_no_matches`
> Test search with no matching documents.
*Line 71*  

#### Function: `test_search_ranking`
> Test that search results are ranked by relevance.
*Line 77*  

#### Function: `test_query_normalization`
> Test query normalization (typos, spacing, punctuation).
*Line 90*  

#### Function: `test_multi_word_query`
> Test search with multiple keywords.
*Line 98*  

#### Function: `test_tag_based_search`
> Test search that includes tag matching.
*Line 103*  

#### Class: `TestEdgeCases`
> Test edge cases and boundary conditions.
*Line 112*  

#### Function: `knowledge_base`
*Line 116*  

#### Function: `test_very_short_query`
> Test search with very short query (1-2 chars).
*Line 121*  

#### Function: `test_very_long_query`
> Test search with very long query (paragraph length).
*Line 126*  

#### Function: `test_special_characters_in_query`
> Test search with special characters.
*Line 136*  

#### Function: `test_unicode_in_query`
> Test search with unicode characters.
*Line 141*  

#### Function: `test_sql_injection_attempt`
> Test that search is safe from SQL injection-style attacks.
*Line 146*  

#### Function: `test_repeated_queries`
> Test that repeated queries return consistent results.
*Line 151*  

#### Class: `TestPerformance`
> Performance benchmarking tests.
*Line 159*  

#### Function: `large_knowledge_base`
> Create a knowledge base with many documents.
*Line 163*  

#### Function: `test_search_response_time`
> Test that search completes within acceptable time.
*Line 179*  

#### Function: `test_concurrent_searches`
> Test multiple concurrent search operations.
*Line 189*  

#### Function: `test_memory_usage`
> Test memory usage during search operations.
*Line 207*  

#### Class: `TestIntegrationWithPerplexity`
> Test integration with EnhancedPerplexityClient.
*Line 213*  

#### Function: `mock_perplexity_client`
> Create a mock Perplexity client.
*Line 217*  

#### Function: `mock_knowledge_base`
> Create a mock knowledge base.
*Line 229*  

#### Function: `test_enhanced_query_with_context`
> Test that queries are enhanced with knowledge base context.
*Line 243*  

#### Function: `test_fallback_to_perplexity_api`
> Test fallback to Perplexity API when no local context found.
*Line 259*  

#### Function: `test_context_ranking_and_selection`
> Test that best context is selected for query enhancement.
*Line 273*  

#### Class: `TestDocumentManagement`
> Test document addition, update, and removal.
*Line 288*  

#### Function: `knowledge_base`
*Line 292*  

#### Function: `test_add_document`
> Test adding a new document to knowledge base.
*Line 300*  

#### Function: `test_update_document`
> Test updating an existing document.
*Line 310*  

#### Function: `test_remove_document`
> Test removing a document.
*Line 315*  

### 📄 hypercode\core\src\core\hypercode-\tests\test_knowledge_base_comprehensive.py

#### Module: `test_knowledge_base_comprehensive`
> Comprehensive Test Suite for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestKnowledgeBaseUnit`
> Unit tests for Knowledge Base functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_docs`
> Sample documents for testing
*Line 36*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 59*  

#### Function: `test_add_single_document`
> Test adding a single document
*Line 65*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 74*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 84*  

#### Function: `test_search_exact_match`
> Test exact search matching
*Line 102*  

#### Function: `test_search_partial_match`
> Test partial search matching
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 124*  

#### Function: `test_search_case_insensitive`
> Test case insensitive search
*Line 135*  

#### Function: `test_empty_search`
> Test empty search query
*Line 147*  

#### Function: `test_nonexistent_search`
> Test search for nonexistent terms
*Line 155*  

#### Function: `test_get_context_for_query`
> Test context extraction
*Line 165*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 176*  

#### Function: `test_document_update`
> Test updating existing documents
*Line 186*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 202*  

#### Function: `test_delete_document`
> Test document deletion
*Line 213*  

#### Class: `TestKnowledgeBaseIntegration`
> Integration tests for Knowledge Base
*Line 229*  

#### Function: `populated_kb`
> Create a populated knowledge base for integration testing
*Line 233*  

#### Function: `test_complex_search_queries`
> Test complex search scenarios
*Line 277*  

#### Function: `test_search_ranking_quality`
> Test that search results are properly ranked
*Line 291*  

#### Function: `test_related_term_expansion`
> Test that related terms are properly expanded
*Line 301*  

#### Function: `test_performance_with_large_dataset`
> Test performance with larger dataset
*Line 313*  

#### Function: `test_concurrent_access_simulation`
> Test simulated concurrent access
*Line 332*  

#### Class: `TestKnowledgeBasePerformance`
> Performance tests for Knowledge Base
*Line 356*  

#### Function: `large_kb`
> Create a large knowledge base for performance testing
*Line 360*  

#### Function: `test_search_performance_large_dataset`
> Test search performance with large dataset
*Line 382*  

#### Function: `test_save_performance_large_dataset`
> Test save performance with large dataset
*Line 396*  

#### Function: `test_load_performance_large_dataset`
> Test load performance with large dataset
*Line 409*  

#### Function: `test_memory_usage_large_dataset`
> Test memory usage with large dataset
*Line 423*  

#### Class: `TestKnowledgeBaseEdgeCases`
> Edge case tests for Knowledge Base
*Line 446*  

#### Function: `edge_case_kb`
> Create knowledge base for edge case testing
*Line 450*  

#### Function: `test_empty_title_handling`
> Test handling of documents with empty titles
*Line 494*  

#### Function: `test_special_characters_handling`
> Test handling of special characters and unicode
*Line 499*  

#### Function: `test_very_long_titles`
> Test handling of very long titles
*Line 507*  

#### Function: `test_empty_content_handling`
> Test handling of documents with empty content
*Line 512*  

#### Function: `test_none_tags_handling`
> Test handling of None tags
*Line 517*  

#### Function: `test_malformed_json_handling`
> Test handling of malformed JSON files
*Line 531*  

#### Function: `test_file_permission_handling`
> Test handling of file permission issues
*Line 544*  

### 📄 hypercode\core\src\core\hypercode-\tests\test_lexer.py

#### Function: `test_lexer_basic_tokens`
*Line 5*  

#### Function: `test_lexer_strings`
*Line 23*  

#### Function: `test_lexer_operators`
*Line 48*  

### 📄 hypercode\core\src\core\hypercode-\tests\test_lexer_extended.py

#### Function: `test_lexer_escaped_strings`
> Test handling of strings with escaped characters.
*Line 5*  

#### Function: `test_lexer_numbers`
> Test various number formats.
*Line 18*  

#### Function: `test_lexer_operators`
> Test all operators.
*Line 39*  

#### Function: `test_lexer_comments`
> Test handling of single-line and multi-line comments.
*Line 86*  

#### Function: `test_lexer_whitespace`
> Test handling of various whitespace characters.
*Line 115*  

#### Function: `test_lexer_error_handling`
> Test error handling for invalid tokens.
*Line 130*  

#### Function: `test_lexer_hex_numbers`
> Test hexadecimal number literals.
*Line 139*  

#### Function: `test_lexer_binary_numbers`
> Test binary number literals.
*Line 157*  

#### Function: `test_lexer_scientific_notation`
> Test scientific notation numbers.
*Line 169*  

#### Function: `test_lexer_string_escapes`
> Test string escape sequences.
*Line 180*  

#### Function: `test_lexer_keywords`
> Test all language keywords.
*Line 197*  

#### Function: `test_lexer_position_tracking`
> Test that line and column numbers are tracked correctly.
*Line 223*  

#### Function: `test_lexer_error_recovery`
> Test that the lexer raises errors on invalid characters.
*Line 243*  

#### Function: `test_lexer_error_messages`
> Test that lexer error messages are informative.
*Line 252*  

### 📄 hypercode\core\src\core\hypercode-\tests\test_parser.py

#### Function: `test_parse_literal`
*Line 12*  

#### Function: `test_parse_variable_declaration`
*Line 24*  

#### Function: `test_parse_binary_expression`
*Line 37*  

### 📄 hypercode\core\src\core\hypercode-\tests\unit\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Phase 1 Unit Tests for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestHyperCodeKnowledgeBase`
> Test suite for HyperCodeKnowledgeBase core functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_documents`
> Sample documents for testing
*Line 33*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 56*  

#### Function: `test_add_document`
> Test adding a single document
*Line 61*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 82*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 92*  

#### Function: `test_search_exact_match`
> Test exact term matching in search
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 126*  

#### Function: `test_search_related_terms`
> Test related term expansion
*Line 139*  

#### Function: `test_search_space_data_boost`
> Test that space data gets boosted in search
*Line 153*  

#### Function: `test_get_context_for_query`
> Test context extraction for queries
*Line 180*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 192*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 203*  

#### Function: `test_empty_search`
> Test search with empty query
*Line 216*  

#### Function: `test_search_nonexistent_term`
> Test search for term that doesn't exist
*Line 221*  

#### Function: `test_document_update`
> Test updating existing document
*Line 231*  

#### Class: `TestResearchDocument`
> Test suite for ResearchDocument dataclass
*Line 250*  

#### Function: `test_document_creation`
> Test creating a research document
*Line 253*  

#### Function: `test_document_optional_fields`
> Test document with optional fields
*Line 273*  

### 📄 hypercode\core\src\core\hypercode-\tests\unit\test_search_algorithm.py

#### Module: `test_search_algorithm`
> Phase 1 Unit Tests for Search Algorithm
*Line 0*  

#### Class: `TestSearchAlgorithm`
> Test suite for search algorithm functionality
*Line 20*  

#### Function: `populated_kb`
> Create a knowledge base with test documents
*Line 24*  

#### Function: `test_exact_title_match_highest_score`
> Test that exact title matches get highest priority
*Line 80*  

#### Function: `test_space_data_boosting`
> Test that space data gets boosted in search results
*Line 92*  

#### Function: `test_related_term_expansion`
> Test related term matching functionality
*Line 105*  

#### Function: `test_tag_matching_scoring`
> Test that tag matches contribute to scoring
*Line 126*  

#### Function: `test_content_frequency_scoring`
> Test that multiple content occurrences increase score
*Line 136*  

#### Function: `test_partial_word_matching`
> Test partial word matching for longer terms
*Line 149*  

#### Function: `test_query_word_ordering`
> Test that query words are properly processed
*Line 167*  

#### Function: `test_case_insensitive_search`
> Test that search is case insensitive
*Line 179*  

#### Function: `test_empty_query_returns_no_results`
> Test that empty queries return no results
*Line 202*  

#### Function: `test_limit_parameter_respected`
> Test that search limit parameter works correctly
*Line 210*  

#### Function: `test_no_results_for_nonexistent_terms`
> Test search for terms that don't exist
*Line 219*  

#### Function: `test_special_characters_in_query`
> Test search with special characters
*Line 227*  

#### Function: `test_unicode_characters`
> Test search with unicode characters
*Line 237*  

#### Function: `test_search_performance_with_large_kb`
> Test search performance with larger knowledge base
*Line 256*  

#### Function: `test_search_result_consistency`
> Test that search results are consistent across multiple calls
*Line 277*  

#### Class: `TestSearchScoringDetails`
> Test detailed scoring algorithm behavior
*Line 292*  

#### Function: `scoring_kb`
> Create KB for detailed scoring tests
*Line 296*  

#### Function: `test_title_match_beats_content_match`
> Test that title matches score higher than content matches
*Line 324*  

#### Function: `test_space_data_boosting_works`
> Test that space data gets boosted
*Line 332*  

#### Function: `test_frequency_scoring`
> Test that content frequency affects scoring
*Line 340*  

### 📄 hypercode\core\src\core\interpreter.py

#### Class: `RuntimeError`
*Line 8*  

#### Function: `__init__`
*Line 9*  

#### Class: `Environment`
*Line 15*  

#### Function: `__init__`
*Line 16*  

#### Function: `define`
*Line 20*  

#### Function: `get`
*Line 23*  

#### Function: `assign`
*Line 30*  

#### Class: `Callable`
*Line 40*  

#### Function: `arity`
*Line 41*  

#### Function: `call`
*Line 44*  

#### Class: `HyperCodeFunction`
*Line 48*  

#### Function: `__init__`
*Line 49*  

#### Function: `call`
*Line 53*  

#### Function: `arity`
*Line 65*  

#### Class: `ReturnException`
*Line 69*  

#### Function: `__init__`
*Line 70*  

#### Class: `Interpreter`
*Line 74*  

#### Function: `__init__`
*Line 75*  

#### Class: `Clock`
*Line 82*  

#### Function: `arity`
*Line 83*  

#### Function: `call`
*Line 86*  

#### Function: `__str__`
*Line 89*  

#### Class: `Double`
*Line 92*  

#### Function: `arity`
*Line 93*  

#### Function: `call`
*Line 96*  

#### Function: `__str__`
*Line 101*  

#### Class: `Square`
*Line 104*  

#### Function: `arity`
*Line 105*  

#### Function: `call`
*Line 108*  

#### Function: `__str__`
*Line 113*  

#### Function: `execute_block`
*Line 120*  

#### Function: `interpret`
*Line 129*  

#### Function: `execute`
*Line 141*  

#### Function: `evaluate`
*Line 144*  

#### Function: `visit_Expression`
*Line 147*  

#### Function: `visit_Print`
*Line 151*  

#### Function: `visit_Let`
*Line 158*  

#### Function: `visit_Block`
*Line 165*  

#### Function: `visit_BlockDecl`
*Line 169*  

#### Function: `visit_Intent`
*Line 175*  

#### Function: `visit_Function`
*Line 180*  

#### Function: `visit_Return`
*Line 185*  

#### Function: `visit_Literal`
*Line 191*  

#### Function: `visit_Grouping`
*Line 194*  

#### Function: `visit_Variable`
*Line 197*  

#### Function: `visit_Assign`
*Line 200*  

#### Function: `visit_Pipe`
*Line 205*  

#### Function: `visit_State`
*Line 234*  

#### Function: `visit_Call`
*Line 244*  

#### Function: `visit_Binary`
*Line 262*  

#### Function: `visit_Unary`
*Line 293*  

#### Function: `is_truthy`
*Line 301*  

#### Function: `stringify`
*Line 308*  

#### Function: `get_output`
*Line 322*  

### 📄 hypercode\core\src\core\lexer.py

#### Module: `lexer`
> HyperCode Lexer Module
*Line 0*  

#### Class: `LexerError`
> Represents a lexical analysis error.
*Line 17*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode programming language.
*Line 33*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 41*  

#### Function: `scan_tokens`
> Scan the source code and return a list of tokens.
*Line 77*  

#### Function: `scan_token`
> Scan a single token.
*Line 87*  

#### Function: `number`
> Lex a number literal.
*Line 164*  

#### Function: `string`
> Lex a string literal.
*Line 197*  

#### Function: `docstring`
> Lex a docstring.
*Line 242*  

#### Function: `identifier`
> Lex an identifier or keyword.
*Line 268*  

#### Function: `error`
> Report a lexing error.
*Line 278*  

#### Function: `is_at_end`
> Check if we've reached the end of the source.
*Line 294*  

#### Function: `advance`
> Consume and return the next character.
*Line 298*  

#### Function: `match`
> Conditionally consume a character if it matches the expected value.
*Line 307*  

#### Function: `peek`
> Look at the next character without consuming it.
*Line 317*  

#### Function: `peek_next`
> Look at the character after the next one without consuming it.
*Line 323*  

#### Function: `add_token`
> Add a new token to the token list.
*Line 329*  

### 📄 hypercode\core\src\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\core\src\core\parser.py

#### Class: `ParseError`
*Line 7*  

#### Class: `Parser`
*Line 11*  

#### Function: `__init__`
*Line 12*  

#### Function: `parse`
> Parse the entire program.
*Line 16*  

#### Function: `declaration`
*Line 25*  

#### Function: `let_declaration`
*Line 38*  

#### Function: `block_declaration`
*Line 48*  

#### Function: `statement`
*Line 54*  

#### Function: `print_statement`
*Line 65*  

#### Function: `expression_statement`
*Line 70*  

#### Function: `block`
*Line 75*  

#### Function: `expression`
*Line 84*  

#### Function: `pipe`
*Line 87*  

#### Function: `assignment`
*Line 103*  

#### Function: `equality`
*Line 118*  

#### Function: `comparison`
*Line 128*  

#### Function: `term`
*Line 141*  

#### Function: `factor`
*Line 149*  

#### Function: `unary`
*Line 157*  

#### Function: `primary`
*Line 164*  

#### Function: `function`
*Line 194*  

#### Function: `if_statement`
*Line 215*  

#### Function: `return_statement`
*Line 227*  

#### Function: `match`
*Line 237*  

#### Function: `consume`
*Line 244*  

#### Function: `error`
*Line 249*  

#### Function: `synchronize`
*Line 255*  

#### Function: `check`
*Line 276*  

#### Function: `advance`
*Line 281*  

#### Function: `is_at_end`
*Line 286*  

#### Function: `peek`
*Line 289*  

#### Function: `previous`
*Line 292*  

### 📄 hypercode\core\src\core\tokens.py

#### Module: `tokens`
> HyperCode Token Types and Definitions
*Line 0*  

#### Class: `TokenType`
*Line 12*  

#### Class: `Token`
> Represents a token in the HyperCode language.
*Line 74*  

#### Function: `__init__`
*Line 86*  

#### Function: `__str__`
*Line 95*  

#### Function: `__repr__`
*Line 98*  

### 📄 hypercode\core\src\duelcode\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode\core\src\duelcode\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode\core\src\duelcode\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode\core\src\duelcode\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode\core\src\duelcode\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode\core\src\duelcode\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode\core\src\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode\core\src\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode\core\src\hypercode-backend-js-COMPLETE.py

#### Module: `hypercode-backend-js-COMPLETE`
> HyperCode JavaScript Backend - Complete Implementation
*Line 0*  

#### Class: `JSCompiler`
> Compiles HyperCode AST to JavaScript.
*Line 19*  

#### Function: `__init__`
> Initialize compiler.
*Line 30*  

#### Function: `compile`
> Compile AST to JavaScript.
*Line 42*  

#### Function: `_generate_header`
> Generate JavaScript header
*Line 65*  

#### Function: `_generate_setup`
> Generate setup code (memory tape, pointer, I/O)
*Line 74*  

#### Function: `_generate_main`
> Generate JavaScript for AST node.
*Line 110*  

#### Function: `_generate_footer`
> Generate JavaScript footer
*Line 162*  

#### Function: `_indent`
> Get current indentation
*Line 179*  

#### Function: `optimize_ast`
> Optimize AST (future: loop unrolling, dead code elimination).
*Line 183*  

#### Function: `main`
> CLI interface for JavaScript backend
*Line 200*  

### 📄 hypercode\core\src\hypercode-idea-generator-WEB.py

#### Module: `hypercode-idea-generator-WEB`
> HyperCode Community Idea Generator - Web Interface (HTML/CSS/JS)
*Line 0*  

### 📄 hypercode\core\src\hypercode-launch-kit.py

#### Module: `hypercode-launch-kit`
> HyperCode Launch Kit - Ultimate System Initialization
*Line 0*  

#### Class: `HyperCodeLaunchKit`
> Complete launch system initialization
*Line 23*  

#### Function: `__init__`
*Line 26*  

#### Function: `create_readme`
> Create the ultimate README.md
*Line 30*  

#### Function: `create_launch_checklist`
> Create launch day checklist
*Line 367*  

#### Function: `create_launch_script`
> Create automated launch script
*Line 620*  

#### Function: `create_first_30_days`
> Create 30-day success roadmap
*Line 718*  

#### Function: `print_summary`
> Print beautiful summary
*Line 974*  

#### Function: `main`
> Run launch kit initialization
*Line 1007*  

### 📄 hypercode\core\src\hypercode-lexer-COMPLETE.py

#### Module: `hypercode-lexer-COMPLETE`
> HyperCode Lexer - Complete Implementation
*Line 0*  

#### Class: `TokenType`
> HyperCode token types - minimal yet powerful
*Line 21*  

#### Class: `Token`
> Represents a single token with position tracking
*Line 45*  

#### Function: `__repr__`
> Neurodivergent-friendly representation
*Line 54*  

#### Class: `LexerError`
> Lexer-specific errors with context
*Line 59*  

#### Function: `__init__`
*Line 62*  

#### Class: `HyperCodeLexer`
> Tokenizes HyperCode programs with accessibility features.
*Line 69*  

#### Function: `__init__`
> Initialize lexer with source code.
*Line 95*  

#### Function: `tokenize`
> Convert HyperCode source to token stream.
*Line 110*  

#### Function: `_advance_position`
> Update position tracking after processing character
*Line 169*  

#### Function: `_skip_comment`
> Skip characters until end of line
*Line 179*  

#### Function: `get_tokens`
> Return current token list
*Line 184*  

#### Function: `filter_tokens`
> Get tokens excluding certain types.
*Line 188*  

#### Function: `print_tokens`
> Print tokens in readable format.
*Line 205*  

#### Function: `get_statistics`
> Get token statistics (useful for analysis).
*Line 236*  

#### Function: `main`
> CLI interface for the lexer
*Line 250*  

### 📄 hypercode\core\src\hypercode-parser-COMPLETE.py

#### Module: `hypercode-parser-COMPLETE`
> HyperCode Parser - Complete Implementation
*Line 0*  

#### Class: `NodeType`
> AST Node types
*Line 22*  

#### Class: `ASTNode`
> Abstract Syntax Tree Node.
*Line 38*  

#### Function: `__repr__`
> Pretty-print AST (neurodivergent-friendly)
*Line 51*  

#### Class: `ParserError`
> Parser-specific errors with context
*Line 68*  

#### Function: `__init__`
*Line 71*  

#### Class: `HyperCodeParser`
> Parses HyperCode token stream into AST.
*Line 80*  

#### Function: `__init__`
> Initialize parser with token stream.
*Line 94*  

#### Function: `parse`
> Parse tokens into AST.
*Line 105*  

#### Function: `_parse_statement`
> Parse a single statement
*Line 127*  

#### Function: `_parse_loop`
> Parse loop structure: [ statements ]
*Line 174*  

#### Function: `_advance`
> Move to next token
*Line 209*  

#### Function: `_is_at_end`
> Check if at end of token stream
*Line 215*  

#### Function: `validate`
> Validate AST structure.
*Line 222*  

#### Function: `print_ast`
> Print AST in readable format.
*Line 237*  

#### Function: `main`
> CLI interface for the parser
*Line 251*  

### 📄 hypercode\core\src\hypercode\__init__.py

#### Module: `__init__`
> HyperCode - A neurodivergent-first programming language with AI compatibility.
*Line 0*  

### 📄 hypercode\core\src\hypercode\__main__.py

#### Function: `main`
*Line 6*  

### 📄 hypercode\core\src\hypercode\cli\__init__.py

#### Module: `__init__`
> HyperCode Command Line Interface
*Line 0*  

#### Function: `main`
> Run the HyperCode lexer from the command line.
*Line 14*  

### 📄 hypercode\core\src\hypercode\config.py

#### Module: `config`
> Configuration module for HyperCode.
*Line 0*  

#### Class: `Config`
> Configuration class for HyperCode
*Line 16*  

#### Function: `get_headers`
> Get headers for API requests
*Line 27*  

### 📄 hypercode\core\src\hypercode\core\__init__.py

#### Module: `__init__`
> Core package for the HyperCode language implementation.
*Line 0*  

### 📄 hypercode\core\src\hypercode\core\cli.py

#### Module: `cli`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\core\src\hypercode\core\error_handler.py

#### Function: `report_parse_error`
*Line 5*  

#### Function: `report`
*Line 12*  

### 📄 hypercode\core\src\hypercode\core\hypercode_ast.py

#### Class: `Node`
*Line 9*  

#### Function: `accept`
*Line 10*  

#### Class: `Expr`
*Line 20*  

#### Class: `Literal`
*Line 25*  

#### Class: `Variable`
*Line 30*  

#### Class: `Assign`
*Line 35*  

#### Class: `Binary`
*Line 41*  

#### Class: `Unary`
*Line 48*  

#### Class: `Grouping`
*Line 54*  

#### Class: `Call`
*Line 59*  

#### Class: `Get`
*Line 66*  

#### Class: `Stmt`
*Line 73*  

#### Class: `Expression`
*Line 78*  

#### Class: `Print`
*Line 83*  

#### Class: `Var`
*Line 88*  

#### Class: `Block`
*Line 94*  

#### Class: `If`
*Line 99*  

#### Class: `Fun`
*Line 106*  

#### Class: `Return`
*Line 113*  

#### Class: `Intent`
*Line 119*  

#### Class: `Program`
*Line 126*  

### 📄 hypercode\core\src\hypercode\core\interpreter.py

#### Class: `Return`
*Line 6*  

#### Function: `__init__`
*Line 7*  

#### Class: `HyperCodeFunction`
*Line 11*  

#### Function: `__init__`
*Line 12*  

#### Function: `__str__`
*Line 16*  

#### Function: `arity`
*Line 19*  

#### Function: `call`
*Line 22*  

#### Class: `Environment`
*Line 35*  

#### Function: `__init__`
*Line 36*  

#### Function: `define`
*Line 40*  

#### Function: `get`
*Line 43*  

#### Function: `assign`
*Line 50*  

#### Class: `Interpreter`
*Line 60*  

#### Function: `__init__`
*Line 61*  

#### Function: `interpret`
*Line 65*  

#### Function: `execute`
*Line 72*  

#### Function: `execute_block`
*Line 75*  

#### Function: `evaluate`
*Line 84*  

#### Function: `visit_Expression`
*Line 87*  

#### Function: `visit_Print`
*Line 90*  

#### Function: `visit_Var`
*Line 94*  

#### Function: `visit_Block`
*Line 100*  

#### Function: `visit_Assign`
*Line 103*  

#### Function: `visit_Binary`
*Line 108*  

#### Function: `visit_Grouping`
*Line 151*  

#### Function: `visit_Literal`
*Line 154*  

#### Function: `visit_Unary`
*Line 157*  

#### Function: `visit_Variable`
*Line 170*  

#### Function: `visit_If`
*Line 173*  

#### Function: `is_truthy`
*Line 179*  

#### Function: `visit_Fun`
*Line 186*  

#### Function: `visit_Return`
*Line 190*  

#### Function: `visit_Call`
*Line 196*  

#### Function: `is_callable`
*Line 214*  

#### Class: `Visitor`
*Line 219*  

#### Function: `visit_Expression`
*Line 220*  

#### Function: `visit_Print`
*Line 223*  

#### Function: `visit_Var`
*Line 226*  

#### Function: `visit_Block`
*Line 229*  

#### Function: `visit_If`
*Line 232*  

#### Function: `visit_Fun`
*Line 235*  

#### Function: `visit_Return`
*Line 238*  

#### Function: `visit_Assign`
*Line 241*  

#### Function: `visit_Binary`
*Line 244*  

#### Function: `visit_Grouping`
*Line 247*  

#### Function: `visit_Literal`
*Line 250*  

#### Function: `visit_Unary`
*Line 253*  

#### Function: `visit_Variable`
*Line 256*  

#### Function: `visit_Call`
*Line 259*  

### 📄 hypercode\core\src\hypercode\core\lexer.py

#### Module: `lexer`
> Core HyperCode language implementation - Lexer
*Line 0*  

#### Class: `LexerError`
> Exception raised for errors in the lexer.
*Line 28*  

#### Function: `__init__`
*Line 35*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode language.
*Line 42*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 45*  

#### Function: `tokenize`
> Convert source code into a list of tokens.
*Line 59*  

#### Function: `is_at_end`
> Check if we've consumed all characters.
*Line 89*  

#### Class: `LexerError`
> Exception raised for errors in the lexer.
*Line 102*  

#### Function: `__init__`
*Line 105*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode language.
*Line 112*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 122*  

#### Function: `tokenize`
> Convert source code into a list of tokens.
*Line 136*  

#### Function: `scan_token`
> Scan the next token from the source.
*Line 164*  

#### Function: `string`
> Scan a string literal.
*Line 251*  

#### Function: `number`
> Scan a number literal.
*Line 273*  

#### Function: `identifier`
> Scan an identifier or keyword.
*Line 306*  

#### Function: `match`
> Match the next character if it matches the expected character.
*Line 316*  

#### Function: `peek`
> Look at the next character without consuming it.
*Line 327*  

#### Function: `peek_next`
> Look at the character after the next one without consuming it.
*Line 333*  

#### Function: `advance`
> Consume and return the next character.
*Line 339*  

#### Function: `add_token`
> Add a new token to the tokens list.
*Line 349*  

#### Function: `error`
> Record a lexer error.
*Line 357*  

#### Function: `is_at_end`
> Check if we've consumed all characters.
*Line 371*  

### 📄 hypercode\core\src\hypercode\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\core\src\hypercode\core\parser.py

#### Class: `ParseError`
*Line 8*  

#### Class: `Parser`
*Line 12*  

#### Function: `__init__`
*Line 13*  

#### Function: `parse`
> Parse the entire program.
*Line 17*  

#### Function: `declaration`
*Line 26*  

#### Function: `var_declaration`
*Line 37*  

#### Function: `statement`
*Line 53*  

#### Function: `print_statement`
*Line 66*  

#### Function: `return_statement`
*Line 71*  

#### Function: `intent_statement`
*Line 79*  

#### Function: `expression_statement`
*Line 92*  

#### Function: `if_statement`
*Line 97*  

#### Function: `function`
*Line 109*  

#### Function: `block`
*Line 128*  

#### Function: `expression`
*Line 135*  

#### Function: `assignment`
*Line 138*  

#### Function: `equality`
*Line 153*  

#### Function: `comparison`
*Line 163*  

#### Function: `term`
*Line 176*  

#### Function: `factor`
*Line 184*  

#### Function: `unary`
*Line 192*  

#### Function: `primary`
*Line 199*  

#### Function: `_primary`
*Line 214*  

#### Function: `finish_call`
*Line 245*  

#### Function: `match`
*Line 258*  

#### Function: `consume`
*Line 265*  

#### Function: `error`
*Line 272*  

#### Function: `synchronize`
*Line 278*  

#### Function: `check`
*Line 298*  

#### Function: `advance`
*Line 303*  

#### Function: `is_at_end`
*Line 308*  

#### Function: `peek`
*Line 311*  

#### Function: `previous`
*Line 314*  

### 📄 hypercode\core\src\hypercode\core\semantic_analyzer.py

#### Module: `semantic_analyzer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\core\src\hypercode\core\sensory_profile.py

#### Module: `sensory_profile`
> Sensory Profile System for HyperCode
*Line 0*  

#### Class: `VisualNoiseLevel`
*Line 15*  

#### Class: `AnimationSpeed`
*Line 22*  

#### Class: `VisualSettings`
> Configuration for visual aspects of the editor.
*Line 29*  

#### Class: `AudioSettings`
> Configuration for audio feedback.
*Line 43*  

#### Class: `AnimationSettings`
> Configuration for animations and transitions.
*Line 58*  

#### Class: `SensoryProfile`
> A complete sensory profile configuration.
*Line 68*  

#### Function: `to_dict`
> Convert the profile to a dictionary.
*Line 77*  

#### Function: `from_dict`
> Create a profile from a dictionary.
*Line 93*  

#### Function: `save`
> Save the profile to a file.
*Line 115*  

#### Function: `load`
> Load a profile from a file.
*Line 121*  

#### Class: `ProfileManager`
> Manages loading and saving of sensory profiles.
*Line 128*  

#### Function: `__init__`
> Initialize with optional custom profiles directory.
*Line 131*  

#### Function: `_ensure_default_profiles`
> Ensure default profiles exist.
*Line 141*  

#### Function: `_create_minimal_profile`
> Create a minimal distraction-free profile.
*Line 154*  

#### Function: `_create_enhanced_profile`
> Create an enhanced profile with helpful visual cues.
*Line 171*  

#### Function: `_create_high_contrast_profile`
> Create a high-contrast profile for better readability.
*Line 198*  

#### Function: `list_profiles`
> List all available profile names.
*Line 224*  

#### Function: `get_profile`
> Get a profile by name.
*Line 228*  

#### Function: `save_profile`
> Save a profile.
*Line 235*  

#### Function: `delete_profile`
> Delete a profile by name.
*Line 240*  

#### Function: `get_profile`
> Helper function to get a profile by name.
*Line 251*  

#### Function: `list_profiles`
> Helper function to list all available profiles.
*Line 263*  

### 📄 hypercode\core\src\hypercode\core\tokens.py

#### Class: `TokenType`
*Line 6*  

#### Class: `Token`
*Line 96*  

#### Function: `__str__`
*Line 103*  

### 📄 hypercode\core\src\hypercode\enhanced_perplexity_client.py

#### Module: `enhanced_perplexity_client`
> Enhanced Perplexity Client with Knowledge Base Integration
*Line 0*  

#### Class: `EnhancedPerplexityClient`
> Enhanced Perplexity client with knowledge base integration
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `query_with_context`
> Send a query with relevant knowledge base context
*Line 25*  

#### Function: `add_research_data`
> Add research data to the knowledge base
*Line 61*  

#### Function: `search_research_data`
> Search the knowledge base
*Line 71*  

#### Function: `list_research_documents`
> List all research documents
*Line 75*  

#### Function: `get_document`
> Get a specific document
*Line 79*  

#### Function: `delete_document`
> Delete a document
*Line 83*  

#### Function: `import_from_perplexity_space`
> Import data from Perplexity Space export
*Line 87*  

#### Function: `test_context_integration`
> Test the context integration
*Line 123*  

#### Function: `create_perplexity_space_import_template`
> Create a template for importing Perplexity Space data
*Line 175*  

### 📄 hypercode\core\src\hypercode\knowledge_base.py

#### Module: `knowledge_base`
> HyperCode Knowledge Base - Perplexity Space Integration
*Line 0*  

#### Class: `ResearchDocument`
> Represents a research document from Perplexity Space
*Line 17*  

#### Function: `__post_init__`
*Line 28*  

#### Function: `generate_id`
> Generate unique ID from content hash
*Line 36*  

#### Function: `validate`
> Validate document data
*Line 41*  

#### Function: `update_timestamp`
> Update the last_updated timestamp
*Line 53*  

#### Class: `HyperCodeKnowledgeBase`
> Knowledge base for HyperCode research data
*Line 100*  

#### Function: `__init__`
*Line 103*  

#### Function: `load`
> Load knowledge base from file
*Line 109*  

#### Function: `save`
> Save knowledge base to file
*Line 125*  

#### Function: `add_document`
> Add a new research document
*Line 135*  

#### Function: `search_documents`
> Search documents by query
*Line 163*  

#### Function: `get_context_for_query`
> Get relevant context for a query
*Line 227*  

#### Function: `list_documents`
> List all documents
*Line 257*  

#### Function: `get_document`
> Get a specific document by ID
*Line 261*  

#### Function: `delete_document`
> Delete a document
*Line 265*  

#### Function: `update_document`
> Update an existing document
*Line 273*  

#### Function: `search_by_tags`
> Search documents by tags with AND/OR operators
*Line 287*  

#### Function: `get_document_statistics`
> Get statistics about the knowledge base
*Line 306*  

#### Function: `export_format`
> Export knowledge base in different formats
*Line 331*  

#### Function: `validate_all_documents`
> Validate all documents and return list of errors
*Line 353*  

#### Function: `cleanup_duplicates`
> Remove duplicate documents based on content hash
*Line 363*  

#### Function: `initialize_sample_data`
> Initialize with sample HyperCode research data
*Line 384*  

### 📄 hypercode\core\src\hypercode\perplexity_client.py

#### Module: `perplexity_client`
> Perplexity AI API client for HyperCode.
*Line 0*  

#### Class: `PerplexityClient`
> Client for interacting with Perplexity AI API
*Line 12*  

#### Function: `__init__`
> Initialize the Perplexity client.
*Line 15*  

#### Function: `query`
> Send a query to the Perplexity API.
*Line 30*  

#### Function: `test_connection`
> Test the connection to the Perplexity API
*Line 72*  

### 📄 hypercode\core\src\hypercode\repl.py

#### Function: `run_repl`
*Line 11*  

#### Function: `run`
*Line 32*  

#### Function: `show_help`
*Line 51*  

### 📄 hypercode\core\src\hypercode_idea_generator.py

#### Module: `hypercode_idea_generator`
> HyperCode Idea Generator - AI-Powered Community Input System
*Line 0*  

#### Class: `HyperCodeIdeaGenerator`
> AI-Powered Idea Generator for HyperCode community input.
*Line 431*  

#### Function: `__init__`
*Line 439*  

#### Function: `get_ideas_by_category`
> Get ideas by category and optionally by difficulty level.
*Line 443*  

#### Function: `get_top_ideas`
> Get most-voted ideas across all categories.
*Line 468*  

#### Function: `vote_for_idea`
> Vote for an idea.
*Line 487*  

#### Function: `get_trending_ideas`
> Get trending ideas (high votes + recent activity).
*Line 497*  

#### Function: `format_idea_card`
> Format idea for display.
*Line 502*  

#### Function: `main`
> Interactive idea generator CLI
*Line 528*  

### 📄 hypercode\core\src\hypercode_poc.py

#### Module: `hypercode_poc`
> HyperCode POC - Neurodivergent-First Programming Language
*Line 0*  

#### Class: `TokenType`
> Brainfuck-inspired core + modern aliases
*Line 18*  

#### Class: `Token`
*Line 34*  

#### Class: `UserConfidenceLevel`
*Line 41*  

#### Class: `EnhancedLexer`
> Smart tokenizer with escape handling + accessibility focus
*Line 48*  

#### Function: `__init__`
*Line 51*  

#### Function: `tokenize`
*Line 74*  

#### Function: `handle_string`
*Line 115*  

#### Function: `handle_number`
*Line 141*  

#### Function: `handle_identifier`
*Line 149*  

#### Function: `advance`
*Line 171*  

#### Class: `ContextAwareErrorMessenger`
> Friendly, adaptive error messages
*Line 176*  

#### Function: `__init__`
*Line 179*  

#### Function: `format_error`
*Line 182*  

#### Class: `SemanticContextStreamer`
> Understand programmer intent from tokens
*Line 189*  

#### Function: `analyze`
*Line 192*  

#### Class: `ConfidenceTracker`
> Adapt system guidance to user skill level
*Line 209*  

#### Function: `__init__`
*Line 212*  

#### Function: `record`
*Line 216*  

#### Class: `HyperCodePOC`
> Main system: Lexer + Error Messenger + Semantic Analyzer + Confidence Tracker
*Line 222*  

#### Function: `__init__`
*Line 225*  

#### Function: `compile`
*Line 232*  

### 📄 hypercode\core\src\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\core\src\parser\debug_ascii.py

#### Module: `debug_ascii`
> ASCII-only debug
*Line 0*  

#### Function: `test_regex_patterns`
> Test regex patterns directly
*Line 14*  

### 📄 hypercode\core\src\parser\debug_full.py

#### Module: `debug_full`
> Debug the full parsing flow
*Line 0*  

#### Function: `debug_full_parsing`
> Debug the full parsing flow
*Line 14*  

### 📄 hypercode\core\src\parser\debug_parser.py

#### Module: `debug_parser`
> Debug the Visual Syntax Parser - Find what's wrong with annotation detection
*Line 0*  

#### Function: `debug_annotation_detection`
> Debug why annotations aren't being detected
*Line 14*  

### 📄 hypercode\core\src\parser\debug_simple.py

#### Module: `debug_simple`
> Simple debug without emoji characters
*Line 0*  

#### Function: `debug_simple`
> Debug without emoji characters
*Line 14*  

### 📄 hypercode\core\src\parser\test_parser.py

#### Module: `test_parser`
> Test the Visual Syntax Parser - First Click Moment Demo
*Line 0*  

#### Function: `test_first_click_moment`
> Test the parser with the first click moment example
*Line 14*  

### 📄 hypercode\core\src\parser\visual_syntax_parser.py

#### Module: `visual_syntax_parser`
> 🎨 Visual Syntax Parser for HyperCode V3
*Line 0*  

#### Class: `SemanticMarker`
> 🎨 Semantic marker types with emoji representations
*Line 18*  

#### Class: `SemanticAnnotation`
> 📋 A single semantic annotation with its metadata
*Line 37*  

#### Function: `__str__`
*Line 46*  

#### Class: `ParsedFunction`
> 🔍 A fully parsed HyperCode function
*Line 51*  

#### Function: `get_annotations_by_type`
> Get all annotations of a specific type
*Line 62*  

#### Class: `VisualSyntaxParser`
> 🎨 Main parser for HyperCode's visual semantic syntax
*Line 69*  

#### Function: `__init__`
*Line 72*  

#### Function: `_build_semantic_patterns`
> 🔍 Build regex patterns for all semantic markers
*Line 76*  

#### Function: `_build_color_scheme`
> 🎨 Build semantic color mapping for IDE highlighting
*Line 105*  

#### Function: `parse_file`
> 📄 Parse an entire HyperCode file
*Line 123*  

#### Function: `parse_content`
> 📝 Parse HyperCode content string
*Line 130*  

#### Function: `_is_function_definition`
> 🔍 Check if line is a function definition
*Line 170*  

#### Function: `_start_new_function`
> 🆕 Create new ParsedFunction from definition line
*Line 179*  

#### Function: `_parse_line_annotations`
> � Parse semantic annotations from a line
*Line 202*  

#### Function: `_parse_annotation_params`
> 🔧 Parse annotation parameters from string
*Line 223*  

#### Function: `generate_syntax_highlighting`
> 🎨 Generate HTML with syntax highlighting for visual markers
*Line 265*  

#### Function: `extract_semantic_summary`
> 📊 Extract semantic summary for analysis
*Line 277*  

#### Function: `validate_neurodiversity_compliance`
> 🧠 Validate neurodiversity-first design principles
*Line 311*  

### 📄 hypercode\core\src\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\core\src\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\core\src\scaffold (1).py

#### Module: `scaffold (1)`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 141*  

#### Function: `create_python_files`
> Create all Python files with proper __init__.py structure.
*Line 151*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 165*  

#### Function: `create_root_files`
> Create root-level configuration files as empty placeholders.
*Line 202*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 213*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 234*  

#### Function: `main`
> Main scaffolding function.
*Line 259*  

### 📄 hypercode\core\src\scaffold.py

#### Module: `scaffold`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 153*  

#### Function: `create_python_files`
> Create all Python files with proper docstrings and structure.
*Line 184*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 254*  

#### Function: `create_root_files`
> Create root-level configuration files with appropriate content.
*Line 291*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 541*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 583*  

#### Function: `main`
> Main scaffolding function.
*Line 621*  

### 📄 hypercode\core\src\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode\core\src\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode\core\src\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode\core\src\utils\code_analyzer_ai.py

#### Module: `code_analyzer_ai`
> Perplexity AI Code Analyzer for HyperCode
*Line 0*  

#### Class: `CodeAnalyzerAI`
> AI-powered code analyzer for HyperCode
*Line 19*  

#### Function: `__init__`
*Line 22*  

#### Function: `analyze_file`
> Analyze a Python file with AI assistance
*Line 25*  

#### Function: `_analyze_complexity`
> Analyze code complexity indicators
*Line 61*  

#### Function: `_check_docstrings`
> Check for docstring coverage
*Line 98*  

#### Function: `_get_ai_code_analysis`
> Get AI analysis of code from Perplexity
*Line 134*  

#### Function: `analyze_project`
> Analyze entire project
*Line 162*  

#### Function: `_get_project_ai_insights`
> Get AI insights for the entire project
*Line 206*  

#### Function: `save_analysis`
> Save analysis to file
*Line 238*  

#### Function: `print_summary`
> Print analysis summary
*Line 244*  

#### Function: `main`
> Main function
*Line 262*  

### 📄 hypercode\core\src\utils\debug_search.py

#### Module: `debug_search`
> Debug search results
*Line 0*  

#### Function: `debug_search`
> Debug why space data isn't being found
*Line 15*  

### 📄 hypercode\core\src\utils\demo_ai_research.py

#### Module: `demo_ai_research`
> HyperCode AI Research + Perplexity Integration Demo
*Line 0*  

#### Function: `demo_ai_research_queries`
> Demonstrate AI Research integration with Perplexity
*Line 16*  

#### Function: `test_document_specific_queries`
> Test queries specific to the HyperCode AI Research document
*Line 90*  

### 📄 hypercode\core\src\utils\demo_enhanced_client.py

#### Module: `demo_enhanced_client`
> Demo: Enhanced Perplexity Client with Knowledge Base
*Line 0*  

#### Function: `demo_knowledge_base_integration`
> Demonstrate the knowledge base integration
*Line 16*  

#### Function: `demonstrate_memory_persistence`
> Demonstrate that the knowledge base persists between sessions
*Line 131*  

### 📄 hypercode\core\src\utils\final_integration_test.py

#### Module: `final_integration_test`
> Final Test: Complete Perplexity Space Integration
*Line 0*  

#### Function: `final_integration_test`
> Complete test of the Perplexity Space integration
*Line 15*  

### 📄 hypercode\core\src\utils\health_scanner_ai.py

#### Module: `health_scanner_ai`
> HyperCode Health Scanner with Perplexity AI Integration
*Line 0*  

#### Class: `HealthScannerAI`
> AI-powered health scanner for HyperCode project
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `analyze_project_structure`
> Analyze project structure and identify health issues
*Line 25*  

#### Function: `analyze_dependencies`
> Analyze dependency management
*Line 64*  

#### Function: `analyze_security`
> Analyze security configuration
*Line 100*  

#### Function: `get_ai_recommendations`
> Get AI-powered recommendations based on health scan
*Line 137*  

#### Function: `run_full_scan`
> Run complete health scan with AI analysis
*Line 164*  

#### Function: `save_report`
> Save health scan report to file
*Line 215*  

#### Function: `print_summary`
> Print a summary of the health scan
*Line 221*  

#### Function: `main`
> Main function to run the health scanner
*Line 241*  

### 📄 hypercode\core\src\utils\import-helper.py

#### Module: `import-helper`
> HyperCode Perplexity Space Import Helper
*Line 0*  

#### Class: `SpaceImportHelper`
> Helper class for managing Perplexity Space imports
*Line 13*  

#### Function: `__init__`
*Line 16*  

#### Function: `validate_document`
> Validate a document structure
*Line 21*  

#### Function: `load_template`
> Load documents from JSON template file
*Line 63*  

#### Function: `validate_all`
> Validate all loaded documents
*Line 83*  

#### Function: `generate_report`
> Generate a validation report
*Line 95*  

#### Function: `create_import_script`
> Generate a Python script to import the data
*Line 141*  

#### Function: `create_template_instructions`
> Generate detailed instructions for filling the template
*Line 193*  

#### Function: `main`
> CLI interface for the import helper
*Line 264*  

### 📄 hypercode\core\src\utils\import_all_space_data.py

#### Module: `import_all_space_data`
> Complete Import of HyperCode Space Data
*Line 0*  

#### Function: `format_content`
> Recursively format nested data into readable text
*Line 16*  

#### Function: `import_all_hypercode_data`
> Import all sections of your HyperCode Space data
*Line 41*  

### 📄 hypercode\core\src\utils\import_hypercode_data.py

#### Module: `import_hypercode_data`
> Import HyperCode Space Data
*Line 0*  

#### Function: `import_hypercode_space_data`
> Import your actual HyperCode Space data
*Line 16*  

### 📄 hypercode\core\src\utils\import_perplexity_space.py

#### Module: `import_perplexity_space`
> Perplexity Space Data Importer
*Line 0*  

#### Function: `create_manual_import_script`
> Create a script for manual data entry from Perplexity Space
*Line 17*  

#### Function: `create_json_import_template`
> Create a JSON template for importing data
*Line 86*  

#### Function: `import_from_json`
> Import data from JSON file
*Line 115*  

#### Function: `test_imported_data`
> Test the imported data with context-aware queries
*Line 153*  

#### Function: `show_import_menu`
> Show the import menu
*Line 188*  

### 📄 hypercode\core\src\utils\local_health_scanner.py

#### Module: `local_health_scanner`
> Local Project Health Scanner for HyperCode
*Line 0*  

#### Class: `ProjectScanner`
> Scans the project for health metrics without external dependencies
*Line 19*  

#### Function: `__init__`
*Line 22*  

#### Function: `scan_project`
> Scan the entire project and return health metrics
*Line 34*  

#### Function: `_scan_directory`
> Recursively scan a directory for Python files
*Line 42*  

#### Function: `_analyze_file`
> Analyze a single Python file
*Line 51*  

#### Function: `_analyze_ast`
> Analyze Python AST for code quality metrics
*Line 74*  

#### Function: `_check_documentation`
> Check documentation coverage
*Line 94*  

#### Function: `_check_tests`
> Check test coverage
*Line 106*  

#### Function: `_calculate_metrics`
> Calculate final metrics
*Line 117*  

#### Function: `print_health_report`
> Print a formatted health report
*Line 128*  

#### Function: `main`
> Main function to run the health scanner
*Line 158*  

### 📄 hypercode\core\src\utils\perplexity_space_collector.py

#### Module: `perplexity_space_collector`
> Perplexity Space Data Collector
*Line 0*  

#### Function: `quick_copy_paste_collector`
> Quick collector for copy-paste workflow
*Line 18*  

#### Function: `create_structured_template`
> Create a structured JSON template for bulk import
*Line 117*  

#### Function: `show_bro_hacks`
> Show BROski's pro tips
*Line 167*  

#### Function: `main_menu`
> Main menu for the collector
*Line 207*  

### 📄 hypercode\core\src\utils\perplexity_space_integration.py

#### Module: `perplexity_space_integration`
> Perplexity Space Integration Guide
*Line 0*  

#### Function: `main`
*Line 16*  

### 📄 hypercode\core\src\utils\run_lexer.py

#### Function: `run_lexer`
> Run the lexer on a source file and print the tokens.
*Line 12*  

### 📄 hypercode\core\src\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode\core\tests\benchmark_knowledge_base.py

#### Module: `benchmark_knowledge_base`
> Performance Benchmark Tool for HyperCode Knowledge Base
*Line 0*  

#### Class: `BenchmarkSuite`
> Comprehensive benchmark suite for Knowledge Base
*Line 24*  

#### Function: `__init__`
*Line 27*  

#### Function: `_get_system_info`
> Get system information for benchmark context
*Line 34*  

#### Function: `generate_test_data`
> Generate test data of specified size
*Line 43*  

#### Function: `benchmark_operation`
> Benchmark a single operation
*Line 93*  

#### Function: `run_benchmark_suite`
> Run complete benchmark suite
*Line 118*  

#### Function: `_calculate_summary`
> Calculate summary statistics
*Line 274*  

#### Function: `_generate_recommendations`
> Generate performance recommendations
*Line 296*  

#### Function: `generate_markdown_report`
> Generate beautiful markdown report
*Line 338*  

#### Function: `save_json_results`
> Save results as JSON
*Line 467*  

#### Function: `main`
> Main benchmark runner
*Line 474*  

### 📄 hypercode\core\tests\conftest.py

#### Function: `sample_hypercode`
*Line 16*  

#### Function: `sample_lexer_tokens`
*Line 27*  

### 📄 hypercode\core\tests\test_accessibility.py

#### Module: `test_accessibility`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\core\tests\test_ai_gateway.py

#### Module: `test_ai_gateway`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\core\tests\test_backends.py

#### Module: `test_backends`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\core\tests\test_core.py

#### Module: `test_core`
> Test harness for core HyperCode components.
*Line 0*  

#### Function: `run_test`
> Test the lexer, parser, and interpreter with the given source code.
*Line 30*  

### 📄 hypercode\core\tests\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode\core\tests\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode\core\tests\test_integration.py

#### Module: `test_integration`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\core\tests\test_intent_blocks.py

#### Module: `test_intent_blocks`
> Test script for Intent Blocks implementation
*Line 0*  

#### Function: `test_intent_block`
> Test parsing of intent blocks
*Line 13*  

### 📄 hypercode\core\tests\test_interpreter.py

#### Function: `run_code`
> A helper function to run code and capture stdout.
*Line 10*  

#### Class: `TestInterpreter`
*Line 28*  

#### Function: `test_if_statement_then`
*Line 30*  

#### Function: `test_if_statement_else`
*Line 42*  

#### Function: `test_function_call`
*Line 54*  

#### Function: `test_function_with_parameters`
*Line 64*  

#### Function: `test_function_with_return`
*Line 74*  

#### Function: `test_recursive_function_call`
*Line 85*  

#### Function: `test_scoping`
*Line 99*  

### 📄 hypercode\core\tests\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Comprehensive test suite for knowledge base search functionality.
*Line 0*  

#### Class: `TestKnowledgeBaseSearch`
> Test suite for knowledge base search functionality.
*Line 12*  

#### Function: `sample_documents`
> Create sample documents for testing.
*Line 16*  

#### Function: `knowledge_base`
> Create a knowledge base instance with sample documents.
*Line 40*  

#### Function: `test_basic_search`
> Test basic search functionality.
*Line 48*  

#### Function: `test_search_with_exact_match`
> Test search with exact phrase matching.
*Line 54*  

#### Function: `test_search_case_insensitive`
> Test that search is case-insensitive.
*Line 59*  

#### Function: `test_search_empty_query`
> Test search with empty query returns all or no documents.
*Line 65*  

#### Function: `test_search_no_matches`
> Test search with no matching documents.
*Line 71*  

#### Function: `test_search_ranking`
> Test that search results are ranked by relevance.
*Line 77*  

#### Function: `test_query_normalization`
> Test query normalization (typos, spacing, punctuation).
*Line 90*  

#### Function: `test_multi_word_query`
> Test search with multiple keywords.
*Line 98*  

#### Function: `test_tag_based_search`
> Test search that includes tag matching.
*Line 103*  

#### Class: `TestEdgeCases`
> Test edge cases and boundary conditions.
*Line 112*  

#### Function: `knowledge_base`
*Line 116*  

#### Function: `test_very_short_query`
> Test search with very short query (1-2 chars).
*Line 121*  

#### Function: `test_very_long_query`
> Test search with very long query (paragraph length).
*Line 126*  

#### Function: `test_special_characters_in_query`
> Test search with special characters.
*Line 136*  

#### Function: `test_unicode_in_query`
> Test search with unicode characters.
*Line 141*  

#### Function: `test_sql_injection_attempt`
> Test that search is safe from SQL injection-style attacks.
*Line 146*  

#### Function: `test_repeated_queries`
> Test that repeated queries return consistent results.
*Line 151*  

#### Class: `TestPerformance`
> Performance benchmarking tests.
*Line 159*  

#### Function: `large_knowledge_base`
> Create a knowledge base with many documents.
*Line 163*  

#### Function: `test_search_response_time`
> Test that search completes within acceptable time.
*Line 179*  

#### Function: `test_concurrent_searches`
> Test multiple concurrent search operations.
*Line 189*  

#### Function: `test_memory_usage`
> Test memory usage during search operations.
*Line 207*  

#### Class: `TestIntegrationWithPerplexity`
> Test integration with EnhancedPerplexityClient.
*Line 213*  

#### Function: `mock_perplexity_client`
> Create a mock Perplexity client.
*Line 217*  

#### Function: `mock_knowledge_base`
> Create a mock knowledge base.
*Line 229*  

#### Function: `test_enhanced_query_with_context`
> Test that queries are enhanced with knowledge base context.
*Line 243*  

#### Function: `test_fallback_to_perplexity_api`
> Test fallback to Perplexity API when no local context found.
*Line 259*  

#### Function: `test_context_ranking_and_selection`
> Test that best context is selected for query enhancement.
*Line 273*  

#### Class: `TestDocumentManagement`
> Test document addition, update, and removal.
*Line 288*  

#### Function: `knowledge_base`
*Line 292*  

#### Function: `test_add_document`
> Test adding a new document to knowledge base.
*Line 300*  

#### Function: `test_update_document`
> Test updating an existing document.
*Line 310*  

#### Function: `test_remove_document`
> Test removing a document.
*Line 315*  

### 📄 hypercode\core\tests\test_knowledge_base_comprehensive.py

#### Module: `test_knowledge_base_comprehensive`
> Comprehensive Test Suite for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestKnowledgeBaseUnit`
> Unit tests for Knowledge Base functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_docs`
> Sample documents for testing
*Line 36*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 59*  

#### Function: `test_add_single_document`
> Test adding a single document
*Line 65*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 74*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 84*  

#### Function: `test_search_exact_match`
> Test exact search matching
*Line 102*  

#### Function: `test_search_partial_match`
> Test partial search matching
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 124*  

#### Function: `test_search_case_insensitive`
> Test case insensitive search
*Line 135*  

#### Function: `test_empty_search`
> Test empty search query
*Line 147*  

#### Function: `test_nonexistent_search`
> Test search for nonexistent terms
*Line 155*  

#### Function: `test_get_context_for_query`
> Test context extraction
*Line 165*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 176*  

#### Function: `test_document_update`
> Test updating existing documents
*Line 186*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 202*  

#### Function: `test_delete_document`
> Test document deletion
*Line 213*  

#### Class: `TestKnowledgeBaseIntegration`
> Integration tests for Knowledge Base
*Line 229*  

#### Function: `populated_kb`
> Create a populated knowledge base for integration testing
*Line 233*  

#### Function: `test_complex_search_queries`
> Test complex search scenarios
*Line 277*  

#### Function: `test_search_ranking_quality`
> Test that search results are properly ranked
*Line 291*  

#### Function: `test_related_term_expansion`
> Test that related terms are properly expanded
*Line 301*  

#### Function: `test_performance_with_large_dataset`
> Test performance with larger dataset
*Line 313*  

#### Function: `test_concurrent_access_simulation`
> Test simulated concurrent access
*Line 332*  

#### Class: `TestKnowledgeBasePerformance`
> Performance tests for Knowledge Base
*Line 356*  

#### Function: `large_kb`
> Create a large knowledge base for performance testing
*Line 360*  

#### Function: `test_search_performance_large_dataset`
> Test search performance with large dataset
*Line 382*  

#### Function: `test_save_performance_large_dataset`
> Test save performance with large dataset
*Line 396*  

#### Function: `test_load_performance_large_dataset`
> Test load performance with large dataset
*Line 409*  

#### Function: `test_memory_usage_large_dataset`
> Test memory usage with large dataset
*Line 423*  

#### Class: `TestKnowledgeBaseEdgeCases`
> Edge case tests for Knowledge Base
*Line 446*  

#### Function: `edge_case_kb`
> Create knowledge base for edge case testing
*Line 450*  

#### Function: `test_empty_title_handling`
> Test handling of documents with empty titles
*Line 494*  

#### Function: `test_special_characters_handling`
> Test handling of special characters and unicode
*Line 499*  

#### Function: `test_very_long_titles`
> Test handling of very long titles
*Line 507*  

#### Function: `test_empty_content_handling`
> Test handling of documents with empty content
*Line 512*  

#### Function: `test_none_tags_handling`
> Test handling of None tags
*Line 517*  

#### Function: `test_malformed_json_handling`
> Test handling of malformed JSON files
*Line 531*  

#### Function: `test_file_permission_handling`
> Test handling of file permission issues
*Line 544*  

### 📄 hypercode\core\tests\test_lexer.py

#### Function: `test_lexer_basic_tokens`
*Line 5*  

#### Function: `test_lexer_strings`
*Line 23*  

#### Function: `test_lexer_operators`
*Line 48*  

### 📄 hypercode\core\tests\test_lexer_extended.py

#### Function: `test_lexer_escaped_strings`
> Test handling of strings with escaped characters.
*Line 5*  

#### Function: `test_lexer_numbers`
> Test various number formats.
*Line 18*  

#### Function: `test_lexer_operators`
> Test all operators.
*Line 39*  

#### Function: `test_lexer_comments`
> Test handling of single-line and multi-line comments.
*Line 86*  

#### Function: `test_lexer_whitespace`
> Test handling of various whitespace characters.
*Line 115*  

#### Function: `test_lexer_error_handling`
> Test error handling for invalid tokens.
*Line 130*  

#### Function: `test_lexer_hex_numbers`
> Test hexadecimal number literals.
*Line 139*  

#### Function: `test_lexer_binary_numbers`
> Test binary number literals.
*Line 157*  

#### Function: `test_lexer_scientific_notation`
> Test scientific notation numbers.
*Line 169*  

#### Function: `test_lexer_string_escapes`
> Test string escape sequences.
*Line 180*  

#### Function: `test_lexer_keywords`
> Test all language keywords.
*Line 197*  

#### Function: `test_lexer_position_tracking`
> Test that line and column numbers are tracked correctly.
*Line 223*  

#### Function: `test_lexer_error_recovery`
> Test that the lexer raises errors on invalid characters.
*Line 243*  

#### Function: `test_lexer_error_messages`
> Test that lexer error messages are informative.
*Line 252*  

### 📄 hypercode\core\tests\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode\core\tests\test_parser.py

#### Function: `test_parse_literal`
*Line 12*  

#### Function: `test_parse_variable_declaration`
*Line 24*  

#### Function: `test_parse_binary_expression`
*Line 37*  

### 📄 hypercode\core\tests\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode\core\tests\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 185*  

### 📄 hypercode\core\tests\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode\core\tests\test_sensory_profiles.py

#### Module: `test_sensory_profiles`
> Tests for the sensory profile system.
*Line 0*  

#### Function: `test_visual_settings_creation`
> Test creating visual settings.
*Line 21*  

#### Function: `test_audio_settings_creation`
> Test creating audio settings.
*Line 35*  

#### Function: `test_animation_settings_creation`
> Test creating animation settings.
*Line 44*  

#### Function: `test_sensory_profile_creation`
> Test creating a complete sensory profile.
*Line 55*  

#### Function: `test_profile_serialization`
> Test serializing AND deserializing a profile.
*Line 71*  

#### Function: `test_profile_file_io`
> Test saving and loading a profile to/from a file.
*Line 92*  

#### Function: `test_profile_manager_initialization`
> Test initializing the profile manager and checking default profiles.
*Line 115*  

#### Function: `test_profile_manager_get_profile`
> Test getting a profile by name.
*Line 129*  

#### Function: `test_profile_manager_save_custom_profile`
> Test saving a custom profile.
*Line 142*  

#### Function: `test_profile_manager_delete_profile`
> Test deleting a profile.
*Line 169*  

### 📄 hypercode\core\tests\test_syntax.py

#### Module: `test_syntax`
> Tests for HyperCode syntax features.
*Line 0*  

#### Function: `test_program_structure`
> Test basic program structure and entry point.
*Line 8*  

#### Function: `test_function_definition`
> Test function definition syntax.
*Line 26*  

#### Function: `test_io_operations`
> Test input/output operations.
*Line 49*  

#### Function: `test_variables`
> Test variable declarations and assignments.
*Line 73*  

#### Function: `test_loops`
> Test loop constructs.
*Line 96*  

#### Function: `test_conditionals`
> Test if/else conditionals.
*Line 117*  

#### Function: `test_goto`
> Test goto and labels.
*Line 142*  

#### Function: `test_comments`
> Test that comments are properly ignored.
*Line 167*  

### 📄 hypercode\core\tests\tests\test_lexer_enhanced.py

#### Function: `test_lexer_edge_cases`
*Line 7*  

#### Function: `test_lexer_error_handling`
*Line 28*  

#### Function: `test_lexer_number_literals`
*Line 43*  

#### Function: `test_lexer_string_interpolation`
*Line 65*  

#### Function: `test_lexer_docstrings`
*Line 79*  

### 📄 hypercode\core\tests\unit\lexer\test_lexer_basic.py

#### Module: `test_lexer_basic`
> Unit tests for the HyperCode lexer's basic functionality.
*Line 0*  

#### Class: `TestLexerBasic`
> Test basic lexer functionality.
*Line 9*  

#### Function: `test_empty_source`
> Test that an empty source returns only EOF token.
*Line 12*  

#### Function: `test_whitespace_handling`
> Test that whitespace is properly handled and ignored.
*Line 19*  

#### Function: `test_single_character_tokens`
> Test recognition of single-character tokens.
*Line 27*  

#### Function: `test_comments_are_ignored`
> Test that comments are properly ignored.
*Line 52*  

#### Function: `test_string_literals`
> Test string literal tokenization.
*Line 72*  

#### Function: `test_number_literals`
> Test number literal tokenization.
*Line 87*  

#### Function: `test_identifiers_and_keywords`
> Test identifier and keyword recognition.
*Line 103*  

#### Function: `test_error_handling`
> Test error handling for invalid tokens.
*Line 139*  

### 📄 hypercode\core\tests\unit\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode\core\tests\unit\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode\core\tests\unit\test_intent_blocks.py

#### Module: `test_intent_blocks`
> Test script for Intent Blocks implementation
*Line 0*  

#### Function: `test_intent_block`
> Test parsing of intent blocks
*Line 13*  

### 📄 hypercode\core\tests\unit\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Phase 1 Unit Tests for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestHyperCodeKnowledgeBase`
> Test suite for HyperCodeKnowledgeBase core functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_documents`
> Sample documents for testing
*Line 33*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 56*  

#### Function: `test_add_document`
> Test adding a single document
*Line 61*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 82*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 92*  

#### Function: `test_search_exact_match`
> Test exact term matching in search
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 126*  

#### Function: `test_search_related_terms`
> Test related term expansion
*Line 139*  

#### Function: `test_search_space_data_boost`
> Test that space data gets boosted in search
*Line 153*  

#### Function: `test_get_context_for_query`
> Test context extraction for queries
*Line 180*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 192*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 203*  

#### Function: `test_empty_search`
> Test search with empty query
*Line 216*  

#### Function: `test_search_nonexistent_term`
> Test search for term that doesn't exist
*Line 221*  

#### Function: `test_document_update`
> Test updating existing document
*Line 231*  

#### Class: `TestResearchDocument`
> Test suite for ResearchDocument dataclass
*Line 250*  

#### Function: `test_document_creation`
> Test creating a research document
*Line 253*  

#### Function: `test_document_optional_fields`
> Test document with optional fields
*Line 273*  

### 📄 hypercode\core\tests\unit\test_lexer.py

#### Module: `test_lexer`
> Test script for the HyperCode lexer.
*Line 0*  

#### Function: `test_lexer`
> Test the lexer with the given source code and print the results.
*Line 12*  

#### Function: `run_tests`
> Run a series of test cases for the lexer.
*Line 42*  

### 📄 hypercode\core\tests\unit\test_lexer_pytest.py

#### Module: `test_lexer_pytest`
> Pytest tests for the HyperCode lexer.
*Line 0*  

#### Function: `test_basic_arithmetic`
> Test basic arithmetic expressions.
*Line 9*  

#### Function: `test_variable_declaration`
> Test variable declarations.
*Line 25*  

#### Function: `test_string_literals`
> Test string literals.
*Line 40*  

### 📄 hypercode\core\tests\unit\test_mcp_connection.py

#### Function: `check_port`
> Check if a port is open on the given host.
*Line 26*  

#### Function: `find_running_servers`
> Scan common ports to find running servers.
*Line 36*  

#### Function: `test_server_connection`
> Test connection to a single MCP server.
*Line 49*  

#### Function: `test_all_servers`
> Test connection to all MCP servers and print results.
*Line 90*  

#### Function: `check_dependencies`
> Check if required dependencies are installed.
*Line 139*  

### 📄 hypercode\core\tests\unit\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode\core\tests\unit\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode\core\tests\unit\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 185*  

### 📄 hypercode\core\tests\unit\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode\core\tests\unit\test_search_algorithm.py

#### Module: `test_search_algorithm`
> Phase 1 Unit Tests for Search Algorithm
*Line 0*  

#### Class: `TestSearchAlgorithm`
> Test suite for search algorithm functionality
*Line 20*  

#### Function: `populated_kb`
> Create a knowledge base with test documents
*Line 24*  

#### Function: `test_exact_title_match_highest_score`
> Test that exact title matches get highest priority
*Line 80*  

#### Function: `test_space_data_boosting`
> Test that space data gets boosted in search results
*Line 92*  

#### Function: `test_related_term_expansion`
> Test related term matching functionality
*Line 105*  

#### Function: `test_tag_matching_scoring`
> Test that tag matches contribute to scoring
*Line 126*  

#### Function: `test_content_frequency_scoring`
> Test that multiple content occurrences increase score
*Line 136*  

#### Function: `test_partial_word_matching`
> Test partial word matching for longer terms
*Line 149*  

#### Function: `test_query_word_ordering`
> Test that query words are properly processed
*Line 167*  

#### Function: `test_case_insensitive_search`
> Test that search is case insensitive
*Line 179*  

#### Function: `test_empty_query_returns_no_results`
> Test that empty queries return no results
*Line 202*  

#### Function: `test_limit_parameter_respected`
> Test that search limit parameter works correctly
*Line 210*  

#### Function: `test_no_results_for_nonexistent_terms`
> Test search for terms that don't exist
*Line 219*  

#### Function: `test_special_characters_in_query`
> Test search with special characters
*Line 227*  

#### Function: `test_unicode_characters`
> Test search with unicode characters
*Line 237*  

#### Function: `test_search_performance_with_large_kb`
> Test search performance with larger knowledge base
*Line 256*  

#### Function: `test_search_result_consistency`
> Test that search results are consistent across multiple calls
*Line 277*  

#### Class: `TestSearchScoringDetails`
> Test detailed scoring algorithm behavior
*Line 292*  

#### Function: `scoring_kb`
> Create KB for detailed scoring tests
*Line 296*  

#### Function: `test_title_match_beats_content_match`
> Test that title matches score higher than content matches
*Line 324*  

#### Function: `test_space_data_boosting_works`
> Test that space data gets boosted
*Line 332*  

#### Function: `test_frequency_scoring`
> Test that content frequency affects scoring
*Line 340*  

### 📄 hypercode\database_analyzer.py

#### Module: `database_analyzer`
> Database Analysis and Improvement Tool
*Line 0*  

#### Class: `EntityMetrics`
*Line 15*  

#### Class: `DocstringStats`
*Line 21*  

#### Class: `DatabaseAnalyzer`
*Line 28*  

#### Function: `__init__`
*Line 29*  

#### Function: `load_database`
> Load and validate the database.
*Line 48*  

#### Function: `analyze_documentation`
> Analyze documentation coverage and quality.
*Line 64*  

#### Function: `analyze_test_coverage`
> Analyze test coverage across the codebase.
*Line 96*  

#### Function: `analyze_code_structure`
> Analyze code structure metrics.
*Line 112*  

#### Function: `generate_report`
> Generate a comprehensive report of findings.
*Line 135*  

#### Function: `get_entities_needing_docs`
> Get entities that need documentation.
*Line 185*  

#### Function: `get_untested_entities`
> Get entities that need tests.
*Line 191*  

#### Function: `main`
> Main function to run the database analyzer.
*Line 196*  

### 📄 hypercode\fix_database_issues.py

#### Module: `fix_database_issues`
> Database Health Check and Fix Script
*Line 0*  

#### Class: `FixedCodeEntity`
> Enhanced version of CodeEntity with validation and better documentation.
*Line 19*  

#### Function: `from_dict`
> Create entity from raw database dict, preserving unknown fields.
*Line 47*  

#### Function: `__post_init__`
> Validate entity data after initialization.
*Line 70*  

#### Function: `_validate_required_fields`
> Ensure all required fields have values.
*Line 81*  

#### Function: `_validate_field_types`
> Check that all fields have the correct types.
*Line 88*  

#### Function: `_normalize_fields`
> Normalize field values.
*Line 101*  

#### Function: `_clean_docstring`
> Clean and standardize the docstring.
*Line 139*  

#### Function: `to_dict`
> Convert entity to dictionary for JSON serialization.
*Line 153*  

#### Class: `DatabaseFixer`
> Handles fixing and validating the Hypercode database.
*Line 171*  

#### Function: `__init__`
> Initialize with path to the database file.
*Line 174*  

#### Function: `load_database`
> Load and validate the database.
*Line 188*  

#### Function: `_check_for_issues`
> Check an entity for common issues.
*Line 225*  

#### Function: `fix_issues`
> Fix common issues in the database.
*Line 252*  

#### Function: `save_database`
> Save the fixed database to a file.
*Line 280*  

#### Function: `generate_report`
> Generate a report of issues and fixes.
*Line 306*  

#### Function: `main`
> Main function to run the database fixer.
*Line 347*  

### 📄 hypercode\hypercode\accessibility\adhd_optimizer.py

#### Module: `adhd_optimizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\hypercode\accessibility\autism_preset.py

#### Module: `autism_preset`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\hypercode\accessibility\dyslexia_formatter.py

#### Module: `dyslexia_formatter`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\hypercode\accessibility\sensory_customizer.py

#### Module: `sensory_customizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\hypercode\accessibility\wcag_auditor.py

#### Module: `wcag_auditor`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\hypercode\benchmarks\__init__.py

#### Function: `benchmark_lexer`
> Benchmark the lexer with the given source code.
*Line 13*  

#### Function: `print_benchmark_results`
> Print benchmark results in a readable format.
*Line 38*  

### 📄 hypercode\hypercode\benchmarks\benchmarks_lexer.py

#### Function: `benchmark_lexer`
> Benchmark the lexer with the given source code.
*Line 7*  

#### Function: `print_benchmark_results`
> Print benchmark results in a readable format.
*Line 32*  

### 📄 hypercode\hypercode\build-hyper-database.py

#### Module: `build-hyper-database`
> Hyper Database Builder - Scans HyperCode repo, builds knowledge graph.
*Line 0*  

#### Class: `HyperDatabaseBuilder`
> Scans codebase and builds semantic knowledge graph.
*Line 39*  

#### Function: `__init__`
> Initialize builder with repo root path.
*Line 42*  

#### Function: `scan_python_file`
> Extract functions, classes from Python file.
*Line 50*  

#### Function: `scan_javascript_file`
> Extract functions from JavaScript (regex-based).
*Line 96*  

#### Function: `should_skip_directory`
> Check if directory should be skipped.
*Line 125*  

#### Function: `build`
> Scan entire repo and build database.
*Line 145*  

#### Function: `generate_markdown_report`
> Generate HYPER_DATABASE.md report.
*Line 179*  

#### Function: `generate_json_report`
> Generate machine-readable HYPER_DATABASE.json.
*Line 266*  

#### Function: `main`
> Main entry point.
*Line 281*  

### 📄 hypercode\hypercode\knowledge_graph\graph_builder.py

#### Module: `graph_builder`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\hypercode\knowledge_graph\sparql_query.py

#### Module: `sparql_query`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\hypercode\knowledge_graph\update_agent.py

#### Module: `update_agent`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\hypercode\live_research\doc_generator.py

#### Module: `doc_generator`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\hypercode\live_research\github_publisher.py

#### Module: `github_publisher`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\hypercode\live_research\paper_indexer.py

#### Module: `paper_indexer`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\hypercode\live_research\research_crawler.py

#### Module: `research_crawler`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\hypercode\live_research\synthesis_engine.py

#### Module: `synthesis_engine`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\hypercode\mcp\__init__.py

#### Module: `__init__`
> HyperCode MCP (Model Context Protocol) Server Package
*Line 0*  

### 📄 hypercode\hypercode\mcp\servers\__init__.py

#### Module: `__init__`
> MCP Servers Package
*Line 0*  

### 📄 hypercode\hypercode\mcp\servers\aws_cli.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\hypercode\mcp\servers\aws_resource_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\hypercode\mcp\servers\code_analysis.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\hypercode\mcp\servers\dataset_downloader.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\hypercode\mcp\servers\file_system.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\hypercode\mcp\servers\human_input.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\hypercode\mcp\servers\hypercode_syntax.py

#### Module: `hypercode_syntax`
> HyperCode Syntax MCP Server
*Line 0*  

#### Class: `HyperCodeSyntaxServer`
> 🎨 MCP Server for HyperCode Visual Syntax Integration
*Line 28*  

#### Function: `__init__`
*Line 31*  

#### Function: `handle_request`
> Handle MCP requests from IDE
*Line 35*  

#### Function: `_initialize`
> Initialize the MCP server
*Line 56*  

#### Function: `_document_changed`
> Handle document changes for real-time parsing
*Line 79*  

#### Function: `_text_hover`
> Provide hover information for semantic annotations
*Line 98*  

#### Function: `_completion`
> Provide completion for semantic annotations
*Line 121*  

#### Function: `_parse_document`
> Parse entire document and return semantic structure
*Line 150*  

#### Function: `_validate_neurodiversity`
> Validate neurodiversity compliance and provide suggestions
*Line 179*  

#### Function: `_generate_diagnostics`
> Generate IDE diagnostics from parsed functions
*Line 216*  

#### Function: `_get_annotation_hover_info`
> Generate hover information for semantic annotations
*Line 266*  

#### Function: `main`
> Main MCP server loop
*Line 294*  

### 📄 hypercode\hypercode\mcp\servers\path_service.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\hypercode\mcp\servers\user_profile_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\hypercode\mcp\servers\valkey_service.py

#### Function: `check_redis_connection`
*Line 40*  

#### Function: `health_check`
> Health check endpoint to verify that the service is running.
*Line 59*  

#### Function: `set_key`
> Set a value for a given key. The value should be a JSON object.
*Line 67*  

#### Function: `get_key`
> Get the value for a given key.
*Line 80*  

#### Function: `hset_key`
> Set a field (key) in a hash (name). The value should be a JSON object.
*Line 95*  

#### Function: `hget_key`
> Get a field (key) from a hash (name).
*Line 107*  

#### Function: `hgetall_hash`
> Get all fields and values for a given hash name.
*Line 126*  

#### Function: `main`
> Main function to run the Valkey Service MCP Server.
*Line 144*  

### 📄 hypercode\hypercode\mcp\servers\web_search.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\hypercode\mcp\setup.py

#### Module: `setup`
> MCP Setup Script
*Line 0*  

#### Function: `install_dependencies`
> Install required dependencies
*Line 16*  

#### Function: `verify_setup`
> Verify that MCP is properly set up
*Line 31*  

#### Function: `show_next_steps`
> Show next steps for using MCP
*Line 54*  

#### Function: `main`
*Line 72*  

### 📄 hypercode\hypercode\mcp\start_servers.py

#### Module: `start_servers`
> MCP Servers Startup Script
*Line 0*  

#### Function: `start_server`
> Start a specific MCP server
*Line 34*  

#### Function: `list_servers`
> List all available servers
*Line 59*  

#### Function: `main`
*Line 66*  

### 📄 hypercode\hypercode\mcp\test_mcp.py

#### Module: `test_mcp`
> MCP Servers Test Script
*Line 0*  

#### Function: `test_server_imports`
> Test that all servers can be imported
*Line 15*  

#### Function: `main`
*Line 47*  

### 📄 hypercode\hypercode\new files to check\backend\research\__init__.py

#### Module: `__init__`
> Initialization for the research module.
*Line 0*  

### 📄 hypercode\hypercode\new files to check\backend\research\db.py

#### Module: `db`
> Database configuration for the HyperCode research module.
*Line 0*  

#### Function: `_get_database_url`
> Return the database URL to connect to.
*Line 35*  

### 📄 hypercode\hypercode\new files to check\backend\research\models.py

#### Module: `models`
> ORM models for the HyperCode research database.
*Line 0*  

#### Class: `Study`
> Top‑level research study.
*Line 32*  

#### Function: `__repr__`
*Line 52*  

#### Class: `Source`
> External or internal resource used in a study.
*Line 56*  

#### Function: `__repr__`
*Line 81*  

#### Class: `LanguageVersion`
> Version of the HyperCode language.
*Line 85*  

#### Function: `__repr__`
*Line 102*  

#### Class: `Task`
> A coding task or challenge used in experiments.
*Line 106*  

#### Function: `__repr__`
*Line 124*  

#### Class: `Participant`
> An anonymised participant in the study.
*Line 128*  

#### Function: `__repr__`
*Line 144*  

#### Class: `Session`
> A single coding session of a participant performing a task.
*Line 148*  

#### Function: `__repr__`
*Line 169*  

#### Class: `Event`
> Low‑level interaction within a session.
*Line 176*  

#### Function: `__repr__`
*Line 193*  

#### Class: `Feedback`
> Qualitative and quantitative feedback for a session.
*Line 199*  

#### Function: `__repr__`
*Line 221*  

### 📄 hypercode\hypercode\new files to check\backend\research\scripts\import_sources_from_folder.py

#### Module: `import_sources_from_folder`
> Import research sources from a folder into the database.
*Line 0*  

#### Function: `infer_kind`
*Line 25*  

#### Function: `main`
*Line 36*  

### 📄 hypercode\hypercode\new files to check\backend\research\scripts\seed_basic_data.py

#### Module: `seed_basic_data`
> Seed the research database with initial data.
*Line 0*  

#### Function: `main`
*Line 25*  

### 📄 hypercode\hypercode\run_lexer.py

#### Function: `run_lexer`
> Run the lexer on a source file and print the tokens.
*Line 13*  

### 📄 hypercode\hypercode\scripts\style_guide_collector.py

#### Module: `style_guide_collector`
> 🎨 HyperCode Style Guide Feedback Collector
*Line 0*  

#### Class: `StyleGuideCollector`
> 🎨 Collects and analyzes style guide feedback from the community
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `_load_feedback`
> 📂 Load existing feedback data
*Line 32*  

#### Function: `_save_feedback`
> 💾 Save feedback data
*Line 51*  

#### Function: `add_feedback`
> 📝 Add new feedback entry
*Line 60*  

#### Function: `_update_analysis`
> 📊 Update analysis based on new feedback
*Line 102*  

#### Function: `analyze_feedback`
> 📊 Generate comprehensive analysis of all feedback
*Line 151*  

#### Function: `_get_top_items`
> 📊 Get top items from a frequency dictionary
*Line 189*  

#### Function: `_calculate_consensus`
> 📊 Calculate consensus for preference categories
*Line 212*  

#### Function: `_generate_recommendations`
> 💡 Generate style guide recommendations based on feedback
*Line 247*  

#### Function: `import_github_issues`
> 📥 Import feedback from GitHub issues
*Line 331*  

#### Function: `generate_report`
> 📊 Generate comprehensive feedback report
*Line 354*  

#### Function: `interactive_feedback`
> 🎯 Interactive feedback collection from command line
*Line 419*  

#### Function: `main`
> 🚀 Main entry point
*Line 527*  

### 📄 hypercode\hypercode\scripts\test_perplexity_api.py

#### Module: `test_perplexity_api`
> Test script for Perplexity API integration.
*Line 0*  

#### Function: `main`
> Test the Perplexity API connection and make a sample query.
*Line 17*  

### 📄 hypercode\hypercode\src\ai_gateway\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\hypercode\src\ai_gateway\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\hypercode\src\ai_gateway\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\hypercode\src\ai_gateway\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\hypercode\src\ai_gateway\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\hypercode\src\ai_gateway\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\hypercode\src\ai_gateway\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\hypercode\src\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\hypercode\src\build.py

#### Module: `build`
> Build script for the HyperCode language.
*Line 0*  

#### Function: `build`
> Builds a HyperCode source file to the target language.
*Line 34*  

### 📄 hypercode\hypercode\src\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\hypercode\src\core\__init__.py

#### Module: `__init__`
> HyperCode Core Module
*Line 0*  

### 📄 hypercode\hypercode\src\core\ast.py

#### Class: `Node`
*Line 9*  

#### Function: `accept`
*Line 10*  

#### Class: `Expr`
*Line 20*  

#### Class: `Literal`
*Line 25*  

#### Class: `Variable`
*Line 30*  

#### Class: `Assign`
*Line 35*  

#### Class: `Binary`
*Line 41*  

#### Class: `Unary`
*Line 48*  

#### Class: `Grouping`
*Line 54*  

#### Class: `Call`
*Line 59*  

#### Class: `Get`
*Line 66*  

#### Class: `Stmt`
*Line 73*  

#### Class: `Expression`
*Line 78*  

#### Class: `Print`
*Line 83*  

#### Class: `Var`
*Line 88*  

#### Class: `Block`
*Line 94*  

#### Class: `Intent`
*Line 99*  

#### Class: `Function`
*Line 104*  

#### Class: `If`
*Line 111*  

#### Class: `Return`
*Line 118*  

#### Class: `Program`
*Line 125*  

### 📄 hypercode\hypercode\src\core\ast_nodes.py

#### Module: `ast_nodes`
> Abstract Syntax Tree (AST) nodes for the HyperCode language.
*Line 0*  

#### Class: `Node`
> Base class for all AST nodes.
*Line 24*  

#### Class: `Expression`
> Base class for all expression nodes.
*Line 31*  

#### Class: `Statement`
> Base class for all statement nodes.
*Line 38*  

#### Class: `Program`
> Represents the entire program as a list of statements.
*Line 45*  

#### Class: `Identifier`
> Represents an identifier (e.g., a variable name).
*Line 52*  

#### Class: `Literal`
> Represents a literal value (e.g., number, string).
*Line 59*  

#### Class: `VariableDeclaration`
> Represents a variable declaration (let or const).
*Line 66*  

#### Class: `BinaryOperation`
> Represents a binary operation (e.g., a + b).
*Line 75*  

### 📄 hypercode\hypercode\src\core\interpreter.py

#### Class: `RuntimeError`
*Line 8*  

#### Function: `__init__`
*Line 9*  

#### Class: `Environment`
*Line 15*  

#### Function: `__init__`
*Line 16*  

#### Function: `define`
*Line 20*  

#### Function: `get`
*Line 23*  

#### Function: `assign`
*Line 30*  

#### Class: `Callable`
*Line 40*  

#### Function: `arity`
*Line 41*  

#### Function: `call`
*Line 44*  

#### Class: `Function`
*Line 48*  

#### Function: `__init__`
*Line 49*  

#### Function: `call`
*Line 53*  

#### Function: `arity`
*Line 65*  

#### Class: `ReturnException`
*Line 69*  

#### Function: `__init__`
*Line 70*  

#### Class: `Interpreter`
*Line 74*  

#### Function: `__init__`
*Line 75*  

#### Class: `Clock`
*Line 82*  

#### Function: `arity`
*Line 83*  

#### Function: `call`
*Line 86*  

#### Function: `__str__`
*Line 89*  

#### Function: `execute_block`
*Line 94*  

#### Function: `interpret`
*Line 103*  

#### Function: `execute`
*Line 112*  

#### Function: `evaluate`
*Line 115*  

#### Function: `visit_Expression`
*Line 118*  

#### Function: `visit_Print`
*Line 122*  

#### Function: `visit_Var`
*Line 129*  

#### Function: `visit_Block`
*Line 136*  

#### Function: `visit_Expression`
*Line 140*  

#### Function: `visit_Print`
*Line 144*  

#### Function: `visit_Intent`
*Line 150*  

#### Function: `visit_Function`
*Line 155*  

#### Function: `visit_Return`
*Line 160*  

#### Function: `visit_Literal`
*Line 166*  

#### Function: `visit_Grouping`
*Line 169*  

#### Function: `visit_Variable`
*Line 172*  

#### Function: `visit_Assign`
*Line 175*  

#### Function: `visit_Call`
*Line 180*  

#### Function: `visit_Binary`
*Line 198*  

#### Function: `visit_Unary`
*Line 229*  

#### Function: `is_truthy`
*Line 237*  

#### Function: `stringify`
*Line 244*  

#### Function: `get_output`
*Line 256*  

### 📄 hypercode\hypercode\src\core\lexer.py

#### Module: `lexer`
> HyperCode Lexer Module
*Line 0*  

#### Class: `LexerError`
> Represents a lexical analysis error.
*Line 17*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode programming language.
*Line 34*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 42*  

#### Function: `scan_tokens`
> Scan the source code and return a list of tokens.
*Line 99*  

#### Function: `scan_token`
> Scan a single token.
*Line 109*  

#### Function: `number`
> Lex a number literal.
*Line 168*  

#### Function: `string`
> Lex a string literal.
*Line 203*  

#### Function: `docstring`
> Lex a docstring.
*Line 252*  

#### Function: `identifier`
> Lex an identifier or keyword.
*Line 278*  

#### Function: `error`
> Report a lexing error.
*Line 288*  

#### Function: `is_at_end`
> Check if we've reached the end of the source.
*Line 312*  

#### Function: `advance`
> Consume and return the next character.
*Line 316*  

#### Function: `match`
> Conditionally consume a character if it matches the expected value.
*Line 325*  

#### Function: `peek`
> Look at the next character without consuming it.
*Line 335*  

#### Function: `peek_next`
> Look at the character after the next one without consuming it.
*Line 341*  

#### Function: `add_token`
> Add a new token to the token list.
*Line 347*  

### 📄 hypercode\hypercode\src\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\hypercode\src\core\parser.py

#### Class: `ParseError`
*Line 7*  

#### Class: `Parser`
*Line 11*  

#### Function: `__init__`
*Line 12*  

#### Function: `parse`
> Parse the entire program.
*Line 16*  

#### Function: `declaration`
*Line 25*  

#### Function: `var_declaration`
*Line 36*  

#### Function: `statement`
*Line 61*  

#### Function: `print_statement`
*Line 72*  

#### Function: `expression_statement`
*Line 77*  

#### Function: `block`
*Line 82*  

#### Function: `expression`
*Line 91*  

#### Function: `assignment`
*Line 94*  

#### Function: `equality`
*Line 109*  

#### Function: `comparison`
*Line 119*  

#### Function: `term`
*Line 132*  

#### Function: `factor`
*Line 140*  

#### Function: `unary`
*Line 148*  

#### Function: `primary`
*Line 155*  

#### Function: `function`
*Line 177*  

#### Function: `if_statement`
*Line 200*  

#### Function: `return_statement`
*Line 212*  

#### Function: `match`
*Line 222*  

#### Function: `consume`
*Line 229*  

#### Function: `error`
*Line 239*  

#### Function: `synchronize`
*Line 245*  

#### Function: `check`
*Line 265*  

#### Function: `advance`
*Line 270*  

#### Function: `is_at_end`
*Line 275*  

#### Function: `peek`
*Line 278*  

#### Function: `previous`
*Line 281*  

### 📄 hypercode\hypercode\src\core\tokens.py

#### Module: `tokens`
> HyperCode Token Types and Definitions
*Line 0*  

#### Class: `TokenType`
*Line 11*  

#### Class: `Token`
> Represents a token in the HyperCode language.
*Line 71*  

#### Function: `__init__`
*Line 83*  

#### Function: `__str__`
*Line 92*  

#### Function: `__repr__`
*Line 95*  

### 📄 hypercode\hypercode\src\duelcode\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode\hypercode\src\duelcode\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode\hypercode\src\duelcode\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode\hypercode\src\duelcode\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode\hypercode\src\duelcode\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode\hypercode\src\duelcode\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode\hypercode\src\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode\hypercode\src\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode\hypercode\src\hypercode-backend-js-COMPLETE.py

#### Module: `hypercode-backend-js-COMPLETE`
> HyperCode JavaScript Backend - Complete Implementation
*Line 0*  

#### Class: `JSCompiler`
> Compiles HyperCode AST to JavaScript.
*Line 19*  

#### Function: `__init__`
> Initialize compiler.
*Line 30*  

#### Function: `compile`
> Compile AST to JavaScript.
*Line 42*  

#### Function: `_generate_header`
> Generate JavaScript header
*Line 65*  

#### Function: `_generate_setup`
> Generate setup code (memory tape, pointer, I/O)
*Line 74*  

#### Function: `_generate_main`
> Generate JavaScript for AST node.
*Line 110*  

#### Function: `_generate_footer`
> Generate JavaScript footer
*Line 162*  

#### Function: `_indent`
> Get current indentation
*Line 179*  

#### Function: `optimize_ast`
> Optimize AST (future: loop unrolling, dead code elimination).
*Line 183*  

#### Function: `main`
> CLI interface for JavaScript backend
*Line 200*  

### 📄 hypercode\hypercode\src\hypercode-idea-generator-WEB.py

#### Module: `hypercode-idea-generator-WEB`
> HyperCode Community Idea Generator - Web Interface (HTML/CSS/JS)
*Line 0*  

### 📄 hypercode\hypercode\src\hypercode-launch-kit.py

#### Module: `hypercode-launch-kit`
> HyperCode Launch Kit - Ultimate System Initialization
*Line 0*  

#### Class: `HyperCodeLaunchKit`
> Complete launch system initialization
*Line 23*  

#### Function: `__init__`
*Line 26*  

#### Function: `create_readme`
> Create the ultimate README.md
*Line 30*  

#### Function: `create_launch_checklist`
> Create launch day checklist
*Line 367*  

#### Function: `create_launch_script`
> Create automated launch script
*Line 620*  

#### Function: `create_first_30_days`
> Create 30-day success roadmap
*Line 718*  

#### Function: `print_summary`
> Print beautiful summary
*Line 974*  

#### Function: `main`
> Run launch kit initialization
*Line 1007*  

### 📄 hypercode\hypercode\src\hypercode-lexer-COMPLETE.py

#### Module: `hypercode-lexer-COMPLETE`
> HyperCode Lexer - Complete Implementation
*Line 0*  

#### Class: `TokenType`
> HyperCode token types - minimal yet powerful
*Line 21*  

#### Class: `Token`
> Represents a single token with position tracking
*Line 45*  

#### Function: `__repr__`
> Neurodivergent-friendly representation
*Line 54*  

#### Class: `LexerError`
> Lexer-specific errors with context
*Line 59*  

#### Function: `__init__`
*Line 62*  

#### Class: `HyperCodeLexer`
> Tokenizes HyperCode programs with accessibility features.
*Line 69*  

#### Function: `__init__`
> Initialize lexer with source code.
*Line 95*  

#### Function: `tokenize`
> Convert HyperCode source to token stream.
*Line 110*  

#### Function: `_advance_position`
> Update position tracking after processing character
*Line 169*  

#### Function: `_skip_comment`
> Skip characters until end of line
*Line 179*  

#### Function: `get_tokens`
> Return current token list
*Line 184*  

#### Function: `filter_tokens`
> Get tokens excluding certain types.
*Line 188*  

#### Function: `print_tokens`
> Print tokens in readable format.
*Line 205*  

#### Function: `get_statistics`
> Get token statistics (useful for analysis).
*Line 236*  

#### Function: `main`
> CLI interface for the lexer
*Line 250*  

### 📄 hypercode\hypercode\src\hypercode-parser-COMPLETE.py

#### Module: `hypercode-parser-COMPLETE`
> HyperCode Parser - Complete Implementation
*Line 0*  

#### Class: `NodeType`
> AST Node types
*Line 22*  

#### Class: `ASTNode`
> Abstract Syntax Tree Node.
*Line 38*  

#### Function: `__repr__`
> Pretty-print AST (neurodivergent-friendly)
*Line 51*  

#### Class: `ParserError`
> Parser-specific errors with context
*Line 68*  

#### Function: `__init__`
*Line 71*  

#### Class: `HyperCodeParser`
> Parses HyperCode token stream into AST.
*Line 80*  

#### Function: `__init__`
> Initialize parser with token stream.
*Line 94*  

#### Function: `parse`
> Parse tokens into AST.
*Line 105*  

#### Function: `_parse_statement`
> Parse a single statement
*Line 127*  

#### Function: `_parse_loop`
> Parse loop structure: [ statements ]
*Line 174*  

#### Function: `_advance`
> Move to next token
*Line 209*  

#### Function: `_is_at_end`
> Check if at end of token stream
*Line 215*  

#### Function: `validate`
> Validate AST structure.
*Line 222*  

#### Function: `print_ast`
> Print AST in readable format.
*Line 237*  

#### Function: `main`
> CLI interface for the parser
*Line 251*  

### 📄 hypercode\hypercode\src\hypercode\__init__.py

#### Module: `__init__`
> HyperCode - A neurodivergent-first programming language with AI compatibility.
*Line 0*  

### 📄 hypercode\hypercode\src\hypercode\__main__.py

#### Function: `main`
*Line 6*  

### 📄 hypercode\hypercode\src\hypercode\config.py

#### Module: `config`
> Configuration module for HyperCode.
*Line 0*  

#### Class: `Config`
> Configuration class for HyperCode
*Line 16*  

#### Function: `get_headers`
> Get headers for API requests
*Line 27*  

### 📄 hypercode\hypercode\src\hypercode\core\__init__.py

#### Module: `__init__`
> Core package for the HyperCode language implementation.
*Line 0*  

### 📄 hypercode\hypercode\src\hypercode\core\ast.py

#### Class: `Node`
*Line 9*  

#### Function: `accept`
*Line 10*  

#### Class: `Expr`
*Line 20*  

#### Class: `Literal`
*Line 25*  

#### Class: `Variable`
*Line 30*  

#### Class: `Assign`
*Line 35*  

#### Class: `Binary`
*Line 41*  

#### Class: `Unary`
*Line 48*  

#### Class: `Grouping`
*Line 54*  

#### Class: `Call`
*Line 59*  

#### Class: `ListLiteral`
*Line 66*  

#### Class: `PipeChain`
> A pipeline expression made of a head value and subsequent steps.
*Line 71*  

#### Class: `Get`
*Line 81*  

#### Class: `Stmt`
*Line 88*  

#### Class: `Expression`
*Line 93*  

#### Class: `Print`
*Line 98*  

#### Class: `Var`
*Line 103*  

#### Class: `Block`
*Line 109*  

#### Class: `If`
*Line 114*  

#### Class: `Fun`
*Line 121*  

#### Class: `Return`
*Line 128*  

#### Class: `Intent`
*Line 134*  

#### Class: `Program`
*Line 141*  

### 📄 hypercode\hypercode\src\hypercode\core\cli.py

#### Module: `cli`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\hypercode\src\hypercode\core\error_handler.py

#### Function: `report_parse_error`
*Line 4*  

#### Function: `report`
*Line 11*  

### 📄 hypercode\hypercode\src\hypercode\core\interpreter.py

#### Class: `Return`
*Line 7*  

#### Function: `__init__`
*Line 8*  

#### Class: `HyperCodeFunction`
*Line 12*  

#### Function: `__init__`
*Line 13*  

#### Function: `__str__`
*Line 17*  

#### Function: `arity`
*Line 20*  

#### Function: `call`
*Line 23*  

#### Class: `Environment`
*Line 36*  

#### Function: `__init__`
*Line 37*  

#### Function: `define`
*Line 41*  

#### Function: `get`
*Line 44*  

#### Function: `assign`
*Line 51*  

#### Class: `Interpreter`
*Line 61*  

#### Function: `__init__`
*Line 62*  

#### Function: `interpret`
*Line 75*  

#### Function: `execute`
*Line 82*  

#### Function: `execute_block`
*Line 85*  

#### Function: `evaluate`
*Line 94*  

#### Function: `visit_Expression`
*Line 97*  

#### Function: `visit_Print`
*Line 100*  

#### Function: `visit_Var`
*Line 104*  

#### Function: `visit_Block`
*Line 110*  

#### Function: `visit_Assign`
*Line 113*  

#### Function: `visit_Binary`
*Line 118*  

#### Function: `visit_Grouping`
*Line 161*  

#### Function: `visit_Literal`
*Line 164*  

#### Function: `visit_Unary`
*Line 167*  

#### Function: `visit_Variable`
*Line 180*  

#### Function: `visit_If`
*Line 183*  

#### Function: `is_truthy`
*Line 189*  

#### Function: `visit_Fun`
*Line 196*  

#### Function: `visit_Return`
*Line 200*  

#### Function: `visit_Call`
*Line 206*  

#### Function: `is_callable`
*Line 219*  

#### Function: `visit_ListLiteral`
*Line 223*  

#### Function: `visit_PipeChain`
*Line 226*  

#### Class: `BuiltinFunction`
*Line 247*  

#### Function: `__init__`
*Line 248*  

#### Function: `__str__`
*Line 252*  

#### Function: `arity`
*Line 255*  

#### Function: `call`
*Line 259*  

#### Class: `Visitor`
*Line 264*  

#### Function: `visit_Expression`
*Line 265*  

#### Function: `visit_Print`
*Line 268*  

#### Function: `visit_Var`
*Line 271*  

#### Function: `visit_Block`
*Line 274*  

#### Function: `visit_If`
*Line 277*  

#### Function: `visit_Fun`
*Line 280*  

#### Function: `visit_Return`
*Line 283*  

#### Function: `visit_Assign`
*Line 286*  

#### Function: `visit_Binary`
*Line 289*  

#### Function: `visit_Grouping`
*Line 292*  

#### Function: `visit_Literal`
*Line 295*  

#### Function: `visit_Unary`
*Line 298*  

#### Function: `visit_Variable`
*Line 301*  

#### Function: `visit_Call`
*Line 304*  

### 📄 hypercode\hypercode\src\hypercode\core\lexer.py

#### Module: `lexer`
> Core HyperCode language implementation - Lexer
*Line 0*  

#### Class: `LexerError`
> Exception raised for errors in the lexer.
*Line 32*  

#### Function: `__init__`
*Line 35*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode language.
*Line 42*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 111*  

#### Function: `tokenize`
> Convert source code into a list of tokens.
*Line 128*  

#### Function: `_match_patterns`
> Try to match the current position against all token patterns.
*Line 163*  

#### Function: `_update_position`
> Update line and column numbers based on the given text.
*Line 189*  

#### Function: `_add_token`
> Add a token to the token list.
*Line 208*  

#### Function: `_handle_unknown`
> Handle unknown characters in the source.
*Line 272*  

### 📄 hypercode\hypercode\src\hypercode\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\hypercode\src\hypercode\core\parser.py

#### Class: `ParseError`
*Line 7*  

#### Class: `Parser`
*Line 11*  

#### Function: `__init__`
*Line 12*  

#### Function: `parse`
> Parse the entire program.
*Line 16*  

#### Function: `declaration`
*Line 25*  

#### Function: `var_declaration`
*Line 36*  

#### Function: `statement`
*Line 52*  

#### Function: `print_statement`
*Line 65*  

#### Function: `return_statement`
*Line 70*  

#### Function: `intent_statement`
*Line 78*  

#### Function: `expression_statement`
*Line 93*  

#### Function: `if_statement`
*Line 98*  

#### Function: `function`
*Line 110*  

#### Function: `block`
*Line 129*  

#### Function: `expression`
*Line 136*  

#### Function: `pipe_expression`
*Line 140*  

#### Function: `assignment`
*Line 151*  

#### Function: `equality`
*Line 173*  

#### Function: `comparison`
*Line 183*  

#### Function: `term`
*Line 196*  

#### Function: `factor`
*Line 204*  

#### Function: `unary`
*Line 212*  

#### Function: `primary`
*Line 219*  

#### Function: `_primary`
*Line 236*  

#### Function: `finish_call`
*Line 276*  

#### Function: `match`
*Line 289*  

#### Function: `consume`
*Line 296*  

#### Function: `error`
*Line 303*  

#### Function: `synchronize`
*Line 309*  

#### Function: `check`
*Line 329*  

#### Function: `advance`
*Line 334*  

#### Function: `is_at_end`
*Line 339*  

#### Function: `peek`
*Line 342*  

#### Function: `previous`
*Line 345*  

### 📄 hypercode\hypercode\src\hypercode\core\semantic_analyzer.py

#### Module: `semantic_analyzer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\hypercode\src\hypercode\core\sensory_profile.py

#### Module: `sensory_profile`
> Sensory Profile System for HyperCode
*Line 0*  

#### Class: `VisualNoiseLevel`
*Line 15*  

#### Class: `AnimationSpeed`
*Line 22*  

#### Class: `VisualSettings`
> Configuration for visual aspects of the editor.
*Line 29*  

#### Class: `AudioSettings`
> Configuration for audio feedback.
*Line 43*  

#### Class: `AnimationSettings`
> Configuration for animations and transitions.
*Line 58*  

#### Class: `SensoryProfile`
> A complete sensory profile configuration.
*Line 68*  

#### Function: `to_dict`
> Convert the profile to a dictionary.
*Line 77*  

#### Function: `from_dict`
> Create a profile from a dictionary.
*Line 85*  

#### Function: `save`
> Save the profile to a file.
*Line 107*  

#### Function: `load`
> Load a profile from a file.
*Line 113*  

#### Class: `ProfileManager`
> Manages loading and saving of sensory profiles.
*Line 120*  

#### Function: `__init__`
> Initialize with optional custom profiles directory.
*Line 123*  

#### Function: `_ensure_default_profiles`
> Ensure default profiles exist.
*Line 133*  

#### Function: `_create_minimal_profile`
> Create a minimal distraction-free profile.
*Line 146*  

#### Function: `_create_enhanced_profile`
> Create an enhanced profile with helpful visual cues.
*Line 163*  

#### Function: `_create_high_contrast_profile`
> Create a high-contrast profile for better readability.
*Line 190*  

#### Function: `list_profiles`
> List all available profile names.
*Line 216*  

#### Function: `get_profile`
> Get a profile by name.
*Line 220*  

#### Function: `save_profile`
> Save a profile.
*Line 227*  

#### Function: `delete_profile`
> Delete a profile by name.
*Line 232*  

#### Function: `get_profile`
> Helper function to get a profile by name.
*Line 243*  

#### Function: `list_profiles`
> Helper function to list all available profiles.
*Line 248*  

### 📄 hypercode\hypercode\src\hypercode\core\tokens.py

#### Class: `TokenType`
*Line 6*  

#### Class: `Token`
*Line 65*  

#### Function: `__str__`
*Line 72*  

### 📄 hypercode\hypercode\src\hypercode\enhanced_perplexity_client.py

#### Module: `enhanced_perplexity_client`
> Enhanced Perplexity Client with Knowledge Base Integration
*Line 0*  

#### Class: `EnhancedPerplexityClient`
> Enhanced Perplexity client with knowledge base integration
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `query_with_context`
> Send a query with relevant knowledge base context
*Line 25*  

#### Function: `add_research_data`
> Add research data to the knowledge base
*Line 61*  

#### Function: `search_research_data`
> Search the knowledge base
*Line 71*  

#### Function: `list_research_documents`
> List all research documents
*Line 75*  

#### Function: `get_document`
> Get a specific document
*Line 79*  

#### Function: `delete_document`
> Delete a document
*Line 83*  

#### Function: `import_from_perplexity_space`
> Import data from Perplexity Space export
*Line 87*  

#### Function: `test_context_integration`
> Test the context integration
*Line 123*  

#### Function: `create_perplexity_space_import_template`
> Create a template for importing Perplexity Space data
*Line 175*  

### 📄 hypercode\hypercode\src\hypercode\knowledge_base.py

#### Module: `knowledge_base`
> HyperCode Knowledge Base - Perplexity Space Integration
*Line 0*  

#### Class: `ResearchDocument`
> Represents a research document from Perplexity Space
*Line 17*  

#### Function: `__post_init__`
*Line 28*  

#### Function: `generate_id`
> Generate unique ID from content hash
*Line 36*  

#### Function: `validate`
> Validate document data
*Line 41*  

#### Function: `update_timestamp`
> Update the last_updated timestamp
*Line 53*  

#### Class: `HyperCodeKnowledgeBase`
> Knowledge base for HyperCode research data
*Line 100*  

#### Function: `__init__`
*Line 103*  

#### Function: `load`
> Load knowledge base from file
*Line 109*  

#### Function: `save`
> Save knowledge base to file
*Line 125*  

#### Function: `add_document`
> Add a new research document
*Line 135*  

#### Function: `search_documents`
> Search documents by query
*Line 163*  

#### Function: `get_context_for_query`
> Get relevant context for a query
*Line 227*  

#### Function: `list_documents`
> List all documents
*Line 257*  

#### Function: `get_document`
> Get a specific document by ID
*Line 261*  

#### Function: `delete_document`
> Delete a document
*Line 265*  

#### Function: `update_document`
> Update an existing document
*Line 273*  

#### Function: `search_by_tags`
> Search documents by tags with AND/OR operators
*Line 287*  

#### Function: `get_document_statistics`
> Get statistics about the knowledge base
*Line 306*  

#### Function: `export_format`
> Export knowledge base in different formats
*Line 331*  

#### Function: `validate_all_documents`
> Validate all documents and return list of errors
*Line 353*  

#### Function: `cleanup_duplicates`
> Remove duplicate documents based on content hash
*Line 363*  

#### Function: `initialize_sample_data`
> Initialize with sample HyperCode research data
*Line 384*  

### 📄 hypercode\hypercode\src\hypercode\perplexity_client.py

#### Module: `perplexity_client`
> Perplexity AI API client for HyperCode.
*Line 0*  

#### Class: `PerplexityClient`
> Client for interacting with Perplexity AI API
*Line 12*  

#### Function: `__init__`
> Initialize the Perplexity client.
*Line 15*  

#### Function: `query`
> Send a query to the Perplexity API.
*Line 30*  

#### Function: `test_connection`
> Test the connection to the Perplexity API
*Line 72*  

### 📄 hypercode\hypercode\src\hypercode\repl.py

#### Function: `run_repl`
*Line 12*  

#### Function: `run`
*Line 33*  

#### Function: `show_help`
*Line 54*  

### 📄 hypercode\hypercode\src\hypercode\std\__init__.py

#### Module: `__init__`
> Standard library for HyperCode (v0.1).
*Line 0*  

### 📄 hypercode\hypercode\src\hypercode\std\builtins.py

#### Module: `builtins`
> HyperCode v0.1 standard built-in functions.
*Line 0*  

#### Function: `echo`
> Return the input unchanged.
*Line 12*  

#### Function: `to_string`
> Convert value to string.
*Line 17*  

#### Function: `length`
> Length of a sequence or mapping; 0 if None.
*Line 22*  

#### Function: `sum_items`
> Sum over an iterable of numbers; returns x if not iterable.
*Line 32*  

#### Function: `add`
> Add two values (numbers or strings/lists supporting +).
*Line 42*  

#### Function: `multiply`
> Multiply numbers or repeat sequences (e.g., "a" * 3).
*Line 47*  

#### Function: `to_list`
> Convert value to list; strings become list of chars; None -> [].
*Line 52*  

#### Function: `upper`
> Uppercase string representation of x.
*Line 66*  

#### Function: `head`
> First element of sequence or None if empty/invalid.
*Line 71*  

#### Function: `tail`
> All but the first element of sequence or [].
*Line 79*  

#### Function: `get_builtins`
> Return mapping of built-in names to callables.
*Line 87*  

### 📄 hypercode\hypercode\src\hypercode_idea_generator.py

#### Module: `hypercode_idea_generator`
> HyperCode Idea Generator - AI-Powered Community Input System
*Line 0*  

#### Class: `HyperCodeIdeaGenerator`
> AI-Powered Idea Generator for HyperCode community input.
*Line 431*  

#### Function: `__init__`
*Line 439*  

#### Function: `get_ideas_by_category`
> Get ideas by category and optionally by difficulty level.
*Line 443*  

#### Function: `get_top_ideas`
> Get most-voted ideas across all categories.
*Line 468*  

#### Function: `vote_for_idea`
> Vote for an idea.
*Line 487*  

#### Function: `get_trending_ideas`
> Get trending ideas (high votes + recent activity).
*Line 497*  

#### Function: `format_idea_card`
> Format idea for display.
*Line 502*  

#### Function: `main`
> Interactive idea generator CLI
*Line 528*  

### 📄 hypercode\hypercode\src\hypercode_poc.py

#### Module: `hypercode_poc`
> HyperCode POC - Neurodivergent-First Programming Language
*Line 0*  

#### Class: `TokenType`
> Brainfuck-inspired core + modern aliases
*Line 18*  

#### Class: `Token`
*Line 34*  

#### Class: `UserConfidenceLevel`
*Line 41*  

#### Class: `EnhancedLexer`
> Smart tokenizer with escape handling + accessibility focus
*Line 48*  

#### Function: `__init__`
*Line 51*  

#### Function: `tokenize`
*Line 74*  

#### Function: `handle_string`
*Line 115*  

#### Function: `handle_number`
*Line 141*  

#### Function: `handle_identifier`
*Line 149*  

#### Function: `advance`
*Line 171*  

#### Class: `ContextAwareErrorMessenger`
> Friendly, adaptive error messages
*Line 176*  

#### Function: `__init__`
*Line 179*  

#### Function: `format_error`
*Line 182*  

#### Class: `SemanticContextStreamer`
> Understand programmer intent from tokens
*Line 189*  

#### Function: `analyze`
*Line 192*  

#### Class: `ConfidenceTracker`
> Adapt system guidance to user skill level
*Line 209*  

#### Function: `__init__`
*Line 212*  

#### Function: `record`
*Line 216*  

#### Class: `HyperCodePOC`
> Main system: Lexer + Error Messenger + Semantic Analyzer + Confidence Tracker
*Line 222*  

#### Function: `__init__`
*Line 225*  

#### Function: `compile`
*Line 232*  

### 📄 hypercode\hypercode\src\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\hypercode\src\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\hypercode\src\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\hypercode\src\parser\debug_ascii.py

#### Module: `debug_ascii`
> ASCII-only debug
*Line 0*  

#### Function: `test_regex_patterns`
> Test regex patterns directly
*Line 14*  

### 📄 hypercode\hypercode\src\parser\debug_full.py

#### Module: `debug_full`
> Debug the full parsing flow
*Line 0*  

#### Function: `debug_full_parsing`
> Debug the full parsing flow
*Line 14*  

### 📄 hypercode\hypercode\src\parser\debug_parser.py

#### Module: `debug_parser`
> Debug the Visual Syntax Parser - Find what's wrong with annotation detection
*Line 0*  

#### Function: `debug_annotation_detection`
> Debug why annotations aren't being detected
*Line 14*  

### 📄 hypercode\hypercode\src\parser\debug_simple.py

#### Module: `debug_simple`
> Simple debug without emoji characters
*Line 0*  

#### Function: `debug_simple`
> Debug without emoji characters
*Line 14*  

### 📄 hypercode\hypercode\src\parser\test_parser.py

#### Module: `test_parser`
> Test the Visual Syntax Parser - First Click Moment Demo
*Line 0*  

#### Function: `test_first_click_moment`
> Test the parser with the first click moment example
*Line 14*  

### 📄 hypercode\hypercode\src\parser\visual_syntax_parser.py

#### Module: `visual_syntax_parser`
> 🎨 Visual Syntax Parser for HyperCode V3
*Line 0*  

#### Class: `SemanticMarker`
> 🎨 Semantic marker types with emoji representations
*Line 18*  

#### Class: `SemanticAnnotation`
> 📋 A single semantic annotation with its metadata
*Line 37*  

#### Function: `__str__`
*Line 46*  

#### Class: `ParsedFunction`
> 🔍 A fully parsed HyperCode function
*Line 51*  

#### Function: `get_annotations_by_type`
> Get all annotations of a specific type
*Line 62*  

#### Class: `VisualSyntaxParser`
> 🎨 Main parser for HyperCode's visual semantic syntax
*Line 69*  

#### Function: `__init__`
*Line 72*  

#### Function: `_build_semantic_patterns`
> 🔍 Build regex patterns for all semantic markers
*Line 76*  

#### Function: `_build_color_scheme`
> 🎨 Build semantic color mapping for IDE highlighting
*Line 105*  

#### Function: `parse_file`
> 📄 Parse an entire HyperCode file
*Line 123*  

#### Function: `parse_content`
> 📝 Parse HyperCode content string
*Line 130*  

#### Function: `_is_function_definition`
> 🔍 Check if line is a function definition
*Line 170*  

#### Function: `_start_new_function`
> 🆕 Create new ParsedFunction from definition line
*Line 179*  

#### Function: `_parse_line_annotations`
> � Parse semantic annotations from a line
*Line 202*  

#### Function: `_parse_annotation_params`
> 🔧 Parse annotation parameters from string
*Line 223*  

#### Function: `generate_syntax_highlighting`
> 🎨 Generate HTML with syntax highlighting for visual markers
*Line 265*  

#### Function: `extract_semantic_summary`
> 📊 Extract semantic summary for analysis
*Line 277*  

#### Function: `validate_neurodiversity_compliance`
> 🧠 Validate neurodiversity-first design principles
*Line 311*  

### 📄 hypercode\hypercode\src\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\hypercode\src\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\hypercode\src\scaffold (1).py

#### Module: `scaffold (1)`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 141*  

#### Function: `create_python_files`
> Create all Python files with proper __init__.py structure.
*Line 151*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 165*  

#### Function: `create_root_files`
> Create root-level configuration files as empty placeholders.
*Line 202*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 213*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 234*  

#### Function: `main`
> Main scaffolding function.
*Line 259*  

### 📄 hypercode\hypercode\src\scaffold.py

#### Module: `scaffold`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 153*  

#### Function: `create_python_files`
> Create all Python files with proper docstrings and structure.
*Line 184*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 254*  

#### Function: `create_root_files`
> Create root-level configuration files with appropriate content.
*Line 291*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 541*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 583*  

#### Function: `main`
> Main scaffolding function.
*Line 621*  

### 📄 hypercode\hypercode\src\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode\hypercode\src\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode\hypercode\src\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode\hypercode\src\utils\code_analyzer_ai.py

#### Module: `code_analyzer_ai`
> Perplexity AI Code Analyzer for HyperCode
*Line 0*  

#### Class: `CodeAnalyzerAI`
> AI-powered code analyzer for HyperCode
*Line 19*  

#### Function: `__init__`
*Line 22*  

#### Function: `analyze_file`
> Analyze a Python file with AI assistance
*Line 25*  

#### Function: `_analyze_complexity`
> Analyze code complexity indicators
*Line 72*  

#### Function: `_check_docstrings`
> Check for docstring coverage
*Line 113*  

#### Function: `_get_ai_code_analysis`
> Get AI analysis of code from Perplexity
*Line 155*  

#### Function: `analyze_project`
> Analyze entire project
*Line 183*  

#### Function: `_get_project_ai_insights`
> Get AI insights for the entire project
*Line 230*  

#### Function: `save_analysis`
> Save analysis to file
*Line 262*  

#### Function: `print_summary`
> Print analysis summary
*Line 270*  

#### Function: `main`
> Main function
*Line 288*  

### 📄 hypercode\hypercode\src\utils\debug_search.py

#### Module: `debug_search`
> Debug search results
*Line 0*  

#### Function: `debug_search`
> Debug why space data isn't being found
*Line 15*  

### 📄 hypercode\hypercode\src\utils\demo_ai_research.py

#### Module: `demo_ai_research`
> HyperCode AI Research + Perplexity Integration Demo
*Line 0*  

#### Function: `demo_ai_research_queries`
> Demonstrate AI Research integration with Perplexity
*Line 16*  

#### Function: `test_document_specific_queries`
> Test queries specific to the HyperCode AI Research document
*Line 90*  

### 📄 hypercode\hypercode\src\utils\demo_enhanced_client.py

#### Module: `demo_enhanced_client`
> Demo: Enhanced Perplexity Client with Knowledge Base
*Line 0*  

#### Function: `demo_knowledge_base_integration`
> Demonstrate the knowledge base integration
*Line 16*  

#### Function: `demonstrate_memory_persistence`
> Demonstrate that the knowledge base persists between sessions
*Line 131*  

### 📄 hypercode\hypercode\src\utils\final_integration_test.py

#### Module: `final_integration_test`
> Final Test: Complete Perplexity Space Integration
*Line 0*  

#### Function: `final_integration_test`
> Complete test of the Perplexity Space integration
*Line 15*  

### 📄 hypercode\hypercode\src\utils\health_scanner_ai.py

#### Module: `health_scanner_ai`
> HyperCode Health Scanner with Perplexity AI Integration
*Line 0*  

#### Class: `HealthScannerAI`
> AI-powered health scanner for HyperCode project
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `analyze_project_structure`
> Analyze project structure and identify health issues
*Line 25*  

#### Function: `analyze_dependencies`
> Analyze dependency management
*Line 68*  

#### Function: `analyze_security`
> Analyze security configuration
*Line 110*  

#### Function: `get_ai_recommendations`
> Get AI-powered recommendations based on health scan
*Line 143*  

#### Function: `run_full_scan`
> Run complete health scan with AI analysis
*Line 170*  

#### Function: `save_report`
> Save health scan report to file
*Line 221*  

#### Function: `print_summary`
> Print a summary of the health scan
*Line 227*  

#### Function: `main`
> Main function to run the health scanner
*Line 247*  

### 📄 hypercode\hypercode\src\utils\import-helper.py

#### Module: `import-helper`
> HyperCode Perplexity Space Import Helper
*Line 0*  

#### Class: `SpaceImportHelper`
> Helper class for managing Perplexity Space imports
*Line 13*  

#### Function: `__init__`
*Line 16*  

#### Function: `validate_document`
> Validate a document structure
*Line 21*  

#### Function: `load_template`
> Load documents from JSON template file
*Line 63*  

#### Function: `validate_all`
> Validate all loaded documents
*Line 83*  

#### Function: `generate_report`
> Generate a validation report
*Line 95*  

#### Function: `create_import_script`
> Generate a Python script to import the data
*Line 141*  

#### Function: `create_template_instructions`
> Generate detailed instructions for filling the template
*Line 193*  

#### Function: `main`
> CLI interface for the import helper
*Line 264*  

### 📄 hypercode\hypercode\src\utils\import_all_space_data.py

#### Module: `import_all_space_data`
> Complete Import of HyperCode Space Data
*Line 0*  

#### Function: `format_content`
> Recursively format nested data into readable text
*Line 16*  

#### Function: `import_all_hypercode_data`
> Import all sections of your HyperCode Space data
*Line 41*  

### 📄 hypercode\hypercode\src\utils\import_hypercode_data.py

#### Module: `import_hypercode_data`
> Import HyperCode Space Data
*Line 0*  

#### Function: `import_hypercode_space_data`
> Import your actual HyperCode Space data
*Line 16*  

### 📄 hypercode\hypercode\src\utils\import_perplexity_space.py

#### Module: `import_perplexity_space`
> Perplexity Space Data Importer
*Line 0*  

#### Function: `create_manual_import_script`
> Create a script for manual data entry from Perplexity Space
*Line 17*  

#### Function: `create_json_import_template`
> Create a JSON template for importing data
*Line 86*  

#### Function: `import_from_json`
> Import data from JSON file
*Line 115*  

#### Function: `test_imported_data`
> Test the imported data with context-aware queries
*Line 153*  

#### Function: `show_import_menu`
> Show the import menu
*Line 188*  

### 📄 hypercode\hypercode\src\utils\local_health_scanner.py

#### Module: `local_health_scanner`
> Local Project Health Scanner for HyperCode
*Line 0*  

#### Class: `ProjectScanner`
> Scans the project for health metrics without external dependencies
*Line 20*  

#### Function: `__init__`
*Line 23*  

#### Function: `scan_project`
> Scan the entire project and return health metrics
*Line 35*  

#### Function: `_scan_directory`
> Recursively scan a directory for Python files
*Line 43*  

#### Function: `_analyze_file`
> Analyze a single Python file
*Line 52*  

#### Function: `_analyze_ast`
> Analyze Python AST for code quality metrics
*Line 77*  

#### Function: `_check_documentation`
> Check documentation coverage
*Line 97*  

#### Function: `_check_tests`
> Check test coverage
*Line 109*  

#### Function: `_calculate_metrics`
> Calculate final metrics
*Line 120*  

#### Function: `print_health_report`
> Print a formatted health report
*Line 132*  

#### Function: `main`
> Main function to run the health scanner
*Line 163*  

### 📄 hypercode\hypercode\src\utils\perplexity_space_collector.py

#### Module: `perplexity_space_collector`
> Perplexity Space Data Collector
*Line 0*  

#### Function: `quick_copy_paste_collector`
> Quick collector for copy-paste workflow
*Line 18*  

#### Function: `create_structured_template`
> Create a structured JSON template for bulk import
*Line 117*  

#### Function: `show_bro_hacks`
> Show BROski's pro tips
*Line 167*  

#### Function: `main_menu`
> Main menu for the collector
*Line 207*  

### 📄 hypercode\hypercode\src\utils\perplexity_space_integration.py

#### Module: `perplexity_space_integration`
> Perplexity Space Integration Guide
*Line 0*  

#### Function: `main`
*Line 16*  

### 📄 hypercode\hypercode\src\utils\run_lexer.py

#### Function: `run_lexer`
> Run the lexer on a source file and print the tokens.
*Line 13*  

### 📄 hypercode\hypercode\src\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode\hypercode\test_mcp_connection.py

#### Function: `check_port`
> Check if a port is open on the given host.
*Line 26*  

#### Function: `find_running_servers`
> Scan common ports to find running servers.
*Line 36*  

#### Function: `test_server_connection`
> Test connection to a single MCP server.
*Line 49*  

#### Function: `test_all_servers`
> Test connection to all MCP servers and print results.
*Line 90*  

#### Function: `check_dependencies`
> Check if required dependencies are installed.
*Line 139*  

### 📄 hypercode\hypercode\tests\benchmark_knowledge_base.py

#### Module: `benchmark_knowledge_base`
> Performance Benchmark Tool for HyperCode Knowledge Base
*Line 0*  

#### Class: `BenchmarkSuite`
> Comprehensive benchmark suite for Knowledge Base
*Line 24*  

#### Function: `__init__`
*Line 27*  

#### Function: `_get_system_info`
> Get system information for benchmark context
*Line 34*  

#### Function: `generate_test_data`
> Generate test data of specified size
*Line 43*  

#### Function: `benchmark_operation`
> Benchmark a single operation
*Line 93*  

#### Function: `run_benchmark_suite`
> Run complete benchmark suite
*Line 118*  

#### Function: `_calculate_summary`
> Calculate summary statistics
*Line 274*  

#### Function: `_generate_recommendations`
> Generate performance recommendations
*Line 296*  

#### Function: `generate_markdown_report`
> Generate beautiful markdown report
*Line 338*  

#### Function: `save_json_results`
> Save results as JSON
*Line 467*  

#### Function: `main`
> Main benchmark runner
*Line 474*  

### 📄 hypercode\hypercode\tests\test_accessibility.py

#### Module: `test_accessibility`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\hypercode\tests\test_ai_gateway.py

#### Module: `test_ai_gateway`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\hypercode\tests\test_backends.py

#### Module: `test_backends`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\hypercode\tests\test_core.py

#### Module: `test_core`
> Test harness for core HyperCode components.
*Line 0*  

#### Function: `run_test`
> Test the lexer, parser, and interpreter with the given source code.
*Line 30*  

### 📄 hypercode\hypercode\tests\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode\hypercode\tests\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode\hypercode\tests\test_integration.py

#### Module: `test_integration`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\hypercode\tests\test_intent_blocks.py

#### Module: `test_intent_blocks`
> Test script for Intent Blocks implementation
*Line 0*  

#### Function: `test_intent_block`
> Test parsing of intent blocks
*Line 13*  

### 📄 hypercode\hypercode\tests\test_interpreter.py

#### Function: `run_code`
> A helper function to run code and capture stdout.
*Line 10*  

#### Class: `TestInterpreter`
*Line 28*  

#### Function: `test_if_statement_then`
*Line 30*  

#### Function: `test_if_statement_else`
*Line 42*  

#### Function: `test_function_call`
*Line 54*  

#### Function: `test_function_with_parameters`
*Line 64*  

#### Function: `test_function_with_return`
*Line 74*  

#### Function: `test_recursive_function_call`
*Line 85*  

#### Function: `test_scoping`
*Line 99*  

### 📄 hypercode\hypercode\tests\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Comprehensive test suite for knowledge base search functionality.
*Line 0*  

#### Class: `TestKnowledgeBaseSearch`
> Test suite for knowledge base search functionality.
*Line 12*  

#### Function: `sample_documents`
> Create sample documents for testing.
*Line 16*  

#### Function: `knowledge_base`
> Create a knowledge base instance with sample documents.
*Line 40*  

#### Function: `test_basic_search`
> Test basic search functionality.
*Line 48*  

#### Function: `test_search_with_exact_match`
> Test search with exact phrase matching.
*Line 54*  

#### Function: `test_search_case_insensitive`
> Test that search is case-insensitive.
*Line 59*  

#### Function: `test_search_empty_query`
> Test search with empty query returns all or no documents.
*Line 65*  

#### Function: `test_search_no_matches`
> Test search with no matching documents.
*Line 71*  

#### Function: `test_search_ranking`
> Test that search results are ranked by relevance.
*Line 77*  

#### Function: `test_query_normalization`
> Test query normalization (typos, spacing, punctuation).
*Line 90*  

#### Function: `test_multi_word_query`
> Test search with multiple keywords.
*Line 98*  

#### Function: `test_tag_based_search`
> Test search that includes tag matching.
*Line 103*  

#### Class: `TestEdgeCases`
> Test edge cases and boundary conditions.
*Line 112*  

#### Function: `knowledge_base`
*Line 116*  

#### Function: `test_very_short_query`
> Test search with very short query (1-2 chars).
*Line 121*  

#### Function: `test_very_long_query`
> Test search with very long query (paragraph length).
*Line 126*  

#### Function: `test_special_characters_in_query`
> Test search with special characters.
*Line 136*  

#### Function: `test_unicode_in_query`
> Test search with unicode characters.
*Line 141*  

#### Function: `test_sql_injection_attempt`
> Test that search is safe from SQL injection-style attacks.
*Line 146*  

#### Function: `test_repeated_queries`
> Test that repeated queries return consistent results.
*Line 151*  

#### Class: `TestPerformance`
> Performance benchmarking tests.
*Line 159*  

#### Function: `large_knowledge_base`
> Create a knowledge base with many documents.
*Line 163*  

#### Function: `test_search_response_time`
> Test that search completes within acceptable time.
*Line 179*  

#### Function: `test_concurrent_searches`
> Test multiple concurrent search operations.
*Line 189*  

#### Function: `test_memory_usage`
> Test memory usage during search operations.
*Line 207*  

#### Class: `TestIntegrationWithPerplexity`
> Test integration with EnhancedPerplexityClient.
*Line 213*  

#### Function: `mock_perplexity_client`
> Create a mock Perplexity client.
*Line 217*  

#### Function: `mock_knowledge_base`
> Create a mock knowledge base.
*Line 229*  

#### Function: `test_enhanced_query_with_context`
> Test that queries are enhanced with knowledge base context.
*Line 243*  

#### Function: `test_fallback_to_perplexity_api`
> Test fallback to Perplexity API when no local context found.
*Line 259*  

#### Function: `test_context_ranking_and_selection`
> Test that best context is selected for query enhancement.
*Line 273*  

#### Class: `TestDocumentManagement`
> Test document addition, update, and removal.
*Line 288*  

#### Function: `knowledge_base`
*Line 292*  

#### Function: `test_add_document`
> Test adding a new document to knowledge base.
*Line 300*  

#### Function: `test_update_document`
> Test updating an existing document.
*Line 310*  

#### Function: `test_remove_document`
> Test removing a document.
*Line 315*  

### 📄 hypercode\hypercode\tests\test_knowledge_base_comprehensive.py

#### Module: `test_knowledge_base_comprehensive`
> Comprehensive Test Suite for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestKnowledgeBaseUnit`
> Unit tests for Knowledge Base functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_docs`
> Sample documents for testing
*Line 36*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 59*  

#### Function: `test_add_single_document`
> Test adding a single document
*Line 65*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 74*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 84*  

#### Function: `test_search_exact_match`
> Test exact search matching
*Line 102*  

#### Function: `test_search_partial_match`
> Test partial search matching
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 124*  

#### Function: `test_search_case_insensitive`
> Test case insensitive search
*Line 135*  

#### Function: `test_empty_search`
> Test empty search query
*Line 147*  

#### Function: `test_nonexistent_search`
> Test search for nonexistent terms
*Line 155*  

#### Function: `test_get_context_for_query`
> Test context extraction
*Line 165*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 176*  

#### Function: `test_document_update`
> Test updating existing documents
*Line 186*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 202*  

#### Function: `test_delete_document`
> Test document deletion
*Line 213*  

#### Class: `TestKnowledgeBaseIntegration`
> Integration tests for Knowledge Base
*Line 229*  

#### Function: `populated_kb`
> Create a populated knowledge base for integration testing
*Line 233*  

#### Function: `test_complex_search_queries`
> Test complex search scenarios
*Line 277*  

#### Function: `test_search_ranking_quality`
> Test that search results are properly ranked
*Line 291*  

#### Function: `test_related_term_expansion`
> Test that related terms are properly expanded
*Line 301*  

#### Function: `test_performance_with_large_dataset`
> Test performance with larger dataset
*Line 313*  

#### Function: `test_concurrent_access_simulation`
> Test simulated concurrent access
*Line 332*  

#### Class: `TestKnowledgeBasePerformance`
> Performance tests for Knowledge Base
*Line 356*  

#### Function: `large_kb`
> Create a large knowledge base for performance testing
*Line 360*  

#### Function: `test_search_performance_large_dataset`
> Test search performance with large dataset
*Line 382*  

#### Function: `test_save_performance_large_dataset`
> Test save performance with large dataset
*Line 396*  

#### Function: `test_load_performance_large_dataset`
> Test load performance with large dataset
*Line 409*  

#### Function: `test_memory_usage_large_dataset`
> Test memory usage with large dataset
*Line 423*  

#### Class: `TestKnowledgeBaseEdgeCases`
> Edge case tests for Knowledge Base
*Line 446*  

#### Function: `edge_case_kb`
> Create knowledge base for edge case testing
*Line 450*  

#### Function: `test_empty_title_handling`
> Test handling of documents with empty titles
*Line 494*  

#### Function: `test_special_characters_handling`
> Test handling of special characters and unicode
*Line 499*  

#### Function: `test_very_long_titles`
> Test handling of very long titles
*Line 507*  

#### Function: `test_empty_content_handling`
> Test handling of documents with empty content
*Line 512*  

#### Function: `test_none_tags_handling`
> Test handling of None tags
*Line 517*  

#### Function: `test_malformed_json_handling`
> Test handling of malformed JSON files
*Line 531*  

#### Function: `test_file_permission_handling`
> Test handling of file permission issues
*Line 544*  

### 📄 hypercode\hypercode\tests\test_lexer.py

#### Function: `test_lexer_basic_tokens`
*Line 5*  

#### Function: `test_lexer_strings`
*Line 23*  

#### Function: `test_lexer_operators`
*Line 48*  

### 📄 hypercode\hypercode\tests\test_lexer_extended.py

#### Function: `test_lexer_escaped_strings`
> Test handling of strings with escaped characters.
*Line 5*  

#### Function: `test_lexer_numbers`
> Test various number formats.
*Line 18*  

#### Function: `test_lexer_operators`
> Test all operators.
*Line 39*  

#### Function: `test_lexer_comments`
> Test handling of single-line and multi-line comments.
*Line 86*  

#### Function: `test_lexer_whitespace`
> Test handling of various whitespace characters.
*Line 115*  

#### Function: `test_lexer_error_handling`
> Test error handling for invalid tokens.
*Line 130*  

#### Function: `test_lexer_hex_numbers`
> Test hexadecimal number literals.
*Line 139*  

#### Function: `test_lexer_binary_numbers`
> Test binary number literals.
*Line 157*  

#### Function: `test_lexer_scientific_notation`
> Test scientific notation numbers.
*Line 169*  

#### Function: `test_lexer_string_escapes`
> Test string escape sequences.
*Line 180*  

#### Function: `test_lexer_keywords`
> Test all language keywords.
*Line 197*  

#### Function: `test_lexer_position_tracking`
> Test that line and column numbers are tracked correctly.
*Line 223*  

#### Function: `test_lexer_error_recovery`
> Test that the lexer raises errors on invalid characters.
*Line 243*  

#### Function: `test_lexer_error_messages`
> Test that lexer error messages are informative.
*Line 252*  

### 📄 hypercode\hypercode\tests\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode\hypercode\tests\test_parser.py

#### Function: `test_parse_literal`
*Line 12*  

#### Function: `test_parse_variable_declaration`
*Line 24*  

#### Function: `test_parse_binary_expression`
*Line 37*  

### 📄 hypercode\hypercode\tests\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode\hypercode\tests\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 185*  

### 📄 hypercode\hypercode\tests\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode\hypercode\tests\test_sensory_profiles.py

#### Module: `test_sensory_profiles`
> Tests for the sensory profile system.
*Line 0*  

#### Function: `test_visual_settings_creation`
> Test creating visual settings.
*Line 21*  

#### Function: `test_audio_settings_creation`
> Test creating audio settings.
*Line 35*  

#### Function: `test_animation_settings_creation`
> Test creating animation settings.
*Line 44*  

#### Function: `test_sensory_profile_creation`
> Test creating a complete sensory profile.
*Line 55*  

#### Function: `test_profile_serialization`
> Test serializing AND deserializing a profile.
*Line 71*  

#### Function: `test_profile_file_io`
> Test saving and loading a profile to/from a file.
*Line 92*  

#### Function: `test_profile_manager_initialization`
> Test initializing the profile manager and checking default profiles.
*Line 115*  

#### Function: `test_profile_manager_get_profile`
> Test getting a profile by name.
*Line 129*  

#### Function: `test_profile_manager_save_custom_profile`
> Test saving a custom profile.
*Line 142*  

#### Function: `test_profile_manager_delete_profile`
> Test deleting a profile.
*Line 169*  

### 📄 hypercode\hypercode\tests\tests\test_lexer_enhanced.py

#### Function: `test_lexer_edge_cases`
*Line 7*  

#### Function: `test_lexer_error_handling`
*Line 28*  

#### Function: `test_lexer_number_literals`
*Line 43*  

#### Function: `test_lexer_string_interpolation`
*Line 65*  

#### Function: `test_lexer_docstrings`
*Line 79*  

### 📄 hypercode\hypercode\tests\unit\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode\hypercode\tests\unit\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode\hypercode\tests\unit\test_intent_blocks.py

#### Module: `test_intent_blocks`
> Test script for Intent Blocks implementation
*Line 0*  

#### Function: `test_intent_block`
> Test parsing of intent blocks
*Line 13*  

### 📄 hypercode\hypercode\tests\unit\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Phase 1 Unit Tests for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestHyperCodeKnowledgeBase`
> Test suite for HyperCodeKnowledgeBase core functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_documents`
> Sample documents for testing
*Line 33*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 56*  

#### Function: `test_add_document`
> Test adding a single document
*Line 61*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 82*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 92*  

#### Function: `test_search_exact_match`
> Test exact term matching in search
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 126*  

#### Function: `test_search_related_terms`
> Test related term expansion
*Line 139*  

#### Function: `test_search_space_data_boost`
> Test that space data gets boosted in search
*Line 153*  

#### Function: `test_get_context_for_query`
> Test context extraction for queries
*Line 180*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 192*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 203*  

#### Function: `test_empty_search`
> Test search with empty query
*Line 216*  

#### Function: `test_search_nonexistent_term`
> Test search for term that doesn't exist
*Line 221*  

#### Function: `test_document_update`
> Test updating existing document
*Line 231*  

#### Class: `TestResearchDocument`
> Test suite for ResearchDocument dataclass
*Line 250*  

#### Function: `test_document_creation`
> Test creating a research document
*Line 253*  

#### Function: `test_document_optional_fields`
> Test document with optional fields
*Line 273*  

### 📄 hypercode\hypercode\tests\unit\test_lexer.py

#### Module: `test_lexer`
> Test script for the HyperCode lexer.
*Line 0*  

#### Function: `test_lexer`
> Test the lexer with the given source code and print the results.
*Line 12*  

#### Function: `run_tests`
> Run a series of test cases for the lexer.
*Line 42*  

### 📄 hypercode\hypercode\tests\unit\test_mcp_connection.py

#### Function: `check_port`
> Check if a port is open on the given host.
*Line 26*  

#### Function: `find_running_servers`
> Scan common ports to find running servers.
*Line 36*  

#### Function: `test_server_connection`
> Test connection to a single MCP server.
*Line 49*  

#### Function: `test_all_servers`
> Test connection to all MCP servers and print results.
*Line 90*  

#### Function: `check_dependencies`
> Check if required dependencies are installed.
*Line 139*  

### 📄 hypercode\hypercode\tests\unit\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode\hypercode\tests\unit\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode\hypercode\tests\unit\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 185*  

### 📄 hypercode\hypercode\tests\unit\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode\hypercode\tests\unit\test_search_algorithm.py

#### Module: `test_search_algorithm`
> Phase 1 Unit Tests for Search Algorithm
*Line 0*  

#### Class: `TestSearchAlgorithm`
> Test suite for search algorithm functionality
*Line 20*  

#### Function: `populated_kb`
> Create a knowledge base with test documents
*Line 24*  

#### Function: `test_exact_title_match_highest_score`
> Test that exact title matches get highest priority
*Line 80*  

#### Function: `test_space_data_boosting`
> Test that space data gets boosted in search results
*Line 92*  

#### Function: `test_related_term_expansion`
> Test related term matching functionality
*Line 105*  

#### Function: `test_tag_matching_scoring`
> Test that tag matches contribute to scoring
*Line 126*  

#### Function: `test_content_frequency_scoring`
> Test that multiple content occurrences increase score
*Line 136*  

#### Function: `test_partial_word_matching`
> Test partial word matching for longer terms
*Line 149*  

#### Function: `test_query_word_ordering`
> Test that query words are properly processed
*Line 167*  

#### Function: `test_case_insensitive_search`
> Test that search is case insensitive
*Line 179*  

#### Function: `test_empty_query_returns_no_results`
> Test that empty queries return no results
*Line 202*  

#### Function: `test_limit_parameter_respected`
> Test that search limit parameter works correctly
*Line 210*  

#### Function: `test_no_results_for_nonexistent_terms`
> Test search for terms that don't exist
*Line 219*  

#### Function: `test_special_characters_in_query`
> Test search with special characters
*Line 227*  

#### Function: `test_unicode_characters`
> Test search with unicode characters
*Line 237*  

#### Function: `test_search_performance_with_large_kb`
> Test search performance with larger knowledge base
*Line 256*  

#### Function: `test_search_result_consistency`
> Test that search results are consistent across multiple calls
*Line 277*  

#### Class: `TestSearchScoringDetails`
> Test detailed scoring algorithm behavior
*Line 292*  

#### Function: `scoring_kb`
> Create KB for detailed scoring tests
*Line 296*  

#### Function: `test_title_match_beats_content_match`
> Test that title matches score higher than content matches
*Line 324*  

#### Function: `test_space_data_boosting_works`
> Test that space data gets boosted
*Line 332*  

#### Function: `test_frequency_scoring`
> Test that content frequency affects scoring
*Line 340*  

### 📄 hypercode\hypercode_db.py

#### Module: `hypercode_db`
> Hypercode Database - In-memory database for querying Hypercode project data.
*Line 0*  

#### Class: `CodeEntity`
> Represents a code entity (class, function, etc.) in the database.
*Line 12*  

#### Function: `__post_init__`
> Validate the entity after initialization.
*Line 25*  

#### Class: `HypercodeDB`
> In-memory database for Hypercode project analysis.
*Line 30*  

#### Function: `__init__`
> Initialize the database with the given JSON file.
*Line 37*  

#### Function: `_load_database`
> Load the database from a JSON file.
*Line 48*  

#### Function: `get_entities_by_type`
> Get all entities of a specific type.
*Line 96*  

#### Function: `get_entities_in_file`
> Get all entities in a specific file.
*Line 107*  

#### Function: `search_entities`
> Search for entities by name, file, or docstring.
*Line 118*  

#### Function: `print_analysis`
> Print a detailed analysis of the codebase.
*Line 150*  

### 📄 hypercode\knowledge_graph\graph_builder.py

#### Module: `graph_builder`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\knowledge_graph\sparql_query.py

#### Module: `sparql_query`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\knowledge_graph\update_agent.py

#### Module: `update_agent`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\live_research\cli.py

#### Function: `print_entry`
> Print a research entry in a readable format.
*Line 10*  

#### Function: `search_entries`
> Search for research entries.
*Line 38*  

#### Function: `view_entry`
> View a specific research entry by ID.
*Line 59*  

#### Function: `add_entry`
> Add a new research entry.
*Line 71*  

#### Function: `import_entries`
> Import entries from a JSON file.
*Line 94*  

#### Function: `export_entries`
> Export all entries to a JSON file.
*Line 126*  

#### Function: `main`
> Main CLI entry point.
*Line 150*  

### 📄 hypercode\live_research\database.py

#### Class: `ResearchDatabase`
*Line 7*  

#### Function: `__init__`
> Initialize the database connection and create tables if they don't exist.
*Line 8*  

#### Function: `_get_connection`
> Create and return a database connection.
*Line 13*  

#### Function: `_create_tables`
> Create the necessary tables if they don't exist.
*Line 17*  

#### Function: `add_research_entry`
> Add a new research entry to the database.
*Line 68*  

#### Function: `get_research_entry`
> Retrieve a research entry by its ID.
*Line 128*  

#### Function: `search_entries`
> Search research entries by content or tags.
*Line 159*  

#### Function: `import_from_json`
> Import research entries from a JSON file.
*Line 220*  

#### Function: `setup_database`
> Initialize and return a configured ResearchDatabase instance.
*Line 241*  

### 📄 hypercode\live_research\doc_generator.py

#### Module: `doc_generator`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\live_research\github_publisher.py

#### Module: `github_publisher`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\live_research\import_research.py

#### Module: `import_research`
> Script to import all JSON research files into the database.
*Line 0*  

#### Function: `import_research_data`
> Import all JSON research files into the database.
*Line 18*  

### 📄 hypercode\live_research\paper_indexer.py

#### Module: `paper_indexer`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\live_research\research_crawler.py

#### Module: `research_crawler`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\live_research\synthesis_engine.py

#### Module: `synthesis_engine`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\live_research\web\app.py

#### Module: `app`
> Flask web application for browsing research data.
*Line 0*  

#### Function: `get_db_connection`
> Create and return a database connection.
*Line 35*  

#### Function: `index`
> Home page showing recent research entries.
*Line 43*  

#### Function: `view_entry`
> View a specific research entry.
*Line 79*  

#### Function: `search`
> Search for research entries.
*Line 121*  

#### Function: `list_tags`
> List all tags with counts.
*Line 194*  

#### Function: `api_entries`
> API endpoint to get all entries in JSON format.
*Line 219*  

#### Function: `page_not_found`
> Handle 404 errors.
*Line 246*  

#### Function: `server_error`
> Handle 500 errors.
*Line 252*  

#### Function: `format_date_filter`
> Format a date string.
*Line 258*  

### 📄 hypercode\live_research\web\run.py

#### Module: `run`
> Run the research web application.
*Line 0*  

### 📄 hypercode\mcp\__init__.py

#### Module: `__init__`
> HyperCode MCP (Model Context Protocol) Server Package
*Line 0*  

### 📄 hypercode\mcp\servers\__init__.py

#### Module: `__init__`
> MCP Servers Package
*Line 0*  

### 📄 hypercode\mcp\servers\aws_cli.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\mcp\servers\aws_resource_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\mcp\servers\code_analysis.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\mcp\servers\dataset_downloader.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\mcp\servers\file_system.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\mcp\servers\human_input.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\mcp\servers\hypercode_syntax.py

#### Module: `hypercode_syntax`
> HyperCode Syntax MCP Server
*Line 0*  

#### Class: `HyperCodeSyntaxServer`
> 🎨 MCP Server for HyperCode Visual Syntax Integration
*Line 28*  

#### Function: `__init__`
*Line 31*  

#### Function: `handle_request`
> Handle MCP requests from IDE
*Line 35*  

#### Function: `_initialize`
> Initialize the MCP server
*Line 56*  

#### Function: `_document_changed`
> Handle document changes for real-time parsing
*Line 79*  

#### Function: `_text_hover`
> Provide hover information for semantic annotations
*Line 98*  

#### Function: `_completion`
> Provide completion for semantic annotations
*Line 121*  

#### Function: `_parse_document`
> Parse entire document and return semantic structure
*Line 150*  

#### Function: `_validate_neurodiversity`
> Validate neurodiversity compliance and provide suggestions
*Line 179*  

#### Function: `_generate_diagnostics`
> Generate IDE diagnostics from parsed functions
*Line 216*  

#### Function: `_get_annotation_hover_info`
> Generate hover information for semantic annotations
*Line 266*  

#### Function: `main`
> Main MCP server loop
*Line 294*  

### 📄 hypercode\mcp\servers\path_service.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\mcp\servers\user_profile_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\mcp\servers\valkey_service.py

#### Function: `check_redis_connection`
*Line 37*  

#### Function: `health_check`
> Health check endpoint to verify that the service is running.
*Line 50*  

#### Function: `set_key`
> Set a value for a given key. The value should be a JSON object.
*Line 57*  

#### Function: `get_key`
> Get the value for a given key.
*Line 69*  

#### Function: `hset_key`
> Set a field (key) in a hash (name). The value should be a JSON object.
*Line 83*  

#### Function: `hget_key`
> Get a field (key) from a hash (name).
*Line 94*  

#### Function: `hgetall_hash`
> Get all fields and values for a given hash name.
*Line 107*  

#### Function: `main`
> Main function to run the Valkey Service MCP Server.
*Line 124*  

### 📄 hypercode\mcp\servers\web_search.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\mcp\setup.py

#### Module: `setup`
> MCP Setup Script
*Line 0*  

#### Function: `install_dependencies`
> Install required dependencies
*Line 15*  

#### Function: `verify_setup`
> Verify that MCP is properly set up
*Line 27*  

#### Function: `show_next_steps`
> Show next steps for using MCP
*Line 45*  

#### Function: `main`
*Line 62*  

### 📄 hypercode\mcp\start_servers.py

#### Module: `start_servers`
> MCP Servers Startup Script
*Line 0*  

#### Function: `start_server`
> Start a specific MCP server
*Line 33*  

#### Function: `list_servers`
> List all available servers
*Line 55*  

#### Function: `main`
*Line 61*  

### 📄 hypercode\mcp\test_mcp.py

#### Module: `test_mcp`
> MCP Servers Test Script
*Line 0*  

#### Function: `test_server_imports`
> Test that all servers can be imported
*Line 14*  

#### Function: `main`
*Line 48*  

### 📄 hypercode\scripts\build-hyper-database.py

#### Module: `build-hyper-database`
> Hyper Database Builder - Scans HyperCode repo, builds knowledge graph.
*Line 0*  

#### Class: `HyperDatabaseBuilder`
> Scans codebase and builds semantic knowledge graph.
*Line 21*  

#### Function: `__init__`
> Initialize builder with repo root path.
*Line 24*  

#### Function: `scan_python_file`
> Extract functions, classes from Python file.
*Line 32*  

#### Function: `scan_javascript_file`
> Extract functions from JavaScript (regex-based).
*Line 78*  

#### Function: `should_skip_directory`
> Check if directory should be skipped.
*Line 107*  

#### Function: `build`
> Scan entire repo and build database.
*Line 131*  

#### Function: `generate_markdown_report`
> Generate HYPER_DATABASE.md report.
*Line 165*  

#### Function: `generate_json_report`
> Generate machine-readable HYPER_DATABASE.json.
*Line 254*  

#### Function: `main`
> Main entry point with proper encoding handling.
*Line 269*  

### 📄 hypercode\scripts\build_knowledge_base.py

#### Module: `build_knowledge_base`
> HyperCode Knowledge Base Builder
*Line 0*  

#### Class: `KnowledgeBaseBuilder`
> Build a knowledge base from the HyperCode repository.
*Line 35*  

#### Function: `__init__`
> Initialize the knowledge base builder.
*Line 38*  

#### Function: `should_skip`
> Check if a path should be skipped during processing.
*Line 79*  

#### Function: `get_file_type`
> Get the file type category.
*Line 162*  

#### Function: `process_file`
> Process a single file and return its metadata.
*Line 244*  

#### Function: `build_index`
> Build the knowledge base index.
*Line 287*  

#### Function: `main`
> Main entry point for the script.
*Line 376*  

### 📄 hypercode\scripts\database_utils\__init__.py

#### Module: `__init__`
> Database utilities for HyperCode.
*Line 0*  

### 📄 hypercode\scripts\database_utils\cli.py

#### Module: `cli`
> CLI interface for HyperCode database utilities.
*Line 0*  

#### Function: `get_database_path`
> Get the path to the HyperCode database.
*Line 13*  

#### Function: `load_database`
> Load the HyperCode database.
*Line 30*  

#### Function: `cmd_stats`
> Show database statistics.
*Line 46*  

#### Function: `cmd_search`
> Search the database.
*Line 74*  

#### Function: `cmd_info`
> Show database information.
*Line 116*  

#### Function: `main`
> Main CLI entry point.
*Line 144*  

### 📄 hypercode\scripts\database_utils\db.py

#### Module: `db`
> Database configuration and connection management for HyperCode research system.
*Line 0*  

#### Function: `init_database`
> Initialize the database with all tables.
*Line 40*  

#### Function: `get_db_context`
> Context manager for database sessions.
*Line 52*  

#### Function: `get_session`
> Get a database session.
*Line 66*  

#### Function: `check_database_health`
> Check database connectivity and health.
*Line 71*  

#### Function: `reset_database`
> Reset the database by dropping all tables and recreating them.
*Line 90*  

#### Function: `get_database_stats`
> Get basic database statistics.
*Line 102*  

### 📄 hypercode\scripts\database_utils\models.py

#### Module: `models`
> Database models for the HyperCode research system.
*Line 0*  

#### Class: `ResearchAgent`
> Represents a specialized research agent in the system.
*Line 17*  

#### Function: `__repr__`
*Line 33*  

#### Class: `ResearchTask`
> Represents a research task to be executed by agents.
*Line 37*  

#### Function: `__repr__`
*Line 71*  

#### Class: `ResearchPaper`
> Represents a research paper or document.
*Line 75*  

#### Function: `__repr__`
*Line 102*  

#### Class: `KnowledgeNode`
> Represents a node in the knowledge graph (entity).
*Line 110*  

#### Function: `__repr__`
*Line 141*  

#### Class: `KnowledgeRelationship`
> Represents a relationship between knowledge nodes.
*Line 145*  

#### Function: `__repr__`
*Line 173*  

#### Class: `ConflictRecord`
> Records conflicts detected during knowledge integration.
*Line 177*  

#### Function: `__repr__`
*Line 208*  

### 📄 hypercode\scripts\document_processor.py

#### Module: `document_processor`
> Document processing utilities for HyperCode knowledge base.
*Line 0*  

#### Class: `DocumentProcessor`
> Process various document types and extract content.
*Line 15*  

#### Function: `get_file_hash`
> Generate a hash for file content.
*Line 19*  

#### Function: `extract_metadata`
> Extract basic metadata from any file.
*Line 29*  

#### Function: `extract_pdf_content`
> Extract text content from PDF files.
*Line 43*  

#### Function: `extract_markdown_content`
> Extract content from Markdown files with frontmatter support.
*Line 74*  

#### Function: `extract_docx_content`
> Extract text content from DOCX files.
*Line 99*  

#### Function: `extract_csv_content`
> Extract content from CSV files.
*Line 133*  

#### Function: `extract_text_content`
> Extract content from plain text files.
*Line 154*  

#### Function: `process_document`
> Process a document based on its file type.
*Line 167*  

### 📄 hypercode\scripts\enhanced_database_builder.py

#### Module: `enhanced_database_builder`
> Enhanced HyperCode Database Builder
*Line 0*  

#### Class: `Entity`
> Represents a code entity (function, class, etc.) in the database.
*Line 35*  

#### Class: `EnhancedHyperDatabaseBuilder`
> Enhanced scanner for building a comprehensive code knowledge graph.
*Line 51*  

#### Function: `__init__`
> Initialize the enhanced database builder.
*Line 66*  

#### Function: `_setup_output_dir`
> Create output directory if it doesn't exist.
*Line 82*  

#### Function: `should_skip_directory`
> Check if a directory should be skipped during scanning.
*Line 86*  

#### Function: `scan_python_file`
> Extract entities from a Python file with enhanced parsing.
*Line 100*  

#### Function: `_calculate_complexity`
> Calculate code complexity of a function or method.
*Line 163*  

#### Function: `build`
> Build the complete database by scanning the repository.
*Line 185*  

#### Function: `_generate_reports`
> Generate all database reports.
*Line 207*  

#### Function: `_generate_markdown_report`
> Generate a detailed markdown report.
*Line 221*  

#### Function: `_generate_json_report`
> Generate a machine-readable JSON report.
*Line 251*  

#### Function: `_generate_metrics_report`
> Generate a metrics report with statistics and recommendations.
*Line 272*  

#### Function: `_generate_health_snapshot`
> Generate health snapshot markdown.
*Line 309*  

#### Function: `_generate_project_structure`
> Generate project structure overview.
*Line 326*  

#### Function: `_generate_doc_coverage`
> Generate documentation coverage report.
*Line 342*  

#### Function: `_generate_entities_list`
> Generate a list of all entities grouped by file.
*Line 374*  

#### Function: `_generate_recommendations`
> Generate actionable recommendations based on metrics.
*Line 393*  

#### Function: `main`
> Main entry point for the enhanced database builder.
*Line 443*  

### 📄 hypercode\scripts\extract-manifests.py

#### Module: `extract-manifests`
> Extract HC Manifests - Read YAML/JSON front-matter from .hc files, validate,
*Line 0*  

#### Class: `ManifestEntry`
*Line 51*  

#### Function: `load_schema`
*Line 57*  

#### Function: `iter_hc_files`
*Line 62*  

#### Function: `parse_front_matter`
> Parse front-matter between leading --- fences.
*Line 87*  

#### Function: `validate_manifest`
*Line 121*  

#### Function: `collect_manifests`
*Line 133*  

#### Function: `update_database`
*Line 150*  

#### Function: `write_report`
*Line 183*  

#### Function: `main`
*Line 198*  

### 📄 hypercode\scripts\generate_directory_readmes.py

#### Module: `generate_directory_readmes`
> Generate README.md files for documentation directories.
*Line 0*  

#### Function: `create_readme`
> Create or update a README.md file with the given content.
*Line 9*  

#### Function: `main`
*Line 20*  

### 📄 hypercode\scripts\hc-manifest-lint.py

#### Module: `hc-manifest-lint`
> HC Manifest Linter (v0)
*Line 0*  

#### Function: `iter_hc_files`
*Line 47*  

#### Function: `parse_front_matter`
*Line 71*  

#### Function: `validate_schema`
*Line 95*  

#### Function: `apply_rules`
*Line 108*  

#### Function: `main`
*Line 137*  

### 📄 hypercode\scripts\organize_docs.py

#### Module: `organize_docs`
> Documentation Organization Script for HyperCode
*Line 0*  

#### Function: `setup_directories`
> Create the new documentation directory structure.
*Line 131*  

#### Function: `move_files`
> Move files to their new locations based on the mapping.
*Line 138*  

#### Function: `generate_report`
> Generate a migration report.
*Line 172*  

#### Function: `main`
*Line 204*  

### 📄 hypercode\scripts\reorganize_repo.py

#### Module: `reorganize_repo`
> Reorganize the HyperCode repository structure to be more maintainable.
*Line 0*  

#### Function: `create_directories`
> Create the new directory structure.
*Line 29*  

#### Function: `move_files`
> Move files to their new locations.
*Line 37*  

#### Function: `update_gitignore`
> Update .gitignore with new paths.
*Line 71*  

#### Function: `main`
*Line 83*  

### 📄 hypercode\scripts\run_lexer.py

#### Module: `run_lexer`
> Test suite for HyperCode lexer.
*Line 0*  

#### Class: `TestLexer`
> Test suite for the HyperCode lexer.
*Line 18*  

#### Function: `setUp`
> Create a fresh lexer instance for each test.
*Line 21*  

#### Function: `test_empty_source`
> Test that an empty source returns only an EOF token.
*Line 25*  

#### Function: `test_basic_tokens`
> Test basic token types are correctly identified.
*Line 31*  

#### Function: `test_string_literals`
> Test string literals with various contents.
*Line 44*  

#### Function: `test_numbers`
> Test different number formats.
*Line 58*  

#### Function: `test_arithmetic_expressions`
> Test complex arithmetic expressions.
*Line 83*  

#### Function: `test_comments`
> Test different types of comments are properly ignored.
*Line 107*  

#### Function: `test_error_handling`
> Test that the lexer properly handles and reports errors.
*Line 121*  

#### Function: `test_error_recovery`
> Test that the lexer can recover from invalid tokens and continue parsing.
*Line 153*  

#### Function: `_assert_token_types`
> Helper to assert token types match expected types.
*Line 179*  

#### Function: `test_lexer_error_class`
> Test that LexerError is properly defined and can be instantiated.
*Line 201*  

### 📄 hypercode\scripts\run_tests.py

#### Module: `run_tests`
> HyperCode Test Runner
*Line 0*  

#### Function: `run_tests`
> Run pytest with the given arguments and coverage reporting.
*Line 16*  

#### Function: `main`
> Parse command line arguments and run tests.
*Line 49*  

### 📄 hypercode\scripts\style_guide_collector.py

#### Module: `style_guide_collector`
> 🎨 HyperCode Style Guide Feedback Collector
*Line 0*  

#### Class: `StyleGuideCollector`
> 🎨 Collects and analyzes style guide feedback from the community
*Line 17*  

#### Function: `__init__`
*Line 20*  

#### Function: `_load_feedback`
> 📂 Load existing feedback data
*Line 31*  

#### Function: `_save_feedback`
> 💾 Save feedback data
*Line 50*  

#### Function: `add_feedback`
> 📝 Add new feedback entry
*Line 59*  

#### Function: `_update_analysis`
> 📊 Update analysis based on new feedback
*Line 101*  

#### Function: `analyze_feedback`
> 📊 Generate comprehensive analysis of all feedback
*Line 150*  

#### Function: `_get_top_items`
> 📊 Get top items from a frequency dictionary
*Line 176*  

#### Function: `_calculate_consensus`
> 📊 Calculate consensus for preference categories
*Line 201*  

#### Function: `_generate_recommendations`
> 💡 Generate style guide recommendations based on feedback
*Line 230*  

#### Function: `import_github_issues`
> 📥 Import feedback from GitHub issues
*Line 288*  

#### Function: `generate_report`
> 📊 Generate comprehensive feedback report
*Line 309*  

#### Function: `interactive_feedback`
> 🎯 Interactive feedback collection from command line
*Line 370*  

#### Function: `main`
> 🚀 Main entry point
*Line 469*  

### 📄 hypercode\scripts\sync-space-to-main.py

#### Module: `sync-space-to-main`
> HyperCode Space-to-Main Sync Script
*Line 0*  

#### Function: `log_error`
> Error-level log with traceback.
*Line 25*  

#### Class: `Colors`
*Line 37*  

#### Function: `log_info`
> Info-level log.
*Line 46*  

#### Function: `log_success`
> Success-level log.
*Line 51*  

#### Function: `log_warning`
> Warning-level log.
*Line 56*  

#### Function: `deep_merge`
> Recursively merge source dict into destination dict.
*Line 61*  

#### Function: `load_config`
> Load sync configuration from TOML file.
*Line 72*  

#### Function: `should_skip_file`
> Check if file should be skipped based on filters.
*Line 112*  

#### Function: `get_all_files`
> Recursively get all files in directory.
*Line 135*  

#### Function: `copy_file`
> Copy file with directory creation. Returns True if copied/would copy.
*Line 145*  

#### Function: `remove_file`
> Remove file. Returns True if removed/would remove.
*Line 157*  

#### Function: `sync_folder`
> Sync source folder to target folder (one-way).
*Line 168*  

#### Function: `delete_orphans`
> Remove files from target that no longer exist in source.
*Line 212*  

#### Function: `sync_all_mappings`
> Execute all mappings from config.
*Line 229*  

#### Function: `write_log`
> Write sync results to log file.
*Line 281*  

#### Function: `print_summary`
> Print sync summary to console.
*Line 303*  

#### Function: `main`
*Line 327*  

### 📄 hypercode\scripts\test_mcp_connection.py

#### Function: `check_port`
> Check if a port is open on the given host.
*Line 25*  

#### Function: `find_running_servers`
> Scan common ports to find running servers.
*Line 34*  

#### Function: `test_server_connection`
> Test connection to a single MCP server.
*Line 46*  

#### Function: `test_all_servers`
> Test connection to all MCP servers and print results.
*Line 82*  

#### Function: `check_dependencies`
> Check if required dependencies are installed.
*Line 124*  

### 📄 hypercode\scripts\test_perplexity_api.py

#### Module: `test_perplexity_api`
> Test script for Perplexity API integration.
*Line 0*  

#### Function: `main`
> Test the Perplexity API connection and make a sample query.
*Line 17*  

### 📄 hypercode\scripts\update_doc_links.py

#### Module: `update_doc_links`
> Update internal documentation links after reorganization.
*Line 0*  

#### Function: `update_links_in_file`
> Update links in a single file.
*Line 27*  

#### Function: `replace_link`
*Line 39*  

#### Function: `main`
*Line 63*  

### 📄 hypercode\scripts\web_interface.py

#### Function: `load_index`
*Line 18*  

#### Function: `search_documents`
*Line 24*  

#### Function: `index`
*Line 58*  

#### Function: `search`
*Line 63*  

#### Function: `get_document`
*Line 71*  

#### Function: `serve_static`
*Line 80*  

#### Function: `create_template_if_not_exists`
> Create the template directory and index.html if they don't exist
*Line 84*  

### 📄 hypercode\src\hypercode\DuelCode\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode\src\hypercode\DuelCode\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode\src\hypercode\DuelCode\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode\src\hypercode\DuelCode\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode\src\hypercode\DuelCode\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode\src\hypercode\DuelCode\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode\src\hypercode\accessibility\adhd_optimizer.py

#### Module: `adhd_optimizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\src\hypercode\accessibility\autism_preset.py

#### Module: `autism_preset`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\src\hypercode\accessibility\dyslexia_formatter.py

#### Module: `dyslexia_formatter`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\src\hypercode\accessibility\sensory_customizer.py

#### Module: `sensory_customizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\src\hypercode\accessibility\wcag_auditor.py

#### Module: `wcag_auditor`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode\src\hypercode\ai_gateway\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\src\hypercode\ai_gateway\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\src\hypercode\ai_gateway\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\src\hypercode\ai_gateway\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\src\hypercode\ai_gateway\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode\src\hypercode\ai_gateway\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\src\hypercode\ai_gateway\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode\src\hypercode\code_analyzer_ai.py

#### Module: `code_analyzer_ai`
> Perplexity AI Code Analyzer for HyperCode
*Line 0*  

#### Class: `CodeAnalyzerAI`
> AI-powered code analyzer for HyperCode
*Line 20*  

#### Function: `__init__`
*Line 23*  

#### Function: `analyze_file`
> Analyze a Python file with AI assistance
*Line 26*  

#### Function: `_analyze_complexity`
> Analyze code complexity indicators
*Line 62*  

#### Function: `_check_docstrings`
> Check for docstring coverage
*Line 99*  

#### Function: `_get_ai_code_analysis`
> Get AI analysis of code from Perplexity
*Line 135*  

#### Function: `analyze_project`
> Analyze entire project
*Line 163*  

#### Function: `_get_project_ai_insights`
> Get AI insights for the entire project
*Line 207*  

#### Function: `save_analysis`
> Save analysis to file
*Line 239*  

#### Function: `print_summary`
> Print analysis summary
*Line 245*  

#### Function: `main`
> Main function
*Line 263*  

### 📄 hypercode\src\hypercode\debug_search.py

#### Module: `debug_search`
> Debug search results
*Line 0*  

#### Function: `debug_search`
> Debug why space data isn't being found
*Line 15*  

### 📄 hypercode\src\hypercode\demo_ai_research.py

#### Module: `demo_ai_research`
> HyperCode AI Research + Perplexity Integration Demo
*Line 0*  

#### Function: `demo_ai_research_queries`
> Demonstrate AI Research integration with Perplexity
*Line 16*  

#### Function: `test_document_specific_queries`
> Test queries specific to the HyperCode AI Research document
*Line 90*  

### 📄 hypercode\src\hypercode\demo_enhanced_client.py

#### Module: `demo_enhanced_client`
> Demo: Enhanced Perplexity Client with Knowledge Base
*Line 0*  

#### Function: `demo_knowledge_base_integration`
> Demonstrate the knowledge base integration
*Line 16*  

#### Function: `demonstrate_memory_persistence`
> Demonstrate that the knowledge base persists between sessions
*Line 131*  

### 📄 hypercode\src\hypercode\final_integration_test.py

#### Module: `final_integration_test`
> Final Test: Complete Perplexity Space Integration
*Line 0*  

#### Function: `final_integration_test`
> Complete test of the Perplexity Space integration
*Line 15*  

### 📄 hypercode\src\hypercode\health_scanner_ai.py

#### Module: `health_scanner_ai`
> HyperCode Health Scanner with Perplexity AI Integration
*Line 0*  

#### Class: `HealthScannerAI`
> AI-powered health scanner for HyperCode project
*Line 19*  

#### Function: `__init__`
*Line 22*  

#### Function: `analyze_project_structure`
> Analyze project structure and identify health issues
*Line 26*  

#### Function: `analyze_dependencies`
> Analyze dependency management
*Line 65*  

#### Function: `analyze_security`
> Analyze security configuration
*Line 101*  

#### Function: `get_ai_recommendations`
> Get AI-powered recommendations based on health scan
*Line 138*  

#### Function: `run_full_scan`
> Run complete health scan with AI analysis
*Line 165*  

#### Function: `save_report`
> Save health scan report to file
*Line 216*  

#### Function: `print_summary`
> Print a summary of the health scan
*Line 222*  

#### Function: `main`
> Main function to run the health scanner
*Line 242*  

### 📄 hypercode\src\hypercode\import-helper.py

#### Module: `import-helper`
> HyperCode Perplexity Space Import Helper
*Line 0*  

#### Class: `SpaceImportHelper`
> Helper class for managing Perplexity Space imports
*Line 13*  

#### Function: `__init__`
*Line 16*  

#### Function: `validate_document`
> Validate a document structure
*Line 21*  

#### Function: `load_template`
> Load documents from JSON template file
*Line 63*  

#### Function: `validate_all`
> Validate all loaded documents
*Line 83*  

#### Function: `generate_report`
> Generate a validation report
*Line 95*  

#### Function: `create_import_script`
> Generate a Python script to import the data
*Line 141*  

#### Function: `create_template_instructions`
> Generate detailed instructions for filling the template
*Line 193*  

#### Function: `main`
> CLI interface for the import helper
*Line 264*  

### 📄 hypercode\src\hypercode\import_all_space_data.py

#### Module: `import_all_space_data`
> Complete Import of HyperCode Space Data
*Line 0*  

#### Function: `format_content`
> Recursively format nested data into readable text
*Line 16*  

#### Function: `import_all_hypercode_data`
> Import all sections of your HyperCode Space data
*Line 41*  

### 📄 hypercode\src\hypercode\import_hypercode_data.py

#### Module: `import_hypercode_data`
> Import HyperCode Space Data
*Line 0*  

#### Function: `import_hypercode_space_data`
> Import your actual HyperCode Space data
*Line 16*  

### 📄 hypercode\src\hypercode\import_perplexity_space.py

#### Module: `import_perplexity_space`
> Perplexity Space Data Importer
*Line 0*  

#### Function: `create_manual_import_script`
> Create a script for manual data entry from Perplexity Space
*Line 17*  

#### Function: `create_json_import_template`
> Create a JSON template for importing data
*Line 86*  

#### Function: `import_from_json`
> Import data from JSON file
*Line 115*  

#### Function: `test_imported_data`
> Test the imported data with context-aware queries
*Line 153*  

#### Function: `show_import_menu`
> Show the import menu
*Line 188*  

### 📄 hypercode\src\hypercode\knowledge_graph\graph_builder.py

#### Module: `graph_builder`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\src\hypercode\knowledge_graph\sparql_query.py

#### Module: `sparql_query`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\src\hypercode\knowledge_graph\update_agent.py

#### Module: `update_agent`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode\src\hypercode\live_research\doc_generator.py

#### Module: `doc_generator`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\src\hypercode\live_research\github_publisher.py

#### Module: `github_publisher`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\src\hypercode\live_research\paper_indexer.py

#### Module: `paper_indexer`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\src\hypercode\live_research\research_crawler.py

#### Module: `research_crawler`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\src\hypercode\live_research\synthesis_engine.py

#### Module: `synthesis_engine`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode\src\hypercode\mcp\servers\aws_cli.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\src\hypercode\mcp\servers\aws_resource_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\src\hypercode\mcp\servers\code_analysis.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\src\hypercode\mcp\servers\dataset_downloader.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\src\hypercode\mcp\servers\file_system.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\src\hypercode\mcp\servers\human_input.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\src\hypercode\mcp\servers\hypercode_syntax.py

#### Module: `hypercode_syntax`
> HyperCode Syntax MCP Server
*Line 0*  

#### Class: `HyperCodeSyntaxServer`
> 🎨 MCP Server for HyperCode Visual Syntax Integration
*Line 28*  

#### Function: `__init__`
*Line 31*  

#### Function: `handle_request`
> Handle MCP requests from IDE
*Line 35*  

#### Function: `_initialize`
> Initialize the MCP server
*Line 56*  

#### Function: `_document_changed`
> Handle document changes for real-time parsing
*Line 79*  

#### Function: `_text_hover`
> Provide hover information for semantic annotations
*Line 98*  

#### Function: `_completion`
> Provide completion for semantic annotations
*Line 121*  

#### Function: `_parse_document`
> Parse entire document and return semantic structure
*Line 150*  

#### Function: `_validate_neurodiversity`
> Validate neurodiversity compliance and provide suggestions
*Line 179*  

#### Function: `_generate_diagnostics`
> Generate IDE diagnostics from parsed functions
*Line 216*  

#### Function: `_get_annotation_hover_info`
> Generate hover information for semantic annotations
*Line 266*  

#### Function: `main`
> Main MCP server loop
*Line 294*  

### 📄 hypercode\src\hypercode\mcp\servers\path_service.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\src\hypercode\mcp\servers\user_profile_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\src\hypercode\mcp\servers\valkey_service.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\src\hypercode\mcp\servers\web_search.py

#### Function: `main`
*Line 4*  

### 📄 hypercode\src\hypercode\perplexity_space_collector.py

#### Module: `perplexity_space_collector`
> Perplexity Space Data Collector
*Line 0*  

#### Function: `quick_copy_paste_collector`
> Quick collector for copy-paste workflow
*Line 18*  

#### Function: `create_structured_template`
> Create a structured JSON template for bulk import
*Line 117*  

#### Function: `show_bro_hacks`
> Show BROski's pro tips
*Line 167*  

#### Function: `main_menu`
> Main menu for the collector
*Line 207*  

### 📄 hypercode\src\hypercode\perplexity_space_integration.py

#### Module: `perplexity_space_integration`
> Perplexity Space Integration Guide
*Line 0*  

#### Function: `main`
*Line 16*  

### 📄 hypercode\src\hypercode\scripts\test_perplexity_api.py

#### Module: `test_perplexity_api`
> Test script for Perplexity API integration.
*Line 0*  

#### Function: `main`
> Test the Perplexity API connection and make a sample query.
*Line 17*  

### 📄 hypercode\src\hypercode\src\build.py

#### Module: `build`
> Build script for the HyperCode language.
*Line 0*  

#### Function: `build`
> Builds a HyperCode source file to the target language.
*Line 34*  

### 📄 hypercode\src\hypercode\src\core\ast_nodes.py

#### Module: `ast_nodes`
> Abstract Syntax Tree (AST) nodes for the HyperCode language.
*Line 0*  

#### Class: `Node`
> Base class for all AST nodes.
*Line 24*  

#### Class: `Expression`
> Base class for all expression nodes.
*Line 31*  

#### Class: `Statement`
> Base class for all statement nodes.
*Line 38*  

#### Class: `Program`
> Represents the entire program as a list of statements.
*Line 45*  

#### Class: `Identifier`
> Represents an identifier (e.g., a variable name).
*Line 52*  

#### Class: `Literal`
> Represents a literal value (e.g., number, string).
*Line 59*  

#### Class: `VariableDeclaration`
> Represents a variable declaration (let or const).
*Line 66*  

#### Class: `BinaryOperation`
> Represents a binary operation (e.g., a + b).
*Line 75*  

### 📄 hypercode\src\hypercode\src\core\lexer.py

#### Class: `LexerError`
*Line 8*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode programming language.
*Line 15*  

#### Function: `__init__`
*Line 32*  

#### Function: `tokenize`
> Convert the source code into a list of tokens.
*Line 87*  

#### Function: `is_at_end`
*Line 111*  

#### Function: `scan_token`
> Scan the next token from the source code.
*Line 114*  

#### Function: `advance`
*Line 205*  

#### Function: `add_token`
> Add a new token to the tokens list.
*Line 210*  

#### Function: `error`
> Record a lexing error.
*Line 223*  

#### Function: `synchronize`
> Synchronize after an error by skipping tokens until we find a statement boundary.
*Line 239*  

#### Function: `previous`
> Return the previous character.
*Line 251*  

#### Function: `peek_next`
> Look ahead two characters.
*Line 257*  

#### Function: `match`
*Line 263*  

#### Function: `peek`
*Line 272*  

#### Function: `peek_next`
*Line 277*  

#### Function: `string`
> Parse a string literal.
*Line 282*  

#### Function: `is_digit`
> Check if a character is a digit (0-9).
*Line 344*  

#### Function: `number`
> Parse a number literal (integer or float).
*Line 348*  

#### Function: `is_alpha`
> Check if a character is alphabetic or underscore.
*Line 403*  

#### Function: `is_alphanumeric`
> Check if a character is alphanumeric or underscore.
*Line 407*  

#### Function: `is_hex_digit`
> Check if a character is a valid hexadecimal digit.
*Line 411*  

#### Function: `identifier`
> Parse an identifier or keyword.
*Line 415*  

### 📄 hypercode\src\hypercode\src\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\src\hypercode\src\core\parser.py

#### Class: `ParseError`
*Line 8*  

#### Class: `Parser`
*Line 12*  

#### Function: `__init__`
*Line 13*  

#### Function: `parse`
> Parse the entire program.
*Line 17*  

#### Function: `declaration`
*Line 26*  

#### Function: `var_declaration`
*Line 39*  

#### Function: `statement`
*Line 64*  

#### Function: `print_statement`
*Line 71*  

#### Function: `expression_statement`
*Line 76*  

#### Function: `block`
*Line 81*  

#### Function: `expression`
*Line 88*  

#### Function: `assignment`
*Line 91*  

#### Function: `equality`
*Line 106*  

#### Function: `comparison`
*Line 116*  

#### Function: `term`
*Line 129*  

#### Function: `factor`
*Line 137*  

#### Function: `unary`
*Line 145*  

#### Function: `primary`
*Line 152*  

#### Function: `match`
*Line 184*  

#### Function: `consume`
*Line 191*  

#### Function: `error`
*Line 201*  

#### Function: `synchronize`
*Line 207*  

#### Function: `check`
*Line 227*  

#### Function: `advance`
*Line 232*  

#### Function: `is_at_end`
*Line 237*  

#### Function: `peek`
*Line 240*  

#### Function: `previous`
*Line 243*  

### 📄 hypercode\src\hypercode\src\hypercode-backend-js-COMPLETE.py

#### Module: `hypercode-backend-js-COMPLETE`
> HyperCode JavaScript Backend - Complete Implementation
*Line 0*  

#### Class: `JSCompiler`
> Compiles HyperCode AST to JavaScript.
*Line 19*  

#### Function: `__init__`
> Initialize compiler.
*Line 30*  

#### Function: `compile`
> Compile AST to JavaScript.
*Line 42*  

#### Function: `_generate_header`
> Generate JavaScript header
*Line 65*  

#### Function: `_generate_setup`
> Generate setup code (memory tape, pointer, I/O)
*Line 74*  

#### Function: `_generate_main`
> Generate JavaScript for AST node.
*Line 110*  

#### Function: `_generate_footer`
> Generate JavaScript footer
*Line 162*  

#### Function: `_indent`
> Get current indentation
*Line 179*  

#### Function: `optimize_ast`
> Optimize AST (future: loop unrolling, dead code elimination).
*Line 183*  

#### Function: `main`
> CLI interface for JavaScript backend
*Line 200*  

### 📄 hypercode\src\hypercode\src\hypercode-idea-generator-WEB.py

#### Module: `hypercode-idea-generator-WEB`
> HyperCode Community Idea Generator - Web Interface (HTML/CSS/JS)
*Line 0*  

### 📄 hypercode\src\hypercode\src\hypercode-launch-kit.py

#### Module: `hypercode-launch-kit`
> HyperCode Launch Kit - Ultimate System Initialization
*Line 0*  

#### Class: `HyperCodeLaunchKit`
> Complete launch system initialization
*Line 23*  

#### Function: `__init__`
*Line 26*  

#### Function: `create_readme`
> Create the ultimate README.md
*Line 30*  

#### Function: `create_launch_checklist`
> Create launch day checklist
*Line 367*  

#### Function: `create_launch_script`
> Create automated launch script
*Line 620*  

#### Function: `create_first_30_days`
> Create 30-day success roadmap
*Line 718*  

#### Function: `print_summary`
> Print beautiful summary
*Line 974*  

#### Function: `main`
> Run launch kit initialization
*Line 1007*  

### 📄 hypercode\src\hypercode\src\hypercode-lexer-COMPLETE.py

#### Module: `hypercode-lexer-COMPLETE`
> HyperCode Lexer - Complete Implementation
*Line 0*  

#### Class: `TokenType`
> HyperCode token types - minimal yet powerful
*Line 21*  

#### Class: `Token`
> Represents a single token with position tracking
*Line 45*  

#### Function: `__repr__`
> Neurodivergent-friendly representation
*Line 54*  

#### Class: `LexerError`
> Lexer-specific errors with context
*Line 59*  

#### Function: `__init__`
*Line 62*  

#### Class: `HyperCodeLexer`
> Tokenizes HyperCode programs with accessibility features.
*Line 69*  

#### Function: `__init__`
> Initialize lexer with source code.
*Line 95*  

#### Function: `tokenize`
> Convert HyperCode source to token stream.
*Line 110*  

#### Function: `_advance_position`
> Update position tracking after processing character
*Line 169*  

#### Function: `_skip_comment`
> Skip characters until end of line
*Line 179*  

#### Function: `get_tokens`
> Return current token list
*Line 184*  

#### Function: `filter_tokens`
> Get tokens excluding certain types.
*Line 188*  

#### Function: `print_tokens`
> Print tokens in readable format.
*Line 205*  

#### Function: `get_statistics`
> Get token statistics (useful for analysis).
*Line 236*  

#### Function: `main`
> CLI interface for the lexer
*Line 250*  

### 📄 hypercode\src\hypercode\src\hypercode-parser-COMPLETE.py

#### Module: `hypercode-parser-COMPLETE`
> HyperCode Parser - Complete Implementation
*Line 0*  

#### Class: `NodeType`
> AST Node types
*Line 22*  

#### Class: `ASTNode`
> Abstract Syntax Tree Node.
*Line 38*  

#### Function: `__repr__`
> Pretty-print AST (neurodivergent-friendly)
*Line 51*  

#### Class: `ParserError`
> Parser-specific errors with context
*Line 68*  

#### Function: `__init__`
*Line 71*  

#### Class: `HyperCodeParser`
> Parses HyperCode token stream into AST.
*Line 80*  

#### Function: `__init__`
> Initialize parser with token stream.
*Line 94*  

#### Function: `parse`
> Parse tokens into AST.
*Line 105*  

#### Function: `_parse_statement`
> Parse a single statement
*Line 127*  

#### Function: `_parse_loop`
> Parse loop structure: [ statements ]
*Line 174*  

#### Function: `_advance`
> Move to next token
*Line 209*  

#### Function: `_is_at_end`
> Check if at end of token stream
*Line 215*  

#### Function: `validate`
> Validate AST structure.
*Line 222*  

#### Function: `print_ast`
> Print AST in readable format.
*Line 237*  

#### Function: `main`
> CLI interface for the parser
*Line 251*  

### 📄 hypercode\src\hypercode\src\hypercode\__init__.py

#### Module: `__init__`
> HyperCode - A neurodivergent-first programming language with AI compatibility.
*Line 0*  

### 📄 hypercode\src\hypercode\src\hypercode\__main__.py

#### Function: `main`
*Line 6*  

### 📄 hypercode\src\hypercode\src\hypercode\config.py

#### Module: `config`
> Configuration module for HyperCode.
*Line 0*  

#### Class: `Config`
> Configuration class for HyperCode
*Line 16*  

#### Function: `get_headers`
> Get headers for API requests
*Line 27*  

### 📄 hypercode\src\hypercode\src\hypercode\core\__init__.py

#### Module: `__init__`
> Core package for the HyperCode language implementation.
*Line 0*  

### 📄 hypercode\src\hypercode\src\hypercode\core\ast.py

#### Class: `Node`
*Line 9*  

#### Function: `accept`
*Line 10*  

#### Class: `Expr`
*Line 20*  

#### Class: `Literal`
*Line 25*  

#### Class: `Variable`
*Line 30*  

#### Class: `Assign`
*Line 35*  

#### Class: `Binary`
*Line 41*  

#### Class: `Unary`
*Line 48*  

#### Class: `Grouping`
*Line 54*  

#### Class: `Stmt`
*Line 60*  

#### Class: `Expression`
*Line 65*  

#### Class: `Print`
*Line 70*  

#### Class: `Var`
*Line 75*  

#### Class: `Block`
*Line 81*  

#### Class: `Program`
*Line 87*  

### 📄 hypercode\src\hypercode\src\hypercode\core\cli.py

#### Module: `cli`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\src\hypercode\src\hypercode\core\error_handler.py

#### Function: `report_parse_error`
*Line 5*  

#### Function: `report`
*Line 12*  

### 📄 hypercode\src\hypercode\src\hypercode\core\lexer.py

#### Module: `lexer`
> Core HyperCode language implementation - Lexer
*Line 0*  

#### Class: `LexerError`
> Exception raised for errors in the lexer.
*Line 32*  

#### Function: `__init__`
*Line 35*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode language.
*Line 42*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 108*  

#### Function: `tokenize`
> Convert source code into a list of tokens.
*Line 125*  

#### Function: `_match_patterns`
> Try to match the current position against all token patterns.
*Line 160*  

#### Function: `_update_position`
> Update line and column numbers based on the given text.
*Line 186*  

#### Function: `_add_token`
> Add a token to the token list.
*Line 205*  

#### Function: `_handle_unknown`
> Handle unknown characters in the source.
*Line 269*  

### 📄 hypercode\src\hypercode\src\hypercode\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\src\hypercode\src\hypercode\core\parser.py

#### Class: `ParseError`
*Line 8*  

#### Class: `Parser`
*Line 12*  

#### Function: `__init__`
*Line 13*  

#### Function: `parse`
> Parse the entire program.
*Line 17*  

#### Function: `declaration`
*Line 26*  

#### Function: `var_declaration`
*Line 39*  

#### Function: `statement`
*Line 64*  

#### Function: `print_statement`
*Line 71*  

#### Function: `expression_statement`
*Line 76*  

#### Function: `block`
*Line 81*  

#### Function: `expression`
*Line 88*  

#### Function: `assignment`
*Line 91*  

#### Function: `equality`
*Line 106*  

#### Function: `comparison`
*Line 116*  

#### Function: `term`
*Line 129*  

#### Function: `factor`
*Line 137*  

#### Function: `unary`
*Line 145*  

#### Function: `primary`
*Line 152*  

#### Function: `match`
*Line 184*  

#### Function: `consume`
*Line 191*  

#### Function: `error`
*Line 201*  

#### Function: `synchronize`
*Line 207*  

#### Function: `check`
*Line 227*  

#### Function: `advance`
*Line 232*  

#### Function: `is_at_end`
*Line 237*  

#### Function: `peek`
*Line 240*  

#### Function: `previous`
*Line 243*  

### 📄 hypercode\src\hypercode\src\hypercode\core\semantic_analyzer.py

#### Module: `semantic_analyzer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode\src\hypercode\src\hypercode\core\tokens.py

#### Class: `TokenType`
*Line 6*  

#### Class: `Token`
*Line 60*  

#### Function: `__str__`
*Line 67*  

### 📄 hypercode\src\hypercode\src\hypercode\enhanced_perplexity_client.py

#### Module: `enhanced_perplexity_client`
> Enhanced Perplexity Client with Knowledge Base Integration
*Line 0*  

#### Class: `EnhancedPerplexityClient`
> Enhanced Perplexity client with knowledge base integration
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `query_with_context`
> Send a query with relevant knowledge base context
*Line 25*  

#### Function: `add_research_data`
> Add research data to the knowledge base
*Line 61*  

#### Function: `search_research_data`
> Search the knowledge base
*Line 71*  

#### Function: `list_research_documents`
> List all research documents
*Line 75*  

#### Function: `get_document`
> Get a specific document
*Line 79*  

#### Function: `delete_document`
> Delete a document
*Line 83*  

#### Function: `import_from_perplexity_space`
> Import data from Perplexity Space export
*Line 87*  

#### Function: `test_context_integration`
> Test the context integration
*Line 123*  

#### Function: `create_perplexity_space_import_template`
> Create a template for importing Perplexity Space data
*Line 175*  

### 📄 hypercode\src\hypercode\src\hypercode\knowledge_base.py

#### Module: `knowledge_base`
> HyperCode Knowledge Base - Perplexity Space Integration
*Line 0*  

#### Class: `ResearchDocument`
> Represents a research document from Perplexity Space
*Line 17*  

#### Function: `__post_init__`
*Line 28*  

#### Function: `generate_id`
> Generate unique ID from content hash
*Line 36*  

#### Function: `validate`
> Validate document data
*Line 41*  

#### Function: `update_timestamp`
> Update the last_updated timestamp
*Line 53*  

#### Class: `HyperCodeKnowledgeBase`
> Knowledge base for HyperCode research data
*Line 100*  

#### Function: `__init__`
*Line 103*  

#### Function: `load`
> Load knowledge base from file
*Line 109*  

#### Function: `save`
> Save knowledge base to file
*Line 125*  

#### Function: `add_document`
> Add a new research document
*Line 135*  

#### Function: `search_documents`
> Search documents by query
*Line 163*  

#### Function: `get_context_for_query`
> Get relevant context for a query
*Line 227*  

#### Function: `list_documents`
> List all documents
*Line 257*  

#### Function: `get_document`
> Get a specific document by ID
*Line 261*  

#### Function: `delete_document`
> Delete a document
*Line 265*  

#### Function: `update_document`
> Update an existing document
*Line 273*  

#### Function: `search_by_tags`
> Search documents by tags with AND/OR operators
*Line 287*  

#### Function: `get_document_statistics`
> Get statistics about the knowledge base
*Line 306*  

#### Function: `export_format`
> Export knowledge base in different formats
*Line 331*  

#### Function: `validate_all_documents`
> Validate all documents and return list of errors
*Line 353*  

#### Function: `cleanup_duplicates`
> Remove duplicate documents based on content hash
*Line 363*  

#### Function: `initialize_sample_data`
> Initialize with sample HyperCode research data
*Line 384*  

### 📄 hypercode\src\hypercode\src\hypercode\perplexity_client.py

#### Module: `perplexity_client`
> Perplexity AI API client for HyperCode.
*Line 0*  

#### Class: `PerplexityClient`
> Client for interacting with Perplexity AI API
*Line 12*  

#### Function: `__init__`
> Initialize the Perplexity client.
*Line 15*  

#### Function: `query`
> Send a query to the Perplexity API.
*Line 30*  

#### Function: `test_connection`
> Test the connection to the Perplexity API
*Line 72*  

### 📄 hypercode\src\hypercode\src\hypercode\repl.py

#### Function: `run_repl`
*Line 7*  

#### Function: `run`
*Line 22*  

### 📄 hypercode\src\hypercode\src\hypercode_idea_generator.py

#### Module: `hypercode_idea_generator`
> HyperCode Idea Generator - AI-Powered Community Input System
*Line 0*  

#### Class: `HyperCodeIdeaGenerator`
> AI-Powered Idea Generator for HyperCode community input.
*Line 431*  

#### Function: `__init__`
*Line 439*  

#### Function: `get_ideas_by_category`
> Get ideas by category and optionally by difficulty level.
*Line 443*  

#### Function: `get_top_ideas`
> Get most-voted ideas across all categories.
*Line 468*  

#### Function: `vote_for_idea`
> Vote for an idea.
*Line 487*  

#### Function: `get_trending_ideas`
> Get trending ideas (high votes + recent activity).
*Line 497*  

#### Function: `format_idea_card`
> Format idea for display.
*Line 502*  

#### Function: `main`
> Interactive idea generator CLI
*Line 528*  

### 📄 hypercode\src\hypercode\src\hypercode_lexer_fixed.py

#### Module: `hypercode_lexer_fixed`
> HyperCode Lexer - Fixed String Handling with Escape Sequences
*Line 0*  

#### Class: `TokenType`
> HyperCode token types
*Line 19*  

#### Class: `Token`
> Represents a single token with position tracking
*Line 44*  

#### Function: `__repr__`
> Readable representation
*Line 54*  

#### Class: `LexerError`
> Lexer error with context
*Line 68*  

#### Function: `__init__`
*Line 71*  

#### Class: `HyperCodeLexerFixed`
> Fixed lexer with proper string escape sequence handling.
*Line 84*  

#### Function: `__init__`
> Initialize lexer.
*Line 125*  

#### Function: `tokenize`
> Convert source to token stream.
*Line 145*  

#### Function: `_parse_string`
> Parse string literal with escape sequence handling.
*Line 217*  

#### Function: `_skip_comment`
> Skip comment until end of line
*Line 300*  

#### Function: `_advance`
> Update position after processing character
*Line 305*  

#### Function: `print_tokens`
> Print tokens in readable format
*Line 315*  

#### Function: `run_tests`
> Comprehensive test suite
*Line 329*  

#### Function: `main`
> Main entry point
*Line 446*  

### 📄 hypercode\src\hypercode\src\hypercode_poc.py

#### Module: `hypercode_poc`
> HyperCode POC - Neurodivergent-First Programming Language
*Line 0*  

#### Class: `TokenType`
> Brainfuck-inspired core + modern aliases
*Line 18*  

#### Class: `Token`
*Line 34*  

#### Class: `UserConfidenceLevel`
*Line 41*  

#### Class: `EnhancedLexer`
> Smart tokenizer with escape handling + accessibility focus
*Line 48*  

#### Function: `__init__`
*Line 51*  

#### Function: `tokenize`
*Line 74*  

#### Function: `handle_string`
*Line 115*  

#### Function: `handle_number`
*Line 141*  

#### Function: `handle_identifier`
*Line 149*  

#### Function: `advance`
*Line 171*  

#### Class: `ContextAwareErrorMessenger`
> Friendly, adaptive error messages
*Line 176*  

#### Function: `__init__`
*Line 179*  

#### Function: `format_error`
*Line 182*  

#### Class: `SemanticContextStreamer`
> Understand programmer intent from tokens
*Line 189*  

#### Function: `analyze`
*Line 192*  

#### Class: `ConfidenceTracker`
> Adapt system guidance to user skill level
*Line 209*  

#### Function: `__init__`
*Line 212*  

#### Function: `record`
*Line 216*  

#### Class: `HyperCodePOC`
> Main system: Lexer + Error Messenger + Semantic Analyzer + Confidence Tracker
*Line 222*  

#### Function: `__init__`
*Line 225*  

#### Function: `compile`
*Line 232*  

### 📄 hypercode\src\hypercode\src\parser\debug_ascii.py

#### Module: `debug_ascii`
> ASCII-only debug
*Line 0*  

#### Function: `test_regex_patterns`
> Test regex patterns directly
*Line 14*  

### 📄 hypercode\src\hypercode\src\parser\debug_full.py

#### Module: `debug_full`
> Debug the full parsing flow
*Line 0*  

#### Function: `debug_full_parsing`
> Debug the full parsing flow
*Line 14*  

### 📄 hypercode\src\hypercode\src\parser\debug_parser.py

#### Module: `debug_parser`
> Debug the Visual Syntax Parser - Find what's wrong with annotation detection
*Line 0*  

#### Function: `debug_annotation_detection`
> Debug why annotations aren't being detected
*Line 14*  

### 📄 hypercode\src\hypercode\src\parser\debug_simple.py

#### Module: `debug_simple`
> Simple debug without emoji characters
*Line 0*  

#### Function: `debug_simple`
> Debug without emoji characters
*Line 14*  

### 📄 hypercode\src\hypercode\src\parser\test_parser.py

#### Module: `test_parser`
> Test the Visual Syntax Parser - First Click Moment Demo
*Line 0*  

#### Function: `test_first_click_moment`
> Test the parser with the first click moment example
*Line 14*  

### 📄 hypercode\src\hypercode\src\parser\visual_syntax_parser.py

#### Module: `visual_syntax_parser`
> 🎨 Visual Syntax Parser for HyperCode V3
*Line 0*  

#### Class: `SemanticMarker`
> 🎨 Semantic marker types with emoji representations
*Line 18*  

#### Class: `SemanticAnnotation`
> 📋 A single semantic annotation with its metadata
*Line 37*  

#### Function: `__str__`
*Line 46*  

#### Class: `ParsedFunction`
> 🔍 A fully parsed HyperCode function
*Line 51*  

#### Function: `get_annotations_by_type`
> Get all annotations of a specific type
*Line 62*  

#### Class: `VisualSyntaxParser`
> 🎨 Main parser for HyperCode's visual semantic syntax
*Line 69*  

#### Function: `__init__`
*Line 72*  

#### Function: `_build_semantic_patterns`
> 🔍 Build regex patterns for all semantic markers
*Line 76*  

#### Function: `_build_color_scheme`
> 🎨 Build semantic color mapping for IDE highlighting
*Line 105*  

#### Function: `parse_file`
> 📄 Parse an entire HyperCode file
*Line 123*  

#### Function: `parse_content`
> 📝 Parse HyperCode content string
*Line 130*  

#### Function: `_is_function_definition`
> 🔍 Check if line is a function definition
*Line 170*  

#### Function: `_start_new_function`
> 🆕 Create new ParsedFunction from definition line
*Line 179*  

#### Function: `_parse_line_annotations`
> � Parse semantic annotations from a line
*Line 202*  

#### Function: `_parse_annotation_params`
> 🔧 Parse annotation parameters from string
*Line 223*  

#### Function: `generate_syntax_highlighting`
> 🎨 Generate HTML with syntax highlighting for visual markers
*Line 265*  

#### Function: `extract_semantic_summary`
> 📊 Extract semantic summary for analysis
*Line 277*  

#### Function: `validate_neurodiversity_compliance`
> 🧠 Validate neurodiversity-first design principles
*Line 311*  

### 📄 hypercode\src\hypercode\src\scaffold (1).py

#### Module: `scaffold (1)`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 141*  

#### Function: `create_python_files`
> Create all Python files with proper __init__.py structure.
*Line 151*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 165*  

#### Function: `create_root_files`
> Create root-level configuration files as empty placeholders.
*Line 202*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 213*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 234*  

#### Function: `main`
> Main scaffolding function.
*Line 259*  

### 📄 hypercode\src\hypercode\src\scaffold.py

#### Module: `scaffold`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 153*  

#### Function: `create_python_files`
> Create all Python files with proper docstrings and structure.
*Line 184*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 254*  

#### Function: `create_root_files`
> Create root-level configuration files with appropriate content.
*Line 291*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 541*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 583*  

#### Function: `main`
> Main scaffolding function.
*Line 621*  

### 📄 hypercode\src\hypercode\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode\src\hypercode\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode\src\hypercode\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode\src\hypercode\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode\src\hypercode\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 183*  

### 📄 hypercode\src\hypercode\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode\src\hypercode\tests\benchmark_knowledge_base.py

#### Module: `benchmark_knowledge_base`
> Performance Benchmark Tool for HyperCode Knowledge Base
*Line 0*  

#### Class: `BenchmarkSuite`
> Comprehensive benchmark suite for Knowledge Base
*Line 24*  

#### Function: `__init__`
*Line 27*  

#### Function: `_get_system_info`
> Get system information for benchmark context
*Line 34*  

#### Function: `generate_test_data`
> Generate test data of specified size
*Line 43*  

#### Function: `benchmark_operation`
> Benchmark a single operation
*Line 93*  

#### Function: `run_benchmark_suite`
> Run complete benchmark suite
*Line 118*  

#### Function: `_calculate_summary`
> Calculate summary statistics
*Line 274*  

#### Function: `_generate_recommendations`
> Generate performance recommendations
*Line 296*  

#### Function: `generate_markdown_report`
> Generate beautiful markdown report
*Line 338*  

#### Function: `save_json_results`
> Save results as JSON
*Line 467*  

#### Function: `main`
> Main benchmark runner
*Line 474*  

### 📄 hypercode\src\hypercode\tests\test_accessibility.py

#### Module: `test_accessibility`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\src\hypercode\tests\test_ai_gateway.py

#### Module: `test_ai_gateway`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\src\hypercode\tests\test_backends.py

#### Module: `test_backends`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\src\hypercode\tests\test_core.py

#### Module: `test_core`
> Test harness for core HyperCode components.
*Line 0*  

#### Function: `run_test`
> Test the lexer and parser with the given source code.
*Line 29*  

### 📄 hypercode\src\hypercode\tests\test_integration.py

#### Module: `test_integration`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode\src\hypercode\tests\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Comprehensive test suite for knowledge base search functionality.
*Line 0*  

#### Class: `TestKnowledgeBaseSearch`
> Test suite for knowledge base search functionality.
*Line 12*  

#### Function: `sample_documents`
> Create sample documents for testing.
*Line 16*  

#### Function: `knowledge_base`
> Create a knowledge base instance with sample documents.
*Line 40*  

#### Function: `test_basic_search`
> Test basic search functionality.
*Line 48*  

#### Function: `test_search_with_exact_match`
> Test search with exact phrase matching.
*Line 54*  

#### Function: `test_search_case_insensitive`
> Test that search is case-insensitive.
*Line 59*  

#### Function: `test_search_empty_query`
> Test search with empty query returns all or no documents.
*Line 65*  

#### Function: `test_search_no_matches`
> Test search with no matching documents.
*Line 71*  

#### Function: `test_search_ranking`
> Test that search results are ranked by relevance.
*Line 77*  

#### Function: `test_query_normalization`
> Test query normalization (typos, spacing, punctuation).
*Line 88*  

#### Function: `test_multi_word_query`
> Test search with multiple keywords.
*Line 96*  

#### Function: `test_tag_based_search`
> Test search that includes tag matching.
*Line 101*  

#### Class: `TestEdgeCases`
> Test edge cases and boundary conditions.
*Line 110*  

#### Function: `knowledge_base`
*Line 114*  

#### Function: `test_very_short_query`
> Test search with very short query (1-2 chars).
*Line 119*  

#### Function: `test_very_long_query`
> Test search with very long query (paragraph length).
*Line 124*  

#### Function: `test_special_characters_in_query`
> Test search with special characters.
*Line 134*  

#### Function: `test_unicode_in_query`
> Test search with unicode characters.
*Line 139*  

#### Function: `test_sql_injection_attempt`
> Test that search is safe from SQL injection-style attacks.
*Line 144*  

#### Function: `test_repeated_queries`
> Test that repeated queries return consistent results.
*Line 149*  

#### Class: `TestPerformance`
> Performance benchmarking tests.
*Line 157*  

#### Function: `large_knowledge_base`
> Create a knowledge base with many documents.
*Line 161*  

#### Function: `test_search_response_time`
> Test that search completes within acceptable time.
*Line 177*  

#### Function: `test_concurrent_searches`
> Test multiple concurrent search operations.
*Line 187*  

#### Function: `test_memory_usage`
> Test memory usage during search operations.
*Line 205*  

#### Class: `TestIntegrationWithPerplexity`
> Test integration with EnhancedPerplexityClient.
*Line 211*  

#### Function: `mock_perplexity_client`
> Create a mock Perplexity client.
*Line 215*  

#### Function: `mock_knowledge_base`
> Create a mock knowledge base.
*Line 227*  

#### Function: `test_enhanced_query_with_context`
> Test that queries are enhanced with knowledge base context.
*Line 241*  

#### Function: `test_fallback_to_perplexity_api`
> Test fallback to Perplexity API when no local context found.
*Line 255*  

#### Function: `test_context_ranking_and_selection`
> Test that best context is selected for query enhancement.
*Line 267*  

#### Class: `TestDocumentManagement`
> Test document addition, update, and removal.
*Line 282*  

#### Function: `knowledge_base`
*Line 286*  

#### Function: `test_add_document`
> Test adding a new document to knowledge base.
*Line 294*  

#### Function: `test_update_document`
> Test updating an existing document.
*Line 304*  

#### Function: `test_remove_document`
> Test removing a document.
*Line 309*  

### 📄 hypercode\src\hypercode\tests\test_knowledge_base_comprehensive.py

#### Module: `test_knowledge_base_comprehensive`
> Comprehensive Test Suite for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestKnowledgeBaseUnit`
> Unit tests for Knowledge Base functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_docs`
> Sample documents for testing
*Line 36*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 59*  

#### Function: `test_add_single_document`
> Test adding a single document
*Line 65*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 74*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 84*  

#### Function: `test_search_exact_match`
> Test exact search matching
*Line 102*  

#### Function: `test_search_partial_match`
> Test partial search matching
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 124*  

#### Function: `test_search_case_insensitive`
> Test case insensitive search
*Line 135*  

#### Function: `test_empty_search`
> Test empty search query
*Line 147*  

#### Function: `test_nonexistent_search`
> Test search for nonexistent terms
*Line 155*  

#### Function: `test_get_context_for_query`
> Test context extraction
*Line 165*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 176*  

#### Function: `test_document_update`
> Test updating existing documents
*Line 186*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 202*  

#### Function: `test_delete_document`
> Test document deletion
*Line 213*  

#### Class: `TestKnowledgeBaseIntegration`
> Integration tests for Knowledge Base
*Line 229*  

#### Function: `populated_kb`
> Create a populated knowledge base for integration testing
*Line 233*  

#### Function: `test_complex_search_queries`
> Test complex search scenarios
*Line 277*  

#### Function: `test_search_ranking_quality`
> Test that search results are properly ranked
*Line 291*  

#### Function: `test_related_term_expansion`
> Test that related terms are properly expanded
*Line 301*  

#### Function: `test_performance_with_large_dataset`
> Test performance with larger dataset
*Line 313*  

#### Function: `test_concurrent_access_simulation`
> Test simulated concurrent access
*Line 332*  

#### Class: `TestKnowledgeBasePerformance`
> Performance tests for Knowledge Base
*Line 356*  

#### Function: `large_kb`
> Create a large knowledge base for performance testing
*Line 360*  

#### Function: `test_search_performance_large_dataset`
> Test search performance with large dataset
*Line 382*  

#### Function: `test_save_performance_large_dataset`
> Test save performance with large dataset
*Line 396*  

#### Function: `test_load_performance_large_dataset`
> Test load performance with large dataset
*Line 409*  

#### Function: `test_memory_usage_large_dataset`
> Test memory usage with large dataset
*Line 423*  

#### Class: `TestKnowledgeBaseEdgeCases`
> Edge case tests for Knowledge Base
*Line 446*  

#### Function: `edge_case_kb`
> Create knowledge base for edge case testing
*Line 450*  

#### Function: `test_empty_title_handling`
> Test handling of documents with empty titles
*Line 494*  

#### Function: `test_special_characters_handling`
> Test handling of special characters and unicode
*Line 499*  

#### Function: `test_very_long_titles`
> Test handling of very long titles
*Line 507*  

#### Function: `test_empty_content_handling`
> Test handling of documents with empty content
*Line 512*  

#### Function: `test_none_tags_handling`
> Test handling of None tags
*Line 517*  

#### Function: `test_malformed_json_handling`
> Test handling of malformed JSON files
*Line 531*  

#### Function: `test_file_permission_handling`
> Test handling of file permission issues
*Line 544*  

### 📄 hypercode\src\hypercode\tests\test_lexer.py

#### Function: `test_lexer_basic_tokens`
*Line 5*  

#### Function: `test_lexer_strings`
*Line 23*  

#### Function: `test_lexer_operators`
*Line 48*  

### 📄 hypercode\src\hypercode\tests\test_lexer_extended.py

#### Function: `test_lexer_escaped_strings`
> Test handling of strings with escaped characters.
*Line 5*  

#### Function: `test_lexer_numbers`
> Test various number formats.
*Line 18*  

#### Function: `test_lexer_operators`
> Test all operators.
*Line 39*  

#### Function: `test_lexer_comments`
> Test handling of single-line and multi-line comments.
*Line 86*  

#### Function: `test_lexer_whitespace`
> Test handling of various whitespace characters.
*Line 115*  

#### Function: `test_lexer_error_handling`
> Test error handling for invalid tokens.
*Line 130*  

#### Function: `test_lexer_hex_numbers`
> Test hexadecimal number literals.
*Line 139*  

#### Function: `test_lexer_binary_numbers`
> Test binary number literals.
*Line 157*  

#### Function: `test_lexer_scientific_notation`
> Test scientific notation numbers.
*Line 169*  

#### Function: `test_lexer_string_escapes`
> Test string escape sequences.
*Line 180*  

#### Function: `test_lexer_keywords`
> Test all language keywords.
*Line 197*  

#### Function: `test_lexer_position_tracking`
> Test that line and column numbers are tracked correctly.
*Line 223*  

#### Function: `test_lexer_error_recovery`
> Test that the lexer raises errors on invalid characters.
*Line 243*  

#### Function: `test_lexer_error_messages`
> Test that lexer error messages are informative.
*Line 252*  

### 📄 hypercode\src\hypercode\tests\test_parser.py

#### Function: `test_parse_literal`
*Line 12*  

#### Function: `test_parse_variable_declaration`
*Line 24*  

#### Function: `test_parse_binary_expression`
*Line 37*  

### 📄 hypercode\src\hypercode\tests\unit\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Phase 1 Unit Tests for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestHyperCodeKnowledgeBase`
> Test suite for HyperCodeKnowledgeBase core functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_documents`
> Sample documents for testing
*Line 33*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 56*  

#### Function: `test_add_document`
> Test adding a single document
*Line 61*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 82*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 92*  

#### Function: `test_search_exact_match`
> Test exact term matching in search
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 126*  

#### Function: `test_search_related_terms`
> Test related term expansion
*Line 139*  

#### Function: `test_search_space_data_boost`
> Test that space data gets boosted in search
*Line 153*  

#### Function: `test_get_context_for_query`
> Test context extraction for queries
*Line 180*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 192*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 203*  

#### Function: `test_empty_search`
> Test search with empty query
*Line 216*  

#### Function: `test_search_nonexistent_term`
> Test search for term that doesn't exist
*Line 221*  

#### Function: `test_document_update`
> Test updating existing document
*Line 231*  

#### Class: `TestResearchDocument`
> Test suite for ResearchDocument dataclass
*Line 250*  

#### Function: `test_document_creation`
> Test creating a research document
*Line 253*  

#### Function: `test_document_optional_fields`
> Test document with optional fields
*Line 273*  

### 📄 hypercode\src\hypercode\tests\unit\test_search_algorithm.py

#### Module: `test_search_algorithm`
> Phase 1 Unit Tests for Search Algorithm
*Line 0*  

#### Class: `TestSearchAlgorithm`
> Test suite for search algorithm functionality
*Line 20*  

#### Function: `populated_kb`
> Create a knowledge base with test documents
*Line 24*  

#### Function: `test_exact_title_match_highest_score`
> Test that exact title matches get highest priority
*Line 80*  

#### Function: `test_space_data_boosting`
> Test that space data gets boosted in search results
*Line 92*  

#### Function: `test_related_term_expansion`
> Test related term matching functionality
*Line 105*  

#### Function: `test_tag_matching_scoring`
> Test that tag matches contribute to scoring
*Line 126*  

#### Function: `test_content_frequency_scoring`
> Test that multiple content occurrences increase score
*Line 136*  

#### Function: `test_partial_word_matching`
> Test partial word matching for longer terms
*Line 149*  

#### Function: `test_query_word_ordering`
> Test that query words are properly processed
*Line 167*  

#### Function: `test_case_insensitive_search`
> Test that search is case insensitive
*Line 179*  

#### Function: `test_empty_query_returns_no_results`
> Test that empty queries return no results
*Line 202*  

#### Function: `test_limit_parameter_respected`
> Test that search limit parameter works correctly
*Line 210*  

#### Function: `test_no_results_for_nonexistent_terms`
> Test search for terms that don't exist
*Line 219*  

#### Function: `test_special_characters_in_query`
> Test search with special characters
*Line 227*  

#### Function: `test_unicode_characters`
> Test search with unicode characters
*Line 237*  

#### Function: `test_search_performance_with_large_kb`
> Test search performance with larger knowledge base
*Line 256*  

#### Function: `test_search_result_consistency`
> Test that search results are consistent across multiple calls
*Line 277*  

#### Class: `TestSearchScoringDetails`
> Test detailed scoring algorithm behavior
*Line 292*  

#### Function: `scoring_kb`
> Create KB for detailed scoring tests
*Line 296*  

#### Function: `test_title_match_beats_content_match`
> Test that title matches score higher than content matches
*Line 324*  

#### Function: `test_space_data_boosting_works`
> Test that space data gets boosted
*Line 332*  

#### Function: `test_frequency_scoring`
> Test that content frequency affects scoring
*Line 340*  

### 📄 hypercode\tag_channels.py

#### Module: `tag_channels`
> Tag Channels - minimal parser and utilities for `@tag` metadata lines.
*Line 0*  

#### Function: `_coerce_value`
*Line 28*  

#### Function: `parse_tag_line`
> Parse a single `@tag` line.
*Line 51*  

#### Function: `parse_tags`
> Parse multiple lines and collect tags into a flat dict by key path.
*Line 80*  

#### Function: `get_tag`
> Get a tag value by dotted key path from a flat tags dict.
*Line 95*  

#### Function: `group_entities_by_tag`
> Group entities by a specific tag key.
*Line 103*  

### 📄 hypercode\test_database.py

#### Module: `test_database`
> Test script for Hypercode database operations.
*Line 0*  

#### Function: `test_database_loading`
> Test loading the database and basic queries.
*Line 10*  

### 📄 hypercode\tests\test_tag_channels.py

#### Function: `test_parse_tag_line_basic`
*Line 12*  

#### Function: `test_parse_tags_multi`
*Line 20*  

#### Function: `test_group_entities_by_tag`
*Line 33*  

### 📄 hypercode\tests\test_v01_core.py

#### Function: `lex_types`
*Line 16*  

#### Function: `run_program`
*Line 22*  

#### Function: `test_lexer_tokenization_basic`
*Line 38*  

#### Function: `test_parser_builds_pipe_and_list`
*Line 54*  

#### Function: `test_interpreter_pipeline_math`
*Line 70*  

#### Function: `test_interpreter_var_and_print`
*Line 76*  

#### Function: `test_interpreter_error_pipeline_non_callable`
*Line 81*  

### 📄 hypercode_backup_20251205_183301\accessibility\adhd_optimizer.py

#### Module: `adhd_optimizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\accessibility\autism_preset.py

#### Module: `autism_preset`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\accessibility\dyslexia_formatter.py

#### Module: `dyslexia_formatter`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\accessibility\sensory_customizer.py

#### Module: `sensory_customizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\accessibility\wcag_auditor.py

#### Module: `wcag_auditor`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\archive\new-files-to-check\backend\research\__init__.py

#### Module: `__init__`
> Initialization for the research module.
*Line 0*  

### 📄 hypercode_backup_20251205_183301\archive\new-files-to-check\backend\research\db.py

#### Module: `db`
> Database configuration for the HyperCode research module.
*Line 0*  

#### Function: `_get_database_url`
> Return the database URL to connect to.
*Line 35*  

### 📄 hypercode_backup_20251205_183301\archive\new-files-to-check\backend\research\models.py

#### Module: `models`
> ORM models for the HyperCode research database.
*Line 0*  

#### Class: `Study`
> Top‑level research study.
*Line 32*  

#### Function: `__repr__`
*Line 52*  

#### Class: `Source`
> External or internal resource used in a study.
*Line 56*  

#### Function: `__repr__`
*Line 81*  

#### Class: `LanguageVersion`
> Version of the HyperCode language.
*Line 85*  

#### Function: `__repr__`
*Line 102*  

#### Class: `Task`
> A coding task or challenge used in experiments.
*Line 106*  

#### Function: `__repr__`
*Line 124*  

#### Class: `Participant`
> An anonymised participant in the study.
*Line 128*  

#### Function: `__repr__`
*Line 144*  

#### Class: `Session`
> A single coding session of a participant performing a task.
*Line 148*  

#### Function: `__repr__`
*Line 169*  

#### Class: `Event`
> Low‑level interaction within a session.
*Line 176*  

#### Function: `__repr__`
*Line 193*  

#### Class: `Feedback`
> Qualitative and quantitative feedback for a session.
*Line 197*  

#### Function: `__repr__`
*Line 219*  

### 📄 hypercode_backup_20251205_183301\archive\new-files-to-check\backend\research\scripts\import_sources_from_folder.py

#### Module: `import_sources_from_folder`
> Import research sources from a folder into the database.
*Line 0*  

#### Function: `infer_kind`
*Line 25*  

#### Function: `main`
*Line 36*  

### 📄 hypercode_backup_20251205_183301\archive\new-files-to-check\backend\research\scripts\seed_basic_data.py

#### Module: `seed_basic_data`
> Seed the research database with initial data.
*Line 0*  

#### Function: `main`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\code_insights.py

#### Function: `analyze_code_patterns`
> Analyze function and class naming patterns.
*Line 8*  

#### Function: `find_undocumented_code`
> Find complex but undocumented code.
*Line 29*  

#### Function: `analyze_test_coverage`
> Analyze test coverage patterns.
*Line 45*  

### 📄 hypercode_backup_20251205_183301\code_quality_report.py

#### Module: `code_quality_report`
> Code Quality Analysis for Hypercode Project
*Line 0*  

#### Function: `get_undocumented_classes_priority`
> Get undocumented classes sorted by importance (more methods = higher priority).
*Line 15*  

#### Function: `get_least_tested_files`
> Get files with most code but least test coverage.
*Line 33*  

#### Function: `find_getter_methods`
> Find get_ methods that could be converted to properties.
*Line 69*  

#### Function: `generate_code_quality_report`
> Generate a comprehensive code quality report.
*Line 103*  

### 📄 hypercode_backup_20251205_183301\core\benchmarks\__init__.py

#### Function: `benchmark_lexer`
> Benchmark the lexer with the given source code.
*Line 12*  

#### Function: `print_benchmark_results`
> Print benchmark results in a readable format.
*Line 36*  

### 📄 hypercode_backup_20251205_183301\core\benchmarks\benchmarks_lexer.py

#### Function: `benchmark_lexer`
> Benchmark the lexer with the given source code.
*Line 6*  

#### Function: `print_benchmark_results`
> Print benchmark results in a readable format.
*Line 30*  

### 📄 hypercode_backup_20251205_183301\core\src\ai_gateway\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\ai_gateway\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\ai_gateway\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\ai_gateway\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\ai_gateway\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\ai_gateway\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\ai_gateway\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\build.py

#### Module: `build`
> Build script for the HyperCode language.
*Line 0*  

#### Function: `build`
> Builds a HyperCode source file to the target language.
*Line 34*  

### 📄 hypercode_backup_20251205_183301\core\src\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\core\__init__.py

#### Module: `__init__`
> HyperCode Core Module
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\ast.py

#### Module: `ast`
> Abstract Syntax Tree (AST) for HyperCode.
*Line 0*  

#### Class: `Node`
> Base class for all AST nodes.
*Line 11*  

#### Class: `Program`
> Represents a complete HyperCode program.
*Line 18*  

#### Class: `Function`
> Represents a function definition.
*Line 25*  

#### Class: `VariableDeclaration`
> Represents a variable declaration.
*Line 34*  

#### Class: `Literal`
> Represents a literal value (number, string, boolean, etc.).
*Line 42*  

#### Class: `BinaryOp`
> Represents a binary operation (e.g., 1 + 2).
*Line 50*  

#### Class: `UnaryOp`
> Represents a unary operation (e.g., -1 or !true).
*Line 59*  

#### Class: `Variable`
> Represents a variable reference.
*Line 67*  

#### Class: `Call`
> Represents a function call.
*Line 74*  

#### Class: `Return`
> Represents a return statement.
*Line 82*  

#### Class: `Block`
> Represents a block of statements.
*Line 89*  

#### Class: `If`
> Represents an if statement.
*Line 96*  

#### Class: `While`
> Represents a while loop.
*Line 105*  

#### Class: `For`
> Represents a for loop.
*Line 113*  

#### Class: `Assign`
> Represents a variable assignment.
*Line 123*  

#### Class: `Logical`
> Represents a logical operation (and/or).
*Line 131*  

### 📄 hypercode_backup_20251205_183301\core\src\core\ast_nodes.py

#### Module: `ast_nodes`
> Abstract Syntax Tree (AST) nodes for the HyperCode language.
*Line 0*  

#### Class: `Node`
> Base class for all AST nodes.
*Line 24*  

#### Class: `Expression`
> Base class for all expression nodes.
*Line 31*  

#### Class: `Statement`
> Base class for all statement nodes.
*Line 38*  

#### Class: `Program`
> Represents the entire program as a list of statements.
*Line 45*  

#### Class: `Identifier`
> Represents an identifier (e.g., a variable name).
*Line 52*  

#### Class: `Literal`
> Represents a literal value (e.g., number, string).
*Line 59*  

#### Class: `VariableDeclaration`
> Represents a variable declaration (let or const).
*Line 66*  

#### Class: `BinaryOperation`
> Represents a binary operation (e.g., a + b).
*Line 75*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\DuelCode\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\accessibility\adhd_optimizer.py

#### Module: `adhd_optimizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\accessibility\autism_preset.py

#### Module: `autism_preset`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\accessibility\dyslexia_formatter.py

#### Module: `dyslexia_formatter`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\accessibility\sensory_customizer.py

#### Module: `sensory_customizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\accessibility\wcag_auditor.py

#### Module: `wcag_auditor`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\ai_gateway\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\code_analyzer_ai.py

#### Module: `code_analyzer_ai`
> Perplexity AI Code Analyzer for HyperCode
*Line 0*  

#### Class: `CodeAnalyzerAI`
> AI-powered code analyzer for HyperCode
*Line 20*  

#### Function: `__init__`
*Line 23*  

#### Function: `analyze_file`
> Analyze a Python file with AI assistance
*Line 26*  

#### Function: `_analyze_complexity`
> Analyze code complexity indicators
*Line 73*  

#### Function: `_check_docstrings`
> Check for docstring coverage
*Line 114*  

#### Function: `_get_ai_code_analysis`
> Get AI analysis of code from Perplexity
*Line 156*  

#### Function: `analyze_project`
> Analyze entire project
*Line 184*  

#### Function: `_get_project_ai_insights`
> Get AI insights for the entire project
*Line 231*  

#### Function: `save_analysis`
> Save analysis to file
*Line 263*  

#### Function: `print_summary`
> Print analysis summary
*Line 271*  

#### Function: `main`
> Main function
*Line 289*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\debug_search.py

#### Module: `debug_search`
> Debug search results
*Line 0*  

#### Function: `debug_search`
> Debug why space data isn't being found
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\demo_ai_research.py

#### Module: `demo_ai_research`
> HyperCode AI Research + Perplexity Integration Demo
*Line 0*  

#### Function: `demo_ai_research_queries`
> Demonstrate AI Research integration with Perplexity
*Line 16*  

#### Function: `test_document_specific_queries`
> Test queries specific to the HyperCode AI Research document
*Line 90*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\demo_enhanced_client.py

#### Module: `demo_enhanced_client`
> Demo: Enhanced Perplexity Client with Knowledge Base
*Line 0*  

#### Function: `demo_knowledge_base_integration`
> Demonstrate the knowledge base integration
*Line 16*  

#### Function: `demonstrate_memory_persistence`
> Demonstrate that the knowledge base persists between sessions
*Line 131*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\final_integration_test.py

#### Module: `final_integration_test`
> Final Test: Complete Perplexity Space Integration
*Line 0*  

#### Function: `final_integration_test`
> Complete test of the Perplexity Space integration
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\health_scanner_ai.py

#### Module: `health_scanner_ai`
> HyperCode Health Scanner with Perplexity AI Integration
*Line 0*  

#### Class: `HealthScannerAI`
> AI-powered health scanner for HyperCode project
*Line 19*  

#### Function: `__init__`
*Line 22*  

#### Function: `analyze_project_structure`
> Analyze project structure and identify health issues
*Line 26*  

#### Function: `analyze_dependencies`
> Analyze dependency management
*Line 69*  

#### Function: `analyze_security`
> Analyze security configuration
*Line 111*  

#### Function: `get_ai_recommendations`
> Get AI-powered recommendations based on health scan
*Line 144*  

#### Function: `run_full_scan`
> Run complete health scan with AI analysis
*Line 171*  

#### Function: `save_report`
> Save health scan report to file
*Line 222*  

#### Function: `print_summary`
> Print a summary of the health scan
*Line 228*  

#### Function: `main`
> Main function to run the health scanner
*Line 248*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\import-helper.py

#### Module: `import-helper`
> HyperCode Perplexity Space Import Helper
*Line 0*  

#### Class: `SpaceImportHelper`
> Helper class for managing Perplexity Space imports
*Line 13*  

#### Function: `__init__`
*Line 16*  

#### Function: `validate_document`
> Validate a document structure
*Line 21*  

#### Function: `load_template`
> Load documents from JSON template file
*Line 63*  

#### Function: `validate_all`
> Validate all loaded documents
*Line 83*  

#### Function: `generate_report`
> Generate a validation report
*Line 95*  

#### Function: `create_import_script`
> Generate a Python script to import the data
*Line 141*  

#### Function: `create_template_instructions`
> Generate detailed instructions for filling the template
*Line 193*  

#### Function: `main`
> CLI interface for the import helper
*Line 264*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\import_all_space_data.py

#### Module: `import_all_space_data`
> Complete Import of HyperCode Space Data
*Line 0*  

#### Function: `format_content`
> Recursively format nested data into readable text
*Line 16*  

#### Function: `import_all_hypercode_data`
> Import all sections of your HyperCode Space data
*Line 41*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\import_hypercode_data.py

#### Module: `import_hypercode_data`
> Import HyperCode Space Data
*Line 0*  

#### Function: `import_hypercode_space_data`
> Import your actual HyperCode Space data
*Line 16*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\import_perplexity_space.py

#### Module: `import_perplexity_space`
> Perplexity Space Data Importer
*Line 0*  

#### Function: `create_manual_import_script`
> Create a script for manual data entry from Perplexity Space
*Line 17*  

#### Function: `create_json_import_template`
> Create a JSON template for importing data
*Line 86*  

#### Function: `import_from_json`
> Import data from JSON file
*Line 115*  

#### Function: `test_imported_data`
> Test the imported data with context-aware queries
*Line 153*  

#### Function: `show_import_menu`
> Show the import menu
*Line 188*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\knowledge_graph\graph_builder.py

#### Module: `graph_builder`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\knowledge_graph\sparql_query.py

#### Module: `sparql_query`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\knowledge_graph\update_agent.py

#### Module: `update_agent`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\live_research\doc_generator.py

#### Module: `doc_generator`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\live_research\github_publisher.py

#### Module: `github_publisher`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\live_research\paper_indexer.py

#### Module: `paper_indexer`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\live_research\research_crawler.py

#### Module: `research_crawler`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\live_research\synthesis_engine.py

#### Module: `synthesis_engine`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\__init__.py

#### Module: `__init__`
> HyperCode MCP (Model Context Protocol) Server Package
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\__init__.py

#### Module: `__init__`
> MCP Servers Package
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\aws_cli.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\aws_resource_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\code_analysis.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\dataset_downloader.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\file_system.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\human_input.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\hypercode_syntax.py

#### Module: `hypercode_syntax`
> HyperCode Syntax MCP Server
*Line 0*  

#### Class: `HyperCodeSyntaxServer`
> 🎨 MCP Server for HyperCode Visual Syntax Integration
*Line 28*  

#### Function: `__init__`
*Line 31*  

#### Function: `handle_request`
> Handle MCP requests from IDE
*Line 35*  

#### Function: `_initialize`
> Initialize the MCP server
*Line 56*  

#### Function: `_document_changed`
> Handle document changes for real-time parsing
*Line 79*  

#### Function: `_text_hover`
> Provide hover information for semantic annotations
*Line 98*  

#### Function: `_completion`
> Provide completion for semantic annotations
*Line 121*  

#### Function: `_parse_document`
> Parse entire document and return semantic structure
*Line 150*  

#### Function: `_validate_neurodiversity`
> Validate neurodiversity compliance and provide suggestions
*Line 179*  

#### Function: `_generate_diagnostics`
> Generate IDE diagnostics from parsed functions
*Line 216*  

#### Function: `_get_annotation_hover_info`
> Generate hover information for semantic annotations
*Line 266*  

#### Function: `main`
> Main MCP server loop
*Line 294*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\path_service.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\user_profile_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\valkey_service.py

#### Function: `check_redis_connection`
*Line 40*  

#### Function: `health_check`
> Health check endpoint to verify that the service is running.
*Line 59*  

#### Function: `set_key`
> Set a value for a given key. The value should be a JSON object.
*Line 67*  

#### Function: `get_key`
> Get the value for a given key.
*Line 80*  

#### Function: `hset_key`
> Set a field (key) in a hash (name). The value should be a JSON object.
*Line 95*  

#### Function: `hget_key`
> Get a field (key) from a hash (name).
*Line 107*  

#### Function: `hgetall_hash`
> Get all fields and values for a given hash name.
*Line 126*  

#### Function: `main`
> Main function to run the Valkey Service MCP Server.
*Line 144*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\servers\web_search.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\setup.py

#### Module: `setup`
> MCP Setup Script
*Line 0*  

#### Function: `install_dependencies`
> Install required dependencies
*Line 16*  

#### Function: `verify_setup`
> Verify that MCP is properly set up
*Line 31*  

#### Function: `show_next_steps`
> Show next steps for using MCP
*Line 54*  

#### Function: `main`
*Line 72*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\start_servers.py

#### Module: `start_servers`
> MCP Servers Startup Script
*Line 0*  

#### Function: `start_server`
> Start a specific MCP server
*Line 34*  

#### Function: `list_servers`
> List all available servers
*Line 59*  

#### Function: `main`
*Line 66*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\mcp\test_mcp.py

#### Module: `test_mcp`
> MCP Servers Test Script
*Line 0*  

#### Function: `test_server_imports`
> Test that all servers can be imported
*Line 15*  

#### Function: `main`
*Line 47*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\perplexity_space_collector.py

#### Module: `perplexity_space_collector`
> Perplexity Space Data Collector
*Line 0*  

#### Function: `quick_copy_paste_collector`
> Quick collector for copy-paste workflow
*Line 18*  

#### Function: `create_structured_template`
> Create a structured JSON template for bulk import
*Line 117*  

#### Function: `show_bro_hacks`
> Show BROski's pro tips
*Line 167*  

#### Function: `main_menu`
> Main menu for the collector
*Line 207*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\perplexity_space_integration.py

#### Module: `perplexity_space_integration`
> Perplexity Space Integration Guide
*Line 0*  

#### Function: `main`
*Line 16*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\scripts\style_guide_collector.py

#### Module: `style_guide_collector`
> 🎨 HyperCode Style Guide Feedback Collector
*Line 0*  

#### Class: `StyleGuideCollector`
> 🎨 Collects and analyzes style guide feedback from the community
*Line 16*  

#### Function: `__init__`
*Line 19*  

#### Function: `_load_feedback`
> 📂 Load existing feedback data
*Line 30*  

#### Function: `_save_feedback`
> 💾 Save feedback data
*Line 49*  

#### Function: `add_feedback`
> 📝 Add new feedback entry
*Line 58*  

#### Function: `_update_analysis`
> 📊 Update analysis based on new feedback
*Line 100*  

#### Function: `analyze_feedback`
> 📊 Generate comprehensive analysis of all feedback
*Line 149*  

#### Function: `_get_top_items`
> 📊 Get top items from a frequency dictionary
*Line 187*  

#### Function: `_calculate_consensus`
> 📊 Calculate consensus for preference categories
*Line 210*  

#### Function: `_generate_recommendations`
> 💡 Generate style guide recommendations based on feedback
*Line 243*  

#### Function: `import_github_issues`
> 📥 Import feedback from GitHub issues
*Line 323*  

#### Function: `generate_report`
> 📊 Generate comprehensive feedback report
*Line 346*  

#### Function: `interactive_feedback`
> 🎯 Interactive feedback collection from command line
*Line 413*  

#### Function: `main`
> 🚀 Main entry point
*Line 521*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\scripts\test_perplexity_api.py

#### Module: `test_perplexity_api`
> Test script for Perplexity API integration.
*Line 0*  

#### Function: `main`
> Test the Perplexity API connection and make a sample query.
*Line 17*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\build.py

#### Module: `build`
> Build script for the HyperCode language.
*Line 0*  

#### Function: `build`
> Builds a HyperCode source file to the target language.
*Line 34*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\core\ast_nodes.py

#### Module: `ast_nodes`
> Abstract Syntax Tree (AST) nodes for the HyperCode language.
*Line 0*  

#### Class: `Node`
> Base class for all AST nodes.
*Line 24*  

#### Class: `Expression`
> Base class for all expression nodes.
*Line 31*  

#### Class: `Statement`
> Base class for all statement nodes.
*Line 38*  

#### Class: `Program`
> Represents the entire program as a list of statements.
*Line 45*  

#### Class: `Identifier`
> Represents an identifier (e.g., a variable name).
*Line 52*  

#### Class: `Literal`
> Represents a literal value (e.g., number, string).
*Line 59*  

#### Class: `VariableDeclaration`
> Represents a variable declaration (let or const).
*Line 66*  

#### Class: `BinaryOperation`
> Represents a binary operation (e.g., a + b).
*Line 75*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\core\lexer.py

#### Module: `lexer`
> HyperCode Lexer Module
*Line 0*  

#### Class: `LexerError`
> Represents a lexical analysis error.
*Line 15*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode programming language.
*Line 32*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 49*  

#### Function: `tokenize`
> Convert the source code into a list of tokens.
*Line 110*  

#### Function: `is_at_end`
*Line 134*  

#### Function: `scan_token`
> Scan the next token from the source code.
*Line 137*  

#### Function: `advance`
*Line 228*  

#### Function: `add_token`
> Add a new token to the tokens list.
*Line 233*  

#### Function: `error`
> Record a lexing error.
*Line 246*  

#### Function: `synchronize`
> Synchronize after an error by skipping tokens until we find a statement boundary.
*Line 262*  

#### Function: `previous`
> Return the previous character.
*Line 274*  

#### Function: `peek_next`
> Look ahead two characters.
*Line 280*  

#### Function: `match`
*Line 286*  

#### Function: `peek`
*Line 295*  

#### Function: `string`
> Parse a string literal.
*Line 300*  

#### Function: `is_digit`
> Check if a character is a digit (0-9).
*Line 362*  

#### Function: `number`
> Parse a number literal (integer or float).
*Line 366*  

#### Function: `is_alpha`
> Check if a character is alphabetic or underscore.
*Line 421*  

#### Function: `is_alphanumeric`
> Check if a character is alphanumeric or underscore.
*Line 425*  

#### Function: `is_hex_digit`
> Check if a character is a valid hexadecimal digit.
*Line 429*  

#### Function: `identifier`
> Parse an identifier or keyword.
*Line 433*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\core\parser.py

#### Class: `ParseError`
*Line 8*  

#### Class: `Parser`
*Line 12*  

#### Function: `__init__`
*Line 13*  

#### Function: `parse`
> Parse the entire program.
*Line 17*  

#### Function: `declaration`
*Line 26*  

#### Function: `var_declaration`
*Line 39*  

#### Function: `statement`
*Line 64*  

#### Function: `print_statement`
*Line 71*  

#### Function: `expression_statement`
*Line 76*  

#### Function: `block`
*Line 81*  

#### Function: `expression`
*Line 88*  

#### Function: `assignment`
*Line 91*  

#### Function: `equality`
*Line 106*  

#### Function: `comparison`
*Line 116*  

#### Function: `term`
*Line 129*  

#### Function: `factor`
*Line 137*  

#### Function: `unary`
*Line 145*  

#### Function: `primary`
*Line 152*  

#### Function: `match`
*Line 184*  

#### Function: `consume`
*Line 191*  

#### Function: `error`
*Line 201*  

#### Function: `synchronize`
*Line 207*  

#### Function: `check`
*Line 227*  

#### Function: `advance`
*Line 232*  

#### Function: `is_at_end`
*Line 237*  

#### Function: `peek`
*Line 240*  

#### Function: `previous`
*Line 243*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode-backend-js-COMPLETE.py

#### Module: `hypercode-backend-js-COMPLETE`
> HyperCode JavaScript Backend - Complete Implementation
*Line 0*  

#### Class: `JSCompiler`
> Compiles HyperCode AST to JavaScript.
*Line 19*  

#### Function: `__init__`
> Initialize compiler.
*Line 30*  

#### Function: `compile`
> Compile AST to JavaScript.
*Line 42*  

#### Function: `_generate_header`
> Generate JavaScript header
*Line 65*  

#### Function: `_generate_setup`
> Generate setup code (memory tape, pointer, I/O)
*Line 74*  

#### Function: `_generate_main`
> Generate JavaScript for AST node.
*Line 110*  

#### Function: `_generate_footer`
> Generate JavaScript footer
*Line 162*  

#### Function: `_indent`
> Get current indentation
*Line 179*  

#### Function: `optimize_ast`
> Optimize AST (future: loop unrolling, dead code elimination).
*Line 183*  

#### Function: `main`
> CLI interface for JavaScript backend
*Line 200*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode-idea-generator-WEB.py

#### Module: `hypercode-idea-generator-WEB`
> HyperCode Community Idea Generator - Web Interface (HTML/CSS/JS)
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode-launch-kit.py

#### Module: `hypercode-launch-kit`
> HyperCode Launch Kit - Ultimate System Initialization
*Line 0*  

#### Class: `HyperCodeLaunchKit`
> Complete launch system initialization
*Line 23*  

#### Function: `__init__`
*Line 26*  

#### Function: `create_readme`
> Create the ultimate README.md
*Line 30*  

#### Function: `create_launch_checklist`
> Create launch day checklist
*Line 367*  

#### Function: `create_launch_script`
> Create automated launch script
*Line 620*  

#### Function: `create_first_30_days`
> Create 30-day success roadmap
*Line 718*  

#### Function: `print_summary`
> Print beautiful summary
*Line 974*  

#### Function: `main`
> Run launch kit initialization
*Line 1007*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode-lexer-COMPLETE.py

#### Module: `hypercode-lexer-COMPLETE`
> HyperCode Lexer - Complete Implementation
*Line 0*  

#### Class: `TokenType`
> HyperCode token types - minimal yet powerful
*Line 21*  

#### Class: `Token`
> Represents a single token with position tracking
*Line 45*  

#### Function: `__repr__`
> Neurodivergent-friendly representation
*Line 54*  

#### Class: `LexerError`
> Lexer-specific errors with context
*Line 59*  

#### Function: `__init__`
*Line 62*  

#### Class: `HyperCodeLexer`
> Tokenizes HyperCode programs with accessibility features.
*Line 69*  

#### Function: `__init__`
> Initialize lexer with source code.
*Line 95*  

#### Function: `tokenize`
> Convert HyperCode source to token stream.
*Line 110*  

#### Function: `_advance_position`
> Update position tracking after processing character
*Line 169*  

#### Function: `_skip_comment`
> Skip characters until end of line
*Line 179*  

#### Function: `get_tokens`
> Return current token list
*Line 184*  

#### Function: `filter_tokens`
> Get tokens excluding certain types.
*Line 188*  

#### Function: `print_tokens`
> Print tokens in readable format.
*Line 205*  

#### Function: `get_statistics`
> Get token statistics (useful for analysis).
*Line 236*  

#### Function: `main`
> CLI interface for the lexer
*Line 250*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode-parser-COMPLETE.py

#### Module: `hypercode-parser-COMPLETE`
> HyperCode Parser - Complete Implementation
*Line 0*  

#### Class: `NodeType`
> AST Node types
*Line 22*  

#### Class: `ASTNode`
> Abstract Syntax Tree Node.
*Line 38*  

#### Function: `__repr__`
> Pretty-print AST (neurodivergent-friendly)
*Line 51*  

#### Class: `ParserError`
> Parser-specific errors with context
*Line 68*  

#### Function: `__init__`
*Line 71*  

#### Class: `HyperCodeParser`
> Parses HyperCode token stream into AST.
*Line 80*  

#### Function: `__init__`
> Initialize parser with token stream.
*Line 94*  

#### Function: `parse`
> Parse tokens into AST.
*Line 105*  

#### Function: `_parse_statement`
> Parse a single statement
*Line 127*  

#### Function: `_parse_loop`
> Parse loop structure: [ statements ]
*Line 174*  

#### Function: `_advance`
> Move to next token
*Line 209*  

#### Function: `_is_at_end`
> Check if at end of token stream
*Line 215*  

#### Function: `validate`
> Validate AST structure.
*Line 222*  

#### Function: `print_ast`
> Print AST in readable format.
*Line 237*  

#### Function: `main`
> CLI interface for the parser
*Line 251*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\__init__.py

#### Module: `__init__`
> HyperCode - A neurodivergent-first programming language with AI compatibility.
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\__main__.py

#### Function: `main`
*Line 6*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\config.py

#### Module: `config`
> Configuration module for HyperCode.
*Line 0*  

#### Class: `Config`
> Configuration class for HyperCode
*Line 16*  

#### Function: `get_headers`
> Get headers for API requests
*Line 27*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\__init__.py

#### Module: `__init__`
> Core package for the HyperCode language implementation.
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\ast.py

#### Class: `Node`
*Line 9*  

#### Function: `accept`
*Line 10*  

#### Class: `Expr`
*Line 20*  

#### Class: `Literal`
*Line 25*  

#### Class: `Variable`
*Line 30*  

#### Class: `Assign`
*Line 35*  

#### Class: `Binary`
*Line 41*  

#### Class: `Unary`
*Line 48*  

#### Class: `Grouping`
*Line 54*  

#### Class: `Call`
*Line 59*  

#### Class: `Get`
*Line 66*  

#### Class: `Stmt`
*Line 73*  

#### Class: `Expression`
*Line 78*  

#### Class: `Print`
*Line 83*  

#### Class: `Var`
*Line 88*  

#### Class: `Block`
*Line 94*  

#### Class: `Intent`
*Line 99*  

#### Class: `Program`
*Line 106*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\cli.py

#### Module: `cli`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\error_handler.py

#### Function: `report_parse_error`
*Line 5*  

#### Function: `report`
*Line 12*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\lexer.py

#### Module: `lexer`
> Core HyperCode language implementation - Lexer
*Line 0*  

#### Class: `LexerError`
> Exception raised for errors in the lexer.
*Line 32*  

#### Function: `__init__`
*Line 35*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode language.
*Line 42*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 109*  

#### Function: `tokenize`
> Convert source code into a list of tokens.
*Line 126*  

#### Function: `_match_patterns`
> Try to match the current position against all token patterns.
*Line 161*  

#### Function: `_update_position`
> Update line and column numbers based on the given text.
*Line 187*  

#### Function: `_add_token`
> Add a token to the token list.
*Line 206*  

#### Function: `_handle_unknown`
> Handle unknown characters in the source.
*Line 270*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\parser.py

#### Class: `ParseError`
*Line 24*  

#### Class: `Parser`
*Line 28*  

#### Function: `__init__`
*Line 29*  

#### Function: `parse`
> Parse the entire program.
*Line 33*  

#### Function: `declaration`
*Line 42*  

#### Function: `var_declaration`
*Line 51*  

#### Function: `statement`
*Line 67*  

#### Function: `print_statement`
*Line 76*  

#### Function: `intent_statement`
*Line 81*  

#### Function: `expression_statement`
*Line 96*  

#### Function: `block`
*Line 101*  

#### Function: `expression`
*Line 108*  

#### Function: `assignment`
*Line 111*  

#### Function: `equality`
*Line 126*  

#### Function: `comparison`
*Line 136*  

#### Function: `term`
*Line 149*  

#### Function: `factor`
*Line 157*  

#### Function: `unary`
*Line 165*  

#### Function: `primary`
*Line 172*  

#### Function: `_primary`
*Line 189*  

#### Function: `finish_call`
*Line 220*  

#### Function: `match`
*Line 233*  

#### Function: `consume`
*Line 240*  

#### Function: `error`
*Line 247*  

#### Function: `synchronize`
*Line 253*  

#### Function: `check`
*Line 273*  

#### Function: `advance`
*Line 278*  

#### Function: `is_at_end`
*Line 283*  

#### Function: `peek`
*Line 286*  

#### Function: `previous`
*Line 289*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\semantic_analyzer.py

#### Module: `semantic_analyzer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\core\tokens.py

#### Class: `TokenType`
*Line 6*  

#### Class: `Token`
*Line 61*  

#### Function: `__str__`
*Line 68*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\enhanced_perplexity_client.py

#### Module: `enhanced_perplexity_client`
> Enhanced Perplexity Client with Knowledge Base Integration
*Line 0*  

#### Class: `EnhancedPerplexityClient`
> Enhanced Perplexity client with knowledge base integration
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `query_with_context`
> Send a query with relevant knowledge base context
*Line 25*  

#### Function: `add_research_data`
> Add research data to the knowledge base
*Line 61*  

#### Function: `search_research_data`
> Search the knowledge base
*Line 71*  

#### Function: `list_research_documents`
> List all research documents
*Line 75*  

#### Function: `get_document`
> Get a specific document
*Line 79*  

#### Function: `delete_document`
> Delete a document
*Line 83*  

#### Function: `import_from_perplexity_space`
> Import data from Perplexity Space export
*Line 87*  

#### Function: `test_context_integration`
> Test the context integration
*Line 123*  

#### Function: `create_perplexity_space_import_template`
> Create a template for importing Perplexity Space data
*Line 175*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\knowledge_base.py

#### Module: `knowledge_base`
> HyperCode Knowledge Base - Perplexity Space Integration
*Line 0*  

#### Class: `ResearchDocument`
> Represents a research document from Perplexity Space
*Line 17*  

#### Function: `__post_init__`
*Line 28*  

#### Function: `generate_id`
> Generate unique ID from content hash
*Line 36*  

#### Function: `validate`
> Validate document data
*Line 41*  

#### Function: `update_timestamp`
> Update the last_updated timestamp
*Line 53*  

#### Class: `HyperCodeKnowledgeBase`
> Knowledge base for HyperCode research data
*Line 100*  

#### Function: `__init__`
*Line 103*  

#### Function: `load`
> Load knowledge base from file
*Line 109*  

#### Function: `save`
> Save knowledge base to file
*Line 125*  

#### Function: `add_document`
> Add a new research document
*Line 135*  

#### Function: `search_documents`
> Search documents by query
*Line 163*  

#### Function: `get_context_for_query`
> Get relevant context for a query
*Line 226*  

#### Function: `list_documents`
> List all documents
*Line 256*  

#### Function: `get_document`
> Get a specific document by ID
*Line 260*  

#### Function: `delete_document`
> Delete a document
*Line 264*  

#### Function: `update_document`
> Update an existing document
*Line 272*  

#### Function: `search_by_tags`
> Search documents by tags with AND/OR operators
*Line 286*  

#### Function: `get_document_statistics`
> Get statistics about the knowledge base
*Line 305*  

#### Function: `export_format`
> Export knowledge base in different formats
*Line 330*  

#### Function: `validate_all_documents`
> Validate all documents and return list of errors
*Line 352*  

#### Function: `cleanup_duplicates`
> Remove duplicate documents based on content hash
*Line 362*  

#### Function: `initialize_sample_data`
> Initialize with sample HyperCode research data
*Line 383*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\perplexity_client.py

#### Module: `perplexity_client`
> Perplexity AI API client for HyperCode.
*Line 0*  

#### Class: `PerplexityClient`
> Client for interacting with Perplexity AI API
*Line 12*  

#### Function: `__init__`
> Initialize the Perplexity client.
*Line 15*  

#### Function: `query`
> Send a query to the Perplexity API.
*Line 30*  

#### Function: `test_connection`
> Test the connection to the Perplexity API
*Line 72*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode\repl.py

#### Function: `run_repl`
*Line 7*  

#### Function: `run`
*Line 22*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode_idea_generator.py

#### Module: `hypercode_idea_generator`
> HyperCode Idea Generator - AI-Powered Community Input System
*Line 0*  

#### Class: `HyperCodeIdeaGenerator`
> AI-Powered Idea Generator for HyperCode community input.
*Line 431*  

#### Function: `__init__`
*Line 439*  

#### Function: `get_ideas_by_category`
> Get ideas by category and optionally by difficulty level.
*Line 443*  

#### Function: `get_top_ideas`
> Get most-voted ideas across all categories.
*Line 468*  

#### Function: `vote_for_idea`
> Vote for an idea.
*Line 487*  

#### Function: `get_trending_ideas`
> Get trending ideas (high votes + recent activity).
*Line 497*  

#### Function: `format_idea_card`
> Format idea for display.
*Line 502*  

#### Function: `main`
> Interactive idea generator CLI
*Line 528*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode_lexer_fixed.py

#### Module: `hypercode_lexer_fixed`
> HyperCode Lexer - Fixed String Handling with Escape Sequences
*Line 0*  

#### Class: `TokenType`
> HyperCode token types
*Line 19*  

#### Class: `Token`
> Represents a single token with position tracking
*Line 44*  

#### Function: `__repr__`
> Readable representation
*Line 54*  

#### Class: `LexerError`
> Lexer error with context
*Line 68*  

#### Function: `__init__`
*Line 71*  

#### Class: `HyperCodeLexerFixed`
> Fixed lexer with proper string escape sequence handling.
*Line 84*  

#### Function: `__init__`
> Initialize lexer.
*Line 125*  

#### Function: `tokenize`
> Convert source to token stream.
*Line 145*  

#### Function: `_parse_string`
> Parse string literal with escape sequence handling.
*Line 217*  

#### Function: `_skip_comment`
> Skip comment until end of line
*Line 300*  

#### Function: `_advance`
> Update position after processing character
*Line 305*  

#### Function: `print_tokens`
> Print tokens in readable format
*Line 315*  

#### Function: `run_tests`
> Comprehensive test suite
*Line 329*  

#### Function: `main`
> Main entry point
*Line 446*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\hypercode_poc.py

#### Module: `hypercode_poc`
> HyperCode POC - Neurodivergent-First Programming Language
*Line 0*  

#### Class: `TokenType`
> Brainfuck-inspired core + modern aliases
*Line 18*  

#### Class: `Token`
*Line 34*  

#### Class: `UserConfidenceLevel`
*Line 41*  

#### Class: `EnhancedLexer`
> Smart tokenizer with escape handling + accessibility focus
*Line 48*  

#### Function: `__init__`
*Line 51*  

#### Function: `tokenize`
*Line 74*  

#### Function: `handle_string`
*Line 115*  

#### Function: `handle_number`
*Line 141*  

#### Function: `handle_identifier`
*Line 149*  

#### Function: `advance`
*Line 171*  

#### Class: `ContextAwareErrorMessenger`
> Friendly, adaptive error messages
*Line 176*  

#### Function: `__init__`
*Line 179*  

#### Function: `format_error`
*Line 182*  

#### Class: `SemanticContextStreamer`
> Understand programmer intent from tokens
*Line 189*  

#### Function: `analyze`
*Line 192*  

#### Class: `ConfidenceTracker`
> Adapt system guidance to user skill level
*Line 209*  

#### Function: `__init__`
*Line 212*  

#### Function: `record`
*Line 216*  

#### Class: `HyperCodePOC`
> Main system: Lexer + Error Messenger + Semantic Analyzer + Confidence Tracker
*Line 222*  

#### Function: `__init__`
*Line 225*  

#### Function: `compile`
*Line 232*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\debug_ascii.py

#### Module: `debug_ascii`
> ASCII-only debug
*Line 0*  

#### Function: `test_regex_patterns`
> Test regex patterns directly
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\debug_full.py

#### Module: `debug_full`
> Debug the full parsing flow
*Line 0*  

#### Function: `debug_full_parsing`
> Debug the full parsing flow
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\debug_parser.py

#### Module: `debug_parser`
> Debug the Visual Syntax Parser - Find what's wrong with annotation detection
*Line 0*  

#### Function: `debug_annotation_detection`
> Debug why annotations aren't being detected
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\debug_simple.py

#### Module: `debug_simple`
> Simple debug without emoji characters
*Line 0*  

#### Function: `debug_simple`
> Debug without emoji characters
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\test_parser.py

#### Module: `test_parser`
> Test the Visual Syntax Parser - First Click Moment Demo
*Line 0*  

#### Function: `test_first_click_moment`
> Test the parser with the first click moment example
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\parser\visual_syntax_parser.py

#### Module: `visual_syntax_parser`
> 🎨 Visual Syntax Parser for HyperCode V3
*Line 0*  

#### Class: `SemanticMarker`
> 🎨 Semantic marker types with emoji representations
*Line 18*  

#### Class: `SemanticAnnotation`
> 📋 A single semantic annotation with its metadata
*Line 37*  

#### Function: `__str__`
*Line 46*  

#### Class: `ParsedFunction`
> 🔍 A fully parsed HyperCode function
*Line 51*  

#### Function: `get_annotations_by_type`
> Get all annotations of a specific type
*Line 62*  

#### Class: `VisualSyntaxParser`
> 🎨 Main parser for HyperCode's visual semantic syntax
*Line 69*  

#### Function: `__init__`
*Line 72*  

#### Function: `_build_semantic_patterns`
> 🔍 Build regex patterns for all semantic markers
*Line 76*  

#### Function: `_build_color_scheme`
> 🎨 Build semantic color mapping for IDE highlighting
*Line 105*  

#### Function: `parse_file`
> 📄 Parse an entire HyperCode file
*Line 123*  

#### Function: `parse_content`
> 📝 Parse HyperCode content string
*Line 130*  

#### Function: `_is_function_definition`
> 🔍 Check if line is a function definition
*Line 170*  

#### Function: `_start_new_function`
> 🆕 Create new ParsedFunction from definition line
*Line 179*  

#### Function: `_parse_line_annotations`
> � Parse semantic annotations from a line
*Line 202*  

#### Function: `_parse_annotation_params`
> 🔧 Parse annotation parameters from string
*Line 223*  

#### Function: `generate_syntax_highlighting`
> 🎨 Generate HTML with syntax highlighting for visual markers
*Line 265*  

#### Function: `extract_semantic_summary`
> 📊 Extract semantic summary for analysis
*Line 277*  

#### Function: `validate_neurodiversity_compliance`
> 🧠 Validate neurodiversity-first design principles
*Line 311*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\scaffold (1).py

#### Module: `scaffold (1)`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 141*  

#### Function: `create_python_files`
> Create all Python files with proper __init__.py structure.
*Line 151*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 165*  

#### Function: `create_root_files`
> Create root-level configuration files as empty placeholders.
*Line 202*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 213*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 234*  

#### Function: `main`
> Main scaffolding function.
*Line 259*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\src\scaffold.py

#### Module: `scaffold`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 153*  

#### Function: `create_python_files`
> Create all Python files with proper docstrings and structure.
*Line 184*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 254*  

#### Function: `create_root_files`
> Create root-level configuration files with appropriate content.
*Line 291*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 541*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 583*  

#### Function: `main`
> Main scaffolding function.
*Line 621*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\test_intent_blocks.py

#### Module: `test_intent_blocks`
> Test script for Intent Blocks implementation
*Line 0*  

#### Function: `test_intent_block`
> Test parsing of intent blocks
*Line 13*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 183*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\benchmark_knowledge_base.py

#### Module: `benchmark_knowledge_base`
> Performance Benchmark Tool for HyperCode Knowledge Base
*Line 0*  

#### Class: `BenchmarkSuite`
> Comprehensive benchmark suite for Knowledge Base
*Line 24*  

#### Function: `__init__`
*Line 27*  

#### Function: `_get_system_info`
> Get system information for benchmark context
*Line 34*  

#### Function: `generate_test_data`
> Generate test data of specified size
*Line 43*  

#### Function: `benchmark_operation`
> Benchmark a single operation
*Line 93*  

#### Function: `run_benchmark_suite`
> Run complete benchmark suite
*Line 118*  

#### Function: `_calculate_summary`
> Calculate summary statistics
*Line 274*  

#### Function: `_generate_recommendations`
> Generate performance recommendations
*Line 296*  

#### Function: `generate_markdown_report`
> Generate beautiful markdown report
*Line 338*  

#### Function: `save_json_results`
> Save results as JSON
*Line 467*  

#### Function: `main`
> Main benchmark runner
*Line 474*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_accessibility.py

#### Module: `test_accessibility`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_ai_gateway.py

#### Module: `test_ai_gateway`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_backends.py

#### Module: `test_backends`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_core.py

#### Module: `test_core`
> Test harness for core HyperCode components.
*Line 0*  

#### Function: `run_test`
> Test the lexer and parser with the given source code.
*Line 29*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_integration.py

#### Module: `test_integration`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Comprehensive test suite for knowledge base search functionality.
*Line 0*  

#### Class: `TestKnowledgeBaseSearch`
> Test suite for knowledge base search functionality.
*Line 12*  

#### Function: `sample_documents`
> Create sample documents for testing.
*Line 16*  

#### Function: `knowledge_base`
> Create a knowledge base instance with sample documents.
*Line 40*  

#### Function: `test_basic_search`
> Test basic search functionality.
*Line 48*  

#### Function: `test_search_with_exact_match`
> Test search with exact phrase matching.
*Line 54*  

#### Function: `test_search_case_insensitive`
> Test that search is case-insensitive.
*Line 59*  

#### Function: `test_search_empty_query`
> Test search with empty query returns all or no documents.
*Line 65*  

#### Function: `test_search_no_matches`
> Test search with no matching documents.
*Line 71*  

#### Function: `test_search_ranking`
> Test that search results are ranked by relevance.
*Line 77*  

#### Function: `test_query_normalization`
> Test query normalization (typos, spacing, punctuation).
*Line 90*  

#### Function: `test_multi_word_query`
> Test search with multiple keywords.
*Line 98*  

#### Function: `test_tag_based_search`
> Test search that includes tag matching.
*Line 103*  

#### Class: `TestEdgeCases`
> Test edge cases and boundary conditions.
*Line 112*  

#### Function: `knowledge_base`
*Line 116*  

#### Function: `test_very_short_query`
> Test search with very short query (1-2 chars).
*Line 121*  

#### Function: `test_very_long_query`
> Test search with very long query (paragraph length).
*Line 126*  

#### Function: `test_special_characters_in_query`
> Test search with special characters.
*Line 136*  

#### Function: `test_unicode_in_query`
> Test search with unicode characters.
*Line 141*  

#### Function: `test_sql_injection_attempt`
> Test that search is safe from SQL injection-style attacks.
*Line 146*  

#### Function: `test_repeated_queries`
> Test that repeated queries return consistent results.
*Line 151*  

#### Class: `TestPerformance`
> Performance benchmarking tests.
*Line 159*  

#### Function: `large_knowledge_base`
> Create a knowledge base with many documents.
*Line 163*  

#### Function: `test_search_response_time`
> Test that search completes within acceptable time.
*Line 179*  

#### Function: `test_concurrent_searches`
> Test multiple concurrent search operations.
*Line 189*  

#### Function: `test_memory_usage`
> Test memory usage during search operations.
*Line 207*  

#### Class: `TestIntegrationWithPerplexity`
> Test integration with EnhancedPerplexityClient.
*Line 213*  

#### Function: `mock_perplexity_client`
> Create a mock Perplexity client.
*Line 217*  

#### Function: `mock_knowledge_base`
> Create a mock knowledge base.
*Line 229*  

#### Function: `test_enhanced_query_with_context`
> Test that queries are enhanced with knowledge base context.
*Line 243*  

#### Function: `test_fallback_to_perplexity_api`
> Test fallback to Perplexity API when no local context found.
*Line 259*  

#### Function: `test_context_ranking_and_selection`
> Test that best context is selected for query enhancement.
*Line 273*  

#### Class: `TestDocumentManagement`
> Test document addition, update, and removal.
*Line 288*  

#### Function: `knowledge_base`
*Line 292*  

#### Function: `test_add_document`
> Test adding a new document to knowledge base.
*Line 300*  

#### Function: `test_update_document`
> Test updating an existing document.
*Line 310*  

#### Function: `test_remove_document`
> Test removing a document.
*Line 315*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_knowledge_base_comprehensive.py

#### Module: `test_knowledge_base_comprehensive`
> Comprehensive Test Suite for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestKnowledgeBaseUnit`
> Unit tests for Knowledge Base functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_docs`
> Sample documents for testing
*Line 36*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 59*  

#### Function: `test_add_single_document`
> Test adding a single document
*Line 65*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 74*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 84*  

#### Function: `test_search_exact_match`
> Test exact search matching
*Line 102*  

#### Function: `test_search_partial_match`
> Test partial search matching
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 124*  

#### Function: `test_search_case_insensitive`
> Test case insensitive search
*Line 135*  

#### Function: `test_empty_search`
> Test empty search query
*Line 147*  

#### Function: `test_nonexistent_search`
> Test search for nonexistent terms
*Line 155*  

#### Function: `test_get_context_for_query`
> Test context extraction
*Line 165*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 176*  

#### Function: `test_document_update`
> Test updating existing documents
*Line 186*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 202*  

#### Function: `test_delete_document`
> Test document deletion
*Line 213*  

#### Class: `TestKnowledgeBaseIntegration`
> Integration tests for Knowledge Base
*Line 229*  

#### Function: `populated_kb`
> Create a populated knowledge base for integration testing
*Line 233*  

#### Function: `test_complex_search_queries`
> Test complex search scenarios
*Line 277*  

#### Function: `test_search_ranking_quality`
> Test that search results are properly ranked
*Line 291*  

#### Function: `test_related_term_expansion`
> Test that related terms are properly expanded
*Line 301*  

#### Function: `test_performance_with_large_dataset`
> Test performance with larger dataset
*Line 313*  

#### Function: `test_concurrent_access_simulation`
> Test simulated concurrent access
*Line 332*  

#### Class: `TestKnowledgeBasePerformance`
> Performance tests for Knowledge Base
*Line 356*  

#### Function: `large_kb`
> Create a large knowledge base for performance testing
*Line 360*  

#### Function: `test_search_performance_large_dataset`
> Test search performance with large dataset
*Line 382*  

#### Function: `test_save_performance_large_dataset`
> Test save performance with large dataset
*Line 396*  

#### Function: `test_load_performance_large_dataset`
> Test load performance with large dataset
*Line 409*  

#### Function: `test_memory_usage_large_dataset`
> Test memory usage with large dataset
*Line 423*  

#### Class: `TestKnowledgeBaseEdgeCases`
> Edge case tests for Knowledge Base
*Line 446*  

#### Function: `edge_case_kb`
> Create knowledge base for edge case testing
*Line 450*  

#### Function: `test_empty_title_handling`
> Test handling of documents with empty titles
*Line 494*  

#### Function: `test_special_characters_handling`
> Test handling of special characters and unicode
*Line 499*  

#### Function: `test_very_long_titles`
> Test handling of very long titles
*Line 507*  

#### Function: `test_empty_content_handling`
> Test handling of documents with empty content
*Line 512*  

#### Function: `test_none_tags_handling`
> Test handling of None tags
*Line 517*  

#### Function: `test_malformed_json_handling`
> Test handling of malformed JSON files
*Line 531*  

#### Function: `test_file_permission_handling`
> Test handling of file permission issues
*Line 544*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_lexer.py

#### Function: `test_lexer_basic_tokens`
*Line 5*  

#### Function: `test_lexer_strings`
*Line 23*  

#### Function: `test_lexer_operators`
*Line 48*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_lexer_extended.py

#### Function: `test_lexer_escaped_strings`
> Test handling of strings with escaped characters.
*Line 5*  

#### Function: `test_lexer_numbers`
> Test various number formats.
*Line 18*  

#### Function: `test_lexer_operators`
> Test all operators.
*Line 39*  

#### Function: `test_lexer_comments`
> Test handling of single-line and multi-line comments.
*Line 86*  

#### Function: `test_lexer_whitespace`
> Test handling of various whitespace characters.
*Line 115*  

#### Function: `test_lexer_error_handling`
> Test error handling for invalid tokens.
*Line 130*  

#### Function: `test_lexer_hex_numbers`
> Test hexadecimal number literals.
*Line 139*  

#### Function: `test_lexer_binary_numbers`
> Test binary number literals.
*Line 157*  

#### Function: `test_lexer_scientific_notation`
> Test scientific notation numbers.
*Line 169*  

#### Function: `test_lexer_string_escapes`
> Test string escape sequences.
*Line 180*  

#### Function: `test_lexer_keywords`
> Test all language keywords.
*Line 197*  

#### Function: `test_lexer_position_tracking`
> Test that line and column numbers are tracked correctly.
*Line 223*  

#### Function: `test_lexer_error_recovery`
> Test that the lexer raises errors on invalid characters.
*Line 243*  

#### Function: `test_lexer_error_messages`
> Test that lexer error messages are informative.
*Line 252*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\test_parser.py

#### Function: `test_parse_literal`
*Line 12*  

#### Function: `test_parse_variable_declaration`
*Line 24*  

#### Function: `test_parse_binary_expression`
*Line 37*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\unit\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Phase 1 Unit Tests for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestHyperCodeKnowledgeBase`
> Test suite for HyperCodeKnowledgeBase core functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_documents`
> Sample documents for testing
*Line 33*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 56*  

#### Function: `test_add_document`
> Test adding a single document
*Line 61*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 82*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 92*  

#### Function: `test_search_exact_match`
> Test exact term matching in search
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 126*  

#### Function: `test_search_related_terms`
> Test related term expansion
*Line 139*  

#### Function: `test_search_space_data_boost`
> Test that space data gets boosted in search
*Line 153*  

#### Function: `test_get_context_for_query`
> Test context extraction for queries
*Line 180*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 192*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 203*  

#### Function: `test_empty_search`
> Test search with empty query
*Line 216*  

#### Function: `test_search_nonexistent_term`
> Test search for term that doesn't exist
*Line 221*  

#### Function: `test_document_update`
> Test updating existing document
*Line 231*  

#### Class: `TestResearchDocument`
> Test suite for ResearchDocument dataclass
*Line 250*  

#### Function: `test_document_creation`
> Test creating a research document
*Line 253*  

#### Function: `test_document_optional_fields`
> Test document with optional fields
*Line 273*  

### 📄 hypercode_backup_20251205_183301\core\src\core\hypercode-\tests\unit\test_search_algorithm.py

#### Module: `test_search_algorithm`
> Phase 1 Unit Tests for Search Algorithm
*Line 0*  

#### Class: `TestSearchAlgorithm`
> Test suite for search algorithm functionality
*Line 20*  

#### Function: `populated_kb`
> Create a knowledge base with test documents
*Line 24*  

#### Function: `test_exact_title_match_highest_score`
> Test that exact title matches get highest priority
*Line 80*  

#### Function: `test_space_data_boosting`
> Test that space data gets boosted in search results
*Line 92*  

#### Function: `test_related_term_expansion`
> Test related term matching functionality
*Line 105*  

#### Function: `test_tag_matching_scoring`
> Test that tag matches contribute to scoring
*Line 126*  

#### Function: `test_content_frequency_scoring`
> Test that multiple content occurrences increase score
*Line 136*  

#### Function: `test_partial_word_matching`
> Test partial word matching for longer terms
*Line 149*  

#### Function: `test_query_word_ordering`
> Test that query words are properly processed
*Line 167*  

#### Function: `test_case_insensitive_search`
> Test that search is case insensitive
*Line 179*  

#### Function: `test_empty_query_returns_no_results`
> Test that empty queries return no results
*Line 202*  

#### Function: `test_limit_parameter_respected`
> Test that search limit parameter works correctly
*Line 210*  

#### Function: `test_no_results_for_nonexistent_terms`
> Test search for terms that don't exist
*Line 219*  

#### Function: `test_special_characters_in_query`
> Test search with special characters
*Line 227*  

#### Function: `test_unicode_characters`
> Test search with unicode characters
*Line 237*  

#### Function: `test_search_performance_with_large_kb`
> Test search performance with larger knowledge base
*Line 256*  

#### Function: `test_search_result_consistency`
> Test that search results are consistent across multiple calls
*Line 277*  

#### Class: `TestSearchScoringDetails`
> Test detailed scoring algorithm behavior
*Line 292*  

#### Function: `scoring_kb`
> Create KB for detailed scoring tests
*Line 296*  

#### Function: `test_title_match_beats_content_match`
> Test that title matches score higher than content matches
*Line 324*  

#### Function: `test_space_data_boosting_works`
> Test that space data gets boosted
*Line 332*  

#### Function: `test_frequency_scoring`
> Test that content frequency affects scoring
*Line 340*  

### 📄 hypercode_backup_20251205_183301\core\src\core\interpreter.py

#### Class: `RuntimeError`
*Line 8*  

#### Function: `__init__`
*Line 9*  

#### Class: `Environment`
*Line 15*  

#### Function: `__init__`
*Line 16*  

#### Function: `define`
*Line 20*  

#### Function: `get`
*Line 23*  

#### Function: `assign`
*Line 30*  

#### Class: `Callable`
*Line 40*  

#### Function: `arity`
*Line 41*  

#### Function: `call`
*Line 44*  

#### Class: `HyperCodeFunction`
*Line 48*  

#### Function: `__init__`
*Line 49*  

#### Function: `call`
*Line 53*  

#### Function: `arity`
*Line 65*  

#### Class: `ReturnException`
*Line 69*  

#### Function: `__init__`
*Line 70*  

#### Class: `Interpreter`
*Line 74*  

#### Function: `__init__`
*Line 75*  

#### Class: `Clock`
*Line 82*  

#### Function: `arity`
*Line 83*  

#### Function: `call`
*Line 86*  

#### Function: `__str__`
*Line 89*  

#### Class: `Double`
*Line 92*  

#### Function: `arity`
*Line 93*  

#### Function: `call`
*Line 96*  

#### Function: `__str__`
*Line 101*  

#### Class: `Square`
*Line 104*  

#### Function: `arity`
*Line 105*  

#### Function: `call`
*Line 108*  

#### Function: `__str__`
*Line 113*  

#### Function: `execute_block`
*Line 120*  

#### Function: `interpret`
*Line 129*  

#### Function: `execute`
*Line 141*  

#### Function: `evaluate`
*Line 144*  

#### Function: `visit_Expression`
*Line 147*  

#### Function: `visit_Print`
*Line 151*  

#### Function: `visit_Let`
*Line 158*  

#### Function: `visit_Block`
*Line 165*  

#### Function: `visit_BlockDecl`
*Line 169*  

#### Function: `visit_Intent`
*Line 175*  

#### Function: `visit_Function`
*Line 180*  

#### Function: `visit_Return`
*Line 185*  

#### Function: `visit_Literal`
*Line 191*  

#### Function: `visit_Grouping`
*Line 194*  

#### Function: `visit_Variable`
*Line 197*  

#### Function: `visit_Assign`
*Line 200*  

#### Function: `visit_Pipe`
*Line 205*  

#### Function: `visit_State`
*Line 234*  

#### Function: `visit_Call`
*Line 244*  

#### Function: `visit_Binary`
*Line 262*  

#### Function: `visit_Unary`
*Line 293*  

#### Function: `is_truthy`
*Line 301*  

#### Function: `stringify`
*Line 308*  

#### Function: `get_output`
*Line 322*  

### 📄 hypercode_backup_20251205_183301\core\src\core\lexer.py

#### Module: `lexer`
> HyperCode Lexer Module
*Line 0*  

#### Class: `LexerError`
> Represents a lexical analysis error.
*Line 17*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode programming language.
*Line 33*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 41*  

#### Function: `scan_tokens`
> Scan the source code and return a list of tokens.
*Line 77*  

#### Function: `scan_token`
> Scan a single token.
*Line 87*  

#### Function: `number`
> Lex a number literal.
*Line 164*  

#### Function: `string`
> Lex a string literal.
*Line 197*  

#### Function: `docstring`
> Lex a docstring.
*Line 242*  

#### Function: `identifier`
> Lex an identifier or keyword.
*Line 268*  

#### Function: `error`
> Report a lexing error.
*Line 278*  

#### Function: `is_at_end`
> Check if we've reached the end of the source.
*Line 294*  

#### Function: `advance`
> Consume and return the next character.
*Line 298*  

#### Function: `match`
> Conditionally consume a character if it matches the expected value.
*Line 307*  

#### Function: `peek`
> Look at the next character without consuming it.
*Line 317*  

#### Function: `peek_next`
> Look at the character after the next one without consuming it.
*Line 323*  

#### Function: `add_token`
> Add a new token to the token list.
*Line 329*  

### 📄 hypercode_backup_20251205_183301\core\src\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\core\parser.py

#### Class: `ParseError`
*Line 7*  

#### Class: `Parser`
*Line 11*  

#### Function: `__init__`
*Line 12*  

#### Function: `parse`
> Parse the entire program.
*Line 16*  

#### Function: `declaration`
*Line 25*  

#### Function: `let_declaration`
*Line 38*  

#### Function: `block_declaration`
*Line 48*  

#### Function: `statement`
*Line 54*  

#### Function: `print_statement`
*Line 65*  

#### Function: `expression_statement`
*Line 70*  

#### Function: `block`
*Line 75*  

#### Function: `expression`
*Line 84*  

#### Function: `pipe`
*Line 87*  

#### Function: `assignment`
*Line 103*  

#### Function: `equality`
*Line 118*  

#### Function: `comparison`
*Line 128*  

#### Function: `term`
*Line 141*  

#### Function: `factor`
*Line 149*  

#### Function: `unary`
*Line 157*  

#### Function: `primary`
*Line 164*  

#### Function: `function`
*Line 194*  

#### Function: `if_statement`
*Line 215*  

#### Function: `return_statement`
*Line 227*  

#### Function: `match`
*Line 237*  

#### Function: `consume`
*Line 244*  

#### Function: `error`
*Line 249*  

#### Function: `synchronize`
*Line 255*  

#### Function: `check`
*Line 276*  

#### Function: `advance`
*Line 281*  

#### Function: `is_at_end`
*Line 286*  

#### Function: `peek`
*Line 289*  

#### Function: `previous`
*Line 292*  

### 📄 hypercode_backup_20251205_183301\core\src\core\tokens.py

#### Module: `tokens`
> HyperCode Token Types and Definitions
*Line 0*  

#### Class: `TokenType`
*Line 12*  

#### Class: `Token`
> Represents a token in the HyperCode language.
*Line 74*  

#### Function: `__init__`
*Line 86*  

#### Function: `__str__`
*Line 95*  

#### Function: `__repr__`
*Line 98*  

### 📄 hypercode_backup_20251205_183301\core\src\duelcode\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode_backup_20251205_183301\core\src\duelcode\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode_backup_20251205_183301\core\src\duelcode\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode_backup_20251205_183301\core\src\duelcode\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode_backup_20251205_183301\core\src\duelcode\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode_backup_20251205_183301\core\src\duelcode\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode_backup_20251205_183301\core\src\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode_backup_20251205_183301\core\src\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode-backend-js-COMPLETE.py

#### Module: `hypercode-backend-js-COMPLETE`
> HyperCode JavaScript Backend - Complete Implementation
*Line 0*  

#### Class: `JSCompiler`
> Compiles HyperCode AST to JavaScript.
*Line 19*  

#### Function: `__init__`
> Initialize compiler.
*Line 30*  

#### Function: `compile`
> Compile AST to JavaScript.
*Line 42*  

#### Function: `_generate_header`
> Generate JavaScript header
*Line 65*  

#### Function: `_generate_setup`
> Generate setup code (memory tape, pointer, I/O)
*Line 74*  

#### Function: `_generate_main`
> Generate JavaScript for AST node.
*Line 110*  

#### Function: `_generate_footer`
> Generate JavaScript footer
*Line 162*  

#### Function: `_indent`
> Get current indentation
*Line 179*  

#### Function: `optimize_ast`
> Optimize AST (future: loop unrolling, dead code elimination).
*Line 183*  

#### Function: `main`
> CLI interface for JavaScript backend
*Line 200*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode-idea-generator-WEB.py

#### Module: `hypercode-idea-generator-WEB`
> HyperCode Community Idea Generator - Web Interface (HTML/CSS/JS)
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode-launch-kit.py

#### Module: `hypercode-launch-kit`
> HyperCode Launch Kit - Ultimate System Initialization
*Line 0*  

#### Class: `HyperCodeLaunchKit`
> Complete launch system initialization
*Line 23*  

#### Function: `__init__`
*Line 26*  

#### Function: `create_readme`
> Create the ultimate README.md
*Line 30*  

#### Function: `create_launch_checklist`
> Create launch day checklist
*Line 367*  

#### Function: `create_launch_script`
> Create automated launch script
*Line 620*  

#### Function: `create_first_30_days`
> Create 30-day success roadmap
*Line 718*  

#### Function: `print_summary`
> Print beautiful summary
*Line 974*  

#### Function: `main`
> Run launch kit initialization
*Line 1007*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode-lexer-COMPLETE.py

#### Module: `hypercode-lexer-COMPLETE`
> HyperCode Lexer - Complete Implementation
*Line 0*  

#### Class: `TokenType`
> HyperCode token types - minimal yet powerful
*Line 21*  

#### Class: `Token`
> Represents a single token with position tracking
*Line 45*  

#### Function: `__repr__`
> Neurodivergent-friendly representation
*Line 54*  

#### Class: `LexerError`
> Lexer-specific errors with context
*Line 59*  

#### Function: `__init__`
*Line 62*  

#### Class: `HyperCodeLexer`
> Tokenizes HyperCode programs with accessibility features.
*Line 69*  

#### Function: `__init__`
> Initialize lexer with source code.
*Line 95*  

#### Function: `tokenize`
> Convert HyperCode source to token stream.
*Line 110*  

#### Function: `_advance_position`
> Update position tracking after processing character
*Line 169*  

#### Function: `_skip_comment`
> Skip characters until end of line
*Line 179*  

#### Function: `get_tokens`
> Return current token list
*Line 184*  

#### Function: `filter_tokens`
> Get tokens excluding certain types.
*Line 188*  

#### Function: `print_tokens`
> Print tokens in readable format.
*Line 205*  

#### Function: `get_statistics`
> Get token statistics (useful for analysis).
*Line 236*  

#### Function: `main`
> CLI interface for the lexer
*Line 250*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode-parser-COMPLETE.py

#### Module: `hypercode-parser-COMPLETE`
> HyperCode Parser - Complete Implementation
*Line 0*  

#### Class: `NodeType`
> AST Node types
*Line 22*  

#### Class: `ASTNode`
> Abstract Syntax Tree Node.
*Line 38*  

#### Function: `__repr__`
> Pretty-print AST (neurodivergent-friendly)
*Line 51*  

#### Class: `ParserError`
> Parser-specific errors with context
*Line 68*  

#### Function: `__init__`
*Line 71*  

#### Class: `HyperCodeParser`
> Parses HyperCode token stream into AST.
*Line 80*  

#### Function: `__init__`
> Initialize parser with token stream.
*Line 94*  

#### Function: `parse`
> Parse tokens into AST.
*Line 105*  

#### Function: `_parse_statement`
> Parse a single statement
*Line 127*  

#### Function: `_parse_loop`
> Parse loop structure: [ statements ]
*Line 174*  

#### Function: `_advance`
> Move to next token
*Line 209*  

#### Function: `_is_at_end`
> Check if at end of token stream
*Line 215*  

#### Function: `validate`
> Validate AST structure.
*Line 222*  

#### Function: `print_ast`
> Print AST in readable format.
*Line 237*  

#### Function: `main`
> CLI interface for the parser
*Line 251*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\__init__.py

#### Module: `__init__`
> HyperCode - A neurodivergent-first programming language with AI compatibility.
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\__main__.py

#### Function: `main`
*Line 6*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\cli\__init__.py

#### Module: `__init__`
> HyperCode Command Line Interface
*Line 0*  

#### Function: `main`
> Run the HyperCode lexer from the command line.
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\config.py

#### Module: `config`
> Configuration module for HyperCode.
*Line 0*  

#### Class: `Config`
> Configuration class for HyperCode
*Line 16*  

#### Function: `get_headers`
> Get headers for API requests
*Line 27*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\__init__.py

#### Module: `__init__`
> Core package for the HyperCode language implementation.
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\cli.py

#### Module: `cli`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\error_handler.py

#### Function: `report_parse_error`
*Line 5*  

#### Function: `report`
*Line 12*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\hypercode_ast.py

#### Class: `Node`
*Line 9*  

#### Function: `accept`
*Line 10*  

#### Class: `Expr`
*Line 20*  

#### Class: `Literal`
*Line 25*  

#### Class: `Variable`
*Line 30*  

#### Class: `Assign`
*Line 35*  

#### Class: `Binary`
*Line 41*  

#### Class: `Unary`
*Line 48*  

#### Class: `Grouping`
*Line 54*  

#### Class: `Call`
*Line 59*  

#### Class: `Get`
*Line 66*  

#### Class: `Stmt`
*Line 73*  

#### Class: `Expression`
*Line 78*  

#### Class: `Print`
*Line 83*  

#### Class: `Var`
*Line 88*  

#### Class: `Block`
*Line 94*  

#### Class: `If`
*Line 99*  

#### Class: `Fun`
*Line 106*  

#### Class: `Return`
*Line 113*  

#### Class: `Intent`
*Line 119*  

#### Class: `Program`
*Line 126*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\interpreter.py

#### Class: `Return`
*Line 6*  

#### Function: `__init__`
*Line 7*  

#### Class: `HyperCodeFunction`
*Line 11*  

#### Function: `__init__`
*Line 12*  

#### Function: `__str__`
*Line 16*  

#### Function: `arity`
*Line 19*  

#### Function: `call`
*Line 22*  

#### Class: `Environment`
*Line 35*  

#### Function: `__init__`
*Line 36*  

#### Function: `define`
*Line 40*  

#### Function: `get`
*Line 43*  

#### Function: `assign`
*Line 50*  

#### Class: `Interpreter`
*Line 60*  

#### Function: `__init__`
*Line 61*  

#### Function: `interpret`
*Line 65*  

#### Function: `execute`
*Line 72*  

#### Function: `execute_block`
*Line 75*  

#### Function: `evaluate`
*Line 84*  

#### Function: `visit_Expression`
*Line 87*  

#### Function: `visit_Print`
*Line 90*  

#### Function: `visit_Var`
*Line 94*  

#### Function: `visit_Block`
*Line 100*  

#### Function: `visit_Assign`
*Line 103*  

#### Function: `visit_Binary`
*Line 108*  

#### Function: `visit_Grouping`
*Line 151*  

#### Function: `visit_Literal`
*Line 154*  

#### Function: `visit_Unary`
*Line 157*  

#### Function: `visit_Variable`
*Line 170*  

#### Function: `visit_If`
*Line 173*  

#### Function: `is_truthy`
*Line 179*  

#### Function: `visit_Fun`
*Line 186*  

#### Function: `visit_Return`
*Line 190*  

#### Function: `visit_Call`
*Line 196*  

#### Function: `is_callable`
*Line 214*  

#### Class: `Visitor`
*Line 219*  

#### Function: `visit_Expression`
*Line 220*  

#### Function: `visit_Print`
*Line 223*  

#### Function: `visit_Var`
*Line 226*  

#### Function: `visit_Block`
*Line 229*  

#### Function: `visit_If`
*Line 232*  

#### Function: `visit_Fun`
*Line 235*  

#### Function: `visit_Return`
*Line 238*  

#### Function: `visit_Assign`
*Line 241*  

#### Function: `visit_Binary`
*Line 244*  

#### Function: `visit_Grouping`
*Line 247*  

#### Function: `visit_Literal`
*Line 250*  

#### Function: `visit_Unary`
*Line 253*  

#### Function: `visit_Variable`
*Line 256*  

#### Function: `visit_Call`
*Line 259*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\lexer.py

#### Module: `lexer`
> Core HyperCode language implementation - Lexer
*Line 0*  

#### Class: `LexerError`
> Exception raised for errors in the lexer.
*Line 28*  

#### Function: `__init__`
*Line 35*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode language.
*Line 42*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 45*  

#### Function: `tokenize`
> Convert source code into a list of tokens.
*Line 59*  

#### Function: `is_at_end`
> Check if we've consumed all characters.
*Line 89*  

#### Class: `LexerError`
> Exception raised for errors in the lexer.
*Line 102*  

#### Function: `__init__`
*Line 105*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode language.
*Line 112*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 122*  

#### Function: `tokenize`
> Convert source code into a list of tokens.
*Line 136*  

#### Function: `scan_token`
> Scan the next token from the source.
*Line 164*  

#### Function: `string`
> Scan a string literal.
*Line 251*  

#### Function: `number`
> Scan a number literal.
*Line 273*  

#### Function: `identifier`
> Scan an identifier or keyword.
*Line 306*  

#### Function: `match`
> Match the next character if it matches the expected character.
*Line 316*  

#### Function: `peek`
> Look at the next character without consuming it.
*Line 327*  

#### Function: `peek_next`
> Look at the character after the next one without consuming it.
*Line 333*  

#### Function: `advance`
> Consume and return the next character.
*Line 339*  

#### Function: `add_token`
> Add a new token to the tokens list.
*Line 349*  

#### Function: `error`
> Record a lexer error.
*Line 357*  

#### Function: `is_at_end`
> Check if we've consumed all characters.
*Line 371*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\parser.py

#### Class: `ParseError`
*Line 8*  

#### Class: `Parser`
*Line 12*  

#### Function: `__init__`
*Line 13*  

#### Function: `parse`
> Parse the entire program.
*Line 17*  

#### Function: `declaration`
*Line 26*  

#### Function: `var_declaration`
*Line 37*  

#### Function: `statement`
*Line 53*  

#### Function: `print_statement`
*Line 66*  

#### Function: `return_statement`
*Line 71*  

#### Function: `intent_statement`
*Line 79*  

#### Function: `expression_statement`
*Line 92*  

#### Function: `if_statement`
*Line 97*  

#### Function: `function`
*Line 109*  

#### Function: `block`
*Line 128*  

#### Function: `expression`
*Line 135*  

#### Function: `assignment`
*Line 138*  

#### Function: `equality`
*Line 153*  

#### Function: `comparison`
*Line 163*  

#### Function: `term`
*Line 176*  

#### Function: `factor`
*Line 184*  

#### Function: `unary`
*Line 192*  

#### Function: `primary`
*Line 199*  

#### Function: `_primary`
*Line 214*  

#### Function: `finish_call`
*Line 245*  

#### Function: `match`
*Line 258*  

#### Function: `consume`
*Line 265*  

#### Function: `error`
*Line 272*  

#### Function: `synchronize`
*Line 278*  

#### Function: `check`
*Line 298*  

#### Function: `advance`
*Line 303*  

#### Function: `is_at_end`
*Line 308*  

#### Function: `peek`
*Line 311*  

#### Function: `previous`
*Line 314*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\semantic_analyzer.py

#### Module: `semantic_analyzer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\sensory_profile.py

#### Module: `sensory_profile`
> Sensory Profile System for HyperCode
*Line 0*  

#### Class: `VisualNoiseLevel`
*Line 15*  

#### Class: `AnimationSpeed`
*Line 22*  

#### Class: `VisualSettings`
> Configuration for visual aspects of the editor.
*Line 29*  

#### Class: `AudioSettings`
> Configuration for audio feedback.
*Line 43*  

#### Class: `AnimationSettings`
> Configuration for animations and transitions.
*Line 58*  

#### Class: `SensoryProfile`
> A complete sensory profile configuration.
*Line 68*  

#### Function: `to_dict`
> Convert the profile to a dictionary.
*Line 77*  

#### Function: `from_dict`
> Create a profile from a dictionary.
*Line 93*  

#### Function: `save`
> Save the profile to a file.
*Line 115*  

#### Function: `load`
> Load a profile from a file.
*Line 121*  

#### Class: `ProfileManager`
> Manages loading and saving of sensory profiles.
*Line 128*  

#### Function: `__init__`
> Initialize with optional custom profiles directory.
*Line 131*  

#### Function: `_ensure_default_profiles`
> Ensure default profiles exist.
*Line 141*  

#### Function: `_create_minimal_profile`
> Create a minimal distraction-free profile.
*Line 154*  

#### Function: `_create_enhanced_profile`
> Create an enhanced profile with helpful visual cues.
*Line 171*  

#### Function: `_create_high_contrast_profile`
> Create a high-contrast profile for better readability.
*Line 198*  

#### Function: `list_profiles`
> List all available profile names.
*Line 224*  

#### Function: `get_profile`
> Get a profile by name.
*Line 228*  

#### Function: `save_profile`
> Save a profile.
*Line 235*  

#### Function: `delete_profile`
> Delete a profile by name.
*Line 240*  

#### Function: `get_profile`
> Helper function to get a profile by name.
*Line 251*  

#### Function: `list_profiles`
> Helper function to list all available profiles.
*Line 263*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\core\tokens.py

#### Class: `TokenType`
*Line 6*  

#### Class: `Token`
*Line 96*  

#### Function: `__str__`
*Line 103*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\enhanced_perplexity_client.py

#### Module: `enhanced_perplexity_client`
> Enhanced Perplexity Client with Knowledge Base Integration
*Line 0*  

#### Class: `EnhancedPerplexityClient`
> Enhanced Perplexity client with knowledge base integration
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `query_with_context`
> Send a query with relevant knowledge base context
*Line 25*  

#### Function: `add_research_data`
> Add research data to the knowledge base
*Line 61*  

#### Function: `search_research_data`
> Search the knowledge base
*Line 71*  

#### Function: `list_research_documents`
> List all research documents
*Line 75*  

#### Function: `get_document`
> Get a specific document
*Line 79*  

#### Function: `delete_document`
> Delete a document
*Line 83*  

#### Function: `import_from_perplexity_space`
> Import data from Perplexity Space export
*Line 87*  

#### Function: `test_context_integration`
> Test the context integration
*Line 123*  

#### Function: `create_perplexity_space_import_template`
> Create a template for importing Perplexity Space data
*Line 175*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\knowledge_base.py

#### Module: `knowledge_base`
> HyperCode Knowledge Base - Perplexity Space Integration
*Line 0*  

#### Class: `ResearchDocument`
> Represents a research document from Perplexity Space
*Line 17*  

#### Function: `__post_init__`
*Line 28*  

#### Function: `generate_id`
> Generate unique ID from content hash
*Line 36*  

#### Function: `validate`
> Validate document data
*Line 41*  

#### Function: `update_timestamp`
> Update the last_updated timestamp
*Line 53*  

#### Class: `HyperCodeKnowledgeBase`
> Knowledge base for HyperCode research data
*Line 100*  

#### Function: `__init__`
*Line 103*  

#### Function: `load`
> Load knowledge base from file
*Line 109*  

#### Function: `save`
> Save knowledge base to file
*Line 125*  

#### Function: `add_document`
> Add a new research document
*Line 135*  

#### Function: `search_documents`
> Search documents by query
*Line 163*  

#### Function: `get_context_for_query`
> Get relevant context for a query
*Line 227*  

#### Function: `list_documents`
> List all documents
*Line 257*  

#### Function: `get_document`
> Get a specific document by ID
*Line 261*  

#### Function: `delete_document`
> Delete a document
*Line 265*  

#### Function: `update_document`
> Update an existing document
*Line 273*  

#### Function: `search_by_tags`
> Search documents by tags with AND/OR operators
*Line 287*  

#### Function: `get_document_statistics`
> Get statistics about the knowledge base
*Line 306*  

#### Function: `export_format`
> Export knowledge base in different formats
*Line 331*  

#### Function: `validate_all_documents`
> Validate all documents and return list of errors
*Line 353*  

#### Function: `cleanup_duplicates`
> Remove duplicate documents based on content hash
*Line 363*  

#### Function: `initialize_sample_data`
> Initialize with sample HyperCode research data
*Line 384*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\perplexity_client.py

#### Module: `perplexity_client`
> Perplexity AI API client for HyperCode.
*Line 0*  

#### Class: `PerplexityClient`
> Client for interacting with Perplexity AI API
*Line 12*  

#### Function: `__init__`
> Initialize the Perplexity client.
*Line 15*  

#### Function: `query`
> Send a query to the Perplexity API.
*Line 30*  

#### Function: `test_connection`
> Test the connection to the Perplexity API
*Line 72*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode\repl.py

#### Function: `run_repl`
*Line 11*  

#### Function: `run`
*Line 32*  

#### Function: `show_help`
*Line 51*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode_idea_generator.py

#### Module: `hypercode_idea_generator`
> HyperCode Idea Generator - AI-Powered Community Input System
*Line 0*  

#### Class: `HyperCodeIdeaGenerator`
> AI-Powered Idea Generator for HyperCode community input.
*Line 431*  

#### Function: `__init__`
*Line 439*  

#### Function: `get_ideas_by_category`
> Get ideas by category and optionally by difficulty level.
*Line 443*  

#### Function: `get_top_ideas`
> Get most-voted ideas across all categories.
*Line 468*  

#### Function: `vote_for_idea`
> Vote for an idea.
*Line 487*  

#### Function: `get_trending_ideas`
> Get trending ideas (high votes + recent activity).
*Line 497*  

#### Function: `format_idea_card`
> Format idea for display.
*Line 502*  

#### Function: `main`
> Interactive idea generator CLI
*Line 528*  

### 📄 hypercode_backup_20251205_183301\core\src\hypercode_poc.py

#### Module: `hypercode_poc`
> HyperCode POC - Neurodivergent-First Programming Language
*Line 0*  

#### Class: `TokenType`
> Brainfuck-inspired core + modern aliases
*Line 18*  

#### Class: `Token`
*Line 34*  

#### Class: `UserConfidenceLevel`
*Line 41*  

#### Class: `EnhancedLexer`
> Smart tokenizer with escape handling + accessibility focus
*Line 48*  

#### Function: `__init__`
*Line 51*  

#### Function: `tokenize`
*Line 74*  

#### Function: `handle_string`
*Line 115*  

#### Function: `handle_number`
*Line 141*  

#### Function: `handle_identifier`
*Line 149*  

#### Function: `advance`
*Line 171*  

#### Class: `ContextAwareErrorMessenger`
> Friendly, adaptive error messages
*Line 176*  

#### Function: `__init__`
*Line 179*  

#### Function: `format_error`
*Line 182*  

#### Class: `SemanticContextStreamer`
> Understand programmer intent from tokens
*Line 189*  

#### Function: `analyze`
*Line 192*  

#### Class: `ConfidenceTracker`
> Adapt system guidance to user skill level
*Line 209*  

#### Function: `__init__`
*Line 212*  

#### Function: `record`
*Line 216*  

#### Class: `HyperCodePOC`
> Main system: Lexer + Error Messenger + Semantic Analyzer + Confidence Tracker
*Line 222*  

#### Function: `__init__`
*Line 225*  

#### Function: `compile`
*Line 232*  

### 📄 hypercode_backup_20251205_183301\core\src\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\core\src\parser\debug_ascii.py

#### Module: `debug_ascii`
> ASCII-only debug
*Line 0*  

#### Function: `test_regex_patterns`
> Test regex patterns directly
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\parser\debug_full.py

#### Module: `debug_full`
> Debug the full parsing flow
*Line 0*  

#### Function: `debug_full_parsing`
> Debug the full parsing flow
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\parser\debug_parser.py

#### Module: `debug_parser`
> Debug the Visual Syntax Parser - Find what's wrong with annotation detection
*Line 0*  

#### Function: `debug_annotation_detection`
> Debug why annotations aren't being detected
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\parser\debug_simple.py

#### Module: `debug_simple`
> Simple debug without emoji characters
*Line 0*  

#### Function: `debug_simple`
> Debug without emoji characters
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\parser\test_parser.py

#### Module: `test_parser`
> Test the Visual Syntax Parser - First Click Moment Demo
*Line 0*  

#### Function: `test_first_click_moment`
> Test the parser with the first click moment example
*Line 14*  

### 📄 hypercode_backup_20251205_183301\core\src\parser\visual_syntax_parser.py

#### Module: `visual_syntax_parser`
> 🎨 Visual Syntax Parser for HyperCode V3
*Line 0*  

#### Class: `SemanticMarker`
> 🎨 Semantic marker types with emoji representations
*Line 18*  

#### Class: `SemanticAnnotation`
> 📋 A single semantic annotation with its metadata
*Line 37*  

#### Function: `__str__`
*Line 46*  

#### Class: `ParsedFunction`
> 🔍 A fully parsed HyperCode function
*Line 51*  

#### Function: `get_annotations_by_type`
> Get all annotations of a specific type
*Line 62*  

#### Class: `VisualSyntaxParser`
> 🎨 Main parser for HyperCode's visual semantic syntax
*Line 69*  

#### Function: `__init__`
*Line 72*  

#### Function: `_build_semantic_patterns`
> 🔍 Build regex patterns for all semantic markers
*Line 76*  

#### Function: `_build_color_scheme`
> 🎨 Build semantic color mapping for IDE highlighting
*Line 105*  

#### Function: `parse_file`
> 📄 Parse an entire HyperCode file
*Line 123*  

#### Function: `parse_content`
> 📝 Parse HyperCode content string
*Line 130*  

#### Function: `_is_function_definition`
> 🔍 Check if line is a function definition
*Line 170*  

#### Function: `_start_new_function`
> 🆕 Create new ParsedFunction from definition line
*Line 179*  

#### Function: `_parse_line_annotations`
> � Parse semantic annotations from a line
*Line 202*  

#### Function: `_parse_annotation_params`
> 🔧 Parse annotation parameters from string
*Line 223*  

#### Function: `generate_syntax_highlighting`
> 🎨 Generate HTML with syntax highlighting for visual markers
*Line 265*  

#### Function: `extract_semantic_summary`
> 📊 Extract semantic summary for analysis
*Line 277*  

#### Function: `validate_neurodiversity_compliance`
> 🧠 Validate neurodiversity-first design principles
*Line 311*  

### 📄 hypercode_backup_20251205_183301\core\src\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\src\scaffold (1).py

#### Module: `scaffold (1)`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 141*  

#### Function: `create_python_files`
> Create all Python files with proper __init__.py structure.
*Line 151*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 165*  

#### Function: `create_root_files`
> Create root-level configuration files as empty placeholders.
*Line 202*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 213*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 234*  

#### Function: `main`
> Main scaffolding function.
*Line 259*  

### 📄 hypercode_backup_20251205_183301\core\src\scaffold.py

#### Module: `scaffold`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 153*  

#### Function: `create_python_files`
> Create all Python files with proper docstrings and structure.
*Line 184*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 254*  

#### Function: `create_root_files`
> Create root-level configuration files with appropriate content.
*Line 291*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 541*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 583*  

#### Function: `main`
> Main scaffolding function.
*Line 621*  

### 📄 hypercode_backup_20251205_183301\core\src\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode_backup_20251205_183301\core\src\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode_backup_20251205_183301\core\src\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\code_analyzer_ai.py

#### Module: `code_analyzer_ai`
> Perplexity AI Code Analyzer for HyperCode
*Line 0*  

#### Class: `CodeAnalyzerAI`
> AI-powered code analyzer for HyperCode
*Line 19*  

#### Function: `__init__`
*Line 22*  

#### Function: `analyze_file`
> Analyze a Python file with AI assistance
*Line 25*  

#### Function: `_analyze_complexity`
> Analyze code complexity indicators
*Line 61*  

#### Function: `_check_docstrings`
> Check for docstring coverage
*Line 98*  

#### Function: `_get_ai_code_analysis`
> Get AI analysis of code from Perplexity
*Line 134*  

#### Function: `analyze_project`
> Analyze entire project
*Line 162*  

#### Function: `_get_project_ai_insights`
> Get AI insights for the entire project
*Line 206*  

#### Function: `save_analysis`
> Save analysis to file
*Line 238*  

#### Function: `print_summary`
> Print analysis summary
*Line 244*  

#### Function: `main`
> Main function
*Line 262*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\debug_search.py

#### Module: `debug_search`
> Debug search results
*Line 0*  

#### Function: `debug_search`
> Debug why space data isn't being found
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\demo_ai_research.py

#### Module: `demo_ai_research`
> HyperCode AI Research + Perplexity Integration Demo
*Line 0*  

#### Function: `demo_ai_research_queries`
> Demonstrate AI Research integration with Perplexity
*Line 16*  

#### Function: `test_document_specific_queries`
> Test queries specific to the HyperCode AI Research document
*Line 90*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\demo_enhanced_client.py

#### Module: `demo_enhanced_client`
> Demo: Enhanced Perplexity Client with Knowledge Base
*Line 0*  

#### Function: `demo_knowledge_base_integration`
> Demonstrate the knowledge base integration
*Line 16*  

#### Function: `demonstrate_memory_persistence`
> Demonstrate that the knowledge base persists between sessions
*Line 131*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\final_integration_test.py

#### Module: `final_integration_test`
> Final Test: Complete Perplexity Space Integration
*Line 0*  

#### Function: `final_integration_test`
> Complete test of the Perplexity Space integration
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\health_scanner_ai.py

#### Module: `health_scanner_ai`
> HyperCode Health Scanner with Perplexity AI Integration
*Line 0*  

#### Class: `HealthScannerAI`
> AI-powered health scanner for HyperCode project
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `analyze_project_structure`
> Analyze project structure and identify health issues
*Line 25*  

#### Function: `analyze_dependencies`
> Analyze dependency management
*Line 64*  

#### Function: `analyze_security`
> Analyze security configuration
*Line 100*  

#### Function: `get_ai_recommendations`
> Get AI-powered recommendations based on health scan
*Line 137*  

#### Function: `run_full_scan`
> Run complete health scan with AI analysis
*Line 164*  

#### Function: `save_report`
> Save health scan report to file
*Line 215*  

#### Function: `print_summary`
> Print a summary of the health scan
*Line 221*  

#### Function: `main`
> Main function to run the health scanner
*Line 241*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\import-helper.py

#### Module: `import-helper`
> HyperCode Perplexity Space Import Helper
*Line 0*  

#### Class: `SpaceImportHelper`
> Helper class for managing Perplexity Space imports
*Line 13*  

#### Function: `__init__`
*Line 16*  

#### Function: `validate_document`
> Validate a document structure
*Line 21*  

#### Function: `load_template`
> Load documents from JSON template file
*Line 63*  

#### Function: `validate_all`
> Validate all loaded documents
*Line 83*  

#### Function: `generate_report`
> Generate a validation report
*Line 95*  

#### Function: `create_import_script`
> Generate a Python script to import the data
*Line 141*  

#### Function: `create_template_instructions`
> Generate detailed instructions for filling the template
*Line 193*  

#### Function: `main`
> CLI interface for the import helper
*Line 264*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\import_all_space_data.py

#### Module: `import_all_space_data`
> Complete Import of HyperCode Space Data
*Line 0*  

#### Function: `format_content`
> Recursively format nested data into readable text
*Line 16*  

#### Function: `import_all_hypercode_data`
> Import all sections of your HyperCode Space data
*Line 41*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\import_hypercode_data.py

#### Module: `import_hypercode_data`
> Import HyperCode Space Data
*Line 0*  

#### Function: `import_hypercode_space_data`
> Import your actual HyperCode Space data
*Line 16*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\import_perplexity_space.py

#### Module: `import_perplexity_space`
> Perplexity Space Data Importer
*Line 0*  

#### Function: `create_manual_import_script`
> Create a script for manual data entry from Perplexity Space
*Line 17*  

#### Function: `create_json_import_template`
> Create a JSON template for importing data
*Line 86*  

#### Function: `import_from_json`
> Import data from JSON file
*Line 115*  

#### Function: `test_imported_data`
> Test the imported data with context-aware queries
*Line 153*  

#### Function: `show_import_menu`
> Show the import menu
*Line 188*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\local_health_scanner.py

#### Module: `local_health_scanner`
> Local Project Health Scanner for HyperCode
*Line 0*  

#### Class: `ProjectScanner`
> Scans the project for health metrics without external dependencies
*Line 19*  

#### Function: `__init__`
*Line 22*  

#### Function: `scan_project`
> Scan the entire project and return health metrics
*Line 34*  

#### Function: `_scan_directory`
> Recursively scan a directory for Python files
*Line 42*  

#### Function: `_analyze_file`
> Analyze a single Python file
*Line 51*  

#### Function: `_analyze_ast`
> Analyze Python AST for code quality metrics
*Line 74*  

#### Function: `_check_documentation`
> Check documentation coverage
*Line 94*  

#### Function: `_check_tests`
> Check test coverage
*Line 106*  

#### Function: `_calculate_metrics`
> Calculate final metrics
*Line 117*  

#### Function: `print_health_report`
> Print a formatted health report
*Line 128*  

#### Function: `main`
> Main function to run the health scanner
*Line 158*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\perplexity_space_collector.py

#### Module: `perplexity_space_collector`
> Perplexity Space Data Collector
*Line 0*  

#### Function: `quick_copy_paste_collector`
> Quick collector for copy-paste workflow
*Line 18*  

#### Function: `create_structured_template`
> Create a structured JSON template for bulk import
*Line 117*  

#### Function: `show_bro_hacks`
> Show BROski's pro tips
*Line 167*  

#### Function: `main_menu`
> Main menu for the collector
*Line 207*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\perplexity_space_integration.py

#### Module: `perplexity_space_integration`
> Perplexity Space Integration Guide
*Line 0*  

#### Function: `main`
*Line 16*  

### 📄 hypercode_backup_20251205_183301\core\src\utils\run_lexer.py

#### Function: `run_lexer`
> Run the lexer on a source file and print the tokens.
*Line 12*  

### 📄 hypercode_backup_20251205_183301\core\src\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode_backup_20251205_183301\core\tests\benchmark_knowledge_base.py

#### Module: `benchmark_knowledge_base`
> Performance Benchmark Tool for HyperCode Knowledge Base
*Line 0*  

#### Class: `BenchmarkSuite`
> Comprehensive benchmark suite for Knowledge Base
*Line 24*  

#### Function: `__init__`
*Line 27*  

#### Function: `_get_system_info`
> Get system information for benchmark context
*Line 34*  

#### Function: `generate_test_data`
> Generate test data of specified size
*Line 43*  

#### Function: `benchmark_operation`
> Benchmark a single operation
*Line 93*  

#### Function: `run_benchmark_suite`
> Run complete benchmark suite
*Line 118*  

#### Function: `_calculate_summary`
> Calculate summary statistics
*Line 274*  

#### Function: `_generate_recommendations`
> Generate performance recommendations
*Line 296*  

#### Function: `generate_markdown_report`
> Generate beautiful markdown report
*Line 338*  

#### Function: `save_json_results`
> Save results as JSON
*Line 467*  

#### Function: `main`
> Main benchmark runner
*Line 474*  

### 📄 hypercode_backup_20251205_183301\core\tests\conftest.py

#### Function: `sample_hypercode`
*Line 16*  

#### Function: `sample_lexer_tokens`
*Line 27*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_accessibility.py

#### Module: `test_accessibility`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_ai_gateway.py

#### Module: `test_ai_gateway`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_backends.py

#### Module: `test_backends`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_core.py

#### Module: `test_core`
> Test harness for core HyperCode components.
*Line 0*  

#### Function: `run_test`
> Test the lexer, parser, and interpreter with the given source code.
*Line 30*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_integration.py

#### Module: `test_integration`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_intent_blocks.py

#### Module: `test_intent_blocks`
> Test script for Intent Blocks implementation
*Line 0*  

#### Function: `test_intent_block`
> Test parsing of intent blocks
*Line 13*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_interpreter.py

#### Function: `run_code`
> A helper function to run code and capture stdout.
*Line 10*  

#### Class: `TestInterpreter`
*Line 28*  

#### Function: `test_if_statement_then`
*Line 30*  

#### Function: `test_if_statement_else`
*Line 42*  

#### Function: `test_function_call`
*Line 54*  

#### Function: `test_function_with_parameters`
*Line 64*  

#### Function: `test_function_with_return`
*Line 74*  

#### Function: `test_recursive_function_call`
*Line 85*  

#### Function: `test_scoping`
*Line 99*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Comprehensive test suite for knowledge base search functionality.
*Line 0*  

#### Class: `TestKnowledgeBaseSearch`
> Test suite for knowledge base search functionality.
*Line 12*  

#### Function: `sample_documents`
> Create sample documents for testing.
*Line 16*  

#### Function: `knowledge_base`
> Create a knowledge base instance with sample documents.
*Line 40*  

#### Function: `test_basic_search`
> Test basic search functionality.
*Line 48*  

#### Function: `test_search_with_exact_match`
> Test search with exact phrase matching.
*Line 54*  

#### Function: `test_search_case_insensitive`
> Test that search is case-insensitive.
*Line 59*  

#### Function: `test_search_empty_query`
> Test search with empty query returns all or no documents.
*Line 65*  

#### Function: `test_search_no_matches`
> Test search with no matching documents.
*Line 71*  

#### Function: `test_search_ranking`
> Test that search results are ranked by relevance.
*Line 77*  

#### Function: `test_query_normalization`
> Test query normalization (typos, spacing, punctuation).
*Line 90*  

#### Function: `test_multi_word_query`
> Test search with multiple keywords.
*Line 98*  

#### Function: `test_tag_based_search`
> Test search that includes tag matching.
*Line 103*  

#### Class: `TestEdgeCases`
> Test edge cases and boundary conditions.
*Line 112*  

#### Function: `knowledge_base`
*Line 116*  

#### Function: `test_very_short_query`
> Test search with very short query (1-2 chars).
*Line 121*  

#### Function: `test_very_long_query`
> Test search with very long query (paragraph length).
*Line 126*  

#### Function: `test_special_characters_in_query`
> Test search with special characters.
*Line 136*  

#### Function: `test_unicode_in_query`
> Test search with unicode characters.
*Line 141*  

#### Function: `test_sql_injection_attempt`
> Test that search is safe from SQL injection-style attacks.
*Line 146*  

#### Function: `test_repeated_queries`
> Test that repeated queries return consistent results.
*Line 151*  

#### Class: `TestPerformance`
> Performance benchmarking tests.
*Line 159*  

#### Function: `large_knowledge_base`
> Create a knowledge base with many documents.
*Line 163*  

#### Function: `test_search_response_time`
> Test that search completes within acceptable time.
*Line 179*  

#### Function: `test_concurrent_searches`
> Test multiple concurrent search operations.
*Line 189*  

#### Function: `test_memory_usage`
> Test memory usage during search operations.
*Line 207*  

#### Class: `TestIntegrationWithPerplexity`
> Test integration with EnhancedPerplexityClient.
*Line 213*  

#### Function: `mock_perplexity_client`
> Create a mock Perplexity client.
*Line 217*  

#### Function: `mock_knowledge_base`
> Create a mock knowledge base.
*Line 229*  

#### Function: `test_enhanced_query_with_context`
> Test that queries are enhanced with knowledge base context.
*Line 243*  

#### Function: `test_fallback_to_perplexity_api`
> Test fallback to Perplexity API when no local context found.
*Line 259*  

#### Function: `test_context_ranking_and_selection`
> Test that best context is selected for query enhancement.
*Line 273*  

#### Class: `TestDocumentManagement`
> Test document addition, update, and removal.
*Line 288*  

#### Function: `knowledge_base`
*Line 292*  

#### Function: `test_add_document`
> Test adding a new document to knowledge base.
*Line 300*  

#### Function: `test_update_document`
> Test updating an existing document.
*Line 310*  

#### Function: `test_remove_document`
> Test removing a document.
*Line 315*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_knowledge_base_comprehensive.py

#### Module: `test_knowledge_base_comprehensive`
> Comprehensive Test Suite for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestKnowledgeBaseUnit`
> Unit tests for Knowledge Base functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_docs`
> Sample documents for testing
*Line 36*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 59*  

#### Function: `test_add_single_document`
> Test adding a single document
*Line 65*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 74*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 84*  

#### Function: `test_search_exact_match`
> Test exact search matching
*Line 102*  

#### Function: `test_search_partial_match`
> Test partial search matching
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 124*  

#### Function: `test_search_case_insensitive`
> Test case insensitive search
*Line 135*  

#### Function: `test_empty_search`
> Test empty search query
*Line 147*  

#### Function: `test_nonexistent_search`
> Test search for nonexistent terms
*Line 155*  

#### Function: `test_get_context_for_query`
> Test context extraction
*Line 165*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 176*  

#### Function: `test_document_update`
> Test updating existing documents
*Line 186*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 202*  

#### Function: `test_delete_document`
> Test document deletion
*Line 213*  

#### Class: `TestKnowledgeBaseIntegration`
> Integration tests for Knowledge Base
*Line 229*  

#### Function: `populated_kb`
> Create a populated knowledge base for integration testing
*Line 233*  

#### Function: `test_complex_search_queries`
> Test complex search scenarios
*Line 277*  

#### Function: `test_search_ranking_quality`
> Test that search results are properly ranked
*Line 291*  

#### Function: `test_related_term_expansion`
> Test that related terms are properly expanded
*Line 301*  

#### Function: `test_performance_with_large_dataset`
> Test performance with larger dataset
*Line 313*  

#### Function: `test_concurrent_access_simulation`
> Test simulated concurrent access
*Line 332*  

#### Class: `TestKnowledgeBasePerformance`
> Performance tests for Knowledge Base
*Line 356*  

#### Function: `large_kb`
> Create a large knowledge base for performance testing
*Line 360*  

#### Function: `test_search_performance_large_dataset`
> Test search performance with large dataset
*Line 382*  

#### Function: `test_save_performance_large_dataset`
> Test save performance with large dataset
*Line 396*  

#### Function: `test_load_performance_large_dataset`
> Test load performance with large dataset
*Line 409*  

#### Function: `test_memory_usage_large_dataset`
> Test memory usage with large dataset
*Line 423*  

#### Class: `TestKnowledgeBaseEdgeCases`
> Edge case tests for Knowledge Base
*Line 446*  

#### Function: `edge_case_kb`
> Create knowledge base for edge case testing
*Line 450*  

#### Function: `test_empty_title_handling`
> Test handling of documents with empty titles
*Line 494*  

#### Function: `test_special_characters_handling`
> Test handling of special characters and unicode
*Line 499*  

#### Function: `test_very_long_titles`
> Test handling of very long titles
*Line 507*  

#### Function: `test_empty_content_handling`
> Test handling of documents with empty content
*Line 512*  

#### Function: `test_none_tags_handling`
> Test handling of None tags
*Line 517*  

#### Function: `test_malformed_json_handling`
> Test handling of malformed JSON files
*Line 531*  

#### Function: `test_file_permission_handling`
> Test handling of file permission issues
*Line 544*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_lexer.py

#### Function: `test_lexer_basic_tokens`
*Line 5*  

#### Function: `test_lexer_strings`
*Line 23*  

#### Function: `test_lexer_operators`
*Line 48*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_lexer_extended.py

#### Function: `test_lexer_escaped_strings`
> Test handling of strings with escaped characters.
*Line 5*  

#### Function: `test_lexer_numbers`
> Test various number formats.
*Line 18*  

#### Function: `test_lexer_operators`
> Test all operators.
*Line 39*  

#### Function: `test_lexer_comments`
> Test handling of single-line and multi-line comments.
*Line 86*  

#### Function: `test_lexer_whitespace`
> Test handling of various whitespace characters.
*Line 115*  

#### Function: `test_lexer_error_handling`
> Test error handling for invalid tokens.
*Line 130*  

#### Function: `test_lexer_hex_numbers`
> Test hexadecimal number literals.
*Line 139*  

#### Function: `test_lexer_binary_numbers`
> Test binary number literals.
*Line 157*  

#### Function: `test_lexer_scientific_notation`
> Test scientific notation numbers.
*Line 169*  

#### Function: `test_lexer_string_escapes`
> Test string escape sequences.
*Line 180*  

#### Function: `test_lexer_keywords`
> Test all language keywords.
*Line 197*  

#### Function: `test_lexer_position_tracking`
> Test that line and column numbers are tracked correctly.
*Line 223*  

#### Function: `test_lexer_error_recovery`
> Test that the lexer raises errors on invalid characters.
*Line 243*  

#### Function: `test_lexer_error_messages`
> Test that lexer error messages are informative.
*Line 252*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_parser.py

#### Function: `test_parse_literal`
*Line 12*  

#### Function: `test_parse_variable_declaration`
*Line 24*  

#### Function: `test_parse_binary_expression`
*Line 37*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 185*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_sensory_profiles.py

#### Module: `test_sensory_profiles`
> Tests for the sensory profile system.
*Line 0*  

#### Function: `test_visual_settings_creation`
> Test creating visual settings.
*Line 21*  

#### Function: `test_audio_settings_creation`
> Test creating audio settings.
*Line 35*  

#### Function: `test_animation_settings_creation`
> Test creating animation settings.
*Line 44*  

#### Function: `test_sensory_profile_creation`
> Test creating a complete sensory profile.
*Line 55*  

#### Function: `test_profile_serialization`
> Test serializing AND deserializing a profile.
*Line 71*  

#### Function: `test_profile_file_io`
> Test saving and loading a profile to/from a file.
*Line 92*  

#### Function: `test_profile_manager_initialization`
> Test initializing the profile manager and checking default profiles.
*Line 115*  

#### Function: `test_profile_manager_get_profile`
> Test getting a profile by name.
*Line 129*  

#### Function: `test_profile_manager_save_custom_profile`
> Test saving a custom profile.
*Line 142*  

#### Function: `test_profile_manager_delete_profile`
> Test deleting a profile.
*Line 169*  

### 📄 hypercode_backup_20251205_183301\core\tests\test_syntax.py

#### Module: `test_syntax`
> Tests for HyperCode syntax features.
*Line 0*  

#### Function: `test_program_structure`
> Test basic program structure and entry point.
*Line 8*  

#### Function: `test_function_definition`
> Test function definition syntax.
*Line 26*  

#### Function: `test_io_operations`
> Test input/output operations.
*Line 49*  

#### Function: `test_variables`
> Test variable declarations and assignments.
*Line 73*  

#### Function: `test_loops`
> Test loop constructs.
*Line 96*  

#### Function: `test_conditionals`
> Test if/else conditionals.
*Line 117*  

#### Function: `test_goto`
> Test goto and labels.
*Line 142*  

#### Function: `test_comments`
> Test that comments are properly ignored.
*Line 167*  

### 📄 hypercode_backup_20251205_183301\core\tests\tests\test_lexer_enhanced.py

#### Function: `test_lexer_edge_cases`
*Line 7*  

#### Function: `test_lexer_error_handling`
*Line 28*  

#### Function: `test_lexer_number_literals`
*Line 43*  

#### Function: `test_lexer_string_interpolation`
*Line 65*  

#### Function: `test_lexer_docstrings`
*Line 79*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\lexer\test_lexer_basic.py

#### Module: `test_lexer_basic`
> Unit tests for the HyperCode lexer's basic functionality.
*Line 0*  

#### Class: `TestLexerBasic`
> Test basic lexer functionality.
*Line 9*  

#### Function: `test_empty_source`
> Test that an empty source returns only EOF token.
*Line 12*  

#### Function: `test_whitespace_handling`
> Test that whitespace is properly handled and ignored.
*Line 19*  

#### Function: `test_single_character_tokens`
> Test recognition of single-character tokens.
*Line 27*  

#### Function: `test_comments_are_ignored`
> Test that comments are properly ignored.
*Line 52*  

#### Function: `test_string_literals`
> Test string literal tokenization.
*Line 72*  

#### Function: `test_number_literals`
> Test number literal tokenization.
*Line 87*  

#### Function: `test_identifiers_and_keywords`
> Test identifier and keyword recognition.
*Line 103*  

#### Function: `test_error_handling`
> Test error handling for invalid tokens.
*Line 139*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_intent_blocks.py

#### Module: `test_intent_blocks`
> Test script for Intent Blocks implementation
*Line 0*  

#### Function: `test_intent_block`
> Test parsing of intent blocks
*Line 13*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Phase 1 Unit Tests for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestHyperCodeKnowledgeBase`
> Test suite for HyperCodeKnowledgeBase core functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_documents`
> Sample documents for testing
*Line 33*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 56*  

#### Function: `test_add_document`
> Test adding a single document
*Line 61*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 82*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 92*  

#### Function: `test_search_exact_match`
> Test exact term matching in search
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 126*  

#### Function: `test_search_related_terms`
> Test related term expansion
*Line 139*  

#### Function: `test_search_space_data_boost`
> Test that space data gets boosted in search
*Line 153*  

#### Function: `test_get_context_for_query`
> Test context extraction for queries
*Line 180*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 192*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 203*  

#### Function: `test_empty_search`
> Test search with empty query
*Line 216*  

#### Function: `test_search_nonexistent_term`
> Test search for term that doesn't exist
*Line 221*  

#### Function: `test_document_update`
> Test updating existing document
*Line 231*  

#### Class: `TestResearchDocument`
> Test suite for ResearchDocument dataclass
*Line 250*  

#### Function: `test_document_creation`
> Test creating a research document
*Line 253*  

#### Function: `test_document_optional_fields`
> Test document with optional fields
*Line 273*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_lexer.py

#### Module: `test_lexer`
> Test script for the HyperCode lexer.
*Line 0*  

#### Function: `test_lexer`
> Test the lexer with the given source code and print the results.
*Line 12*  

#### Function: `run_tests`
> Run a series of test cases for the lexer.
*Line 42*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_lexer_pytest.py

#### Module: `test_lexer_pytest`
> Pytest tests for the HyperCode lexer.
*Line 0*  

#### Function: `test_basic_arithmetic`
> Test basic arithmetic expressions.
*Line 9*  

#### Function: `test_variable_declaration`
> Test variable declarations.
*Line 25*  

#### Function: `test_string_literals`
> Test string literals.
*Line 40*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_mcp_connection.py

#### Function: `check_port`
> Check if a port is open on the given host.
*Line 26*  

#### Function: `find_running_servers`
> Scan common ports to find running servers.
*Line 36*  

#### Function: `test_server_connection`
> Test connection to a single MCP server.
*Line 49*  

#### Function: `test_all_servers`
> Test connection to all MCP servers and print results.
*Line 90*  

#### Function: `check_dependencies`
> Check if required dependencies are installed.
*Line 139*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 185*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode_backup_20251205_183301\core\tests\unit\test_search_algorithm.py

#### Module: `test_search_algorithm`
> Phase 1 Unit Tests for Search Algorithm
*Line 0*  

#### Class: `TestSearchAlgorithm`
> Test suite for search algorithm functionality
*Line 20*  

#### Function: `populated_kb`
> Create a knowledge base with test documents
*Line 24*  

#### Function: `test_exact_title_match_highest_score`
> Test that exact title matches get highest priority
*Line 80*  

#### Function: `test_space_data_boosting`
> Test that space data gets boosted in search results
*Line 92*  

#### Function: `test_related_term_expansion`
> Test related term matching functionality
*Line 105*  

#### Function: `test_tag_matching_scoring`
> Test that tag matches contribute to scoring
*Line 126*  

#### Function: `test_content_frequency_scoring`
> Test that multiple content occurrences increase score
*Line 136*  

#### Function: `test_partial_word_matching`
> Test partial word matching for longer terms
*Line 149*  

#### Function: `test_query_word_ordering`
> Test that query words are properly processed
*Line 167*  

#### Function: `test_case_insensitive_search`
> Test that search is case insensitive
*Line 179*  

#### Function: `test_empty_query_returns_no_results`
> Test that empty queries return no results
*Line 202*  

#### Function: `test_limit_parameter_respected`
> Test that search limit parameter works correctly
*Line 210*  

#### Function: `test_no_results_for_nonexistent_terms`
> Test search for terms that don't exist
*Line 219*  

#### Function: `test_special_characters_in_query`
> Test search with special characters
*Line 227*  

#### Function: `test_unicode_characters`
> Test search with unicode characters
*Line 237*  

#### Function: `test_search_performance_with_large_kb`
> Test search performance with larger knowledge base
*Line 256*  

#### Function: `test_search_result_consistency`
> Test that search results are consistent across multiple calls
*Line 277*  

#### Class: `TestSearchScoringDetails`
> Test detailed scoring algorithm behavior
*Line 292*  

#### Function: `scoring_kb`
> Create KB for detailed scoring tests
*Line 296*  

#### Function: `test_title_match_beats_content_match`
> Test that title matches score higher than content matches
*Line 324*  

#### Function: `test_space_data_boosting_works`
> Test that space data gets boosted
*Line 332*  

#### Function: `test_frequency_scoring`
> Test that content frequency affects scoring
*Line 340*  

### 📄 hypercode_backup_20251205_183301\database_analyzer.py

#### Module: `database_analyzer`
> Database Analysis and Improvement Tool
*Line 0*  

#### Class: `EntityMetrics`
*Line 15*  

#### Class: `DocstringStats`
*Line 21*  

#### Class: `DatabaseAnalyzer`
*Line 28*  

#### Function: `__init__`
*Line 29*  

#### Function: `load_database`
> Load and validate the database.
*Line 48*  

#### Function: `analyze_documentation`
> Analyze documentation coverage and quality.
*Line 64*  

#### Function: `analyze_test_coverage`
> Analyze test coverage across the codebase.
*Line 96*  

#### Function: `analyze_code_structure`
> Analyze code structure metrics.
*Line 112*  

#### Function: `generate_report`
> Generate a comprehensive report of findings.
*Line 135*  

#### Function: `get_entities_needing_docs`
> Get entities that need documentation.
*Line 185*  

#### Function: `get_untested_entities`
> Get entities that need tests.
*Line 191*  

#### Function: `main`
> Main function to run the database analyzer.
*Line 196*  

### 📄 hypercode_backup_20251205_183301\fix_database_issues.py

#### Module: `fix_database_issues`
> Database Health Check and Fix Script
*Line 0*  

#### Class: `FixedCodeEntity`
> Enhanced version of CodeEntity with validation and better documentation.
*Line 18*  

#### Function: `__post_init__`
> Validate entity data after initialization.
*Line 45*  

#### Function: `_validate_required_fields`
> Ensure all required fields have values.
*Line 58*  

#### Function: `_validate_field_types`
> Check that all fields have the correct types.
*Line 65*  

#### Function: `_normalize_fields`
> Normalize field values.
*Line 78*  

#### Function: `_clean_docstring`
> Clean and standardize the docstring.
*Line 104*  

#### Function: `to_dict`
> Convert entity to dictionary for JSON serialization.
*Line 118*  

#### Class: `DatabaseFixer`
> Handles fixing and validating the Hypercode database.
*Line 136*  

#### Function: `__init__`
> Initialize with path to the database file.
*Line 139*  

#### Function: `load_database`
> Load and validate the database.
*Line 153*  

#### Function: `_check_for_issues`
> Check an entity for common issues.
*Line 190*  

#### Function: `fix_issues`
> Fix common issues in the database.
*Line 217*  

#### Function: `save_database`
> Save the fixed database to a file.
*Line 245*  

#### Function: `generate_report`
> Generate a report of issues and fixes.
*Line 271*  

#### Function: `main`
> Main function to run the database fixer.
*Line 312*  

### 📄 hypercode_backup_20251205_183301\hypercode\accessibility\adhd_optimizer.py

#### Module: `adhd_optimizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\accessibility\autism_preset.py

#### Module: `autism_preset`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\accessibility\dyslexia_formatter.py

#### Module: `dyslexia_formatter`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\accessibility\sensory_customizer.py

#### Module: `sensory_customizer`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\accessibility\wcag_auditor.py

#### Module: `wcag_auditor`
> Neurodivergent-first accessibility tools
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\benchmarks\__init__.py

#### Function: `benchmark_lexer`
> Benchmark the lexer with the given source code.
*Line 13*  

#### Function: `print_benchmark_results`
> Print benchmark results in a readable format.
*Line 38*  

### 📄 hypercode_backup_20251205_183301\hypercode\benchmarks\benchmarks_lexer.py

#### Function: `benchmark_lexer`
> Benchmark the lexer with the given source code.
*Line 7*  

#### Function: `print_benchmark_results`
> Print benchmark results in a readable format.
*Line 32*  

### 📄 hypercode_backup_20251205_183301\hypercode\build-hyper-database.py

#### Module: `build-hyper-database`
> Hyper Database Builder - Scans HyperCode repo, builds knowledge graph.
*Line 0*  

#### Class: `HyperDatabaseBuilder`
> Scans codebase and builds semantic knowledge graph.
*Line 21*  

#### Function: `__init__`
> Initialize builder with repo root path.
*Line 24*  

#### Function: `scan_python_file`
> Extract functions, classes from Python file.
*Line 32*  

#### Function: `scan_javascript_file`
> Extract functions from JavaScript (regex-based).
*Line 78*  

#### Function: `should_skip_directory`
> Check if directory should be skipped.
*Line 107*  

#### Function: `build`
> Scan entire repo and build database.
*Line 127*  

#### Function: `generate_markdown_report`
> Generate HYPER_DATABASE.md report.
*Line 161*  

#### Function: `generate_json_report`
> Generate machine-readable HYPER_DATABASE.json.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 263*  

### 📄 hypercode_backup_20251205_183301\hypercode\knowledge_graph\graph_builder.py

#### Module: `graph_builder`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\knowledge_graph\sparql_query.py

#### Module: `sparql_query`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\knowledge_graph\update_agent.py

#### Module: `update_agent`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\live_research\doc_generator.py

#### Module: `doc_generator`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\live_research\github_publisher.py

#### Module: `github_publisher`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\live_research\paper_indexer.py

#### Module: `paper_indexer`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\live_research\research_crawler.py

#### Module: `research_crawler`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\live_research\synthesis_engine.py

#### Module: `synthesis_engine`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\__init__.py

#### Module: `__init__`
> HyperCode MCP (Model Context Protocol) Server Package
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\__init__.py

#### Module: `__init__`
> MCP Servers Package
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\aws_cli.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\aws_resource_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\code_analysis.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\dataset_downloader.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\file_system.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\human_input.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\hypercode_syntax.py

#### Module: `hypercode_syntax`
> HyperCode Syntax MCP Server
*Line 0*  

#### Class: `HyperCodeSyntaxServer`
> 🎨 MCP Server for HyperCode Visual Syntax Integration
*Line 28*  

#### Function: `__init__`
*Line 31*  

#### Function: `handle_request`
> Handle MCP requests from IDE
*Line 35*  

#### Function: `_initialize`
> Initialize the MCP server
*Line 56*  

#### Function: `_document_changed`
> Handle document changes for real-time parsing
*Line 79*  

#### Function: `_text_hover`
> Provide hover information for semantic annotations
*Line 98*  

#### Function: `_completion`
> Provide completion for semantic annotations
*Line 121*  

#### Function: `_parse_document`
> Parse entire document and return semantic structure
*Line 150*  

#### Function: `_validate_neurodiversity`
> Validate neurodiversity compliance and provide suggestions
*Line 179*  

#### Function: `_generate_diagnostics`
> Generate IDE diagnostics from parsed functions
*Line 216*  

#### Function: `_get_annotation_hover_info`
> Generate hover information for semantic annotations
*Line 266*  

#### Function: `main`
> Main MCP server loop
*Line 294*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\path_service.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\user_profile_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\valkey_service.py

#### Function: `check_redis_connection`
*Line 40*  

#### Function: `health_check`
> Health check endpoint to verify that the service is running.
*Line 59*  

#### Function: `set_key`
> Set a value for a given key. The value should be a JSON object.
*Line 67*  

#### Function: `get_key`
> Get the value for a given key.
*Line 80*  

#### Function: `hset_key`
> Set a field (key) in a hash (name). The value should be a JSON object.
*Line 95*  

#### Function: `hget_key`
> Get a field (key) from a hash (name).
*Line 107*  

#### Function: `hgetall_hash`
> Get all fields and values for a given hash name.
*Line 126*  

#### Function: `main`
> Main function to run the Valkey Service MCP Server.
*Line 144*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\servers\web_search.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\setup.py

#### Module: `setup`
> MCP Setup Script
*Line 0*  

#### Function: `install_dependencies`
> Install required dependencies
*Line 16*  

#### Function: `verify_setup`
> Verify that MCP is properly set up
*Line 31*  

#### Function: `show_next_steps`
> Show next steps for using MCP
*Line 54*  

#### Function: `main`
*Line 72*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\start_servers.py

#### Module: `start_servers`
> MCP Servers Startup Script
*Line 0*  

#### Function: `start_server`
> Start a specific MCP server
*Line 34*  

#### Function: `list_servers`
> List all available servers
*Line 59*  

#### Function: `main`
*Line 66*  

### 📄 hypercode_backup_20251205_183301\hypercode\mcp\test_mcp.py

#### Module: `test_mcp`
> MCP Servers Test Script
*Line 0*  

#### Function: `test_server_imports`
> Test that all servers can be imported
*Line 15*  

#### Function: `main`
*Line 47*  

### 📄 hypercode_backup_20251205_183301\hypercode\new files to check\backend\research\__init__.py

#### Module: `__init__`
> Initialization for the research module.
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\new files to check\backend\research\db.py

#### Module: `db`
> Database configuration for the HyperCode research module.
*Line 0*  

#### Function: `_get_database_url`
> Return the database URL to connect to.
*Line 35*  

### 📄 hypercode_backup_20251205_183301\hypercode\new files to check\backend\research\models.py

#### Module: `models`
> ORM models for the HyperCode research database.
*Line 0*  

#### Class: `Study`
> Top‑level research study.
*Line 32*  

#### Function: `__repr__`
*Line 52*  

#### Class: `Source`
> External or internal resource used in a study.
*Line 56*  

#### Function: `__repr__`
*Line 81*  

#### Class: `LanguageVersion`
> Version of the HyperCode language.
*Line 85*  

#### Function: `__repr__`
*Line 102*  

#### Class: `Task`
> A coding task or challenge used in experiments.
*Line 106*  

#### Function: `__repr__`
*Line 124*  

#### Class: `Participant`
> An anonymised participant in the study.
*Line 128*  

#### Function: `__repr__`
*Line 144*  

#### Class: `Session`
> A single coding session of a participant performing a task.
*Line 148*  

#### Function: `__repr__`
*Line 169*  

#### Class: `Event`
> Low‑level interaction within a session.
*Line 176*  

#### Function: `__repr__`
*Line 193*  

#### Class: `Feedback`
> Qualitative and quantitative feedback for a session.
*Line 199*  

#### Function: `__repr__`
*Line 221*  

### 📄 hypercode_backup_20251205_183301\hypercode\new files to check\backend\research\scripts\import_sources_from_folder.py

#### Module: `import_sources_from_folder`
> Import research sources from a folder into the database.
*Line 0*  

#### Function: `infer_kind`
*Line 25*  

#### Function: `main`
*Line 36*  

### 📄 hypercode_backup_20251205_183301\hypercode\new files to check\backend\research\scripts\seed_basic_data.py

#### Module: `seed_basic_data`
> Seed the research database with initial data.
*Line 0*  

#### Function: `main`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\hypercode\run_lexer.py

#### Function: `run_lexer`
> Run the lexer on a source file and print the tokens.
*Line 13*  

### 📄 hypercode_backup_20251205_183301\hypercode\scripts\style_guide_collector.py

#### Module: `style_guide_collector`
> 🎨 HyperCode Style Guide Feedback Collector
*Line 0*  

#### Class: `StyleGuideCollector`
> 🎨 Collects and analyzes style guide feedback from the community
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `_load_feedback`
> 📂 Load existing feedback data
*Line 32*  

#### Function: `_save_feedback`
> 💾 Save feedback data
*Line 51*  

#### Function: `add_feedback`
> 📝 Add new feedback entry
*Line 60*  

#### Function: `_update_analysis`
> 📊 Update analysis based on new feedback
*Line 102*  

#### Function: `analyze_feedback`
> 📊 Generate comprehensive analysis of all feedback
*Line 151*  

#### Function: `_get_top_items`
> 📊 Get top items from a frequency dictionary
*Line 189*  

#### Function: `_calculate_consensus`
> 📊 Calculate consensus for preference categories
*Line 212*  

#### Function: `_generate_recommendations`
> 💡 Generate style guide recommendations based on feedback
*Line 247*  

#### Function: `import_github_issues`
> 📥 Import feedback from GitHub issues
*Line 331*  

#### Function: `generate_report`
> 📊 Generate comprehensive feedback report
*Line 354*  

#### Function: `interactive_feedback`
> 🎯 Interactive feedback collection from command line
*Line 419*  

#### Function: `main`
> 🚀 Main entry point
*Line 527*  

### 📄 hypercode_backup_20251205_183301\hypercode\scripts\test_perplexity_api.py

#### Module: `test_perplexity_api`
> Test script for Perplexity API integration.
*Line 0*  

#### Function: `main`
> Test the Perplexity API connection and make a sample query.
*Line 17*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\ai_gateway\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\ai_gateway\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\ai_gateway\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\ai_gateway\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\ai_gateway\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\ai_gateway\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\ai_gateway\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\base_gateway.py

#### Module: `base_gateway`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\build.py

#### Module: `build`
> Build script for the HyperCode language.
*Line 0*  

#### Function: `build`
> Builds a HyperCode source file to the target language.
*Line 34*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\claude_adapter.py

#### Module: `claude_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `ClaudeAdapterAdapter`
> Adapter for Claude Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\core\__init__.py

#### Module: `__init__`
> HyperCode Core Module
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\core\ast.py

#### Class: `Node`
*Line 9*  

#### Function: `accept`
*Line 10*  

#### Class: `Expr`
*Line 20*  

#### Class: `Literal`
*Line 25*  

#### Class: `Variable`
*Line 30*  

#### Class: `Assign`
*Line 35*  

#### Class: `Binary`
*Line 41*  

#### Class: `Unary`
*Line 48*  

#### Class: `Grouping`
*Line 54*  

#### Class: `Call`
*Line 59*  

#### Class: `Get`
*Line 66*  

#### Class: `Stmt`
*Line 73*  

#### Class: `Expression`
*Line 78*  

#### Class: `Print`
*Line 83*  

#### Class: `Var`
*Line 88*  

#### Class: `Block`
*Line 94*  

#### Class: `Intent`
*Line 99*  

#### Class: `Function`
*Line 104*  

#### Class: `If`
*Line 111*  

#### Class: `Return`
*Line 118*  

#### Class: `Program`
*Line 125*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\core\ast_nodes.py

#### Module: `ast_nodes`
> Abstract Syntax Tree (AST) nodes for the HyperCode language.
*Line 0*  

#### Class: `Node`
> Base class for all AST nodes.
*Line 24*  

#### Class: `Expression`
> Base class for all expression nodes.
*Line 31*  

#### Class: `Statement`
> Base class for all statement nodes.
*Line 38*  

#### Class: `Program`
> Represents the entire program as a list of statements.
*Line 45*  

#### Class: `Identifier`
> Represents an identifier (e.g., a variable name).
*Line 52*  

#### Class: `Literal`
> Represents a literal value (e.g., number, string).
*Line 59*  

#### Class: `VariableDeclaration`
> Represents a variable declaration (let or const).
*Line 66*  

#### Class: `BinaryOperation`
> Represents a binary operation (e.g., a + b).
*Line 75*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\core\interpreter.py

#### Class: `RuntimeError`
*Line 8*  

#### Function: `__init__`
*Line 9*  

#### Class: `Environment`
*Line 15*  

#### Function: `__init__`
*Line 16*  

#### Function: `define`
*Line 20*  

#### Function: `get`
*Line 23*  

#### Function: `assign`
*Line 30*  

#### Class: `Callable`
*Line 40*  

#### Function: `arity`
*Line 41*  

#### Function: `call`
*Line 44*  

#### Class: `Function`
*Line 48*  

#### Function: `__init__`
*Line 49*  

#### Function: `call`
*Line 53*  

#### Function: `arity`
*Line 65*  

#### Class: `ReturnException`
*Line 69*  

#### Function: `__init__`
*Line 70*  

#### Class: `Interpreter`
*Line 74*  

#### Function: `__init__`
*Line 75*  

#### Class: `Clock`
*Line 82*  

#### Function: `arity`
*Line 83*  

#### Function: `call`
*Line 86*  

#### Function: `__str__`
*Line 89*  

#### Function: `execute_block`
*Line 94*  

#### Function: `interpret`
*Line 103*  

#### Function: `execute`
*Line 112*  

#### Function: `evaluate`
*Line 115*  

#### Function: `visit_Expression`
*Line 118*  

#### Function: `visit_Print`
*Line 122*  

#### Function: `visit_Var`
*Line 129*  

#### Function: `visit_Block`
*Line 136*  

#### Function: `visit_Expression`
*Line 140*  

#### Function: `visit_Print`
*Line 144*  

#### Function: `visit_Intent`
*Line 150*  

#### Function: `visit_Function`
*Line 155*  

#### Function: `visit_Return`
*Line 160*  

#### Function: `visit_Literal`
*Line 166*  

#### Function: `visit_Grouping`
*Line 169*  

#### Function: `visit_Variable`
*Line 172*  

#### Function: `visit_Assign`
*Line 175*  

#### Function: `visit_Call`
*Line 180*  

#### Function: `visit_Binary`
*Line 198*  

#### Function: `visit_Unary`
*Line 229*  

#### Function: `is_truthy`
*Line 237*  

#### Function: `stringify`
*Line 244*  

#### Function: `get_output`
*Line 256*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\core\lexer.py

#### Module: `lexer`
> HyperCode Lexer Module
*Line 0*  

#### Class: `LexerError`
> Represents a lexical analysis error.
*Line 17*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode programming language.
*Line 34*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 42*  

#### Function: `scan_tokens`
> Scan the source code and return a list of tokens.
*Line 99*  

#### Function: `scan_token`
> Scan a single token.
*Line 109*  

#### Function: `number`
> Lex a number literal.
*Line 168*  

#### Function: `string`
> Lex a string literal.
*Line 203*  

#### Function: `docstring`
> Lex a docstring.
*Line 252*  

#### Function: `identifier`
> Lex an identifier or keyword.
*Line 278*  

#### Function: `error`
> Report a lexing error.
*Line 288*  

#### Function: `is_at_end`
> Check if we've reached the end of the source.
*Line 312*  

#### Function: `advance`
> Consume and return the next character.
*Line 316*  

#### Function: `match`
> Conditionally consume a character if it matches the expected value.
*Line 325*  

#### Function: `peek`
> Look at the next character without consuming it.
*Line 335*  

#### Function: `peek_next`
> Look at the character after the next one without consuming it.
*Line 341*  

#### Function: `add_token`
> Add a new token to the token list.
*Line 347*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\core\parser.py

#### Class: `ParseError`
*Line 7*  

#### Class: `Parser`
*Line 11*  

#### Function: `__init__`
*Line 12*  

#### Function: `parse`
> Parse the entire program.
*Line 16*  

#### Function: `declaration`
*Line 25*  

#### Function: `var_declaration`
*Line 36*  

#### Function: `statement`
*Line 61*  

#### Function: `print_statement`
*Line 72*  

#### Function: `expression_statement`
*Line 77*  

#### Function: `block`
*Line 82*  

#### Function: `expression`
*Line 91*  

#### Function: `assignment`
*Line 94*  

#### Function: `equality`
*Line 109*  

#### Function: `comparison`
*Line 119*  

#### Function: `term`
*Line 132*  

#### Function: `factor`
*Line 140*  

#### Function: `unary`
*Line 148*  

#### Function: `primary`
*Line 155*  

#### Function: `function`
*Line 177*  

#### Function: `if_statement`
*Line 200*  

#### Function: `return_statement`
*Line 212*  

#### Function: `match`
*Line 222*  

#### Function: `consume`
*Line 229*  

#### Function: `error`
*Line 239*  

#### Function: `synchronize`
*Line 245*  

#### Function: `check`
*Line 265*  

#### Function: `advance`
*Line 270*  

#### Function: `is_at_end`
*Line 275*  

#### Function: `peek`
*Line 278*  

#### Function: `previous`
*Line 281*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\core\tokens.py

#### Module: `tokens`
> HyperCode Token Types and Definitions
*Line 0*  

#### Class: `TokenType`
*Line 11*  

#### Class: `Token`
> Represents a token in the HyperCode language.
*Line 71*  

#### Function: `__init__`
*Line 83*  

#### Function: `__str__`
*Line 92*  

#### Function: `__repr__`
*Line 95*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\duelcode\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\duelcode\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\duelcode\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\duelcode\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\duelcode\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\duelcode\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\duelcode_validator.py

#### Module: `duelcode_validator`
> Enhanced DuelCode Documentation Validator
*Line 0*  

#### Class: `Severity`
*Line 16*  

#### Class: `ValidationResult`
*Line 23*  

#### Class: `DuelCodeValidator`
> Validates DuelCode documentation files against the required format.
*Line 30*  

#### Function: `__init__`
*Line 51*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 58*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 71*  

#### Function: `validate`
> Run all validation checks.
*Line 81*  

#### Function: `validate_structure`
> Validate the overall document structure.
*Line 93*  

#### Function: `validate_headings`
> Validate heading hierarchy and formatting.
*Line 129*  

#### Function: `validate_code_blocks`
> Validate code blocks for proper formatting and language specification.
*Line 171*  

#### Function: `validate_checklists`
> Validate checklist items in the document.
*Line 210*  

#### Function: `validate_visual_elements`
> Validate visual elements like diagrams, images, etc.
*Line 245*  

#### Function: `validate_links`
> Validate internal and external links.
*Line 263*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 283*  

#### Function: `main`
> Main entry point for the validator.
*Line 316*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\enhanced_validator.py

#### Module: `enhanced_validator`
> Enhanced DuelCode Validator with additional validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 19*  

#### Class: `DuelCodeEnhancedValidator`
> Enhanced validator with additional rules for DuelCode documentation.
*Line 26*  

#### Function: `__init__`
*Line 83*  

#### Function: `_add_result`
> Add a validation result with proper line number.
*Line 90*  

#### Function: `_find_lines`
> Find all lines matching the pattern with their line numbers.
*Line 103*  

#### Function: `validate_code_blocks_have_language`
> Ensure all code blocks have a specified language.
*Line 115*  

#### Function: `validate_has_visual_representation`
> Ensure each part has a visual representation.
*Line 128*  

#### Function: `validate_has_practical_exercise`
> Ensure each part has a practical exercise.
*Line 140*  

#### Function: `validate_has_learning_objectives`
> Ensure learning objectives are present and well-formed.
*Line 152*  

#### Function: `validate_has_checklist`
> Ensure a checklist is present and has items.
*Line 174*  

#### Function: `validate_has_conclusion`
> Ensure the document has a conclusion section.
*Line 195*  

#### Function: `validate_has_whats_next`
> Suggest adding a 'What's Next' section.
*Line 204*  

#### Function: `validate_code_quality`
> Check code quality in code blocks.
*Line 213*  

#### Function: `_analyze_code_block`
> Analyze a code block for quality issues.
*Line 234*  

#### Function: `_analyze_python_code`
> Python-specific code analysis.
*Line 256*  

#### Function: `_analyze_javascript_code`
> JavaScript/TypeScript-specific code analysis.
*Line 277*  

#### Function: `validate_has_glossary`
> Suggest adding a glossary for technical terms.
*Line 291*  

#### Function: `validate_has_see_also`
> Suggest adding a 'See Also' section with related resources.
*Line 325*  

#### Function: `validate_has_faq`
> Suggest adding an FAQ section.
*Line 334*  

#### Function: `validate_has_acknowledgments`
> Suggest adding an acknowledgments section.
*Line 344*  

#### Function: `validate_all`
> Run all validations.
*Line 353*  

#### Function: `print_validation_results`
> Print validation results in a user-friendly format.
*Line 376*  

#### Function: `main`
> Main entry point for the enhanced validator.
*Line 407*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode-backend-js-COMPLETE.py

#### Module: `hypercode-backend-js-COMPLETE`
> HyperCode JavaScript Backend - Complete Implementation
*Line 0*  

#### Class: `JSCompiler`
> Compiles HyperCode AST to JavaScript.
*Line 19*  

#### Function: `__init__`
> Initialize compiler.
*Line 30*  

#### Function: `compile`
> Compile AST to JavaScript.
*Line 42*  

#### Function: `_generate_header`
> Generate JavaScript header
*Line 65*  

#### Function: `_generate_setup`
> Generate setup code (memory tape, pointer, I/O)
*Line 74*  

#### Function: `_generate_main`
> Generate JavaScript for AST node.
*Line 110*  

#### Function: `_generate_footer`
> Generate JavaScript footer
*Line 162*  

#### Function: `_indent`
> Get current indentation
*Line 179*  

#### Function: `optimize_ast`
> Optimize AST (future: loop unrolling, dead code elimination).
*Line 183*  

#### Function: `main`
> CLI interface for JavaScript backend
*Line 200*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode-idea-generator-WEB.py

#### Module: `hypercode-idea-generator-WEB`
> HyperCode Community Idea Generator - Web Interface (HTML/CSS/JS)
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode-launch-kit.py

#### Module: `hypercode-launch-kit`
> HyperCode Launch Kit - Ultimate System Initialization
*Line 0*  

#### Class: `HyperCodeLaunchKit`
> Complete launch system initialization
*Line 23*  

#### Function: `__init__`
*Line 26*  

#### Function: `create_readme`
> Create the ultimate README.md
*Line 30*  

#### Function: `create_launch_checklist`
> Create launch day checklist
*Line 367*  

#### Function: `create_launch_script`
> Create automated launch script
*Line 620*  

#### Function: `create_first_30_days`
> Create 30-day success roadmap
*Line 718*  

#### Function: `print_summary`
> Print beautiful summary
*Line 974*  

#### Function: `main`
> Run launch kit initialization
*Line 1007*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode-lexer-COMPLETE.py

#### Module: `hypercode-lexer-COMPLETE`
> HyperCode Lexer - Complete Implementation
*Line 0*  

#### Class: `TokenType`
> HyperCode token types - minimal yet powerful
*Line 21*  

#### Class: `Token`
> Represents a single token with position tracking
*Line 45*  

#### Function: `__repr__`
> Neurodivergent-friendly representation
*Line 54*  

#### Class: `LexerError`
> Lexer-specific errors with context
*Line 59*  

#### Function: `__init__`
*Line 62*  

#### Class: `HyperCodeLexer`
> Tokenizes HyperCode programs with accessibility features.
*Line 69*  

#### Function: `__init__`
> Initialize lexer with source code.
*Line 95*  

#### Function: `tokenize`
> Convert HyperCode source to token stream.
*Line 110*  

#### Function: `_advance_position`
> Update position tracking after processing character
*Line 169*  

#### Function: `_skip_comment`
> Skip characters until end of line
*Line 179*  

#### Function: `get_tokens`
> Return current token list
*Line 184*  

#### Function: `filter_tokens`
> Get tokens excluding certain types.
*Line 188*  

#### Function: `print_tokens`
> Print tokens in readable format.
*Line 205*  

#### Function: `get_statistics`
> Get token statistics (useful for analysis).
*Line 236*  

#### Function: `main`
> CLI interface for the lexer
*Line 250*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode-parser-COMPLETE.py

#### Module: `hypercode-parser-COMPLETE`
> HyperCode Parser - Complete Implementation
*Line 0*  

#### Class: `NodeType`
> AST Node types
*Line 22*  

#### Class: `ASTNode`
> Abstract Syntax Tree Node.
*Line 38*  

#### Function: `__repr__`
> Pretty-print AST (neurodivergent-friendly)
*Line 51*  

#### Class: `ParserError`
> Parser-specific errors with context
*Line 68*  

#### Function: `__init__`
*Line 71*  

#### Class: `HyperCodeParser`
> Parses HyperCode token stream into AST.
*Line 80*  

#### Function: `__init__`
> Initialize parser with token stream.
*Line 94*  

#### Function: `parse`
> Parse tokens into AST.
*Line 105*  

#### Function: `_parse_statement`
> Parse a single statement
*Line 127*  

#### Function: `_parse_loop`
> Parse loop structure: [ statements ]
*Line 174*  

#### Function: `_advance`
> Move to next token
*Line 209*  

#### Function: `_is_at_end`
> Check if at end of token stream
*Line 215*  

#### Function: `validate`
> Validate AST structure.
*Line 222*  

#### Function: `print_ast`
> Print AST in readable format.
*Line 237*  

#### Function: `main`
> CLI interface for the parser
*Line 251*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\__init__.py

#### Module: `__init__`
> HyperCode - A neurodivergent-first programming language with AI compatibility.
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\__main__.py

#### Function: `main`
*Line 6*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\config.py

#### Module: `config`
> Configuration module for HyperCode.
*Line 0*  

#### Class: `Config`
> Configuration class for HyperCode
*Line 16*  

#### Function: `get_headers`
> Get headers for API requests
*Line 27*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\__init__.py

#### Module: `__init__`
> Core package for the HyperCode language implementation.
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\ast.py

#### Class: `Node`
*Line 9*  

#### Function: `accept`
*Line 10*  

#### Class: `Expr`
*Line 20*  

#### Class: `Literal`
*Line 25*  

#### Class: `Variable`
*Line 30*  

#### Class: `Assign`
*Line 35*  

#### Class: `Binary`
*Line 41*  

#### Class: `Unary`
*Line 48*  

#### Class: `Grouping`
*Line 54*  

#### Class: `Call`
*Line 59*  

#### Class: `Get`
*Line 66*  

#### Class: `Stmt`
*Line 73*  

#### Class: `Expression`
*Line 78*  

#### Class: `Print`
*Line 83*  

#### Class: `Var`
*Line 88*  

#### Class: `Block`
*Line 94*  

#### Class: `If`
*Line 99*  

#### Class: `Fun`
*Line 106*  

#### Class: `Return`
*Line 113*  

#### Class: `Intent`
*Line 119*  

#### Class: `Program`
*Line 126*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\cli.py

#### Module: `cli`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\error_handler.py

#### Function: `report_parse_error`
*Line 5*  

#### Function: `report`
*Line 12*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\interpreter.py

#### Class: `Return`
*Line 8*  

#### Function: `__init__`
*Line 9*  

#### Class: `HyperCodeFunction`
*Line 13*  

#### Function: `__init__`
*Line 14*  

#### Function: `__str__`
*Line 18*  

#### Function: `arity`
*Line 21*  

#### Function: `call`
*Line 24*  

#### Class: `Environment`
*Line 37*  

#### Function: `__init__`
*Line 38*  

#### Function: `define`
*Line 42*  

#### Function: `get`
*Line 45*  

#### Function: `assign`
*Line 52*  

#### Class: `Interpreter`
*Line 62*  

#### Function: `__init__`
*Line 63*  

#### Function: `interpret`
*Line 67*  

#### Function: `execute`
*Line 74*  

#### Function: `execute_block`
*Line 77*  

#### Function: `evaluate`
*Line 86*  

#### Function: `visit_Expression`
*Line 89*  

#### Function: `visit_Print`
*Line 92*  

#### Function: `visit_Var`
*Line 96*  

#### Function: `visit_Block`
*Line 102*  

#### Function: `visit_Assign`
*Line 105*  

#### Function: `visit_Binary`
*Line 110*  

#### Function: `visit_Grouping`
*Line 153*  

#### Function: `visit_Literal`
*Line 156*  

#### Function: `visit_Unary`
*Line 159*  

#### Function: `visit_Variable`
*Line 172*  

#### Function: `visit_If`
*Line 175*  

#### Function: `is_truthy`
*Line 181*  

#### Function: `visit_Fun`
*Line 188*  

#### Function: `visit_Return`
*Line 192*  

#### Function: `visit_Call`
*Line 198*  

#### Function: `is_callable`
*Line 216*  

#### Class: `Visitor`
*Line 221*  

#### Function: `visit_Expression`
*Line 222*  

#### Function: `visit_Print`
*Line 225*  

#### Function: `visit_Var`
*Line 228*  

#### Function: `visit_Block`
*Line 231*  

#### Function: `visit_If`
*Line 234*  

#### Function: `visit_Fun`
*Line 237*  

#### Function: `visit_Return`
*Line 240*  

#### Function: `visit_Assign`
*Line 243*  

#### Function: `visit_Binary`
*Line 246*  

#### Function: `visit_Grouping`
*Line 249*  

#### Function: `visit_Literal`
*Line 252*  

#### Function: `visit_Unary`
*Line 255*  

#### Function: `visit_Variable`
*Line 258*  

#### Function: `visit_Call`
*Line 261*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\lexer.py

#### Module: `lexer`
> Core HyperCode language implementation - Lexer
*Line 0*  

#### Class: `LexerError`
> Exception raised for errors in the lexer.
*Line 32*  

#### Function: `__init__`
*Line 35*  

#### Class: `Lexer`
> Lexical analyzer for the HyperCode language.
*Line 42*  

#### Function: `__init__`
> Initialize the lexer with source code.
*Line 109*  

#### Function: `tokenize`
> Convert source code into a list of tokens.
*Line 126*  

#### Function: `_match_patterns`
> Try to match the current position against all token patterns.
*Line 161*  

#### Function: `_update_position`
> Update line and column numbers based on the given text.
*Line 187*  

#### Function: `_add_token`
> Add a token to the token list.
*Line 206*  

#### Function: `_handle_unknown`
> Handle unknown characters in the source.
*Line 270*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\optimizer.py

#### Module: `optimizer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\parser.py

#### Class: `ParseError`
*Line 8*  

#### Class: `Parser`
*Line 12*  

#### Function: `__init__`
*Line 13*  

#### Function: `parse`
> Parse the entire program.
*Line 17*  

#### Function: `declaration`
*Line 26*  

#### Function: `var_declaration`
*Line 37*  

#### Function: `statement`
*Line 53*  

#### Function: `print_statement`
*Line 66*  

#### Function: `return_statement`
*Line 71*  

#### Function: `intent_statement`
*Line 79*  

#### Function: `expression_statement`
*Line 94*  

#### Function: `if_statement`
*Line 99*  

#### Function: `function`
*Line 111*  

#### Function: `block`
*Line 130*  

#### Function: `expression`
*Line 137*  

#### Function: `assignment`
*Line 140*  

#### Function: `equality`
*Line 155*  

#### Function: `comparison`
*Line 165*  

#### Function: `term`
*Line 178*  

#### Function: `factor`
*Line 186*  

#### Function: `unary`
*Line 194*  

#### Function: `primary`
*Line 201*  

#### Function: `_primary`
*Line 218*  

#### Function: `finish_call`
*Line 249*  

#### Function: `match`
*Line 262*  

#### Function: `consume`
*Line 269*  

#### Function: `error`
*Line 276*  

#### Function: `synchronize`
*Line 282*  

#### Function: `check`
*Line 302*  

#### Function: `advance`
*Line 307*  

#### Function: `is_at_end`
*Line 312*  

#### Function: `peek`
*Line 315*  

#### Function: `previous`
*Line 318*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\semantic_analyzer.py

#### Module: `semantic_analyzer`
> Core HyperCode language implementation
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\sensory_profile.py

#### Module: `sensory_profile`
> Sensory Profile System for HyperCode
*Line 0*  

#### Class: `VisualNoiseLevel`
*Line 15*  

#### Class: `AnimationSpeed`
*Line 22*  

#### Class: `VisualSettings`
> Configuration for visual aspects of the editor.
*Line 29*  

#### Class: `AudioSettings`
> Configuration for audio feedback.
*Line 43*  

#### Class: `AnimationSettings`
> Configuration for animations and transitions.
*Line 58*  

#### Class: `SensoryProfile`
> A complete sensory profile configuration.
*Line 68*  

#### Function: `to_dict`
> Convert the profile to a dictionary.
*Line 77*  

#### Function: `from_dict`
> Create a profile from a dictionary.
*Line 85*  

#### Function: `save`
> Save the profile to a file.
*Line 107*  

#### Function: `load`
> Load a profile from a file.
*Line 113*  

#### Class: `ProfileManager`
> Manages loading and saving of sensory profiles.
*Line 120*  

#### Function: `__init__`
> Initialize with optional custom profiles directory.
*Line 123*  

#### Function: `_ensure_default_profiles`
> Ensure default profiles exist.
*Line 133*  

#### Function: `_create_minimal_profile`
> Create a minimal distraction-free profile.
*Line 146*  

#### Function: `_create_enhanced_profile`
> Create an enhanced profile with helpful visual cues.
*Line 163*  

#### Function: `_create_high_contrast_profile`
> Create a high-contrast profile for better readability.
*Line 190*  

#### Function: `list_profiles`
> List all available profile names.
*Line 216*  

#### Function: `get_profile`
> Get a profile by name.
*Line 220*  

#### Function: `save_profile`
> Save a profile.
*Line 227*  

#### Function: `delete_profile`
> Delete a profile by name.
*Line 232*  

#### Function: `get_profile`
> Helper function to get a profile by name.
*Line 243*  

#### Function: `list_profiles`
> Helper function to list all available profiles.
*Line 248*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\core\tokens.py

#### Class: `TokenType`
*Line 6*  

#### Class: `Token`
*Line 61*  

#### Function: `__str__`
*Line 68*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\enhanced_perplexity_client.py

#### Module: `enhanced_perplexity_client`
> Enhanced Perplexity Client with Knowledge Base Integration
*Line 0*  

#### Class: `EnhancedPerplexityClient`
> Enhanced Perplexity client with knowledge base integration
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `query_with_context`
> Send a query with relevant knowledge base context
*Line 25*  

#### Function: `add_research_data`
> Add research data to the knowledge base
*Line 61*  

#### Function: `search_research_data`
> Search the knowledge base
*Line 71*  

#### Function: `list_research_documents`
> List all research documents
*Line 75*  

#### Function: `get_document`
> Get a specific document
*Line 79*  

#### Function: `delete_document`
> Delete a document
*Line 83*  

#### Function: `import_from_perplexity_space`
> Import data from Perplexity Space export
*Line 87*  

#### Function: `test_context_integration`
> Test the context integration
*Line 123*  

#### Function: `create_perplexity_space_import_template`
> Create a template for importing Perplexity Space data
*Line 175*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\knowledge_base.py

#### Module: `knowledge_base`
> HyperCode Knowledge Base - Perplexity Space Integration
*Line 0*  

#### Class: `ResearchDocument`
> Represents a research document from Perplexity Space
*Line 17*  

#### Function: `__post_init__`
*Line 28*  

#### Function: `generate_id`
> Generate unique ID from content hash
*Line 36*  

#### Function: `validate`
> Validate document data
*Line 41*  

#### Function: `update_timestamp`
> Update the last_updated timestamp
*Line 53*  

#### Class: `HyperCodeKnowledgeBase`
> Knowledge base for HyperCode research data
*Line 100*  

#### Function: `__init__`
*Line 103*  

#### Function: `load`
> Load knowledge base from file
*Line 109*  

#### Function: `save`
> Save knowledge base to file
*Line 125*  

#### Function: `add_document`
> Add a new research document
*Line 135*  

#### Function: `search_documents`
> Search documents by query
*Line 163*  

#### Function: `get_context_for_query`
> Get relevant context for a query
*Line 227*  

#### Function: `list_documents`
> List all documents
*Line 257*  

#### Function: `get_document`
> Get a specific document by ID
*Line 261*  

#### Function: `delete_document`
> Delete a document
*Line 265*  

#### Function: `update_document`
> Update an existing document
*Line 273*  

#### Function: `search_by_tags`
> Search documents by tags with AND/OR operators
*Line 287*  

#### Function: `get_document_statistics`
> Get statistics about the knowledge base
*Line 306*  

#### Function: `export_format`
> Export knowledge base in different formats
*Line 331*  

#### Function: `validate_all_documents`
> Validate all documents and return list of errors
*Line 353*  

#### Function: `cleanup_duplicates`
> Remove duplicate documents based on content hash
*Line 363*  

#### Function: `initialize_sample_data`
> Initialize with sample HyperCode research data
*Line 384*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\perplexity_client.py

#### Module: `perplexity_client`
> Perplexity AI API client for HyperCode.
*Line 0*  

#### Class: `PerplexityClient`
> Client for interacting with Perplexity AI API
*Line 12*  

#### Function: `__init__`
> Initialize the Perplexity client.
*Line 15*  

#### Function: `query`
> Send a query to the Perplexity API.
*Line 30*  

#### Function: `test_connection`
> Test the connection to the Perplexity API
*Line 72*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode\repl.py

#### Function: `run_repl`
*Line 12*  

#### Function: `run`
*Line 33*  

#### Function: `show_help`
*Line 54*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode_idea_generator.py

#### Module: `hypercode_idea_generator`
> HyperCode Idea Generator - AI-Powered Community Input System
*Line 0*  

#### Class: `HyperCodeIdeaGenerator`
> AI-Powered Idea Generator for HyperCode community input.
*Line 431*  

#### Function: `__init__`
*Line 439*  

#### Function: `get_ideas_by_category`
> Get ideas by category and optionally by difficulty level.
*Line 443*  

#### Function: `get_top_ideas`
> Get most-voted ideas across all categories.
*Line 468*  

#### Function: `vote_for_idea`
> Vote for an idea.
*Line 487*  

#### Function: `get_trending_ideas`
> Get trending ideas (high votes + recent activity).
*Line 497*  

#### Function: `format_idea_card`
> Format idea for display.
*Line 502*  

#### Function: `main`
> Interactive idea generator CLI
*Line 528*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\hypercode_poc.py

#### Module: `hypercode_poc`
> HyperCode POC - Neurodivergent-First Programming Language
*Line 0*  

#### Class: `TokenType`
> Brainfuck-inspired core + modern aliases
*Line 18*  

#### Class: `Token`
*Line 34*  

#### Class: `UserConfidenceLevel`
*Line 41*  

#### Class: `EnhancedLexer`
> Smart tokenizer with escape handling + accessibility focus
*Line 48*  

#### Function: `__init__`
*Line 51*  

#### Function: `tokenize`
*Line 74*  

#### Function: `handle_string`
*Line 115*  

#### Function: `handle_number`
*Line 141*  

#### Function: `handle_identifier`
*Line 149*  

#### Function: `advance`
*Line 171*  

#### Class: `ContextAwareErrorMessenger`
> Friendly, adaptive error messages
*Line 176*  

#### Function: `__init__`
*Line 179*  

#### Function: `format_error`
*Line 182*  

#### Class: `SemanticContextStreamer`
> Understand programmer intent from tokens
*Line 189*  

#### Function: `analyze`
*Line 192*  

#### Class: `ConfidenceTracker`
> Adapt system guidance to user skill level
*Line 209*  

#### Function: `__init__`
*Line 212*  

#### Function: `record`
*Line 216*  

#### Class: `HyperCodePOC`
> Main system: Lexer + Error Messenger + Semantic Analyzer + Confidence Tracker
*Line 222*  

#### Function: `__init__`
*Line 225*  

#### Function: `compile`
*Line 232*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\mistral_adapter.py

#### Module: `mistral_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `MistralAdapterAdapter`
> Adapter for Mistral Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\ollama_adapter.py

#### Module: `ollama_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OllamaAdapterAdapter`
> Adapter for Ollama Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\openai_adapter.py

#### Module: `openai_adapter`
> AI model compatibility layer
*Line 0*  

#### Class: `OpenaiAdapterAdapter`
> Adapter for Openai Adapter AI model.
*Line 22*  

#### Function: `__init__`
*Line 25*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\parser\debug_ascii.py

#### Module: `debug_ascii`
> ASCII-only debug
*Line 0*  

#### Function: `test_regex_patterns`
> Test regex patterns directly
*Line 14*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\parser\debug_full.py

#### Module: `debug_full`
> Debug the full parsing flow
*Line 0*  

#### Function: `debug_full_parsing`
> Debug the full parsing flow
*Line 14*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\parser\debug_parser.py

#### Module: `debug_parser`
> Debug the Visual Syntax Parser - Find what's wrong with annotation detection
*Line 0*  

#### Function: `debug_annotation_detection`
> Debug why annotations aren't being detected
*Line 14*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\parser\debug_simple.py

#### Module: `debug_simple`
> Simple debug without emoji characters
*Line 0*  

#### Function: `debug_simple`
> Debug without emoji characters
*Line 14*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\parser\test_parser.py

#### Module: `test_parser`
> Test the Visual Syntax Parser - First Click Moment Demo
*Line 0*  

#### Function: `test_first_click_moment`
> Test the parser with the first click moment example
*Line 14*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\parser\visual_syntax_parser.py

#### Module: `visual_syntax_parser`
> 🎨 Visual Syntax Parser for HyperCode V3
*Line 0*  

#### Class: `SemanticMarker`
> 🎨 Semantic marker types with emoji representations
*Line 18*  

#### Class: `SemanticAnnotation`
> 📋 A single semantic annotation with its metadata
*Line 37*  

#### Function: `__str__`
*Line 46*  

#### Class: `ParsedFunction`
> 🔍 A fully parsed HyperCode function
*Line 51*  

#### Function: `get_annotations_by_type`
> Get all annotations of a specific type
*Line 62*  

#### Class: `VisualSyntaxParser`
> 🎨 Main parser for HyperCode's visual semantic syntax
*Line 69*  

#### Function: `__init__`
*Line 72*  

#### Function: `_build_semantic_patterns`
> 🔍 Build regex patterns for all semantic markers
*Line 76*  

#### Function: `_build_color_scheme`
> 🎨 Build semantic color mapping for IDE highlighting
*Line 105*  

#### Function: `parse_file`
> 📄 Parse an entire HyperCode file
*Line 123*  

#### Function: `parse_content`
> 📝 Parse HyperCode content string
*Line 130*  

#### Function: `_is_function_definition`
> 🔍 Check if line is a function definition
*Line 170*  

#### Function: `_start_new_function`
> 🆕 Create new ParsedFunction from definition line
*Line 179*  

#### Function: `_parse_line_annotations`
> � Parse semantic annotations from a line
*Line 202*  

#### Function: `_parse_annotation_params`
> 🔧 Parse annotation parameters from string
*Line 223*  

#### Function: `generate_syntax_highlighting`
> 🎨 Generate HTML with syntax highlighting for visual markers
*Line 265*  

#### Function: `extract_semantic_summary`
> 📊 Extract semantic summary for analysis
*Line 277*  

#### Function: `validate_neurodiversity_compliance`
> 🧠 Validate neurodiversity-first design principles
*Line 311*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\prompt_normalizer.py

#### Module: `prompt_normalizer`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\rag_engine.py

#### Module: `rag_engine`
> AI model compatibility layer
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\scaffold (1).py

#### Module: `scaffold (1)`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 141*  

#### Function: `create_python_files`
> Create all Python files with proper __init__.py structure.
*Line 151*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 165*  

#### Function: `create_root_files`
> Create root-level configuration files as empty placeholders.
*Line 202*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 213*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 234*  

#### Function: `main`
> Main scaffolding function.
*Line 259*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\scaffold.py

#### Module: `scaffold`
> HyperCode Project Scaffolder
*Line 0*  

#### Function: `create_directories`
> Create all required directories.
*Line 153*  

#### Function: `create_python_files`
> Create all Python files with proper docstrings and structure.
*Line 184*  

#### Function: `create_example_files`
> Create example HyperCode files.
*Line 254*  

#### Function: `create_root_files`
> Create root-level configuration files with appropriate content.
*Line 291*  

#### Function: `create_healthcheck`
> Create the healthcheck script for Docker.
*Line 541*  

#### Function: `print_summary`
> Print summary of created structure.
*Line 583*  

#### Function: `main`
> Main scaffolding function.
*Line 621*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\test_framework.py

#### Module: `test_framework`
> Automated Testing Suite for DuelCode Framework
*Line 0*  

#### Class: `TestResult`
*Line 17*  

#### Class: `TestCase`
*Line 24*  

#### Class: `TestRun`
*Line 34*  

#### Class: `DuelCodeTestSuite`
*Line 44*  

#### Function: `__init__`
*Line 45*  

#### Function: `discover_tutorials`
> Find all tutorial markdown files.
*Line 49*  

#### Function: `run_validator`
> Run the ultra validator on a file.
*Line 56*  

#### Function: `parse_validator_output`
> Parse validator output to count issues by severity.
*Line 71*  

#### Function: `test_tutorial`
> Test a single tutorial file.
*Line 99*  

#### Function: `test_validator_integrity`
> Test that validator itself is working correctly.
*Line 135*  

#### Function: `test_template_validity`
> Test that templates pass validation.
*Line 176*  

#### Function: `run_all_tests`
> Run the complete test suite.
*Line 221*  

#### Function: `generate_report`
> Generate a detailed test report.
*Line 248*  

#### Function: `main`
> Main entry point.
*Line 295*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\test_validator.py

#### Module: `test_validator`
> Test script for the DuelCode validator.
*Line 0*  

#### Function: `test_valid_file`
> Test with a valid DuelCode file.
*Line 11*  

#### Function: `test_invalid_file`
> Test with an invalid DuelCode file.
*Line 65*  

#### Function: `main`
> Run the test suite.
*Line 90*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\ultra_validator.py

#### Module: `ultra_validator`
> Ultra-Enhanced DuelCode Validator with advanced validation rules.
*Line 0*  

#### Class: `Severity`
*Line 12*  

#### Class: `ValidationResult`
*Line 20*  

#### Class: `DuelCodeUltraValidator`
> Ultra-enhanced validator with comprehensive rules for DuelCode documentation.
*Line 28*  

#### Function: `__init__`
*Line 88*  

#### Function: `_add_result`
*Line 95*  

#### Function: `_find_lines`
*Line 106*  

#### Function: `validate_code_blocks_have_language`
> Validate all code blocks have language specifications.
*Line 118*  

#### Function: `validate_has_visual_representation`
> Check for visual elements like diagrams, charts, or ASCII art.
*Line 152*  

#### Function: `validate_has_practical_exercise`
> Check for practical exercises or challenges.
*Line 171*  

#### Function: `validate_has_learning_objectives`
> Check for learning objectives section.
*Line 192*  

#### Function: `validate_has_checklist`
> Check for checklist elements.
*Line 215*  

#### Function: `validate_has_conclusion`
> Check for conclusion section.
*Line 234*  

#### Function: `validate_has_whats_next`
> Check for 'What's Next' section.
*Line 257*  

#### Function: `validate_code_quality`
> Validate code block quality and best practices.
*Line 278*  

#### Function: `_validate_code_block_content`
> Validate specific code block content based on language.
*Line 305*  

#### Function: `validate_has_glossary`
> Check for glossary section.
*Line 340*  

#### Function: `validate_has_see_also`
> Check for 'See Also' section.
*Line 360*  

#### Function: `validate_has_faq`
> Check for FAQ section.
*Line 380*  

#### Function: `validate_has_acknowledgments`
> Check for acknowledgments section.
*Line 402*  

#### Function: `validate_accessibility`
> Check for accessibility features.
*Line 422*  

#### Function: `validate_interactive_elements`
> Check for interactive elements.
*Line 443*  

#### Function: `validate_all`
> Run all validations and return results.
*Line 463*  

#### Function: `print_results`
> Print validation results in a formatted way.
*Line 487*  

#### Function: `main`
*Line 537*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\code_analyzer_ai.py

#### Module: `code_analyzer_ai`
> Perplexity AI Code Analyzer for HyperCode
*Line 0*  

#### Class: `CodeAnalyzerAI`
> AI-powered code analyzer for HyperCode
*Line 19*  

#### Function: `__init__`
*Line 22*  

#### Function: `analyze_file`
> Analyze a Python file with AI assistance
*Line 25*  

#### Function: `_analyze_complexity`
> Analyze code complexity indicators
*Line 72*  

#### Function: `_check_docstrings`
> Check for docstring coverage
*Line 113*  

#### Function: `_get_ai_code_analysis`
> Get AI analysis of code from Perplexity
*Line 155*  

#### Function: `analyze_project`
> Analyze entire project
*Line 183*  

#### Function: `_get_project_ai_insights`
> Get AI insights for the entire project
*Line 230*  

#### Function: `save_analysis`
> Save analysis to file
*Line 262*  

#### Function: `print_summary`
> Print analysis summary
*Line 270*  

#### Function: `main`
> Main function
*Line 288*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\debug_search.py

#### Module: `debug_search`
> Debug search results
*Line 0*  

#### Function: `debug_search`
> Debug why space data isn't being found
*Line 15*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\demo_ai_research.py

#### Module: `demo_ai_research`
> HyperCode AI Research + Perplexity Integration Demo
*Line 0*  

#### Function: `demo_ai_research_queries`
> Demonstrate AI Research integration with Perplexity
*Line 16*  

#### Function: `test_document_specific_queries`
> Test queries specific to the HyperCode AI Research document
*Line 90*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\demo_enhanced_client.py

#### Module: `demo_enhanced_client`
> Demo: Enhanced Perplexity Client with Knowledge Base
*Line 0*  

#### Function: `demo_knowledge_base_integration`
> Demonstrate the knowledge base integration
*Line 16*  

#### Function: `demonstrate_memory_persistence`
> Demonstrate that the knowledge base persists between sessions
*Line 131*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\final_integration_test.py

#### Module: `final_integration_test`
> Final Test: Complete Perplexity Space Integration
*Line 0*  

#### Function: `final_integration_test`
> Complete test of the Perplexity Space integration
*Line 15*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\health_scanner_ai.py

#### Module: `health_scanner_ai`
> HyperCode Health Scanner with Perplexity AI Integration
*Line 0*  

#### Class: `HealthScannerAI`
> AI-powered health scanner for HyperCode project
*Line 18*  

#### Function: `__init__`
*Line 21*  

#### Function: `analyze_project_structure`
> Analyze project structure and identify health issues
*Line 25*  

#### Function: `analyze_dependencies`
> Analyze dependency management
*Line 68*  

#### Function: `analyze_security`
> Analyze security configuration
*Line 110*  

#### Function: `get_ai_recommendations`
> Get AI-powered recommendations based on health scan
*Line 143*  

#### Function: `run_full_scan`
> Run complete health scan with AI analysis
*Line 170*  

#### Function: `save_report`
> Save health scan report to file
*Line 221*  

#### Function: `print_summary`
> Print a summary of the health scan
*Line 227*  

#### Function: `main`
> Main function to run the health scanner
*Line 247*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\import-helper.py

#### Module: `import-helper`
> HyperCode Perplexity Space Import Helper
*Line 0*  

#### Class: `SpaceImportHelper`
> Helper class for managing Perplexity Space imports
*Line 13*  

#### Function: `__init__`
*Line 16*  

#### Function: `validate_document`
> Validate a document structure
*Line 21*  

#### Function: `load_template`
> Load documents from JSON template file
*Line 63*  

#### Function: `validate_all`
> Validate all loaded documents
*Line 83*  

#### Function: `generate_report`
> Generate a validation report
*Line 95*  

#### Function: `create_import_script`
> Generate a Python script to import the data
*Line 141*  

#### Function: `create_template_instructions`
> Generate detailed instructions for filling the template
*Line 193*  

#### Function: `main`
> CLI interface for the import helper
*Line 264*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\import_all_space_data.py

#### Module: `import_all_space_data`
> Complete Import of HyperCode Space Data
*Line 0*  

#### Function: `format_content`
> Recursively format nested data into readable text
*Line 16*  

#### Function: `import_all_hypercode_data`
> Import all sections of your HyperCode Space data
*Line 41*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\import_hypercode_data.py

#### Module: `import_hypercode_data`
> Import HyperCode Space Data
*Line 0*  

#### Function: `import_hypercode_space_data`
> Import your actual HyperCode Space data
*Line 16*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\import_perplexity_space.py

#### Module: `import_perplexity_space`
> Perplexity Space Data Importer
*Line 0*  

#### Function: `create_manual_import_script`
> Create a script for manual data entry from Perplexity Space
*Line 17*  

#### Function: `create_json_import_template`
> Create a JSON template for importing data
*Line 86*  

#### Function: `import_from_json`
> Import data from JSON file
*Line 115*  

#### Function: `test_imported_data`
> Test the imported data with context-aware queries
*Line 153*  

#### Function: `show_import_menu`
> Show the import menu
*Line 188*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\local_health_scanner.py

#### Module: `local_health_scanner`
> Local Project Health Scanner for HyperCode
*Line 0*  

#### Class: `ProjectScanner`
> Scans the project for health metrics without external dependencies
*Line 20*  

#### Function: `__init__`
*Line 23*  

#### Function: `scan_project`
> Scan the entire project and return health metrics
*Line 35*  

#### Function: `_scan_directory`
> Recursively scan a directory for Python files
*Line 43*  

#### Function: `_analyze_file`
> Analyze a single Python file
*Line 52*  

#### Function: `_analyze_ast`
> Analyze Python AST for code quality metrics
*Line 77*  

#### Function: `_check_documentation`
> Check documentation coverage
*Line 97*  

#### Function: `_check_tests`
> Check test coverage
*Line 109*  

#### Function: `_calculate_metrics`
> Calculate final metrics
*Line 120*  

#### Function: `print_health_report`
> Print a formatted health report
*Line 132*  

#### Function: `main`
> Main function to run the health scanner
*Line 163*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\perplexity_space_collector.py

#### Module: `perplexity_space_collector`
> Perplexity Space Data Collector
*Line 0*  

#### Function: `quick_copy_paste_collector`
> Quick collector for copy-paste workflow
*Line 18*  

#### Function: `create_structured_template`
> Create a structured JSON template for bulk import
*Line 117*  

#### Function: `show_bro_hacks`
> Show BROski's pro tips
*Line 167*  

#### Function: `main_menu`
> Main menu for the collector
*Line 207*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\perplexity_space_integration.py

#### Module: `perplexity_space_integration`
> Perplexity Space Integration Guide
*Line 0*  

#### Function: `main`
*Line 16*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\utils\run_lexer.py

#### Function: `run_lexer`
> Run the lexer on a source file and print the tokens.
*Line 13*  

### 📄 hypercode_backup_20251205_183301\hypercode\src\validate_duelcode.py

#### Module: `validate_duelcode`
> DuelCode Documentation Validator
*Line 0*  

#### Class: `DuelCodeValidator`
*Line 23*  

#### Function: `__init__`
*Line 24*  

#### Function: `validate_sections`
> Check if all required sections are present.
*Line 30*  

#### Function: `check_formatting`
> Check for common formatting issues.
*Line 39*  

#### Function: `check_visual_aids`
> Check for presence of visual aids.
*Line 55*  

#### Function: `validate`
> Run all validations and return results.
*Line 60*  

#### Function: `main`
*Line 68*  

### 📄 hypercode_backup_20251205_183301\hypercode\test_mcp_connection.py

#### Function: `check_port`
> Check if a port is open on the given host.
*Line 26*  

#### Function: `find_running_servers`
> Scan common ports to find running servers.
*Line 36*  

#### Function: `test_server_connection`
> Test connection to a single MCP server.
*Line 49*  

#### Function: `test_all_servers`
> Test connection to all MCP servers and print results.
*Line 90*  

#### Function: `check_dependencies`
> Check if required dependencies are installed.
*Line 139*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\benchmark_knowledge_base.py

#### Module: `benchmark_knowledge_base`
> Performance Benchmark Tool for HyperCode Knowledge Base
*Line 0*  

#### Class: `BenchmarkSuite`
> Comprehensive benchmark suite for Knowledge Base
*Line 24*  

#### Function: `__init__`
*Line 27*  

#### Function: `_get_system_info`
> Get system information for benchmark context
*Line 34*  

#### Function: `generate_test_data`
> Generate test data of specified size
*Line 43*  

#### Function: `benchmark_operation`
> Benchmark a single operation
*Line 93*  

#### Function: `run_benchmark_suite`
> Run complete benchmark suite
*Line 118*  

#### Function: `_calculate_summary`
> Calculate summary statistics
*Line 274*  

#### Function: `_generate_recommendations`
> Generate performance recommendations
*Line 296*  

#### Function: `generate_markdown_report`
> Generate beautiful markdown report
*Line 338*  

#### Function: `save_json_results`
> Save results as JSON
*Line 467*  

#### Function: `main`
> Main benchmark runner
*Line 474*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_accessibility.py

#### Module: `test_accessibility`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_ai_gateway.py

#### Module: `test_ai_gateway`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_backends.py

#### Module: `test_backends`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_core.py

#### Module: `test_core`
> Test harness for core HyperCode components.
*Line 0*  

#### Function: `run_test`
> Test the lexer, parser, and interpreter with the given source code.
*Line 30*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_integration.py

#### Module: `test_integration`
> Comprehensive test suite
*Line 0*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_intent_blocks.py

#### Module: `test_intent_blocks`
> Test script for Intent Blocks implementation
*Line 0*  

#### Function: `test_intent_block`
> Test parsing of intent blocks
*Line 13*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_interpreter.py

#### Function: `run_code`
> A helper function to run code and capture stdout.
*Line 10*  

#### Class: `TestInterpreter`
*Line 28*  

#### Function: `test_if_statement_then`
*Line 30*  

#### Function: `test_if_statement_else`
*Line 42*  

#### Function: `test_function_call`
*Line 54*  

#### Function: `test_function_with_parameters`
*Line 64*  

#### Function: `test_function_with_return`
*Line 74*  

#### Function: `test_recursive_function_call`
*Line 85*  

#### Function: `test_scoping`
*Line 99*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Comprehensive test suite for knowledge base search functionality.
*Line 0*  

#### Class: `TestKnowledgeBaseSearch`
> Test suite for knowledge base search functionality.
*Line 12*  

#### Function: `sample_documents`
> Create sample documents for testing.
*Line 16*  

#### Function: `knowledge_base`
> Create a knowledge base instance with sample documents.
*Line 40*  

#### Function: `test_basic_search`
> Test basic search functionality.
*Line 48*  

#### Function: `test_search_with_exact_match`
> Test search with exact phrase matching.
*Line 54*  

#### Function: `test_search_case_insensitive`
> Test that search is case-insensitive.
*Line 59*  

#### Function: `test_search_empty_query`
> Test search with empty query returns all or no documents.
*Line 65*  

#### Function: `test_search_no_matches`
> Test search with no matching documents.
*Line 71*  

#### Function: `test_search_ranking`
> Test that search results are ranked by relevance.
*Line 77*  

#### Function: `test_query_normalization`
> Test query normalization (typos, spacing, punctuation).
*Line 90*  

#### Function: `test_multi_word_query`
> Test search with multiple keywords.
*Line 98*  

#### Function: `test_tag_based_search`
> Test search that includes tag matching.
*Line 103*  

#### Class: `TestEdgeCases`
> Test edge cases and boundary conditions.
*Line 112*  

#### Function: `knowledge_base`
*Line 116*  

#### Function: `test_very_short_query`
> Test search with very short query (1-2 chars).
*Line 121*  

#### Function: `test_very_long_query`
> Test search with very long query (paragraph length).
*Line 126*  

#### Function: `test_special_characters_in_query`
> Test search with special characters.
*Line 136*  

#### Function: `test_unicode_in_query`
> Test search with unicode characters.
*Line 141*  

#### Function: `test_sql_injection_attempt`
> Test that search is safe from SQL injection-style attacks.
*Line 146*  

#### Function: `test_repeated_queries`
> Test that repeated queries return consistent results.
*Line 151*  

#### Class: `TestPerformance`
> Performance benchmarking tests.
*Line 159*  

#### Function: `large_knowledge_base`
> Create a knowledge base with many documents.
*Line 163*  

#### Function: `test_search_response_time`
> Test that search completes within acceptable time.
*Line 179*  

#### Function: `test_concurrent_searches`
> Test multiple concurrent search operations.
*Line 189*  

#### Function: `test_memory_usage`
> Test memory usage during search operations.
*Line 207*  

#### Class: `TestIntegrationWithPerplexity`
> Test integration with EnhancedPerplexityClient.
*Line 213*  

#### Function: `mock_perplexity_client`
> Create a mock Perplexity client.
*Line 217*  

#### Function: `mock_knowledge_base`
> Create a mock knowledge base.
*Line 229*  

#### Function: `test_enhanced_query_with_context`
> Test that queries are enhanced with knowledge base context.
*Line 243*  

#### Function: `test_fallback_to_perplexity_api`
> Test fallback to Perplexity API when no local context found.
*Line 259*  

#### Function: `test_context_ranking_and_selection`
> Test that best context is selected for query enhancement.
*Line 273*  

#### Class: `TestDocumentManagement`
> Test document addition, update, and removal.
*Line 288*  

#### Function: `knowledge_base`
*Line 292*  

#### Function: `test_add_document`
> Test adding a new document to knowledge base.
*Line 300*  

#### Function: `test_update_document`
> Test updating an existing document.
*Line 310*  

#### Function: `test_remove_document`
> Test removing a document.
*Line 315*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_knowledge_base_comprehensive.py

#### Module: `test_knowledge_base_comprehensive`
> Comprehensive Test Suite for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestKnowledgeBaseUnit`
> Unit tests for Knowledge Base functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_docs`
> Sample documents for testing
*Line 36*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 59*  

#### Function: `test_add_single_document`
> Test adding a single document
*Line 65*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 74*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 84*  

#### Function: `test_search_exact_match`
> Test exact search matching
*Line 102*  

#### Function: `test_search_partial_match`
> Test partial search matching
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 124*  

#### Function: `test_search_case_insensitive`
> Test case insensitive search
*Line 135*  

#### Function: `test_empty_search`
> Test empty search query
*Line 147*  

#### Function: `test_nonexistent_search`
> Test search for nonexistent terms
*Line 155*  

#### Function: `test_get_context_for_query`
> Test context extraction
*Line 165*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 176*  

#### Function: `test_document_update`
> Test updating existing documents
*Line 186*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 202*  

#### Function: `test_delete_document`
> Test document deletion
*Line 213*  

#### Class: `TestKnowledgeBaseIntegration`
> Integration tests for Knowledge Base
*Line 229*  

#### Function: `populated_kb`
> Create a populated knowledge base for integration testing
*Line 233*  

#### Function: `test_complex_search_queries`
> Test complex search scenarios
*Line 277*  

#### Function: `test_search_ranking_quality`
> Test that search results are properly ranked
*Line 291*  

#### Function: `test_related_term_expansion`
> Test that related terms are properly expanded
*Line 301*  

#### Function: `test_performance_with_large_dataset`
> Test performance with larger dataset
*Line 313*  

#### Function: `test_concurrent_access_simulation`
> Test simulated concurrent access
*Line 332*  

#### Class: `TestKnowledgeBasePerformance`
> Performance tests for Knowledge Base
*Line 356*  

#### Function: `large_kb`
> Create a large knowledge base for performance testing
*Line 360*  

#### Function: `test_search_performance_large_dataset`
> Test search performance with large dataset
*Line 382*  

#### Function: `test_save_performance_large_dataset`
> Test save performance with large dataset
*Line 396*  

#### Function: `test_load_performance_large_dataset`
> Test load performance with large dataset
*Line 409*  

#### Function: `test_memory_usage_large_dataset`
> Test memory usage with large dataset
*Line 423*  

#### Class: `TestKnowledgeBaseEdgeCases`
> Edge case tests for Knowledge Base
*Line 446*  

#### Function: `edge_case_kb`
> Create knowledge base for edge case testing
*Line 450*  

#### Function: `test_empty_title_handling`
> Test handling of documents with empty titles
*Line 494*  

#### Function: `test_special_characters_handling`
> Test handling of special characters and unicode
*Line 499*  

#### Function: `test_very_long_titles`
> Test handling of very long titles
*Line 507*  

#### Function: `test_empty_content_handling`
> Test handling of documents with empty content
*Line 512*  

#### Function: `test_none_tags_handling`
> Test handling of None tags
*Line 517*  

#### Function: `test_malformed_json_handling`
> Test handling of malformed JSON files
*Line 531*  

#### Function: `test_file_permission_handling`
> Test handling of file permission issues
*Line 544*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_lexer.py

#### Function: `test_lexer_basic_tokens`
*Line 5*  

#### Function: `test_lexer_strings`
*Line 23*  

#### Function: `test_lexer_operators`
*Line 48*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_lexer_extended.py

#### Function: `test_lexer_escaped_strings`
> Test handling of strings with escaped characters.
*Line 5*  

#### Function: `test_lexer_numbers`
> Test various number formats.
*Line 18*  

#### Function: `test_lexer_operators`
> Test all operators.
*Line 39*  

#### Function: `test_lexer_comments`
> Test handling of single-line and multi-line comments.
*Line 86*  

#### Function: `test_lexer_whitespace`
> Test handling of various whitespace characters.
*Line 115*  

#### Function: `test_lexer_error_handling`
> Test error handling for invalid tokens.
*Line 130*  

#### Function: `test_lexer_hex_numbers`
> Test hexadecimal number literals.
*Line 139*  

#### Function: `test_lexer_binary_numbers`
> Test binary number literals.
*Line 157*  

#### Function: `test_lexer_scientific_notation`
> Test scientific notation numbers.
*Line 169*  

#### Function: `test_lexer_string_escapes`
> Test string escape sequences.
*Line 180*  

#### Function: `test_lexer_keywords`
> Test all language keywords.
*Line 197*  

#### Function: `test_lexer_position_tracking`
> Test that line and column numbers are tracked correctly.
*Line 223*  

#### Function: `test_lexer_error_recovery`
> Test that the lexer raises errors on invalid characters.
*Line 243*  

#### Function: `test_lexer_error_messages`
> Test that lexer error messages are informative.
*Line 252*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_parser.py

#### Function: `test_parse_literal`
*Line 12*  

#### Function: `test_parse_variable_declaration`
*Line 24*  

#### Function: `test_parse_binary_expression`
*Line 37*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 185*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\test_sensory_profiles.py

#### Module: `test_sensory_profiles`
> Tests for the sensory profile system.
*Line 0*  

#### Function: `test_visual_settings_creation`
> Test creating visual settings.
*Line 21*  

#### Function: `test_audio_settings_creation`
> Test creating audio settings.
*Line 35*  

#### Function: `test_animation_settings_creation`
> Test creating animation settings.
*Line 44*  

#### Function: `test_sensory_profile_creation`
> Test creating a complete sensory profile.
*Line 55*  

#### Function: `test_profile_serialization`
> Test serializing AND deserializing a profile.
*Line 71*  

#### Function: `test_profile_file_io`
> Test saving and loading a profile to/from a file.
*Line 92*  

#### Function: `test_profile_manager_initialization`
> Test initializing the profile manager and checking default profiles.
*Line 115*  

#### Function: `test_profile_manager_get_profile`
> Test getting a profile by name.
*Line 129*  

#### Function: `test_profile_manager_save_custom_profile`
> Test saving a custom profile.
*Line 142*  

#### Function: `test_profile_manager_delete_profile`
> Test deleting a profile.
*Line 169*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\tests\test_lexer_enhanced.py

#### Function: `test_lexer_edge_cases`
*Line 7*  

#### Function: `test_lexer_error_handling`
*Line 28*  

#### Function: `test_lexer_number_literals`
*Line 43*  

#### Function: `test_lexer_string_interpolation`
*Line 65*  

#### Function: `test_lexer_docstrings`
*Line 79*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_direct_access.py

#### Module: `test_direct_access`
> Direct Test of Implementation Guide Content
*Line 0*  

#### Function: `test_direct_implementation_access`
> Test direct access to implementation guide content
*Line 15*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_implementation_guide.py

#### Module: `test_implementation_guide`
> Test Implementation Guide Integration
*Line 0*  

#### Function: `test_search_functionality`
> Test search for implementation guide terms
*Line 15*  

#### Function: `test_implementation_guide_content`
> Test the implementation guide document directly
*Line 37*  

#### Function: `test_context_queries`
> Test context-aware queries
*Line 82*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_intent_blocks.py

#### Module: `test_intent_blocks`
> Test script for Intent Blocks implementation
*Line 0*  

#### Function: `test_intent_block`
> Test parsing of intent blocks
*Line 13*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_knowledge_base.py

#### Module: `test_knowledge_base`
> Phase 1 Unit Tests for HyperCode Knowledge Base
*Line 0*  

#### Class: `TestHyperCodeKnowledgeBase`
> Test suite for HyperCodeKnowledgeBase core functionality
*Line 20*  

#### Function: `temp_kb`
> Create a temporary knowledge base for testing
*Line 24*  

#### Function: `sample_documents`
> Sample documents for testing
*Line 33*  

#### Function: `test_init_empty_kb`
> Test knowledge base initialization
*Line 56*  

#### Function: `test_add_document`
> Test adding a single document
*Line 61*  

#### Function: `test_add_multiple_documents`
> Test adding multiple documents
*Line 82*  

#### Function: `test_save_and_load`
> Test saving and loading knowledge base
*Line 92*  

#### Function: `test_search_exact_match`
> Test exact term matching in search
*Line 113*  

#### Function: `test_search_tag_matching`
> Test tag-based search
*Line 126*  

#### Function: `test_search_related_terms`
> Test related term expansion
*Line 139*  

#### Function: `test_search_space_data_boost`
> Test that space data gets boosted in search
*Line 153*  

#### Function: `test_get_context_for_query`
> Test context extraction for queries
*Line 180*  

#### Function: `test_context_length_limit`
> Test context length limiting
*Line 192*  

#### Function: `test_list_documents`
> Test listing all documents
*Line 203*  

#### Function: `test_empty_search`
> Test search with empty query
*Line 216*  

#### Function: `test_search_nonexistent_term`
> Test search for term that doesn't exist
*Line 221*  

#### Function: `test_document_update`
> Test updating existing document
*Line 231*  

#### Class: `TestResearchDocument`
> Test suite for ResearchDocument dataclass
*Line 250*  

#### Function: `test_document_creation`
> Test creating a research document
*Line 253*  

#### Function: `test_document_optional_fields`
> Test document with optional fields
*Line 273*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_lexer.py

#### Module: `test_lexer`
> Test script for the HyperCode lexer.
*Line 0*  

#### Function: `test_lexer`
> Test the lexer with the given source code and print the results.
*Line 12*  

#### Function: `run_tests`
> Run a series of test cases for the lexer.
*Line 42*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_mcp_connection.py

#### Function: `check_port`
> Check if a port is open on the given host.
*Line 26*  

#### Function: `find_running_servers`
> Scan common ports to find running servers.
*Line 36*  

#### Function: `test_server_connection`
> Test connection to a single MCP server.
*Line 49*  

#### Function: `test_all_servers`
> Test connection to all MCP servers and print results.
*Line 90*  

#### Function: `check_dependencies`
> Check if required dependencies are installed.
*Line 139*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_mcp_integration.py

#### Module: `test_mcp_integration`
> Test script for HyperCode MCP Server integration
*Line 0*  

#### Function: `test_mcp_server`
> Test the MCP server functionality
*Line 15*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_perplexity.py

#### Module: `test_perplexity`
> Test script for Perplexity API integration with HyperCode AI Research
*Line 0*  

#### Function: `test_perplexity_connection`
> Test Perplexity API with detailed logging
*Line 16*  

#### Function: `test_ai_research_integration`
> Test integration with AI Research document content
*Line 66*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_real_data.py

#### Module: `test_real_data`
> Test the enhanced KnowledgeBase with real Perplexity Space data
*Line 0*  

#### Function: `test_enhanced_knowledge_base`
> Test enhanced KnowledgeBase functionality
*Line 16*  

#### Function: `test_real_perplexity_data_simulation`
> Simulate testing with real Perplexity Space data
*Line 185*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_real_space_data.py

#### Module: `test_real_space_data`
> Test with Real Perplexity Space Data
*Line 0*  

#### Function: `test_real_space_data`
> Test queries that use your actual Perplexity Space data
*Line 15*  

### 📄 hypercode_backup_20251205_183301\hypercode\tests\unit\test_search_algorithm.py

#### Module: `test_search_algorithm`
> Phase 1 Unit Tests for Search Algorithm
*Line 0*  

#### Class: `TestSearchAlgorithm`
> Test suite for search algorithm functionality
*Line 20*  

#### Function: `populated_kb`
> Create a knowledge base with test documents
*Line 24*  

#### Function: `test_exact_title_match_highest_score`
> Test that exact title matches get highest priority
*Line 80*  

#### Function: `test_space_data_boosting`
> Test that space data gets boosted in search results
*Line 92*  

#### Function: `test_related_term_expansion`
> Test related term matching functionality
*Line 105*  

#### Function: `test_tag_matching_scoring`
> Test that tag matches contribute to scoring
*Line 126*  

#### Function: `test_content_frequency_scoring`
> Test that multiple content occurrences increase score
*Line 136*  

#### Function: `test_partial_word_matching`
> Test partial word matching for longer terms
*Line 149*  

#### Function: `test_query_word_ordering`
> Test that query words are properly processed
*Line 167*  

#### Function: `test_case_insensitive_search`
> Test that search is case insensitive
*Line 179*  

#### Function: `test_empty_query_returns_no_results`
> Test that empty queries return no results
*Line 202*  

#### Function: `test_limit_parameter_respected`
> Test that search limit parameter works correctly
*Line 210*  

#### Function: `test_no_results_for_nonexistent_terms`
> Test search for terms that don't exist
*Line 219*  

#### Function: `test_special_characters_in_query`
> Test search with special characters
*Line 227*  

#### Function: `test_unicode_characters`
> Test search with unicode characters
*Line 237*  

#### Function: `test_search_performance_with_large_kb`
> Test search performance with larger knowledge base
*Line 256*  

#### Function: `test_search_result_consistency`
> Test that search results are consistent across multiple calls
*Line 277*  

#### Class: `TestSearchScoringDetails`
> Test detailed scoring algorithm behavior
*Line 292*  

#### Function: `scoring_kb`
> Create KB for detailed scoring tests
*Line 296*  

#### Function: `test_title_match_beats_content_match`
> Test that title matches score higher than content matches
*Line 324*  

#### Function: `test_space_data_boosting_works`
> Test that space data gets boosted
*Line 332*  

#### Function: `test_frequency_scoring`
> Test that content frequency affects scoring
*Line 340*  

### 📄 hypercode_backup_20251205_183301\hypercode_db.py

#### Module: `hypercode_db`
> Hypercode Database - In-memory database for querying Hypercode project data.
*Line 0*  

#### Class: `CodeEntity`
> Represents a code entity (class, function, etc.) in the database.
*Line 12*  

#### Function: `__post_init__`
> Validate the entity after initialization.
*Line 23*  

#### Class: `HypercodeDB`
> In-memory database for Hypercode project analysis.
*Line 28*  

#### Function: `__init__`
> Initialize the database with the given JSON file.
*Line 35*  

#### Function: `_load_database`
> Load the database from a JSON file.
*Line 46*  

#### Function: `get_entities_by_type`
> Get all entities of a specific type.
*Line 93*  

#### Function: `get_entities_in_file`
> Get all entities in a specific file.
*Line 104*  

#### Function: `print_analysis`
> Print a detailed analysis of the codebase.
*Line 116*  

### 📄 hypercode_backup_20251205_183301\knowledge_graph\graph_builder.py

#### Module: `graph_builder`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode_backup_20251205_183301\knowledge_graph\sparql_query.py

#### Module: `sparql_query`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode_backup_20251205_183301\knowledge_graph\update_agent.py

#### Module: `update_agent`
> Semantic knowledge graph management
*Line 0*  

### 📄 hypercode_backup_20251205_183301\live_research\cli.py

#### Function: `print_entry`
> Print a research entry in a readable format.
*Line 10*  

#### Function: `search_entries`
> Search for research entries.
*Line 38*  

#### Function: `view_entry`
> View a specific research entry by ID.
*Line 59*  

#### Function: `add_entry`
> Add a new research entry.
*Line 71*  

#### Function: `import_entries`
> Import entries from a JSON file.
*Line 94*  

#### Function: `export_entries`
> Export all entries to a JSON file.
*Line 126*  

#### Function: `main`
> Main CLI entry point.
*Line 150*  

### 📄 hypercode_backup_20251205_183301\live_research\database.py

#### Class: `ResearchDatabase`
*Line 7*  

#### Function: `__init__`
> Initialize the database connection and create tables if they don't exist.
*Line 8*  

#### Function: `_get_connection`
> Create and return a database connection.
*Line 13*  

#### Function: `_create_tables`
> Create the necessary tables if they don't exist.
*Line 17*  

#### Function: `add_research_entry`
> Add a new research entry to the database.
*Line 68*  

#### Function: `get_research_entry`
> Retrieve a research entry by its ID.
*Line 128*  

#### Function: `search_entries`
> Search research entries by content or tags.
*Line 159*  

#### Function: `import_from_json`
> Import research entries from a JSON file.
*Line 220*  

#### Function: `setup_database`
> Initialize and return a configured ResearchDatabase instance.
*Line 241*  

### 📄 hypercode_backup_20251205_183301\live_research\doc_generator.py

#### Module: `doc_generator`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\live_research\github_publisher.py

#### Module: `github_publisher`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\live_research\import_research.py

#### Module: `import_research`
> Script to import all JSON research files into the database.
*Line 0*  

#### Function: `import_research_data`
> Import all JSON research files into the database.
*Line 18*  

### 📄 hypercode_backup_20251205_183301\live_research\paper_indexer.py

#### Module: `paper_indexer`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\live_research\research_crawler.py

#### Module: `research_crawler`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\live_research\synthesis_engine.py

#### Module: `synthesis_engine`
> Automated research paper collection and synthesis
*Line 0*  

### 📄 hypercode_backup_20251205_183301\live_research\web\app.py

#### Module: `app`
> Flask web application for browsing research data.
*Line 0*  

#### Function: `get_db_connection`
> Create and return a database connection.
*Line 35*  

#### Function: `index`
> Home page showing recent research entries.
*Line 43*  

#### Function: `view_entry`
> View a specific research entry.
*Line 79*  

#### Function: `search`
> Search for research entries.
*Line 121*  

#### Function: `list_tags`
> List all tags with counts.
*Line 194*  

#### Function: `api_entries`
> API endpoint to get all entries in JSON format.
*Line 219*  

#### Function: `page_not_found`
> Handle 404 errors.
*Line 246*  

#### Function: `server_error`
> Handle 500 errors.
*Line 252*  

#### Function: `format_date_filter`
> Format a date string.
*Line 258*  

### 📄 hypercode_backup_20251205_183301\live_research\web\run.py

#### Module: `run`
> Run the research web application.
*Line 0*  

### 📄 hypercode_backup_20251205_183301\mcp\__init__.py

#### Module: `__init__`
> HyperCode MCP (Model Context Protocol) Server Package
*Line 0*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\__init__.py

#### Module: `__init__`
> MCP Servers Package
*Line 0*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\aws_cli.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\aws_resource_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\code_analysis.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\dataset_downloader.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\file_system.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\human_input.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\hypercode_syntax.py

#### Module: `hypercode_syntax`
> HyperCode Syntax MCP Server
*Line 0*  

#### Class: `HyperCodeSyntaxServer`
> 🎨 MCP Server for HyperCode Visual Syntax Integration
*Line 28*  

#### Function: `__init__`
*Line 31*  

#### Function: `handle_request`
> Handle MCP requests from IDE
*Line 35*  

#### Function: `_initialize`
> Initialize the MCP server
*Line 56*  

#### Function: `_document_changed`
> Handle document changes for real-time parsing
*Line 79*  

#### Function: `_text_hover`
> Provide hover information for semantic annotations
*Line 98*  

#### Function: `_completion`
> Provide completion for semantic annotations
*Line 121*  

#### Function: `_parse_document`
> Parse entire document and return semantic structure
*Line 150*  

#### Function: `_validate_neurodiversity`
> Validate neurodiversity compliance and provide suggestions
*Line 179*  

#### Function: `_generate_diagnostics`
> Generate IDE diagnostics from parsed functions
*Line 216*  

#### Function: `_get_annotation_hover_info`
> Generate hover information for semantic annotations
*Line 266*  

#### Function: `main`
> Main MCP server loop
*Line 294*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\path_service.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\user_profile_manager.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\valkey_service.py

#### Function: `check_redis_connection`
*Line 37*  

#### Function: `health_check`
> Health check endpoint to verify that the service is running.
*Line 50*  

#### Function: `set_key`
> Set a value for a given key. The value should be a JSON object.
*Line 57*  

#### Function: `get_key`
> Get the value for a given key.
*Line 69*  

#### Function: `hset_key`
> Set a field (key) in a hash (name). The value should be a JSON object.
*Line 83*  

#### Function: `hget_key`
> Get a field (key) from a hash (name).
*Line 94*  

#### Function: `hgetall_hash`
> Get all fields and values for a given hash name.
*Line 107*  

#### Function: `main`
> Main function to run the Valkey Service MCP Server.
*Line 124*  

### 📄 hypercode_backup_20251205_183301\mcp\servers\web_search.py

#### Function: `main`
*Line 4*  

### 📄 hypercode_backup_20251205_183301\mcp\setup.py

#### Module: `setup`
> MCP Setup Script
*Line 0*  

#### Function: `install_dependencies`
> Install required dependencies
*Line 15*  

#### Function: `verify_setup`
> Verify that MCP is properly set up
*Line 27*  

#### Function: `show_next_steps`
> Show next steps for using MCP
*Line 45*  

#### Function: `main`
*Line 62*  

### 📄 hypercode_backup_20251205_183301\mcp\start_servers.py

#### Module: `start_servers`
> MCP Servers Startup Script
*Line 0*  

#### Function: `start_server`
> Start a specific MCP server
*Line 33*  

#### Function: `list_servers`
> List all available servers
*Line 55*  

#### Function: `main`
*Line 61*  

### 📄 hypercode_backup_20251205_183301\mcp\test_mcp.py

#### Module: `test_mcp`
> MCP Servers Test Script
*Line 0*  

#### Function: `test_server_imports`
> Test that all servers can be imported
*Line 14*  

#### Function: `main`
*Line 48*  

### 📄 hypercode_backup_20251205_183301\scripts\build-hyper-database.py

#### Module: `build-hyper-database`
> Hyper Database Builder - Scans HyperCode repo, builds knowledge graph.
*Line 0*  

#### Class: `HyperDatabaseBuilder`
> Scans codebase and builds semantic knowledge graph.
*Line 21*  

#### Function: `__init__`
> Initialize builder with repo root path.
*Line 24*  

#### Function: `scan_python_file`
> Extract functions, classes from Python file.
*Line 32*  

#### Function: `scan_javascript_file`
> Extract functions from JavaScript (regex-based).
*Line 78*  

#### Function: `should_skip_directory`
> Check if directory should be skipped.
*Line 107*  

#### Function: `build`
> Scan entire repo and build database.
*Line 127*  

#### Function: `generate_markdown_report`
> Generate HYPER_DATABASE.md report.
*Line 161*  

#### Function: `generate_json_report`
> Generate machine-readable HYPER_DATABASE.json.
*Line 250*  

#### Function: `main`
> Main entry point with proper encoding handling.
*Line 265*  

### 📄 hypercode_backup_20251205_183301\scripts\build_knowledge_base.py

#### Module: `build_knowledge_base`
> HyperCode Knowledge Base Builder
*Line 0*  

#### Class: `KnowledgeBaseBuilder`
> Build a knowledge base from the HyperCode repository.
*Line 35*  

#### Function: `__init__`
> Initialize the knowledge base builder.
*Line 38*  

#### Function: `should_skip`
> Check if a path should be skipped during processing.
*Line 79*  

#### Function: `get_file_type`
> Get the file type category.
*Line 162*  

#### Function: `process_file`
> Process a single file and return its metadata.
*Line 244*  

#### Function: `build_index`
> Build the knowledge base index.
*Line 287*  

#### Function: `main`
> Main entry point for the script.
*Line 376*  

### 📄 hypercode_backup_20251205_183301\scripts\document_processor.py

#### Module: `document_processor`
> Document processing utilities for HyperCode knowledge base.
*Line 0*  

#### Class: `DocumentProcessor`
> Process various document types and extract content.
*Line 15*  

#### Function: `get_file_hash`
> Generate a hash for file content.
*Line 19*  

#### Function: `extract_metadata`
> Extract basic metadata from any file.
*Line 29*  

#### Function: `extract_pdf_content`
> Extract text content from PDF files.
*Line 43*  

#### Function: `extract_markdown_content`
> Extract content from Markdown files with frontmatter support.
*Line 74*  

#### Function: `extract_docx_content`
> Extract text content from DOCX files.
*Line 99*  

#### Function: `extract_csv_content`
> Extract content from CSV files.
*Line 133*  

#### Function: `extract_text_content`
> Extract content from plain text files.
*Line 154*  

#### Function: `process_document`
> Process a document based on its file type.
*Line 167*  

### 📄 hypercode_backup_20251205_183301\scripts\generate_directory_readmes.py

#### Module: `generate_directory_readmes`
> Generate README.md files for documentation directories.
*Line 0*  

#### Function: `create_readme`
> Create or update a README.md file with the given content.
*Line 9*  

#### Function: `main`
*Line 20*  

### 📄 hypercode_backup_20251205_183301\scripts\organize_docs.py

#### Module: `organize_docs`
> Documentation Organization Script for HyperCode
*Line 0*  

#### Function: `setup_directories`
> Create the new documentation directory structure.
*Line 131*  

#### Function: `move_files`
> Move files to their new locations based on the mapping.
*Line 138*  

#### Function: `generate_report`
> Generate a migration report.
*Line 172*  

#### Function: `main`
*Line 204*  

### 📄 hypercode_backup_20251205_183301\scripts\reorganize_repo.py

#### Module: `reorganize_repo`
> Reorganize the HyperCode repository structure to be more maintainable.
*Line 0*  

#### Function: `create_directories`
> Create the new directory structure.
*Line 29*  

#### Function: `move_files`
> Move files to their new locations.
*Line 37*  

#### Function: `update_gitignore`
> Update .gitignore with new paths.
*Line 71*  

#### Function: `main`
*Line 83*  

### 📄 hypercode_backup_20251205_183301\scripts\run_lexer.py

#### Module: `run_lexer`
> Test suite for HyperCode lexer.
*Line 0*  

#### Class: `TestLexer`
> Test suite for the HyperCode lexer.
*Line 18*  

#### Function: `setUp`
> Create a fresh lexer instance for each test.
*Line 21*  

#### Function: `test_empty_source`
> Test that an empty source returns only an EOF token.
*Line 25*  

#### Function: `test_basic_tokens`
> Test basic token types are correctly identified.
*Line 31*  

#### Function: `test_string_literals`
> Test string literals with various contents.
*Line 44*  

#### Function: `test_numbers`
> Test different number formats.
*Line 58*  

#### Function: `test_arithmetic_expressions`
> Test complex arithmetic expressions.
*Line 83*  

#### Function: `test_comments`
> Test different types of comments are properly ignored.
*Line 107*  

#### Function: `test_error_handling`
> Test that the lexer properly handles and reports errors.
*Line 121*  

#### Function: `test_error_recovery`
> Test that the lexer can recover from invalid tokens and continue parsing.
*Line 153*  

#### Function: `_assert_token_types`
> Helper to assert token types match expected types.
*Line 179*  

#### Function: `test_lexer_error_class`
> Test that LexerError is properly defined and can be instantiated.
*Line 201*  

### 📄 hypercode_backup_20251205_183301\scripts\run_tests.py

#### Module: `run_tests`
> HyperCode Test Runner
*Line 0*  

#### Function: `run_tests`
> Run pytest with the given arguments and coverage reporting.
*Line 16*  

#### Function: `main`
> Parse command line arguments and run tests.
*Line 49*  

### 📄 hypercode_backup_20251205_183301\scripts\style_guide_collector.py

#### Module: `style_guide_collector`
> 🎨 HyperCode Style Guide Feedback Collector
*Line 0*  

#### Class: `StyleGuideCollector`
> 🎨 Collects and analyzes style guide feedback from the community
*Line 17*  

#### Function: `__init__`
*Line 20*  

#### Function: `_load_feedback`
> 📂 Load existing feedback data
*Line 31*  

#### Function: `_save_feedback`
> 💾 Save feedback data
*Line 50*  

#### Function: `add_feedback`
> 📝 Add new feedback entry
*Line 59*  

#### Function: `_update_analysis`
> 📊 Update analysis based on new feedback
*Line 101*  

#### Function: `analyze_feedback`
> 📊 Generate comprehensive analysis of all feedback
*Line 150*  

#### Function: `_get_top_items`
> 📊 Get top items from a frequency dictionary
*Line 176*  

#### Function: `_calculate_consensus`
> 📊 Calculate consensus for preference categories
*Line 201*  

#### Function: `_generate_recommendations`
> 💡 Generate style guide recommendations based on feedback
*Line 230*  

#### Function: `import_github_issues`
> 📥 Import feedback from GitHub issues
*Line 288*  

#### Function: `generate_report`
> 📊 Generate comprehensive feedback report
*Line 309*  

#### Function: `interactive_feedback`
> 🎯 Interactive feedback collection from command line
*Line 370*  

#### Function: `main`
> 🚀 Main entry point
*Line 469*  

### 📄 hypercode_backup_20251205_183301\scripts\sync-space-to-main.py

#### Module: `sync-space-to-main`
> HyperCode Space-to-Main Sync Script
*Line 0*  

#### Function: `log_error`
> Error-level log with traceback.
*Line 25*  

#### Class: `Colors`
*Line 37*  

#### Function: `log_info`
> Info-level log.
*Line 46*  

#### Function: `log_success`
> Success-level log.
*Line 51*  

#### Function: `log_warning`
> Warning-level log.
*Line 56*  

#### Function: `deep_merge`
> Recursively merge source dict into destination dict.
*Line 61*  

#### Function: `load_config`
> Load sync configuration from TOML file.
*Line 72*  

#### Function: `should_skip_file`
> Check if file should be skipped based on filters.
*Line 112*  

#### Function: `get_all_files`
> Recursively get all files in directory.
*Line 135*  

#### Function: `copy_file`
> Copy file with directory creation. Returns True if copied/would copy.
*Line 145*  

#### Function: `remove_file`
> Remove file. Returns True if removed/would remove.
*Line 157*  

#### Function: `sync_folder`
> Sync source folder to target folder (one-way).
*Line 168*  

#### Function: `delete_orphans`
> Remove files from target that no longer exist in source.
*Line 212*  

#### Function: `sync_all_mappings`
> Execute all mappings from config.
*Line 229*  

#### Function: `write_log`
> Write sync results to log file.
*Line 281*  

#### Function: `print_summary`
> Print sync summary to console.
*Line 303*  

#### Function: `main`
*Line 327*  

### 📄 hypercode_backup_20251205_183301\scripts\test_mcp_connection.py

#### Function: `check_port`
> Check if a port is open on the given host.
*Line 25*  

#### Function: `find_running_servers`
> Scan common ports to find running servers.
*Line 34*  

#### Function: `test_server_connection`
> Test connection to a single MCP server.
*Line 46*  

#### Function: `test_all_servers`
> Test connection to all MCP servers and print results.
*Line 82*  

#### Function: `check_dependencies`
> Check if required dependencies are installed.
*Line 124*  

### 📄 hypercode_backup_20251205_183301\scripts\test_perplexity_api.py

#### Module: `test_perplexity_api`
> Test script for Perplexity API integration.
*Line 0*  

#### Function: `main`
> Test the Perplexity API connection and make a sample query.
*Line 17*  

### 📄 hypercode_backup_20251205_183301\scripts\update_doc_links.py

#### Module: `update_doc_links`
> Update internal documentation links after reorganization.
*Line 0*  

#### Function: `update_links_in_file`
> Update links in a single file.
*Line 27*  

#### Function: `replace_link`
*Line 39*  

#### Function: `main`
*Line 63*  

### 📄 hypercode_backup_20251205_183301\scripts\web_interface.py

#### Function: `load_index`
*Line 18*  

#### Function: `search_documents`
*Line 24*  

#### Function: `index`
*Line 58*  

#### Function: `search`
*Line 63*  

#### Function: `get_document`
*Line 71*  

#### Function: `serve_static`
*Line 80*  

#### Function: `create_template_if_not_exists`
> Create the template directory and index.html if they don't exist
*Line 84*  

### 📄 hypercode_backup_20251205_183301\test_database.py

#### Module: `test_database`
> Test script for Hypercode database operations.
*Line 0*  

#### Function: `test_database_loading`
> Test loading the database and basic queries.
*Line 10*  
