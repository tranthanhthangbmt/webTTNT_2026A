\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Rational decisions

## Chapter 16

---
## Outline

- Rational preferences

- Utilities

- Money

- Multiattribute utilities

- Decision networks

- Value of information

---
## Preferences

An agent chooses among <u>prizes</u> ($A$, $B$, etc.) and 
<u>lotteries</u>, i.e., situations with uncertain prizes

Lottery $L = [p,A;\ (1-p),B]$

 

![Hình ảnh](../TaiLieu/slide_md/figures/lottery.png)

Notation:
  
$A \pref B$  &nbsp;&nbsp;&nbsp;&nbsp;  $A$ preferred to $B$
  
$A \indiff B$  &nbsp;&nbsp;&nbsp;&nbsp;  indifference between $A$ and $B$
  
$A \prefeq B$  &nbsp;&nbsp;&nbsp;&nbsp;  $B$ not preferred to $A$

---
## Rational preferences

Idea: preferences of a rational agent must obey constraints.

Rational preferences $\implies$ 
    
   behavior describable as maximization of expected utility

Constraints:
  
\underline{Orderability}
    
$(A \pref B) \lor (B \pref A) \lor (A \indiff B)$
  
\underline{Transitivity}
    
$(A \pref B) \land (B \pref C) \implies (A \pref C)$
  
\underline{Continuity}
    
$A \pref B \pref C \implies \Exi{p} [p,A;\ 1-p,C] \indiff B$
  
\underline{Substitutability}
    
$A \indiff B \implies [p,A;\ 1-p,C] \indiff [p,B; 1-p,C]$
  
\underline{Monotonicity}
    
$A \pref B \implies (p \geq q \lequiv [p,A;\ 1-p,B] \prefeq [q,A;\ 1-q,B])$

---
## Rational preferences contd.

Violating the constraints leads to self-evident irrationality

For example: an agent with intransitive preferences
can be induced to give away all its money

If $B \pref C$, then an agent who has $C$
would pay (say) 1 cent to get $B$

If $A \pref B$, then an agent who has $B$
would pay (say) 1 cent to get $A$

If $C \pref A$, then an agent who has $A$
would pay (say) 1 cent to get $C$

 

\  &nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp; ![Hình ảnh](../TaiLieu/slide_md/figures/cash-machine.png)

---
## Maximizing expected utility

<u>Theorem</u> (Ramsey, 1931; von Neumann and Morgenstern, 1944):

Given preferences satisfying the constraints

there exists a real-valued function $U$ such that
    
    $U(A) \geq U(B)\ \lequiv \ A\prefeq B$
    
    $U([p_1,S_1;\ \ldots\ ;\ p_n,S_n]) = \mysum_i\ p_i U(S_i)$

<u>MEU principle</u>:
  
Choose the action that maximizes expected utility

Note: an agent can be entirely rational (consistent with MEU)

without ever representing or manipulating utilities and probabilities

E.g., a lookup table for perfect tictactoe

---
## Utilities

Utilities map states to real numbers. Which numbers?

Standard approach to assessment of human utilities:
  
  compare a given state $A$ to a <u>standard lottery</u> $L_p$ that has
    
    "best possible prize" $\ubest$ with probability $p$
    
    "worst possible catastrophe" $\uworst$ with probability $(1-p)$
  
  adjust lottery probability $p$ until $A \indiff L_p$

![Hình ảnh](../TaiLieu/slide_md/figures/micromort.png)

---
## Utility scales

<u>Normalized utilities</u>: $\ubest = 1.0$, $\uworst = 0.0$

<u>Micromorts</u>: one-millionth chance of death
  
  useful for Russian roulette, paying to reduce product risks, etc.

<u>QALYs</u>: quality-adjusted life years
  
  useful for medical decisions involving substantial risk

Note: behavior is <u>invariant</u> w.r.t. +ve linear transformation
\[
  U'(x) = k_1 U(x) + k_2  &nbsp;&nbsp; \mbox{where } k_1 > 0
\]
With deterministic prizes only (no lottery choices), only

<u>ordinal utility</u> can be determined, i.e., total order on prizes

---
## Money

Money does <u>not</u> behave as a utility function

Given a lottery $L$ with expected monetary value $EMV(L)$,

usually $U(L) < U(EMV(L))$, i.e., people are <u>risk-averse</u>

Utility curve: for what probability $p$ am I indifferent between\
a fixed prize $x$ and a lottery $[p,\$M;\ (1-p),\$0]$ for large $M$?

Typical empirical data, extrapolated with <u>risk-prone</u> behavior:

![Hình ảnh](../TaiLieu/slide_md/figures/beard-utility.png)

---
## Student group utility

For each $x$, adjust $p$ until half the class votes for lottery (M=10,000)

![Hình ảnh](../TaiLieu/slide_md/figures/student-utility.png)

---
## Decision networks

Add <u>action nodes</u> and <u>utility</u> nodes to belief networks

to enable rational decision making

![Hình ảnh](../TaiLieu/slide_md/figures/airport-id.png)

Algorithm:
  
  For each value of action node
    
    compute expected value of utility node given action, evidence
  
  Return MEU action

---
## Multiattribute utility

How can we handle utility functions of many variables $X_1\ldots X_n$?

E.g., what is $U(Deaths,Noise,Cost)$?

How can complex utility functions be assessed from 

preference behaviour?

Idea 1: identify conditions under which decisions can be made without
complete identification of $U(x_1,\ldots,x_n)$

Idea 2: identify various types of <u>independence</u> in preferences

and derive consequent canonical forms for $U(x_1,\ldots,x_n)$

---
## Strict dominance

Typically define attributes such that $U$ is <u>monotonic</u> in each

<u>Strict dominance</u>: choice $B$ strictly dominates choice $A$ iff
    
$\All{i} X_i(B) \geq X_i(A)$  &nbsp;&nbsp;  (and hence $U(B) \geq U(A)$)

![Hình ảnh](../TaiLieu/slide_md/figures/strict-dominance.png)

Strict dominance seldom holds in practice

---
## Stochastic dominance

\twograph{graphs/dominance-density.ps}{graphs/dominance-cumulative.ps}

Distribution $p_1$ <u>stochastically dominates</u> distribution $p_2$ iff
    
  $\displaystyle\All{t} \int_{-\infty}^t p_1(x)dx \leq \int_{-\infty}^t p_2(t)dt$

If $U$ is monotonic in $x$, then $A_1$ with outcome distribution $p_1$

stochastically dominates $A_2$ with outcome distribution $p_2$:
    
  $\displaystyle\int_{-\infty}^{\infty} p_1(x) U(x)dx \geq \int_{-\infty}^{\infty} p_2(x) U(x)dx $

Multiattribute case: stochastic dominance on all attributes $\implies$ optimal

---
## Stochastic dominance contd.

Stochastic dominance can often be determined without

exact distributions using <u>qualitative</u> reasoning

E.q., construction cost increases with distance from city
    
      $S_2$ is further from the city than $S_1$
  
  $\implies$ $S_1$ stochastically dominates $S_2$ on cost

E.g., injury increases with collision speed

Can annotate belief networks with stochastic dominance information:
  
  $X \qplus Y$ ($X$ positively influences $Y$) means that
  
  For every value $\mbf{z}$ of $Y$'s other parents $\mbf{Z}$
    
    $\All{x_1,x_2} x_1 \geq x_2 \implies
      P(Y|x_1,\mbf{z})$ stochastically dominates $ P(Y|x_2,\mbf{z})$

---
## Example: car insurance

Which arcs are positive or negative influences?

![Hình ảnh](../TaiLieu/slide_md/figures/insurance-net.png)

---
## Preference structure: Deterministic

$X_1$ and $X_2$ <u>preferentially independent</u> of $X_3$ iff
  
  preference between $\< x_1,x_2,x_3 \>$ and $\< x_1',x_2',x_3 \>$
  
  does not depend on $x_3$

E.g., $\<Noise,Cost,Safety\>$:
  
  $\<$20,000 suffer, \$4.6 billion, 0.06 deaths/mpm$\>$ vs.
  
  $\<$70,000 suffer, \$4.2 billion, 0.06 deaths/mpm$\>$

<u>Theorem</u> (Leontief, 1947): if every pair of attributes is P.I. of its complement,
then every subset of attributes is P.I of its complement: <u>mutual P.I.</u>.

<u>Theorem</u> (Debreu, 1960): mutual P.I. $\implies$ $\exists$ <u>additive</u> value function:
\[
  V(S) = \mysum_i V_i(X_i(S))
\]
Hence assess $n$ single-attribute functions; often a good approximation

---
## Preference structure: Stochastic

Need to consider preferences over lotteries:

$\mbf{X}$ is <u>utility-independent</u> of $\mbf{Y}$ iff
  
  preferences over lotteries $\mbf{X}$ do not depend on $\mbf{y}$

Mutual U.I.: each subset is U.I of its complement

$\implies$ $\exists$ <u>multiplicative</u> utility function:
  
$U  =  k_1U_1 + k_2U_2 + k_3U_3$
    
 + $k_1k_2U_1U_2 + k_2k_3U_2U_3 + k_3k_1U_3U_1$
    
 + $k_1k_2k_3U_1U_2U_3$

Routine procedures and software packages for generating preference
tests to identify various canonical families of utility functions

---
## Value of information

Idea: compute value of acquiring each possible piece of evidence

Can be done <u>directly from decision network</u>

Example: buying oil drilling rights
  
  Two blocks $A$ and $B$, exactly one has oil, worth $k$
  
  Prior probabilities 0.5 each, mutually exclusive
  
  Current price of each block is $k/2$
  
  Consultant offers accurate survey of $A$. Fair price?

Solution: compute expected value of information
  
  = expected value of best action given the information
    
    minus expected value of best action without information

Survey may say "oil in A" or "no oil in A", prob. 0.5 each
  
  = [$0.5 \times {}$ value of "buy A" given "oil in A"
    
    + $0.5 \times {}$ value of "buy B" given "no oil in A"]
    
    -- 0
  
  = $(0.5 \times k/2) + (0.5 \times k/2) - 0 = k/2$

---
## General formula

Current evidence $E$, current best action $
  pha$

Possible action outcomes $S_i$, potential new evidence $E_j$
\[
  EU(
  pha|E) = \max_{a} \mysum_i\ U(S_i)\;P(S_i|E,a)
\]
Suppose we knew $E_j \eq e_{jk}$, then we would choose $
  pha_{e_{jk}}$ s.t.
\[
  EU(
  pha_{e_{jk}}|E,E_j \eq e_{jk}) = \max_a \mysum_i\ U(S_i)\;P(S_i|E,a,E_j \eq e_{jk})
\]
$E_j$ is a random variable whose value is {\it currently} unknown

$\implies$ must compute expected gain over all possible values:
\[
VPI_{E}(E_j) = \left(\mysum_k\ P(E_j \eq e_{jk}|E)
EU(
  pha_{e_{jk}}|E,E_j \eq e_{jk})\right) - EU(
  pha|E) 
\]
(VPI = value of perfect information)

---
## Properties of VPI

<u>Nonnegative</u>---in *expectation*, not *post hoc*
\[
\All{j,E} VPI_{E}(E_j)\geq 0\
\]
<u>Nonadditive</u>---consider, e.g., obtaining $E_j$ twice
\[
VPI_{E}(E_j,E_k) \not= VPI_{E}(E_j) + VPI_{E}(E_k)
\]
<u>Order-independent</u>
\[
VPI_{E}(E_j,E_k) = VPI_{E}(E_j) + VPI_{E,E_j}(E_k)
                   = VPI_{E}(E_k) + VPI_{E,E_k}(E_j) 
\]
Note: when more than one piece of evidence can be gathered,

maximizing VPI for each to select one is not always optimal

$\implies$ evidence-gathering becomes a <u>sequential</u> decision problem

---
## Qualitative behaviors

a) Choice is obvious, information worth little

b) Choice is nonobvious, information worth a lot

c) Choice is nonobvious, information worth little

 

![Hình ảnh](../TaiLieu/slide_md/figures/3cases.png)