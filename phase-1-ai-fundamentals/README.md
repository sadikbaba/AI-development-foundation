# Phase 1: AI Fundamentals

## Goal

Understand the core ideas behind Artificial Intelligence before using ML frameworks, neural networks, or AI APIs.

The goal is to understand:

- what AI is
- how agents perceive an environment
- how they make decisions
- how search and heuristics work
- how knowledge and reasoning are represented
- how reinforcement learning differs from rule-based systems

---

## 1. AI, Machine Learning, and Deep Learning

Artificial Intelligence is the broad field of building systems that perform tasks requiring intelligent behavior.

AI can use:

- rules
- search
- planning
- knowledge representation
- reasoning
- machine learning
- deep learning
- reinforcement learning

Machine Learning is part of AI.

It allows systems to learn patterns from data instead of having every rule manually programmed.

Deep Learning is part of Machine Learning.

It uses neural networks with multiple layers.

```text
AI
├── Rule-based systems
├── Search
├── Planning
├── Knowledge representation
├── Reasoning
├── Machine Learning
│   ├── Traditional Machine Learning
│   └── Deep Learning
└── Other approaches
```

---

## 2. Intelligent Agents

An intelligent agent receives information from its environment and chooses actions to achieve a goal.

```text
Environment
    ↓
Percept
    ↓
Agent
    ↓
Decision
    ↓
Action
    ↓
Environment changes
```

Important parts:

- Environment: the world the agent interacts with
- Percept: information received from the environment
- Action: something the agent does
- Agent function: maps percepts to actions

An agent does not need Machine Learning.

A rule-based agent can still be an AI system.

---

## 3. Search

Search means exploring possible states or actions to find a path or solution that reaches a goal.

```text
Start
  ↓
Possible states
  ↓
Possible paths
  ↓
Goal
```

Search does not always mean finding the shortest path.

The objective could be:

- shortest
- cheapest
- safest
- fastest

Actual search algorithms will be studied later.

---

## 4. Heuristics

A heuristic is an estimate that helps guide a search or decision toward a promising option.

Example:

```text
Position A = 10
Position B = 5
Position C = 8
```

If lower is better, the system may prefer Position B.

A heuristic helps reduce unnecessary exploration, but it does not always guarantee the best result.

---

## 5. Planning

Planning means creating a sequence of actions that can achieve a goal.

```text
Current state
    ↓
Action
    ↓
New state
    ↓
Action
    ↓
Goal
```

Difference:

```text
Search:
Which possible path can reach the goal?

Planning:
What sequence of actions should I perform?
```

---

## 6. Decision Making

Decision making means choosing an action from available options.

A decision can depend on:

- goals
- constraints
- cost
- risk
- reward
- expected outcome
- heuristic score

Simple distinction:

```text
Decision:
What should I do now?

Planning:
What sequence of actions should I perform?
```

---

## 7. Knowledge Representation

Knowledge representation is how information is structured so an AI system can use it.

A simple system can use facts and rules.

```text
Fact:
Rex is a dog.

Rule:
If something is a dog,
then it is an animal.
```

---

## 8. Reasoning

Reasoning means using known facts and rules to derive new information.

```text
Rex is a dog
+
Dogs are animals
↓
Rex is an animal
```

Knowledge representation stores the knowledge.

Reasoning uses that knowledge.

---

## 9. Reinforcement Learning

Reinforcement Learning is an approach where an agent learns through interaction with an environment.

```text
Agent
  ↓
Action
  ↓
Environment
  ↓
Reward
  ↓
Agent learns
```

Important parts:

- Agent: the learner
- Environment: what the agent interacts with
- Reward: feedback from an action
- Policy: strategy used to choose actions

Difference from a rule-based system:

```text
Rule-based system:
Developer writes the behavior.

Reinforcement Learning:
Agent learns behavior from rewards and experience.
```

---

# Phase Project

## Rule-Based Grid Agent

The Phase 1 project is a small Python agent that navigates a grid using rules and a Manhattan-distance heuristic.

It deliberately does not use Machine Learning.

Project location:

```text
projects/rule-based-grid-agent/
```

Main file:

```text
projects/rule-based-grid-agent/agent.py
```

Environment:

```text
S . . .
. # . .
. # . .
. . . G
```

Where:

```text
S = start
G = goal
# = obstacle
. = open cell
```

The final agent loop should be:

```text
Perceive
    ↓
Generate possible actions
    ↓
Check boundaries
    ↓
Reject obstacles
    ↓
Keep valid moves
    ↓
Calculate heuristic scores
    ↓
Choose best action
    ↓
Move
    ↓
Update position
    ↓
Track path
    ↓
Goal reached?
    ↓
No: repeat
Yes: stop
```

---

## Current Project Progress

Completed:

- grid environment
- starting position
- goal position
- `(row, column)` position representation
- possible actions
- perception of neighboring cells
- boundary checking
- obstacle checking
- valid-move filtering
- goal checking
- Manhattan-distance heuristic
- heuristic scoring
- best-action selection

Current agent can:

```text
Environment
    ↓
Generate moves
    ↓
Check boundaries
    ↓
Perceive cells
    ↓
Reject obstacles
    ↓
Keep valid moves
    ↓
Score moves
    ↓
Choose best action
```

The agent can decide which move looks best, but it does not move through the grid yet.

---

## Next Steps

1. Update the agent position using `best_action`.
2. Track the path.
3. Repeat the decision process.
4. Stop when `G` is reached.
5. Test the full agent.
6. Refactor the learning version into cleaner functions.

---

## Progress

### Rule-Based Grid Agent

Approximately **75% complete**.

Remaining work:

- movement
- agent loop
- path tracking
- final testing
- refactoring

### Phase 1

Approximately **85% complete**.

The theory is mostly complete.

The main remaining work is:

- finish the Rule-Based Grid Agent
- verify the Phase 1 exit criteria

---

# Exit Criteria

Before finishing Phase 1, I should be able to explain without notes:

- AI vs Machine Learning vs Deep Learning
- intelligent agents
- environment, percepts, and actions
- agent functions
- search
- heuristics
- planning
- decision making
- knowledge representation
- reasoning
- basic Reinforcement Learning
- agent, environment, reward, and policy
- rule-based systems vs Reinforcement Learning

I should also be able to build a simple rule-based agent that moves from `S` to `G`.

The final goal is to look at an AI system and understand:

```text
What does it know?

What does it perceive?

How does it make decisions?

How does it reach its goal?
```