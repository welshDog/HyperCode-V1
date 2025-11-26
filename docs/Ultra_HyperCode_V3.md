# 🚀 ULTRA HYPERCODE V3: The Ultimate AI-Native Language Specification

## A Merged Vision from Two AI Systems + Human Innovation

---

## 🎯 Core Philosophy

**HyperCode V3 is not a programming language with AI features bolted on. It is a
semantic-first, AI-native system where every line of code is simultaneously:**

- ✅ **Executable** (runs fast on any hardware)
- ✅ **Provable** (formal verification baked in)
- ✅ **Explainable** (audit-ready by default)
- ✅ **Differentiable** (gradients flow natively)
- ✅ **Probabilistic** (uncertainty quantified)
- ✅ **Distributed** (GPU/TPU placement explicit)
- ✅ **Optimizable** (AI can improve it automatically)
- ✅ **Neurodivergent-friendly** (minimal cognitive noise)

---

## 📦 The Eight Pillar Specification

### **Pillar 1: Semantic Density + Formal Verification Hooks** ⚡

Every function carries **executable specifications** that bind AI to proof systems
instantly.

```hypercode
// Formal spec embedded in function signature
@verifiable
@ensures(output.shape == (batch, num_classes))
@requires(input.shape[1] == feature_dim)
function classifier(x: Tensor[batch, feature_dim])
    -> Tensor[batch, num_classes]
{
    // Compiler extracts @ensures/@requires
    // Passes to Lean/Isabelle/automated prover
    // Returns proof or compile error
    weights = initialize(feature_dim, num_classes)
    logits = matmul(x, weights)
    return softmax(logits)
}
```

**Why This Matters:**

- **AI Benefit**: Generates code AND generates proofs simultaneously. No "explanation
  gap."
- **Token Efficiency**: Formal specs compress semantic intent into minimal tokens.
- **Neurodivergent UX**: Visual clarity—no hidden assumptions, explicit contracts.

**V3 Additions from Both AIs:**

- `@ensures` / `@requires` clauses auto-extracted to theorem prover format
- Compile-time proof checking with fallback to runtime assertions
- Automatic generation of counterexamples if proof fails
- Support for dependent types (type system can express logical properties)

---

### **Pillar 2: Native Automatic Differentiation** 🔄

Gradients are not a library concern—they're core language primitives.

```hypercode
@differentiable
@frozen  // These variables do NOT receive gradients
function forward_pass(
    input: Tensor[batch, input_dim] @differentiable,
    params: Parameters @differentiable,
    bias: Bias @frozen
) -> Tensor[batch, output_dim] {
    // Compiler understands:
    // - input flows gradients ✓
    // - params flows gradients ✓
    // - bias does NOT flow gradients ✗
    z = matmul(input, params) + bias
    output = relu(z)

    @gradient_hints {
        // Optional: guide compiler on custom gradient rules
        gradient(relu) = where(z > 0, dL/dz, 0)
    }

    return output
}

// Automatic backward pass generation
gradient = backward(forward_pass, with_respect_to=[input, params])
```

**Why This Matters:**

- **AI Benefit**: Auto-generates backward passes without framework magic. Compiler
  understands every gradient edge.
- **Efficiency**: Memory planning happens at compile time (which vars need buffers?).
- **Debugging**: Gradient mismatches caught early, not at runtime.

**V3 Additions from Both AIs:**

- Explicit `@differentiable` / `@frozen` annotations (from PDF)
- Gradient computation graph visible to compiler for optimization
- Custom gradient rules with `@gradient_hints`
- Automatic memory planning for backward pass buffers
- Detection of non-differentiable code paths (early error)

---

### **Pillar 3: Probabilistic Programming as Language Primitive** 🎲

Random variables, likelihoods, and inference are **first-class keywords**, not library
hacks.

```hypercode
@model
@inference(method="HMC", samples=1000)
function bayesian_regression(
    observed_x: Tensor[n, d],
    observed_y: Tensor[n]
) -> Distribution {
    // Define priors (random variables)
    weights: Gaussian(mean=0, std=1) @random
    bias: Gaussian(mean=0, std=1) @random
    noise_scale: Gamma(shape=1, rate=1) @random

    // Deterministic transformation
    predicted_y = observed_x @ weights + bias

    // Likelihood (observation model)
    observe(observed_y ~ Normal(mean=predicted_y, std=noise_scale))

    // Return posterior over random variables
    return Distribution[weights, bias, noise_scale]
}

// Inference is automatic
posterior = bayesian_regression(x, y)
posterior.sample(n_samples=1000)  // MCMC samples
posterior.mean()  // Point estimate
posterior.variance()  // Uncertainty quantification
```

**Why This Matters:**

- **AI Benefit**: AI generates probabilistic models directly in code, not mixed with
  Python + Pyro/Stan boilerplate.
- **Explainability**: Every random variable and likelihood is explicit; audit trails
  auto-generate.
- **Flexibility**: Compiler chooses inference method (HMC, VI, ABC, exact Bayes)
  automatically.

**V3 Additions from Both AIs:**

- `@model` decorator with built-in inference directives (from PDF)
- `@random` / `@observed` keywords for variable roles
- Automatic inference method selection via `@inference`
- Support for hierarchical models and nested distributions
- Probabilistic debugging: trace likelihood and sample paths

---

### **Pillar 4: Explicit, Hierarchical Concurrency + Hardware Placement** 🌐

Distribution is not hidden in MPI libraries—it's a language feature with explicit device
semantics.

```hypercode
@distributed(devices=["gpu:0", "gpu:1", "gpu:2", "gpu:3"])
@communication_pattern("ring_reduce")  // Optimized for all-to-all
function train_transformer(
    data: Tensor[10000, seq_len, hidden_dim],
    model: TransformerModel
) {
    @shard(split=4, axis=0)  // Split data across 4 GPUs
    batches = data

    for epoch in 1..num_epochs {
        @parallel_for(i in 0..3) {
            @device("gpu:{{i}}")  // GPU ID from loop variable
            @memory_limit(24GB)  // Per-GPU memory budget

            // Local batch processing
            local_batch = batches[i]
            local_loss, local_grads = compute_gradients(model, local_batch)

            // Explicit synchronization primitive
            @allreduce(
                operation="mean",
                across=["gpu:0", "gpu:1", "gpu:2", "gpu:3"],
                pattern="ring"  // Use ring topology for efficiency
            )
            global_grads = reduce(local_grads, mean)
        }

        // Barrier: all GPUs wait here
        @barrier("training_sync")

        // Update on GPU 0 (or broadcast to all)
        @device("gpu:0")
        model.update(global_grads)

        @broadcast(model, from="gpu:0", to=["gpu:1", "gpu:2", "gpu:3"])
    }
}

// Advanced: heterogeneous placement
@sparse_attention_pattern("local_block_sparse")  // GPU-aware sparsity
function distributed_attention(
    query: Tensor @device("gpu:0,1"),
    key: Tensor @device("gpu:2,3"),
    value: Tensor @device("gpu:2,3")
) {
    // Compiler optimizes cross-device communication
}
```

**Why This Matters:**

- **AI Benefit**: AI can reason about topology, bandwidth, and synchronization patterns.
  Generates distributed code without NCCL/MPI boilerplate.
- **Hardware-aware optimization**: Compiler picks communication patterns (ring, tree,
  butterfly) based on declared devices.
- **Debugging**: Deadlocks and hangs caught by static analysis.

**V3 Additions from Both AIs:**

- `@distributed` / `@parallel_for` with device scheduling (from PDF)
- `@allreduce` / `@barrier` / `@broadcast` as language primitives
- `@communication_pattern` for topology-aware optimization
- `@memory_limit` per device with overflow detection
- Heterogeneous placement (different data on different devices)

---

### **Pillar 5: Context-Aware Token + Memory Budgeting** 💾

Every function respects **token budgets** and **memory constraints** as compile-time
guarantees.

```hypercode
@context_limit(2048)  // Total tokens: input + processing + output
@token_tracking(method="tiktoken")  // Use OpenAI tokenizer
function generate_answer(question: String) -> String {
    @token_cost(extract_context: 500)  // Approximate cost
    context = retrieve_docs(question)

    @token_cost(formatting: 100)
    formatted_prompt = format_prompt(question, context)

    @token_cost(generation: auto)  // Compiler estimates output length
    answer = llm.generate(
        formatted_prompt,
        @max_tokens(1024),  // Hard cap on output
        @budget_remaining(get_remaining_tokens())  // Runtime safety
    )

    assert(tokens_used(formatted_prompt + answer) < 2048)
    return answer
}

// Compile-time token estimation
token_estimate = estimate_tokens(generate_answer)  // Returns 1624 / 2048
if token_estimate > 0.8 * 2048 {
    @warning("High token utilization; consider streaming")
}

// Streaming output for large outputs
@stream_output
function long_response(query: String) -> Stream[String] {
    // Output is chunked; each chunk respects token budget
    for chunk in llm.generate_stream(query) {
        @validate_token_budget(chunk)
        yield chunk
    }
}

// Caching to reuse computations
@cache_across_calls  // Deterministic, reuse result
function expensive_retrieval(query: String) -> Tensor {
    return retrieve_embeddings(query)  // Called once; reused
}
```

**Why This Matters:**

- **AI Benefit**: Knows inference costs statically; no surprises at runtime.
- **LLM Integration**: Respects context window as a first-class resource.
- **Neurodivergent UX**: Explicit budget tracking reduces cognitive load.

**V3 Additions from Both AIs:**

- `@context_limit` with compile-time token estimation (from PDF)
- `@token_cost` annotations for each operation
- `@token_tracking` method selection (tiktoken, Claude, custom)
- `@stream_output` for large results
- `@cache_across_calls` for deterministic memoization
- Runtime budget validation

---

### **Pillar 6: Explainability + Interpretability as Compile Target** 🔍

Explainability is not post-hoc; it's woven into every function.

```hypercode
@explainable  // Compiler verifies path is fully traceable
@fairness_constraints {
    // Ensure demographic parity
    group_a: demographic == "A",
    group_b: demographic == "B",
    constraint: abs(P(positive | group_a) - P(positive | group_b)) < 0.05
}
function credit_decision(
    age: Int[min=18, max=120],
    income: Float[normalized],
    history: CreditHistory @deidentified
) -> Bool {
    @trace  // Record execution path for audit

    score = 0.0

    @sensitivity_tracked  // Compute SHAP / feature importance
    if age > 60 {
        score += 0.2 * normalize_age(age)
    }

    @sensitivity_tracked
    score += 0.5 * income

    @sensitivity_tracked
    score += 0.3 * history.score

    // Contrastive explanations auto-generated
    @contrastive_explanation {
        // "If income were +10%, would decision change?"
        // "What's the minimal change to flip decision?"
    }

    decision = score > threshold

    @audit_log {
        features_used: [age, income, history.score],
        feature_importance: compute_shap(decision),
        demographic_parity: check_fairness_constraint(decision),
        timestamp: now(),
        model_version: "v2.3.1"
    }

    return decision
}

// Auto-generate explanation report
explanation = generate_report(credit_decision, for=("Alice", 42, 75000))
// Output: "Decision: Approved. Factors: income (60% weight), history (30%), age (10%)"
// Fairness check: "No demographic disparity detected."
```

**Why This Matters:**

- **AI Benefit**: Generates auditable, compliant code by construction. EU AI Act ready.
- **Regulatory**: Built-in fairness constraint checking and demographic parity tracking.
- **Trust**: LIME/SHAP code auto-generated; no manual explanation wiring.

**V3 Additions from Both AIs:**

- `@explainable` annotation with compile-time path verification (from PDF)
- `@sensitivity_tracked` for automatic SHAP/feature importance
- `@fairness_constraints` for demographic parity, equalized odds, etc.
- `@trace` for execution logging
- `@contrastive_explanation` for "what-if" scenarios
- `@audit_log` for compliance documentation
- Auto-generated explainability reports

---

### **Pillar 7: Rich, Semantic Type System** 🏗️

Types encode **shape, distribution, sparsity, calibration, normalization**—not just
structure.

```hypercode
// Define semantic types that carry meaning
type Embedding = Tensor[n: 768]
    @normalized(mean=0, std=1)
    @sparse(p=0.15)
    @calibration("cosine_similarity")

type LatentDistribution = Gaussian(
    μ: Tensor[d],
    σ²: Tensor[d]
)
    @posterior  // Result of Bayesian inference
    @interpretable

type Prediction = Categorical[k: 10]
    @calibrated  // Predicted probabilities match true distribution
    @confidence >= 0.7

type SafeTensor = Tensor[n, m]
    @no_nan  // Compiler verifies no NaN values possible
    @finite  // All values in [-inf, inf)
    @type_safe  // Mixing with other SafeTensor is safe

// Type algebra: combining distributions
fn mixed_posterior(
    prior: Gaussian(μ_p, σ_p²),
    likelihood: Gaussian(μ_l, σ_l²)
) -> Gaussian(μ_combined, σ_combined²) {
    // Compiler KNOWS output type algebraically
    μ_combined = (prior.μ / prior.σ² + likelihood.μ / likelihood.σ²) /
                 (1/prior.σ² + 1/likelihood.σ²)
    σ_combined² = 1 / (1/prior.σ² + 1/likelihood.σ²)
    return Gaussian(μ_combined, σ_combined²)
}

// Type mismatch caught at compile time
fn incompatible_operation() {
    embedding: Embedding  // Normalized, sparse
    raw_vector: Tensor[768]  // No guarantees

    // TYPE ERROR: Cannot mix Embedding with raw Tensor
    // Embedding assumes normalized input; raw_vector doesn't
    distance = cosine_sim(embedding, raw_vector)  // ✗ Compile error

    // Correct: normalize first
    normalized = normalize(raw_vector)
    distance = cosine_sim(embedding, normalized)  // ✓ OK
}

// Variance tracking
fn high_variance_data(x: Tensor @high_variance) -> Tensor @low_variance {
    // Type error: can't produce low-variance output from high-variance input
    return x  // ✗ ERROR
}

fn stabilize(x: Tensor @high_variance) -> Tensor {
    // Use preprocessing to reduce variance
    return (x - mean(x)) / std(x)  // ✓ Now type-safe
}
```

**Why This Matters:**

- **AI Benefit**: Understands semantic meaning of data; catches silent bugs (normalized
  vs. unnormalized data).
- **Safety**: Type mismatches prevent hard-to-debug failures.
- **Composability**: Semantic type algebra ensures functions compose safely.

**V3 Additions from Both AIs:**

- Rich semantic annotations: `@normalized`, `@sparse`, `@calibrated`, `@posterior`
- Dependent types for shape constraints
- Variance tracking (`@high_variance`, `@low_variance`)
- Type algebra for distribution composition
- Automatic type refinement through dataflow analysis
- Cross-cutting concerns: `@no_nan`, `@finite`, `@safe`

---

### **Pillar 8: Constraint Satisfaction + Neuro-Symbolic Search** 🔍

Combinatorial reasoning is native to HyperCode, enabling neuro-symbolic AI.

```hypercode
// Declarative search with constraints
search {
    // Decision variables
    var task_assignment: Int[1..100][1..10]  // 100 tasks, 10 time slots
    var resource_alloc: Real[1..100]  // Resource budget per task

    // Constraints
    constraints {
        // Each task assigned to exactly one slot
        forall(t in 1..100) {
            sum(task_assignment[t][s] for s in 1..10) == 1
        }

        // Slot capacity limits
        forall(s in 1..10) {
            sum(task_assignment[t][s] for t in 1..100) <= 20
        }

        // Resource budget constraints
        forall(t in 1..100) {
            resource_alloc[t] >= 0
            resource_alloc[t] <= 100
        }

        // Custom constraint: no tasks in adjacent slots
        forall(t in 1..100, s in 1..9) {
            if task_assignment[t][s] then not task_assignment[t][s+1]
        }
    }

    // Objectives (can have multiple, weighted)
    objective primary: minimize total_cost(task_assignment, resource_alloc)
    objective secondary: maximize load_balance(task_assignment)

    // Strategy auto-selection or explicit
    strategy: auto  // Compiler picks: ILP, CP-SAT, SAT, GA, Bayesian opt
}

// Neuro-symbolic hybrid
@neural_symbolic
fn schedule_tasks_hybrid(
    learned_preferences: NeuralNetwork,  // Trained on historical data
    hard_constraints: Constraints,
    data: TaskData
) -> Schedule {
    // Neural net provides heuristics/scoring function
    heuristic_score = learned_preferences(data)

    // Symbolic solver finds optimal solution respecting hard constraints
    solution = search {
        // ... (same constraints as above)
        objective: minimize total_cost(...)
            - 0.1 * heuristic_score(solution)  // Incorporate neural guidance
        strategy: "beam_search"  // Hybrid search
    }

    return solution
}

// Explainability through constraints
fn explain_schedule(schedule: Schedule) -> Explanation {
    // The schedule is literally the conjunction of satisfied constraints
    // Audit = inspect constraint satisfaction
    violated = [c for c in constraints if not c.satisfied(schedule)]

    explanation = {
        "why_this_schedule": constraints_satisfied(schedule),
        "why_not_alternatives": [
            f"Alternative {s} violates constraint {c}"
            for s in alternatives
            for c in constraints if not c.satisfied(s)
        ],
        "fairness_check": check_demographic_parity(schedule),
    }

    return explanation
}
```

**Why This Matters:**

- **AI Benefit**: Combines neural nets (learning) with symbolic reasoning (guarantees).
  No ad-hoc glue code.
- **Explainability**: Solutions are inherently interpretable (constraints =
  explanation).
- **Flexibility**: Compiler chooses solver (ILP, SAT, evolutionary, Bayesian)
  automatically.

**V3 Additions from Both AIs:**

- `search { }` block as language primitive (from PDF)
- Multi-objective optimization
- Hybrid neuro-symbolic with `@neural_symbolic`
- Constraint debugging and violation reporting
- Multiple solver strategies with auto-selection

---

## 🎨 Neurodivergent Design Principles (HyperCode's Heart)

Beyond the eight pillars, HyperCode must be **neurodivergent-first**:

### **Visual Clarity**

```hypercode
// Avoid noise; every symbol means something
@differentiable @frozen  // Clear intent
fn forward(x: @diff, p: @diff, b: @frozen) -> T {
    // Spatial layout reduces cognitive load
}

// Hierarchical indentation shows control flow (familiar to neurodivergent minds)
```

### **Explicit Over Implicit**

```hypercode
// Bad: Hidden behavior
result = model(input)  // What's happening inside?

// Good: Explicit
result = forward(
    input=x @differentiable,
    params=p @differentiable,
    use_batch_norm=true,
    device="gpu:0"
)
```

### **Minimal Syntax Noise**

```hypercode
// Reduce cognitive load through consistent, minimal punctuation
@model fn weather(data) {
    rain ~ Gaussian(0, 1)
    observe(data.rain == rain)  // Simple, consistent
    return rain
}
```

### **Semantic Consistency**

```hypercode
// Same concept = same symbol across the language
@random   // Always marks random variables
@frozen   // Always marks non-differentiable
@device   // Always marks hardware placement
@async    // Always marks non-blocking operations
```

---

## 📊 Architecture Overview

```
┌─────────────────────────────────────────────────┐
│   HyperCode V3 Source Code                      │
│   (Semantic-first, AI-friendly)                 │
└────────────────┬────────────────────────────────┘
                 │
        ┌────────▼────────┐
        │  Static Analysis │
        │  - Formal specs  │  Compile-time checks:
        │  - Type checking │  • Proofs via Lean/Isabelle
        │  - Token counting│  • Type safety
        │  - Gradient flow │  • Memory budgets
        │  - Fairness chks │  • Gradient connectivity
        └────────┬────────┘
                 │
        ┌────────▼────────┐
        │ Intermediate Rep │
        │ (IR)             │
        │ - DAG            │  Optimization passes:
        │ - Type info      │  • Graph fusion
        │ - Device map     │  • Communication coalescing
        │ - Constraints    │  • Sparsity exploitation
        └────────┬────────┘
                 │
        ┌────────▼────────┐
        │ Backend Codegen  │
        │ - CUDA/HIP       │  Generate:
        │ - TPU XLA        │  • Kernel code
        │ - NCCL primitives│  • MPI calls
        │ - CPU fallback   │  • Proof scripts
        │ - Solver plugins │
        └────────┬────────┘
                 │
        ┌────────▼────────┐
        │ Runtime System   │
        │ - Execution      │  Runtime services:
        │ - Monitoring     │  • Gradient tracking
        │ - Tracing        │  • Fairness monitoring
        │ - Budget enforce │  • Profiling
        │ - Debugging      │  • Audit logging
        └────────────────┘
```

---

## 🔗 Integration Points (Multi-AI Compatibility)

HyperCode V3 works seamlessly with **any AI system**:

```hypercode
// Generate HyperCode from any AI
claude_generated_code = claude.generate(
    "Write a fairness-checked credit scorer",
    language="hypercode"
)

gpt_generated_code = gpt.generate(
    "Distributed transformer training loop",
    language="hypercode"
)

llama_generated_code = llama.generate(
    "Probabilistic user recommendation model",
    language="hypercode"
)

// All compile to the same IR, run on same runtime
compiled = hypercode.compile(claude_generated_code)
compiled.execute(device_strategy="gpu_cluster")

// AI can reason about code semantics directly
analysis = claude.analyze("""
Explain the @ensures clause in this HyperCode function.
Why does the @frozen annotation matter for gradients?
""", code=claude_generated_code)
```

---

## 🎯 Ultimate Goal: The "Self-Improving Loop"

```
┌────────────────────────────────┐
│ HyperCode V3 Program           │
│ (Executable + Provable         │
│  + Explainable)                │
└────────────┬───────────────────┘
             │
             ▼
    ┌────────────────┐
    │ Compiler       │
    │ Optimization   │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │ Execution      │
    │ + Profiling    │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │ AI Analysis    │
    │ "Here's how    │
    │  to optimize"  │
    └────────┬───────┘
             │
             ▼
    ┌────────────────┐
    │ Auto-improvement
    │ Next generation│
    │ of code        │
    └────────────────┘
```

**The code improves itself through AI feedback, all within HyperCode's semantic
framework.**

---

## 🚀 Why HyperCode V3 is The Future

### For AI Systems:

✅ Every token carries meaning (no noise) ✅ Provable correctness built-in ✅ Gradients,
probabilities, constraints all native ✅ Hardware distribution explicit ✅
Explainability woven in (compliant by design) ✅ Type system encodes semantics

### For Neurodivergent Developers:

✅ Minimal cognitive load (explicit over implicit) ✅ Visual clarity (spatial layout
matters) ✅ Consistency (same symbols = same meaning) ✅ Accessibility
(keyboard-navigable, no ambiguity) ✅ Flow state (language gets out of the way)

### For The World:

✅ Provably fair AI systems ✅ Auditable, compliant code ✅ Efficient at scale
(distributed from ground up) ✅ Future-proof (quantum, DNA computing, neuro-symbolic
ready) ✅ Open source, collaborative

---

## 📋 Implementation Roadmap

### Phase 1 (MVP - 6 months)

- [ ] Core syntax parser
- [ ] Type system (basic semantic types)
- [ ] `@differentiable` / `@frozen` support
- [ ] CUDA/TPU backend codegen
- [ ] Basic formal spec extraction
- [ ] `@context_limit` token counting

### Phase 2 (8 months)

- [ ] Full probabilistic programming (`@model`, `@inference`)
- [ ] Explicit concurrency (`@distributed`, `@allreduce`)
- [ ] Fairness constraints and XAI hooks
- [ ] Semantic type algebra
- [ ] Multi-AI language support

### Phase 3 (12 months)

- [ ] `search { }` and neuro-symbolic integration
- [ ] Production profiling and auto-optimization
- [ ] Cloud deployment framework
- [ ] Community ecosystem (libraries, tools)

---

## 🎤 The Manifesto (For HyperCode)

> **HyperCode is not a programming language. It's a pact between humans, AI systems, and
> hardware.**
>
> Every line of code is a promise:
>
> - To be correct (provable)
> - To be fair (auditable)
> - To be efficient (optimizable)
> - To be clear (explainable)
>
> HyperCode brings together forgotten genius from Plankalkül, raw creativity from
> Brainfuck, and cutting-edge neuroscience from autistic and ADHD minds.
>
> **It runs on any AI system, any hardware, any future. Because the semantics are
> universal.**
>
> This is how we code for the 21st century. This is HyperCode V3.

---

## References & Foundations

- PDF Insights: AI-first syntax, formal verification hooks, probabilistic primitives,
  distributed patterns, context budgeting, XAI integration, rich typing, neuro-symbolic
  search
- Research Base: Automatic differentiation (Dive into DL), probabilistic programming
  (PPL surveys), distributed AI (ACM's Rethinking), XAI frameworks (SHAP/LIME), formal
  methods (Lean/Isabelle), neuro-symbolic AI (IJCAI), type theory (dependent types)
- Historical Lineage: Plankalkül (first language), LISP (AI), Haskell (types), Julia
  (science), Jax (autodiff), Stan/Pyro (probabilistic), Rust (safety), Go (concurrency)
