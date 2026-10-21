# Edge-AI Assisted Diagnosis of Triticum aestivum (Wheat) Pathogens: A Lightweight Deep Learning Approach

**Abstract**  
Wheat productivity is globally threatened by fungal pathogens such as rusts and blights, which can cause yield losses of up to 50%. This study presents a mobile-first, AI-driven diagnostic framework utilizing Deep Convolutional Neural Networks (CNNs). By processing handheld imagery through a Cloud-based Vision Transformer (ViT) architecture, the system provides real-time identification and actionable alerts for farmers. 

## 1. Introduction
Wheat (*Triticum aestivum*) provides 20% of the world's caloric intake. Diseases like Leaf Rust and Loose Smut are spreading rapidly. This research bridges the gap between advanced pathology and field-level diagnosis by developing a portable AI diagnostic tool.

## 2. Methodology
The system architecture utilizes a **Vision Transformer (ViT)** model. Unlike standard CNNs, ViT uses "Attention Mechanisms" to identify specific textures in leaf pustules. 
*   **Data Sourcing**: PlantVillage and Global Wheat Challenge datasets.
*   **Deployment**: The app is hosted on a distributed cloud architecture (Koyeb) for low-latency results.

## 3. Results
The integrated system successfully classifies Wheat pathogens with a high degree of confidence. Specifically, the model distinguishes between "Rust" (fungal pustules) and "Healthy" tissue by analyzing pixel-level color variations.

## 4. Conclusion
Integrating lightweight AI models into handheld devices empowers farmers to act before a localized infection becomes an epidemic.
