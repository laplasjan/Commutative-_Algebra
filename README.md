# Commutative-Algebra- Grafy: Key Features
- Graph Construction - T_pqr
 \
Generates a customizable graph T_pqr based on input parameters 𝑝, 𝑞, and r.
Supports varying configurations depending on the values of 𝑝,𝑞,𝑟
p,q,r, including edge connections and node weights.
- Weight Assignment - nadawanie_wag
Assigns weights to nodes in a graph using a provided list.
Ensures the graph nodes are initialized with custom weights for further operations.
-Weight Transformations:

 - Reflection - odbicie: Reflects weights of a node and updates its neighbors based on specific transformation rules.
 - Increment/Decrement - ro_1 and ro_2: Globally adjusts node weights by a fixed increment or decrement.
 - Iterative Weight Normalization
Procedures to transform all node weights to positive or negative values using iterative reflection:
- Positive Weight Normalization:
- - zmiana_na_dodatnie_obl: Iteratively adjusts negative weights without sorting.
- - zmiana_na_dodatnie: Prioritizes nodes with the smallest weights.
- Negative Weight Normalization:
- - zmiana_na_ujemne_obl: Iteratively adjusts positive weights without sorting.
- - zmiana_na_ujemne: Prioritizes nodes with the largest weights.
- - Selective Node Exclusion
Allows specific nodes to be excluded from transformations:
- - omijanie_dodatnich: Avoids certain nodes during positive weight normalization.
- - omijanie_ujemnych: Avoids certain nodes during negative weight normalization.

# Usage Instructions
Run the Notebook:
Execute the notebook in a Python environment that supports networkx and matplotlib.

- Graph Creation:
Call T_pqr(p, q, r) with desired parameters to generate a graph.

- Weight Assignment and Transformation:
Use nadawanie_wag to initialize weights and apply transformations like odbicie or zmiana_na_dodatnie.

- Iterative Procedures:
Apply functions like zmiana_na_dodatnie or omijanie_ujemnych to perform weight normalization or selective adjustments.

- Visualization:
Use matplotlib to visualize the final graph configuration.

# Output Highlights
Sequential transformations of node weights with iteration details.
Terminal state of node weights and the sequence of transformations applied.
Configurable parameters for iterative limits and node exclusions.
This notebook serves as a foundation for exploring graph theory concepts, particularly focusing on weighted graph transformations and custom manipulations. For more details, please refer to the code comments within the notebook.
