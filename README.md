# VAST Mini Challenge-1  
#### **This repository will remain private until approved by my instructor Dr. Anna baynes**

---
### Background
FishEye International is an organization focused on combating illegal, unreported, and unregulated (IUU) fishing, it uses natural language processing to analyze online news articles about fishing and marine trade, extracting names of entities and their relationships to create a knowledge graph for further investigation into illegal fishing activities. One challenge they face is how to quickly understand and explore the context around a tip related to potential IUU fishing. While FishEye has a traditional node-link visualization, it can be overwhelming due to the volume of information.
Our task is to use visual analytics to create a more effective tool for FishEye analysts. This tool should highlight relevant context and hide irrelevant information, enabling dynamic and interactive exploration around tips. The ultimate goal is to assist FishEye in identifying potential entities, such as companies, that could be involved in illegal fishing activities.

---
### Entities to investigate
1. Mar de la Vida OJSC
2. 979893388
3. Oceanfront Oasis Inc Carrie
4. 8327
---

### Questions [Q1, Q2, Q3, Q4]
1. **[Q1]** Use visual analytics to dynamically display and explore context around the suspected entities listed above. What did you learn about each one? Can you connect them to illegal fishing? Provide evidence for or against the case that each entity is involved in illegal fishing and use visual analytics to express confidence in your conclusions. Limit your response to 600 words and 6 images.

2. **[Q2]** Use your visual analytics tool to compare and contrast what you learned about the suspect entities. Are there patterns that may indicate illegal activity? Use visual analytics to express confidence that a pattern exists and where uncertainty may be affecting this confidence. Limit your response to 400 words and 4 images.

3. **[Q3]** What other companies should FishEye investigate for illegal fishing? Show how your visual analytics can be used to find entities that are worthy of further investigation. Limit your response to 600 words and 6 images.

4. **[Q4]** Reflection: What was the most difficult aspect of working with this knowledge graph? Did you have the tools and resources you needed to complete the challenge? What additional resources would have helped you? Limit your response to 300 words
---

### Dataset Description:
  - Directed multi-graph: multiple edges between the same two nodes are possible.
  - Contains 3721 Nodes and 7422 Edges.
  - JSON format matches D3's node-link format (Compatible with networkx.nodelinkgraph).
  - The node entries must include a unique id key for each node.
  - The links entries include source and target keys that refer to node id values.

  - #### Node Attributes:
    - **Id**      : Identifier of the node is also usually the name of the entity. Some nodes have a numeric ID and do not have a name even if   they are a person, company, or organization.
    - **type**    : Type of the node as defined above. It is an optional attribute
    - **country** : Country associated with the entity. It is an optional attribute.
    - **dataset** : Always ‘MC1’
      
  - #### Edge Attributes:    
    - **source**  : ID of the source node
    - **target**  : ID of the target node
    - **type**    : Type of the edge as defined above. It is an optional attribute
    - **dataset** : Always ‘MC1’

---
