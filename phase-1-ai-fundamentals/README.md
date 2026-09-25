# Phase 1: AI Fundamentals

## Goal

Understand what Artificial Intelligence means, how AI systems perceive their environment, make decisions, reason, and solve problems.

The goal of this phase is not to memorize AI terminology.

It is to build a mental model that makes later topics such as Machine Learning, Deep Learning, and AI systems easier to understand.

---

# 1. AI, Machine Learning, and Deep Learning

## What is AI?

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

## What is Machine Learning?

Machine Learning (ML) is an approach within AI where a system learns patterns or relationships from data instead of having every rule manually written by the programmer.

For example, a decision tree can be trained using examples of previous customers and learn patterns that help it make predictions about new customers.

The important part is that the system **learns from data**.

## What is Deep Learning?

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

## How are they related?

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

## Real examples

### Rule-based heater

```text
IF temperature < 18°C
→ turn heater on
```

This can be AI because the system is using programmed rules to make decisions.

It does not have to use machine learning.

### Trained decision tree

A decision tree trained using examples is machine learning.

It is also AI because machine learning is part of AI.

### Deep neural network for image recognition

A neural network with many layers trained on a collection of images is deep learning.

Therefore it is also machine learning and AI.

## Important distinction

Not every system that recognizes patterns is automatically deep learning.

A system can perform tasks such as recognizing handwritten digits using traditional machine learning methods without using a deep neural network.

What makes something deep learning is the use of deep neural networks.

---

# 2. Intelligent Agents

## What is an agent?

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

## Environment

The environment is everything outside the agent that the agent interacts with.

For a robot vacuum, the environment could include:

* Floor
* Walls
* Furniture
* Dirt
* People
* Obstacles
* Charging station

For a chess-playing program, the environment is the current game state, including the board and pieces.

## Percepts

A percept is the information an agent receives from its environment at a particular moment.

For example, a robot vacuum might receive:

```text
Dirt detected
Wall detected
Battery = 8%
Obstacle detected
```

A percept is **information received by the agent**, not the decision the agent makes.

## Actions

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

## Agent function

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

The agent function is not the action itself.

It is the mapping that connects the information the agent receives to the action it should choose.

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

This is not machine learning.

The behavior has been explicitly programmed by the developer.

## Example

Consider a robot moving through a room.

Its sensor detects a wall 30 cm ahead.

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

# 3. Search

## What is search?

In AI, search means exploring possible actions or states to find a path or solution that reaches a goal.

For example, imagine an agent starts at `A` and wants to reach `G`.

```text
A → B → D → G

A → C → E → G
```

The agent has multiple possible paths.

Search is the process of exploring those possibilities to find a path toward the goal.

## Why AI needs search

Many problems do not have one obvious action.

An agent may have:

* A starting situation
* Several possible actions
* Different states that result from those actions
* A goal it wants to reach

Search allows the agent to explore those possibilities.

For example:

* A robot navigating a maze
* A puzzle-solving system
* A game-playing system
* A route-finding system

Search is useful whenever there are multiple possible choices and the system needs to explore them.

## Search space

The **search space** is the collection of possible states and transitions that the system can explore while solving a problem.

For example:

```text
        B
       / \
Start A   D → Goal
       \ /
        C
```

The system can explore different paths from the starting state toward the goal.

Search does not necessarily mean finding the shortest path.

It means exploring possibilities to find a solution that reaches the goal.

Whether we want the shortest, cheapest, safest, or fastest solution depends on the problem.

The actual search algorithms will be studied later.

---

# 4. Heuristics

## What is a heuristic?

A heuristic is an estimate or rule that helps guide a search or decision toward a promising option.

It does not guarantee that the chosen option is actually the best one.

For example, if an agent wants to reach a goal, it could estimate how far each available position is from the goal.

```text
Position A → estimated distance: 10
Position B → estimated distance: 5
Position C → estimated distance: 8
```

The agent may prefer B because it appears closer to the goal.

## Why use one?

Without guidance, a system may have to explore many possible options.

A heuristic helps prioritize options that appear more promising.

This can reduce unnecessary exploration and make problem solving faster.

The important distinction is:

```text
Search
= explores possibilities

Heuristic
= helps guide that exploration
```

A heuristic does not perform the search by itself.

## What do we give up?

A heuristic is an estimate, so it can be wrong.

An option that looks promising may turn out to be worse because of an obstacle, cost, or another factor that the estimate did not account for.

This creates an important trade-off:

```text
Better guidance
      ↓
Less unnecessary exploration
      ↓
Potentially faster problem solving
```

But the quality of the result depends on the search method and the heuristic being used.

---

# 5. Planning

## What is planning?

Planning is creating a sequence of actions that can achieve a goal from a current situation while considering the effects and dependencies of those actions.

A simple representation is:

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

For example, making tea requires several actions that depend on one another:

```text
Get cup
   ↓
Prepare tea
   ↓
Boil water
   ↓
Pour water
   ↓
Finish tea
```

Planning is concerned with deciding what sequence of actions should be performed to reach the desired goal.

## Planning vs search

Search explores possible paths or states to find a solution.

Planning focuses on constructing a sequence of actions that achieves a goal while considering the current state and the effects of those actions.

They can overlap because a planning system may use search to find a suitable action sequence.

```text
Search:
Which possible path can reach the goal?

Planning:
What sequence of actions should I perform to reach the goal?
```

---

# 6. Decision Making

Decision making is choosing an action from available options based on goals, information, constraints, expected outcomes, cost, risk, or other factors.

For example, a delivery robot may have several possible routes:

```text
Route A → shorter but blocked
Route B → longer but clear
Route C → dangerous
```

The robot needs to choose an action based on the information available to it.

The distinction from planning is:

```text
Decision:
What should I do now?

Planning:
What sequence of actions should I perform to achieve the goal?
```

A heuristic can also help with decision making by providing an estimate about which option appears more promising.

---

# 7. Knowledge Representation

Knowledge representation is the way knowledge is structured and stored so that an AI system can use it for reasoning and decision making.

A simple representation can contain facts and rules.

```text
Fact:
Rex is a dog.

Rule:
If something is a dog,
then it is an animal.
```

The system can use the rule with the known fact to derive new knowledge:

```text
Rex is a dog
      +
Dogs are animals
      ↓
Rex is an animal
```

Knowledge representation is therefore about structuring knowledge in a form that a system can use.

It is not simply giving an AI access to a website or external source.

A source can provide information, while knowledge representation describes how that information is structured for use by the system.

---

# 8. Reasoning

Reasoning is the process of using known information and rules to derive a conclusion or new knowledge.

For example:

```text
Fact:
Lagos is in Nigeria.

Fact:
Nigeria is in Africa.

Rule:
If a city is in a country
and that country is in a continent,
then the city is in that continent.
```

Reasoning produces:

```text
Lagos is in Africa.
```

The important distinction is:

```text
Knowledge Representation
        ↓
Facts + Rules
        ↓
Reasoning
        ↓
New Knowledge
        ↓
Decision / Action
```

Knowledge representation structures the knowledge.

Reasoning uses that knowledge to derive conclusions.

---

# 9. Reinforcement Learning

Reinforcement Learning (RL) is an approach where an agent learns how to make decisions by interacting with an environment and receiving feedback through rewards or penalties.

The basic loop is:

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

The agent learns from experience rather than having every desired behavior explicitly written as a rule.

## Agent

The agent is the learner or decision maker.

Examples include:

* A robot
* A game-playing program
* An autonomous system

The agent chooses actions.

## Environment

The environment is everything the agent interacts with.

For a robot navigating a maze, the environment can include:

* Walls
* Floor
* Paths
* Goal
* Current state of the maze

## Reward

A reward is feedback about the outcome of an action.

For example:

```text
Reach goal       → +100
Move toward goal → +5
Hit wall         → -10
Move away        → -5
```

The exact values depend on how the problem is designed.

The important idea is that rewards provide feedback that helps the agent learn which behaviors tend to produce better outcomes.

## Policy

A policy is the strategy an agent uses to choose an action given its current situation.

In simple form:

```text
Situation
    ↓
Policy
    ↓
Action
```

In reinforcement learning, the policy can be learned through interaction and experience rather than being completely programmed by hand.

## How this differs from ordinary rule-based systems

A rule-based system might explicitly contain:

```text
IF wall detected
THEN turn right
```

The developer specifies the behavior.

In reinforcement learning:

```text
Agent
  ↓
Takes actions
  ↓
Receives rewards
  ↓
Learns from experience
  ↓
Improves its decisions
```

Reinforcement learning does not mean the system learns without any human-designed structure.

Humans still define important parts of the problem, such as the environment, available actions, and reward system.

---

# Phase Project

## Rule-Based Grid Agent

The project for this phase is a small Python agent that navigates a grid using rules and a simple heuristic.

The project will deliberately **not use machine learning**.

The agent will have:

* A starting position
* A goal
* Obstacles
* Available movements
* Percepts about its surroundings
* Rules for choosing actions
* A simple heuristic for moving toward the goal

A simplified environment might look like:

```text
S . . .
. # . .
. # . .
. . . G
```

Where:

```text
S = starting position
G = goal
# = obstacle
. = open space
```

The agent will repeatedly:

```text
Perceive
   ↓
Check possible actions
   ↓
Apply rules
   ↓
Use heuristic
   ↓
Choose an action
   ↓
Move
   ↓
Repeat
```

The project is intended to connect the concepts from this phase rather than introduce advanced search algorithms.

Real search algorithms such as BFS, DFS, and A* will be studied later in Phase 2.

## What this project teaches

This project reinforces:

* Intelligent agents
* Environment
* Percepts
* Actions
* Agent function
* Reasoning
* Decision making
* Heuristics
* State representation
* Goal-oriented behavior

It also demonstrates an important point:

**AI does not automatically mean machine learning.**

A system can display intelligent behavior using rules, representations, reasoning, search, planning, or other approaches.

---

# Exit Criteria

By the end of this phase, I should be able to:

* Explain AI, Machine Learning, and Deep Learning clearly.
* Explain how AI, ML, and DL relate to one another.
* Explain what an intelligent agent is.
* Identify an agent, environment, percept, and action.
* Explain what an agent function does.
* Explain search without confusing it with planning.
* Explain what a heuristic does and why it is useful.
* Explain the difference between planning and decision making.
* Explain basic knowledge representation using facts and rules.
* Explain reasoning as deriving conclusions from known information and rules.
* Explain the basic reinforcement learning idea.
* Explain the roles of agent, environment, reward, and policy in reinforcement learning.
* Distinguish a rule-based system from a reinforcement learning system.
* Build a simple rule-based agent that navigates a grid.

The final goal is not to memorize definitions.

The goal is to look at an AI system and understand **what it knows, what it perceives, how it makes decisions, and how it reaches its goal.**
