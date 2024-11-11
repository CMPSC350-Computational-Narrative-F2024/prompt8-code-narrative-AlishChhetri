# 1. Prompts Used

Zero-shot: “Generate Python code that illustrates a journey of discovery. The code should simulate a search or exploration process.”

Few-shot with chaining: “Make each function call a step in a search journey. Use meaningful names and add guiding comments.”

Many-shot with chain of thought: “Add dialogue between functions to mimic discovery. Use narrative-focused variable names and clarify each step with comments.”

## 2. Prompting Strategy

I began with a zero-shot prompt to set the discovery theme, then moved to few-shot with chaining for clearer steps, and finally used many-shot with chain of thought to refine the narrative flow and commentary. This layered prompting approach developed continuity, meaningful names, and a storytelling feel.

## 3. Output Evaluation

Narrative Structure: Copilot’s code needed prompts to align with the theme, while GPT-4 naturally provided a clear journey with cohesive narrative elements.

Comments: Copilot’s initial comments were functional, but iterative prompts improved storytelling. GPT-4 provided descriptive comments aligned with the discovery theme from the start.

Design Choices: Copilot’s variable names became more thematic with prompts, while GPT-4 required fewer adjustments to achieve a natural exploration feel.

### Copilot

Copilot initially generated logical but plain code with functional names and limited narrative. Through iterative prompting, its storytelling improved, with variable names and comments that better represented exploration. Overall, it needed more guidance to reach a narrative-driven structure.

### Other Single LLM (GPT)

GPT-4’s code aligned more naturally with the narrative goal. It used descriptive variable names and comments that felt like a guided journey, requiring minimal adjustments to convey discovery. The output was engaging and required fewer refinements to support the story.

## 4. Reflection

Iterative prompting enhanced Copilot’s narrative quality, making it align more with the storytelling theme. GPT-4, however, achieved a narrative flow more intuitively, showing its advantage in handling narrative-based prompts with fewer adjustments. This highlights the natural differences in each model’s approach to "code as a narrative."
