\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Complex decisions

## Chapter 17, Sections 1--3

---
## Outline

- Decision problems

- Value iteration

- Policy iteration

---
## Sequential decision problems

![Hình ảnh](../TaiLieu/slide_md/figures/decision-problems.png)

---
## Example MDP

![Hình ảnh](../TaiLieu/slide_md/figures/sequential-decision-world.png)\hspace*{1in}

![Hình ảnh](../TaiLieu/slide_md/figures/sequential-decision-model.png)

Model $M_{ij}^a \equiv P(j|i,a)$ = probability that doing $a$ in $i$ leads to $j$

Each state has a *reward* $R(i)$
    
   = -0.04 (small penalty) for nonterminal states
    
   = $\pm 1$ for terminal states

---
## Solving MDPs

In search problems, aim is to find an optimal *sequence*

In MDPs, aim is to find an optimal *policy*
    
   i.e., best action for every possible state
    
   (because can't predict where one will end up)

Optimal policy and state values for the given $R(i)$:

\twofig{figures/sequential-decision-policy.ps}
{figures/sequential-decision-values.ps}

---
## Utility

In *sequential* decision problems, preferences are expressed

between *sequences* of states

Usually use an *additive* utility function:
    
$U([s_1,s_2,s_3,\ldots,s_n]) = R(s_1) + R(s_2) + R(s_3) + \cdots + R(s_n)$

(cf. path cost in search problems)

Utility of a *state* (a.k.a. its *value*) is defined to be
    
$U(s_i) = {}$ <u>expected sum of rewards until termination</u>
    
\phantom{$U(s_i) = {}$} <u>assuming optimal actions</u>

Given the utilities of the states, choosing the
best action is just MEU: choose the action such that the
expected utility of the immediate successors is highest.

---
## Bellman equation

Definition of utility of states leads to a simple relationship among
utilities of neighboring states:

<u>expected sum of rewards</u>
  
= <u>current reward</u>
    
+ <u>expected sum of rewards after taking best action</u>

Bellman equation (1957):
\[ U(i) = R(i) + \max_a \mysum_j U(j) M_{ij}^a\]

$U(1,1) = -0.04$

\tab + $\max\{ 0.8 U(1,2) + 0.1 U(2,1) + 0.1 U(1,1),$*up*

\tab \phantom{+ \mbox{$\max\{$}}$0.9 U(1,1) + 0.1 U(1,2) $*left*

\tab \phantom{+ \mbox{$\max\{$}}$0.9 U(1,1) + 0.1 U(2,1) $*down*

\tab \phantom{+ \mbox{$\max\{$}}$0.8 U(2,1) + 0.1 U(1,2) + 0.1 U(1,1) \}$*right*

One equation per state = $n$ <u>nonlinear</u> equations in $n$ unknowns

---
## Value iteration algorithm

<u>Idea</u>: Start with arbitrary utility values
    
          Update to make them <u>locally consistent</u> with Bellman eqn.
    
          Everywhere locally consistent $\Rightarrow$ global optimality

repeat until "no change"
\[ U(i) \leftarrow R(i) + \max_a \mysum_j U(j) M_{ij}^a  &nbsp;&nbsp;&nbsp;&nbsp;  \mbox{for all } i\]

![Hình ảnh](../TaiLieu/slide_md/figures/4x3-vi-curve.png)

---
## Policy iteration (Howard, 1960)

Idea: search for optimal policy and utility values simultaneously

Algorithm:
  
  $\pi \leftarrow {}$ an arbitrary initial policy
  
  repeat until no change in $\pi$
    
    compute utilities given $\pi$
    
    update $\pi$ as if utilities were correct (i.e., local MEU)

To compute utilities given a fixed $\pi$:
\[ U(i) = R(i) + \mysum_j U(j) M_{ij}^{\pi(i)} &nbsp;&nbsp;&nbsp;&nbsp;  \mbox{for all } i \]
i.e., $n$ simultaneous <u>linear</u> equations in $n$ unknowns,
solve in $O(n^3)$

---
## What if I live forever? (digression)

Using the additive definition of utilities, $U(i)$s are infinite!

Moreover, value iteration fails to terminate

How should we compare two infinite lifetimes?

1) Discounting: future rewards are discounted at rate $\gamma \leq 1$
\[ U([s_0,\ldots s_{\infty}]) = \mysum_{t=0}^{\infty} \gamma^t R(s_t)\]
Maximum utility bounded above by $R_{{\rm max}}/(1-\gamma)$

Smaller $\gamma \Rightarrow {}$ shorter horizon

2) Maximize <u>system gain</u> = average reward per time step

Theorem: optimal policy has constant gain after initial transient

E.g., taxi driver's daily scheme cruising for passengers