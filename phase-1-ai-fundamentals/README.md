# Phase 1: AI Fundamentals

## Goal

Understand the core ideas behind Artificial Intelligence before using ML frameworks, neural networks, or AI APIs.

The goal is to understand how AI systems:

- perceive an environment
- represent information
- evaluate possible actions
- make decisions
- work toward goals
- learn in systems such as Reinforcement Learning

---

## 1. AI, Machine Learning, and Deep Learning

Artificial Intelligence is the broad field of building systems that perform tasks requiring intelligent behavior.

AI can use:

- rules
- search
- planning
- reasoning
- knowledge representation
- Machine Learning
- Deep Learning
- Reinforcement Learning

Machine Learning is part of AI and allows systems to learn patterns from data.

Deep Learning is part of Machine Learning and uses neural networks with multiple layers.

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

Not every AI system uses Machine Learning.

---

## 2. Intelligent Agents

An intelligent agent receives information from an environment and chooses actions to achieve a goal.

Important parts:

- Environment: the world the agent interacts with
- Percept: information received from the environment
- Action: something the agent does
- Agent function: maps information to actions

A rule-based system can still be an intelligent agent.

---

## 3. Search

Search means exploring possible states or actions to find a solution that reaches a goal.

A search objective might be finding a solution that is:

- shortest
- cheapest
- safest
- fastest

Actual search algorithms are studied later.

---

## 4. Heuristics

A heuristic is an estimate that helps guide a system toward a promising option.

A heuristic can make decision making more efficient, but it does not automatically guarantee the best possible solution.

The Phase 1 project uses **Manhattan distance** as its heuristic.

---

## 5. Planning

Planning means creating a sequence of actions that can achieve a goal.

```text
Search:
Which possible path can reach the goal?

Planning:
What sequence of actions should I perform?
```

---

## 6. Decision Making

Decision making means choosing an action from available options.

A decision may depend on:

- goals
- constraints
- cost
- risk
- reward
- expected outcome
- heuristic score

```text
Decision:
What should I do now?

Planning:
What sequence of actions should I perform?
```

---

## 7. Knowledge Representation

Knowledge representation describes how information is structured so an AI system can use it.

A simple representation can contain facts and rules.

```text
Fact:
Rex is a dog.

Rule:
If something is a dog,
then it is an animal.
```

---

## 8. Reasoning

Reasoning means using known information and rules to derive new information.

```text
Rex is a dog
+
Dogs are animals

Result:
Rex is an animal
```

Knowledge representation stores knowledge.

Reasoning uses that knowledge.

---

## 9. Reinforcement Learning

Reinforcement Learning is an approach where an agent learns through interaction with an environment.

Important parts:

- Agent: the learner
- Environment: what the agent interacts with
- Reward: feedback from an action
- Policy: strategy used to choose actions

```text
Rule-based system:
Developer programs the behavior.

Reinforcement Learning:
Agent learns behavior through rewards and experience.
```

---

# Phase Project

## Rule-Based Grid Agent

The Phase 1 project is a small Python agent that navigates a grid using rules and a Manhattan-distance heuristic.

It deliberately does not use Machine Learning.

Project:

```text
projects/rule-based-grid-agent/
```

Main implementation:

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

---

## Agent Design

The project is organized into small functions with clear responsibilities.

```text
get_possible_moves()
Generate possible actions.

is_in_bounds()
Check whether a position exists inside the grid.

is_valid_move()
Reject positions outside the grid or blocked by obstacles.

get_valid_moves()
Keep only usable actions.

heuristic()
Calculate Manhattan distance to the goal.

choose_best_move()
Choose the valid action with the lowest heuristic score.

move_agent()
Return the position belonging to the chosen action.

is_goal()
Check whether the agent reached the goal.

run_agent()
Control the complete agent cycle.
```

---

## Agent Cycle

The completed agent performs this process repeatedly:

```text
Current position
    |
Generate possible moves
    |
Check boundaries and obstacles
    |
Keep valid moves
    |
Calculate heuristic scores
    |
Choose best move
    |
Move
    |
Update current position
    |
Track path
    |
Check goal
    |
Repeat until goal
```

The agent now moves from `S` toward `G`, avoids obstacles, records its path, and stops when the goal is reached.

---

## What This Project Reinforces

The project connects the main Phase 1 concepts:

- intelligent agents
- environment
- percepts
- actions
- state representation
- rules
- heuristics
- decision making
- goal checking
- repeated agent behavior

It also demonstrates an important idea:

**AI does not automatically mean Machine Learning.**

This agent performs goal-directed behavior using ordinary Python rules and a heuristic.

---

# Progress

## Rule-Based Grid Agent

Approximately **95% complete**.

The core agent is complete:

- environment
- current state
- possible actions
- boundary checking
- obstacle checking
- valid-action filtering
- Manhattan-distance heuristic
- decision making
- movement
- path tracking
- agent loop
- goal detection
- organized function structure

Remaining work:

- final testing
- handle the case where no valid move exists
- optional cleanup after testing

---

## Phase 1

Approximately **95% complete**.

The theory has been studied and the Phase 1 project is functionally complete.

The remaining work is mainly:

- final project verification
- Phase 1 retrieval test
- verify the exit criteria without relying on notes

---

# Exit Criteria

Before completing Phase 1, I should be able to explain without notes:

- AI vs Machine Learning vs Deep Learning
- intelligent agents
- environments, percepts, and actions
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

I should also understand how the Rule-Based Grid Agent:

- represents its environment
- represents its current state
- generates actions
- rejects invalid actions
- evaluates valid actions
- chooses a move
- updates its state
- records its path
- repeats until reaching its goal

The final objective is to look at an AI system and understand:

```text
What does it know?

What does it perceive?

What actions can it take?

How does it choose an action?

How does it know when its goal has been reached?
```