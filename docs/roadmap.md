# Stage 1: AI Foundations

Understand the field before touching frameworks and APIs. Time: 1 to 2 months. This is the first stage of a larger AI engineering path, later stages are not covered here.

---

## Baseline Audit

**Already solid:** general Python fluency (from the Django/backend track), basic programming reasoning.

**Genuinely new:** the AI vs ML vs deep learning distinction, intelligent agents, search and planning, decision making, knowledge representation, reasoning, reinforcement learning concepts, formal problem formulation, NumPy, Pandas, probability, statistics, linear algebra, basic calculus applied to AI.

**Dependency order:**
- Supporting Foundations (math and Python tooling) can start in parallel with AI Fundamentals, since neither depends on the other yet.
- AI Problem Solving depends on AI Fundamentals, formulating a problem requires first knowing what kind of system is being built.
- Math foundations (probability, linear algebra, calculus) should be at least at review level before Stage 2 (ML), but are not blocking for the conceptual parts of this stage.

**What NOT to study yet:** any ML framework (scikit-learn, PyTorch, TensorFlow), neural networks, LLM APIs, prompt engineering. This stage is concepts and math only.

---

## Phase 1: AI Fundamentals

**Goal:** Build an accurate mental model of what AI actually is, so later frameworks are understood, not just used.

**Concepts:**
- AI vs machine learning vs deep learning, as nested, not interchangeable, terms
- Intelligent agents: percepts, actions, environment, agent function
- Search as a general problem-solving tool (not yet the algorithms, the concept)
- Heuristics: what they are, why they trade correctness guarantees for speed
- Planning and decision making as distinct from search
- Knowledge representation: how facts and rules are encoded for a system to use
- Reasoning: deriving new facts from known ones
- Reinforcement learning concepts at an intuitive level only (agent, environment, reward, policy)

**Prerequisites:** None.

**Practical exercises:** Write a one-page explanation, in your own words, of the AI/ML/deep-learning nesting with one real example of each. Model a simple environment (e.g. a grid) as an agent with percepts and actions on paper before writing code.

**Python mini project:** A simple rule-based agent (no ML) that navigates a small grid using if/else logic and a basic heuristic (e.g. move toward the goal). This reinforces agents, heuristics, and decision making without needing any ML library.

**Skills gained:** Can correctly place a given AI system (chatbot, recommendation engine, self-driving perception) into the AI/ML/deep-learning hierarchy and justify it.

**What NOT to study yet:** Any real search algorithm implementation (A*, BFS-based search), that is Phase 2.

**Exit criteria:** Can explain, without notes, the difference between search, planning, and reinforcement learning using one sentence each.

---

## Phase 2: AI Problem Solving

**Goal:** Learn to formulate a problem the way an AI system needs it formulated, before reaching for any tool.

**Concepts:**
- Problem formulation: goal, actions, states
- State spaces: how a problem's possibilities are represented as a graph of states
- Search strategies at a conceptual level (uninformed vs informed, not full algorithm implementation yet, that belongs in a later DSA/AI crossover)
- Constraints: what limits valid states or actions
- Optimization: finding the best solution, not just a valid one
- Evaluation: how to judge whether a solution or a system is actually good

**Prerequisites:** Phase 1.

**Practical exercises:** Formally formulate the 8-puzzle or a simple maze as a state-space problem: define states, actions, goal test, and a heuristic. Do this on paper before coding.

**Python mini project:** A small state-space search solver for a simple problem (e.g. a maze or the 8-puzzle) using basic search (this connects directly to BFS/DFS from the DSA roadmap, reuse that skill here). Explain why this project was chosen: it forces explicit problem formulation, which is the actual Stage 1 skill, the search algorithm itself is secondary.

**Skills gained:** Can take a vague real-world problem and formally write it as states, actions, goal test, and constraints.

**What NOT to study yet:** Advanced search (A*, minimax, adversarial search), full optimization theory, those come with dedicated later stages.

**Exit criteria:** Given a new unfamiliar problem, produces a correct formal state-space formulation (states, actions, goal, constraints) within 20 minutes.

---

## Phase 3: Supporting Foundations

**Goal:** Build the practical Python, math, and data-handling toolkit that every later AI/ML stage depends on.

**Concepts:**
- Python for data work: idioms used constantly in AI code (list/array operations, vectorized thinking)
- NumPy: arrays, vectorized operations, broadcasting, why this replaces manual loops
- Pandas: DataFrames, indexing, filtering, grouping, basic cleaning
- Probability: events, distributions, conditional probability, expectation, at the level needed to read an ML paper's basics
- Statistics: mean, variance, standard deviation, correlation, what a distribution's shape tells you
- Linear algebra: vectors, matrices, dot product, matrix multiplication, what these represent geometrically
- Basic calculus: derivatives and gradients at the intuition level (what a gradient means, not full proofs), since this underlies later optimization

**Prerequisites:** Basic Python (already have).

**Practical exercises:** Rewrite a manual-loop array computation using NumPy vectorized operations and compare runtime. Load a real CSV dataset with Pandas, clean missing values, and compute summary statistics. Compute a dot product and matrix multiplication by hand, then verify with NumPy. Explain what a gradient represents using a simple 2D function.

**Python mini project:** A small exploratory data analysis script on a real public dataset: load with Pandas, clean it, compute statistics, and produce two or three summary insights. This reinforces the exact NumPy/Pandas/stats skills every later ML stage assumes are already solid.

**Skills gained:** Comfortable manipulating arrays and DataFrames without looking up basic syntax, and can explain probability, correlation, and gradients in plain language.

**What NOT to study yet:** Any ML model training, this phase is data handling and math only, no learning algorithms yet.

**Exit criteria:** Given a new small CSV file, can load it, clean it, and produce basic summary statistics and one visualization within 30 minutes, unaided.

---

## Stage 1 Milestone Challenge

Combine all three phases: take a real small dataset (Pandas/NumPy), formulate one question about it as a formal problem (states/goal/constraints, from Phase 2), and write a one-page explanation connecting it back to where it sits in the AI/ML/deep-learning hierarchy (Phase 1). This proves the three phases connect, not just that each was learned in isolation.

---

## Portfolio Checklist (Stage 1)
- [ ] Written AI/ML/deep-learning explanation with real examples
- [ ] Rule-based grid agent project
- [ ] State-space search solver (maze or 8-puzzle) with a written formulation
- [ ] Exploratory data analysis script on a real dataset
- [ ] Stage 1 milestone write-up connecting all three phases

## Free Learning Resources
- Artificial Intelligence: A Modern Approach (Russell and Norvig), the standard reference for Phase 1 and 2 concepts, read selectively
- NumPy official docs (numpy.org/doc/stable), for Phase 3
- Pandas official docs (pandas.pydata.org/docs), for Phase 3
- 3Blue1Brown's linear algebra and calculus video series (freely available), for visual intuition on Phase 3 math
- Khan Academy probability and statistics, for Phase 3 review

## What Comes Next
Stage 2 and beyond (machine learning fundamentals, then deep learning, then applied AI/LLM engineering) are not covered here and should be requested as their own roadmap once Stage 1's exit criteria are met.
