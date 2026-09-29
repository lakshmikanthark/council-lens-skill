<!-- SPDX-License-Identifier: Apache-2.0 -->

# GitHub setup

Recommended repository name:

```text
council-lens-skill
```

Suggested description:

> Evidence-aware multi-perspective decision review Skill for ChatGPT, with blind challenge, adaptive depth and reproducible release QA.

Suggested topics:

```text
chatgpt-skills
ai-agents
decision-making
llm
prompt-engineering
reasoning
ai-tools
open-source
```

## Publish

1. Create an empty GitHub repository named `council-lens-skill`.
2. Extract this release ZIP locally.
3. From the extracted repository folder:

```bash
git init
git add .
git commit -m "release: Council Lens v2.0.0"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

4. Confirm the GitHub Actions validation workflow passes.
5. Optionally create a `v2.0.0` release and attach `dist/skill.zip`.

Do not rename the project to include OpenAI, ChatGPT or GPT as the product name. Describing compatibility with ChatGPT in the README is intentional; using the mark as the product identity is not.
