# Phase 1: AI Fundamentals

## Goal

Understand what Artificial Intelligence means, how AI systems perceive their environment, make decisions, and solve problems.

---

## 1. AI, Machine Learning, and Deep Learning

### What is AI?

Artificial Intelligence (AI) is the field of building computer systems that can perform tasks that require some form of intelligent behavior.

AI is the broad idea. It is not limited to machine learning or neural networks.

An AI system can use:

* Rules
* Search
* Planning
* Knowledge representation
* Reasoning
* Machine learning
* Deep learning
* Reinforcement learning

For example, a simple program that follows rules to control a robot can be an AI system even though it does not learn from data.

### What is Machine Learning?

Machine Learning (ML) is an approach within AI where a system learns patterns or relationships from data instead of having every rule manually written by the programmer.

For example, a decision tree can be trained using examples of previous customers and learn patterns that help it make predictions about new customers.

The important part is that the system **learns from data**.

### What is Deep Learning?

Deep Learning (DL) is a subset of machine learning that uses neural networks with multiple layers.

A neural network is a machine learning model made of connected computational units that perform mathematical calculations using adjustable values called weights.

During training, the network:

1. Receives input data.
2. Produces a prediction.
3. Compares the prediction with the correct answer.
4. Measures the error.
5. Adjusts its weights.
6. Repeats the process to improve.

"Deep" refers to using multiple layers in the neural network.

A simplified example of image recognition might look like:

```text
Pixels
  ↓
Simple patterns
  ↓
Edges and shapes
  ↓
More complex parts
  ↓
Object representation
  ↓
Prediction
```

### How are they related?

AI is the broad field.

Machine Learning is one approach used within AI.

Deep Learning is a type of Machine Learning.

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

They are therefore related, but they are not interchangeable terms.

### Real examples

**Rule-based heater**

```text
IF temperature < 18°C
→ turn heater on
```

This can be AI because the system is using programmed rules to make decisions. It does not have to use machine learning.

**Trained decision tree**

A decision tree trained using examples is machine learning. It is also AI because machine learning is part of AI.

**Deep neural network for image recognition**

A neural network with many layers trained on a large collection of images is deep learning. Therefore it is also machine learning and AI.

### Important distinction

Not every system that recognizes patterns is automatically deep learning.

A system can perform tasks such as recognizing handwritten digits using traditional machine learning methods without using a deep neural network.

What makes something **deep learning** is the use of deep neural networks.

---

## 2. Intelligent Agents

### What is an agent?

An intelligent agent is a system that receives information from its environment and chooses actions based on that information to achieve a goal.

A simple agent loop is:

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
    ↓
New percept
```

An agent does not need to be conscious or human-like.

It also does not have to use machine learning.

A rule-based robot can still be an AI agent.

### Environment

The environment is everything outside the agent that the agent interacts with.

For a robot vacuum, the environment could include:

* Floor
* Walls
* Furniture
* Dirt
* People
* Obstacles
* Charging station

For a chess-playing program, the environment is the game state, including the board and pieces.

### Percepts

A percept is the information an agent receives from its environment at a particular moment.

For example, a robot vacuum might receive:

```text
Dirt detected
Wall detected
Battery = 8%
Obstacle detected
```

A percept is **information received by the agent**, not the decision the agent makes.

### Actions

An action is something the agent does in response to its information.

For a robot vacuum, possible actions include:

```text
Clean
Move forward
Turn left
Turn right
Return to charger
```

The distinction is:

```text
Percept: Wall detected
Decision: Turn left
Action: Turn left
```

### Agent function

An agent function maps a percept, or percept history, to the action the agent should take.

In simple form:

```text
Percept → Agent Function → Action
```

For example:

```text
Dirt detected
→ Clean

Wall detected
→ Turn right

Battery below 10%
→ Return to charger
```

The agent function is not the action itself. It is the mapping that connects the information the agent receives to the action it should choose.

In simple words:

> "When I receive this information, what should I do?"

An agent function can be implemented using ordinary programming rules:

```python
def agent(percept):
    if percept == "dirt":
        return "clean"

    if percept == "wall":
        return "turn_right"

    if percept == "low_battery":
        return "return_to_charger"
```

This is not machine learning. The behavior has been explicitly programmed by the developer.

### Example

Consider a robot moving through a room.

Its sensor detects a wall 30 cm ahead.

The robot decides that turning left is safer and then turns left.

```text
Environment:
Room with a wall

Percept:
Wall detected 30 cm ahead

Decision:
Turn left

Action:
Turn left
```

The agent receives information from the environment, processes that information, chooses an action, and affects the environment.

---

## 3. Search

### What is search?

In AI, search means exploring possible actions or states to find a path or solution that reaches a goal.

For example, imagine an agent starts at `A` and wants to reach `G`.

```text
A → B → D → G
A → C → E → G
```

The agent has multiple possible paths.

Search is the process of exploring those possibilities to find a path toward the goal.

### Why AI needs search

Many problems do not have one obvious action.

An agent may have:

* A starting situation
* Several possible actions
* Different states that result from those actions
* A goal it wants to reach

Search allows the agent to explore those possibilities.

For example, a robot trying to navigate a maze needs to consider different movements until it finds a way to the destination.

A puzzle-solving system may explore different moves until it reaches the desired puzzle state.

A game-playing system may explore possible moves before choosing one.

### Search space

The **search space** is the collection of possible states and transitions that the system can explore while solving a problem.

For example:

```text
        B
       / \
Start A   D → Goal
       \ /
        C
```

Here, the system can explore different paths from the starting state toward the goal.

Search does not necessarily mean finding the shortest path.

It simply means exploring possibilities to find a solution that reaches the goal.

Whether we want the shortest, cheapest, safest, or fastest solution depends on the problem.

---

## 4. Heuristics

### What is a heuristic?

### Why use one?

### What do we give up?

---

## 5. Planning

### What is planning?

### Planning vs search

---

## 6. Decision Making

---

## 7. Knowledge Representation

---

## 8. Reasoning

---

## 9. Reinforcement Learning

### Agent

### Environment

### Reward

### Policy

### How this differs from ordinary rule-based systems

---

## Phase Project

### Rule-Based Grid Agent

---

### What this project teaches

---

## Exit Criteria

By the end of this phase, I should be able to:

* Explain AI, ML, and Deep Learning clearly.
* Explain what an intelligent agent is.
* Explain search without confusing it with planning.
* Explain what a heuristic does.
* Explain basic reasoning and knowledge representation.
* Explain the basic reinforcement learning idea.
