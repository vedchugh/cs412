---
tags: ['CS 412: Introduction to Data Mining', school]
title: 'CS 412: Data Mining'
created: '2020-01-29T17:51:52.498Z'
modified: '2020-02-26T06:13:34.425Z'
---

# CS 412: Data Mining
---
## Week 1

Notes:

 - The Apriori Algorithm
https://www.hackerearth.com/blog/developers/beginners-tutorial-apriori-algorithm-data-mining-r-implementation
Apriori algorithm is a classical algorithm in data mining. It is used for mining frequent itemsets and relevant association rules. It is devised to operate on a database containing a lot of transactions, for instance, items brought by customers in a store.

- Mining Frequent Patterns by Exploring Vertical Data Format
- FPGrowth
- Closed Pattern: Lossless compression 
Closet+

- [Support/Confidence](https://www.quora.com/What-is-support-and-confidence-in-data-mining#)

## Week 2

- 3.1. Limitation of the Support-Confidence Framework
  - Not all patterns/rules are interesting 
  - Objective: Support and correlation. 
  - Subjective: Relevant to users request. 
  - Data may give wrong results/correlations. 

- 3.2. Interestingness Measures: Lift and χ2
  - Lift: Measure of dependent/correlated events: A measure of the performance of a targeting model (association rule) at predicting or classifying cases as having an enhanced response (with respect to the population as a whole), measured against a random choice targeting model.
  
  - χ2: A way to test correlated events
  - Formula: https://www.youtube.com/watch?v=ZUGKFoHUHQI and https://www.mathsisfun.com/data/chi-square-test.html


- 3.3. Null Invariance Measures
  - null-invariance: value does not change with the # of null-transactions. 
  - Can be crucial for analysis of massive transactions. Many transactions may contain neither milk nor coffee. 
  - Null invariance implies no effect of null transactions on deciding the correlation between variables.


- 4.1. Mining Multi-Level Associations
  - items have hierarchies 
  - how to set min-support? same for all levels? Levels with lowered reduced. 
  - if high level support rules derived lower ones, then the lower ones are redundant.
  - can also group based on items. diamonds, gold, milk. 

- 4.2. Mining Multi-Dimensional Associations
  - single-dim like items are all products. 
  - multi-dim like 16-20 buys popcorn buys coke
  - items with multple categories(gender, profession, role) or numbers(age, size)

- 4.3. Mining Quantitative Associations
  - Age and salary. 
  - Can be bined for best results
  - can be used to mine for intersting data rules. Ex: gender = female => wage: mean=7/hour (overall mean = 9)

- 4.4. Mining Negative Correlations
  - Rare patterns. Set a low support. Role watches
  - Nevatige patterns: Unlikely to happen together. Ex. Person buys a Ford (truck) and a Ford Fusion (hybrid) car. 
  - Lift can be used to define negatively correlated events. Small datasets.
  - Be careful of null transactions when setting rules. 
  - Kulczynski can be used to measure negative correlated events. Larger datasets. 
  
- 4.5. Mining Compressed Patterns
  - Many scattered patterns are not useful. 
  - Use a distance function to measure similarly. 
  - Create clusters based on distance. 
  - Close support and item-set. 
  - The set of transaction for pattern "abcd" is {T1, T3, T4}. The set of transaction for pattern "abde" is {T1, T2, T3}. The distance is calculated as 1-2/4 = 0.5
  - Redundancy aware Top K Patterns with Maximal Marginal Significance. 
  

## Quiz 2a
1. Suppose a school collected some data on students' preference for hot dogs(HD) vs. hamburgers(HM). We have the following 2×2 contingency table summarizing the statistics. If lift is used to measure the correlation between HD and HM, what is the value for lift(HD, HM)? A. 1
1. Suppose Coursera collected statistics on the number of students who take courses on data mining (DM) and machine learning (ML). We have the following 2×2 contingency table summarizing the statistics. If lift is used to measure the correlation between DM and ML, what is the value for lift(DM, ML)? 7/4
2. Suppose a school collected some data on students’ preference for hot dogs (HD) vs. hamburgers (HM). We have the following 2×2 contingency table summarizing the statistics. If χ2 is used to measure the correlation between HD and HM, what is the χ2 score? A. 0
3. What is the value range of the χ2 measure? A. 0 to +infinity
3. What is the value range of the Kulczynski measure? 0 to 1
4. Which of the following measures is NOT null invariant? chi squared since they are considered. 
4. Which of the following measures is NOT null invariant? lyft
5. <p>χ<sup>2</sup>1 = χ<sup>2</sup>2, c<sub>1</sub>≠ c<sub>2</sub></p>
5. Suppose we are interested in analyzing the transaction history of several supermarkets with respect to the purchase of apples (A) and bananas (B). We have the following table summarizing the transactions. A. cosine, kulcyzynski,lift

## Quiz 2b
1. Suppose one needs to frequent patterns at two different levels, with mini-support (minsup) of 5% (higher level) and 3% (lower level), respectively. If using shared multi-level mining, which mini-support (minsup) threshold should be used to generate candidate patterns for the lower level? A. 3%
2. A store had 100,000 total transactions in Q4 2014. 10,000 transactions contained eggs, while 5,000 contained bacon. 2,000 transactions contained both eggs and bacon. Which of the following choices for the value of ε is the smallest such that {eggs, bacon} is considered a negative pattern under the null-invariant definition? A. .5
3. Below is a table of transactions. According to the introduced pattern distance measure, what is the distance between pattern "abcd" and pattern "acde"? A. .25
4. Given the itemsets in table 1, which of the following patterns are in the δ-cluster containing the pattern {A, C, E, S} for δ = 0.0001? A. {F,A,C,E,S}

## Week 3
- 5.1. Sequential Pattern and Sequential Pattern Mining
  - Shopping sequences
  - time series databases
  - weblog click streams
  - Sequential pattern mining: Give a set of sequences, find the complete set of frequent subsequences. 
  - Gapped: Gaps allowed
  - non-gapped: No gaps allowed
  
- 5.2. GSP: Apriori-Based Sequential Pattern Mining
  - Get all candidates then count support for each, remove those with lower min-support. 

- 5.3. SPADE – Sequential Pattern Mining in Vertical Data Format
  - Similar to vertical format

- 5.4. PrefixSpan – Sequential Pattern Mining by Pattern-Growth
  - Prefix: Anything in front
  - Suffix: Anything after the prexi
  - Major cost of PrefixSpan: Constructing projected DBs. 
  
- 5.5. CloSpan – Mining Closed Sequential Patterns
  - A closed sequential pattern: There exists no superpatterns. 
  - Why mine for closed sequential patterns? 
  - Explore backward subpattern and backward superpattern for pruning redundant search. 

- 6.1. Graph Pattern and Graph Pattern Mining
  - Gene networks, protein network
  - Social networks, web communities 
  - Computer networks
  - Web graphs

- 6.2. Apriori-Based Graph Pattern Mining Methods
  - Anti-monotonicity: A size k subgraph is frequent if and only if all of its subgraphs are frequent. 
  - Mining process: Candidate-generation -> 
  - Breadth-search: Apriori joining two size-k graphs. 
  - AGM
  - FSG 
  
- 6.3. gSpan: A Pattern-Growth-Based Method
  - Pattern growth approach 
  - Depth-first growth of subgraphs from k-edge to k+1 edge then k+2 subgraphs. 
  - Major challange: Generating lots of duplicates
  - GSpan algo, right most path extension is subgraph pattern growth. 
- 6.4. CloseGraph: Mining Closed Graph Patterns
  -  A graph g is closed in a database if there exists no proper supergraph of g that has the same support as g. A closed graph pattern mining algorithm, CloseGraph, is developed by exploring several interesting pruning methods. Our performance study shows that CloseGraph not only dramatically reduces unnecessary subgraphs to be generated but also substantially increases the efficiency of mining, especially in the presence of large graph patterns.

- 6.5. SpiderMine: Mining Top-L Large Structural Patterns in a Single Network
  - Large patterns are informative to characterize a large network
  - Large patterns are compose of smaller ones (spiders)
  - SpiderMing algo:

- 6.6. Graph Pattern Mining Application I: Graph Indexing
  - Graph Index: Find all the graphs in a graph DB containing a given query graph. 
  - Only graph (c) contains Q
  - Path indices

- 6.7. Graph Pattern Mining Application II: Graph Similarity Search
  - Find graphs in a graph DB containing substructures similar to a given query graph. 
  - Feature based similarity search

- Summary:
  - Apriori based graph pattern mining methods
  - gSpan using growth based methods
  - CloseGraph for mining closed graph patterns
  - SpiderMine for mining top k large structural patterns in a single network
  - Applications: Graph indexing and grapt similarity search
  

- 7.1 Pattern Discovery for Software Bug Mining
  - Static bug detection. 
  - Why pattern mining? Code or running sequences contain hidden patterns. 
  - Mining rules from source code
    - Bugs as deviant behaviour: Static analysis
    - Mining programming rules
    - Mining function precedence protocols. 
  - Mining for copy and paste bugs
    - 12% linux bugs
    - 19% in windows system
  - Mine "forget-to-change" bugs by sequential pattern mining. 
  - Done by building a sequence database from source code. 
  - CP-Miner for example. 
  - 


## Week 4
- 8.1. Why Constraint-Based Mining
  - 
  - Classification, clustering, outlier?
  - SQL-like queries
  - Level types
  - Rules. 

- 8.2. Different Kinds of Constraints: Different Pruning Strategies
  - Pattern space pruning: 
  - data space pruning

- 8.3. Constrained Mining With Pattern Anti-Monotonicity
  - If itemset S violates contraint C, do does any superset. Mining of itemset S can be terminated.

- 8.4. Constrained Mining with Pattern Monotonicity
  - If itemset S satifies the contraint c, so does any of it's superset. 

- 8.5. Constrained Mining with Data Anti-Monotonicity
  - In the mining process, if a data entry cannot satisfy a pattern p under c, t cannot satisfy p's superset either. 
- 8.6. Constrained Mining with Succinct Constraints
  - Succinctness: if the contraint c can be enforced by directly manipulating the data. 
- 8.7. Constrained Mining with Convertible Constraints
  - Convert tough contraints into (anti-)monotone by proper ordering of items in transaction.

- 8.8. Handling Multiple Constraints
  - Beneficial to use multiple contraints in pattern mining. 
  - Different contraints may require potentially conflicting item ordering. 
  
- 8.9. Constraint-Based Sequential-Pattern Mining
  - Similar with contraint-based itemset mining


- 9.1. From Frequent Pattern Mining to Phrase Mining
  - Mining for semantically meaningful phrases

- 9.2. Previous Phrase Mining Methods
  - Originated from Chunking
  - Model is as a sequence labeling problem. 
  - Requires annotation, high cost and doesn't transfer. 
  - Unsupervised phrase mining
    - Topic modeling: Represents documents by multiple topics in diff proportions
    - No prior annotation 
  - Statistical topic models: LDA - Latent Dirichlet Allocation
  - BoW models
  - Simultaneously inferring phrases
    - Bigram Topic model: Prob generative model that contains on previous word and topic when drawing next word. 
    - Topic N-Grams 
    - Slow inference and complex
  - Post Topic-Modeling Phrase
    - TurboTopics: Phrase construction as a post processing step to LDA
  - KERT: Phrase construction as a post processing step to LDA
    - Performs Frequest pattern mining to extract 

- 9.3. ToPMine: Phrase Mining without Training Data
  - First phrase mining, doc segmentation, and phrase ranking
  - Topic model inference with phrase contraint
  - Phrase mining:  
  - Collocating mining: A seq of words that occur more frequesnt than expectex. 

- 9.4. SegPhrase: Phrase Mining with Tiny Training Sets
  - A small set of training data may enhance quality of phrase mining. 
  - ClassPhrase: Frequent Pattern minining, feature extraction, classification
  - SegPhrase


## Week 6
- Course Part 2 Overview: Cluster Analysis
  - Helps partion massive data into groups based on it's features. 
  - Help data mining processes such as pattern discovery, classification, and outliers. 
  - Applications: Summarization, compression, reduction
  - Data Mining book: Chapter 2 and 10 https://d396qusza40orc.cloudfront.net/clusteranalysis/Han_Data%20Mining%203e_Chapters%202%2C10%2C11%2C13.pdf

- 1.1. What Is Cluster Analysis?
  - Cluster? Collection of data objects which are similar or dissimilar. 
  - Cluster Analysis/Data Segmentation: Partitioning data points into set of similar groups.

- 1.2. Applications of Cluster Analysis
  - Lots of them. 
  - Preprossesing for other tasks. 
  - Outlier detection 
  - Data summarization, compression, 
  - Rec systems
  - Help with supervised tasks as well. 

- 1.3. Requirements and Challenges
  - Partitioning criteria: Single vs hierarchical partitioning.
  - Separation of clusters: Exclusive (one cluster) or non-exclusive (one or more clusters)
  - Similarity Measure: Distance based vs connectivity-based 
  - Clustering space: Full space(low dim) vs subspaces (high dim)
  - Quality: Different data types and noisy data
  - Scalability: Clustering all or just a sample. High dimensional data. 
  - Constraint based: Give user preferences or contraints or user queries. 

- 1.4. A Multi-Dimensional Categorization
  - Techniques: Distance vs density based
  - Data type centered: numberical data, text, time, or any othere data type. 
  - Additional insight-centered

- 1.5. An Overview of Typical Clustering Methodologies
  - Distance based: 
    - paritioning: k-means, k-median, k-medoids
    - Hierarchical algo: agglomerative vs divisive methods
  - Density-based and grid-based methods
    - Density based: https://cse.buffalo.edu/~jing/cse601/fa12/materials/clustering_density.pdf
    - Grid based: 
  - Probabilistic and generative models: Mixter of Gaussians, EM. 
  - High-dim clustering: 
    - Subspace clustering. Find cluster on various subspaces. Bottom up or top down. 
    - Dim reduction. 
    - PLSI then LDA for text data. Each topic is a cluster. 
  - NMF. Non negative matrix factorization. 

- 1.6. An Overview of Clustering Different Types of Data
  - Numerical: Most algo designed for this
  - Categorical data: Discrete
  - Text data: High dim, sparse. Combinations of k-means. 
  - Multimedia: images, audio, video. 
  - Time series: Temporally dependent
  - Sequence: weblogs, bio sequences
  - Stream data: real-time 
  - Graphs: Similar nodes and edges. Good for generative models, combinatorial algo, spectral methods. 

- 1.7. An Overview of User Insights and Clustering
  - Visual insights: Really helpful

- 2.1. Basic Concepts: Measuring Similarity between Objects
  - High inter-class similarity: Cohesive
  - Low inter class similarity: Distintive between clusters
  - Similarity measure or function
    - Measure how two data objects are alike. 0 to 1. 
  - Dissimilarity (distance) measure
    - Inverse of similarity in a way. The lower then better. 
    - Min = 0
  - Proximity. Similarity or Dissimilarity

- 2.2. Distance on Numeric Data Minkowski Distance
  - Data matrix. 
  - Dissimilarity matrix: Euclidean distance
  - Minkowski Distance
  - if p = 1 then we use L1 Norm or Manhattan distance: In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|.
  - if p = 2 then we use the l2 norm euclidean distance
  - if p goes to infinity then use supremum distance
  - 

- 2.3. Proximity Measure for Symetric vs Asymmetric Binary Variables
  - Symetric = chance they appear/not 
  - Asymmetric = they both appear

- 2.4. Distance between Categorical Attributes, Ordinal Attributes, and Mixed Types
  - AKA nominal attributes
  - Example: Color, profession, gender
  - Method: Simple matching or convert to binary values
  - Ordinal: Can be discrete or continuous values. Can be treated like interval-scaled. Example: 0,1/3,2/3,1
  - Attribute mixed types: 

- 2.4 Office Hour: Running Sample on How to Calculate Distance between Categorical Data
  - Using simple match formula. d = (m-p)/m. 
    - m is the number of attributes. p is the number of exactly matches attributes. 
  - Convert into binary representation. Sort of like one-hot encoding. 
    - For symmetric values: count matching columns, including 0s. 
    - For asymmetric values: ignore 0s, count matching values. 
    - Same fomula: d = (m-p)/m. 

- 2.5. Proximity Measure between Two Vectors: Cosine Similarity
  - Doc can be represented by a bag of terms or long vector. Each attribute recording freq of a term. 
  - Formula

- 2.6. Correlation Measures between Two Variables: Covariance and Correlation Coefficient
  - Variance: measure how much value of x deviates from the mean or expected of x. 
    - Formula: expected value of the square deviation from the mean. 
  - Covariance: how 2 variables corelate
    - positve covariance: if > 0
    - negative: if < 0
    - independence: If x1 and x2 are independent. 
    - range from -1 to 1.
    - Jaccard Index: https://www.statisticshowto.datasciencecentral.com/jaccard-index/
    - https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/correlation-coefficient-formula/#hand

  






