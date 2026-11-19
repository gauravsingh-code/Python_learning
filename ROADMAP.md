# AI Engineer Roadmap (Pareto / 80-20 Edition)

**Goal:** Get job-ready as an AI Engineer (build, ship, and evaluate ML + LLM systems).
**Assumes:** CS graduate, about 2–3 focused hours a day. Total time is about 20–24 weeks.
**Rule:** For every hour of watching or reading, spend 2 hours coding. Every phase ends with a project you push to GitHub.

Practice files follow your existing pattern: `practice/step_XX.py` or `notebooks/step_XX.ipynb`.

---

## The 20% That Gives 80% of Results

| Area | The vital 20% | What to skip or delay |
|---|---|---|
| Python | functions, comprehensions, dicts, classes, file I/O, venv/pip | metaclasses, decorators internals, async (until later) |
| Math | vectors, dot product, matrix multiply, gradient, probability, mean/variance | proofs, advanced linear algebra, measure theory |
| Data | pandas (load, filter, groupby, merge, missing values), NumPy arrays | rarely used pandas APIs |
| Classic ML | train/test split, linear/logistic regression, trees, **XGBoost/RandomForest**, metrics, overfitting | SVM kernels, Naive Bayes math, rarely used algorithms |
| Deep Learning | tensors, training loop, loss, backprop (concept), MLP, CNN basics, **Transformers/attention** | RNN/LSTM details, GANs, writing CUDA |
| LLM / GenAI | **prompting, embeddings, RAG, tool calling/agents, evaluation, fine-tuning (LoRA) basics** | pretraining LLMs from scratch |
| Engineering | Git, FastAPI, Docker, logging, testing, cloud deploy basics | Kubernetes in depth (learn later) |

> Industry note: Most AI Engineer jobs now ask for **PyTorch** and **LLM application skills** (RAG, agents) more than TensorFlow. Learn PyTorch first. Keras/TF is optional.

---

## Phase 0 — Setup (Day 1)
- [x] VS Code + Python extension, Jupyter, Git + GitHub account (local repo initialized; push to GitHub pending)
- [x] Use a virtual environment (you have `tf_env`; create `ml_env` with `torch` later)
- [ ] Learn: `python -m venv`, `pip install`, `requirements.txt`

## Phase 1 — Python for ML (Weeks 1–2)
Each step is one file in `practice/`.

| Step | Topic | Must-know |
|---|---|---|
| 01 ✅ | Variables, types, lists, loops, comprehensions | done |
| 02 | Dicts, sets, tuples, unpacking | `dict.get`, `.items()`, dict comprehension |
| 03 | Functions | default args, `*args/**kwargs`, `lambda`, `map/filter/sorted(key=)` |
| 04 | Strings & file I/O | f-strings, `split/join/strip`, `open`, `json`, `csv` |
| 05 | Error handling & modules | `try/except`, `import`, `if __name__ == "__main__"` |
| 06 | OOP | class, `__init__`, methods, inheritance, `__repr__` (scikit-learn and PyTorch use this heavily) |
| 07 | Pythonic tools | `enumerate`, `zip`, generators, type hints, `dataclass` |

**Project:** A CLI expense or house-price tracker that reads/writes JSON/CSV and uses classes.

## Phase 2 — Math for ML, the Practical Way (Weeks 3–4, alongside Phase 3)
Learn each concept **in NumPy code**, not on paper.
- **Linear algebra:** vectors, dot product (= similarity), matrix multiply (= a neural net layer), transpose, shape
- **Calculus:** derivative = slope, gradient, chain rule (= backprop), **gradient descent** (implement it yourself)
- **Probability/Stats:** mean, variance, std, normal distribution, conditional probability, Bayes idea, correlation
- **Resources:** 3Blue1Brown "Essence of Linear Algebra" + "Neural Networks" (YouTube), StatQuest (YouTube)

**Mini-project:** Implement linear regression with gradient descent in pure NumPy.

## Phase 3 — Data Stack: NumPy, pandas, Matplotlib (Weeks 3–5)
- **NumPy:** arrays, shape/reshape, indexing, boolean masks, broadcasting, vectorization (no loops)
- **pandas:** `read_csv`, `head/info/describe`, `loc/iloc`, filtering, `groupby`, `merge`, `fillna/dropna`, `apply`, `value_counts`
- **Visualization:** histogram, scatter, box plot, correlation heatmap (Matplotlib/Seaborn)
- **EDA workflow:** load → inspect → clean → visualize → find insights

**Project:** EDA on a Kaggle dataset (for example, House Prices or Titanic) in a notebook, written up with insights.

## Phase 4 — Classical Machine Learning with scikit-learn (Weeks 6–9)
**Core concepts (the most important 20% of all ML):**
- Supervised vs. unsupervised, features/labels, train/validation/test split
- **Overfitting vs. underfitting**, bias–variance, regularization (L1/L2)
- **Cross-validation**, hyperparameter tuning (`GridSearchCV`/`RandomizedSearchCV`)
- **Metrics:** regression (MAE, RMSE, R²); classification (accuracy, precision, recall, F1, ROC-AUC, confusion matrix)
- **Feature engineering:** scaling, one-hot encoding, handling missing values, `Pipeline` + `ColumnTransformer`
- Data leakage (common interview question)

**Algorithms (learn the intuition plus the sklearn API):**
1. Linear and logistic regression
2. Decision tree → **Random Forest** → **Gradient Boosting (XGBoost/LightGBM)** (the most-used models on tabular data)
3. KNN (concept only)
4. K-Means + PCA (unsupervised)

**Resource:** *Hands-On Machine Learning* (Aurélien Géron), chapters 1–7. Andrew Ng's ML Specialization (Coursera), optional.

**Projects (pick 2):** house price regression, customer churn classification, then save the model with `joblib`.

## Phase 5 — Deep Learning with PyTorch (Weeks 10–13)
- Tensors, autograd, GPU (`.to(device)`)
- **The training loop** (memorize it): forward → loss → `backward()` → `optimizer.step()` → `zero_grad()`
- `Dataset`/`DataLoader`, `nn.Module`, activations, loss functions, optimizers (SGD, Adam)
- MLP → CNN (image classification) → **transfer learning** with pretrained models
- Regularization: dropout, batch norm, early stopping
- **Transformers & attention** (most important): tokens, embeddings, self-attention, encoder vs. decoder

**Resources:** Andrej Karpathy's "Neural Networks: Zero to Hero" (YouTube; build micrograd + makeGPT), fast.ai Practical Deep Learning, PyTorch official tutorials.

**Projects:** MNIST/CIFAR classifier, fine-tuning a pretrained ResNet on a custom dataset, nanoGPT following Karpathy.

## Phase 6 — LLMs and GenAI Engineering (Weeks 14–18) ⭐ The core of an AI Engineer role
- **Hugging Face:** `transformers`, `pipeline`, tokenizers, model hub
- **LLM APIs:** OpenAI, Anthropic, or Gemini; open models via Ollama (local)
- **Prompt engineering:** system prompts, few-shot examples, structured output (JSON / Pydantic)
- **Embeddings + vector DBs:** cosine similarity, Chroma/FAISS/pgvector
- **RAG (Retrieval-Augmented Generation):** chunking → embed → retrieve → rerank → generate (the most in-demand skill)
- **Agents & tool calling:** function calling, MCP (Model Context Protocol), LangGraph/LlamaIndex (learn the concepts and avoid locking into one framework)
- **Evaluation:** test sets, LLM-as-judge, RAGAS, hallucination checks (this sets strong candidates apart)
- **Fine-tuning:** when to use it vs. RAG, LoRA/QLoRA with `peft`
- Cost, latency, token limits, caching, guardrails

**Projects (portfolio centerpieces):**
1. "Chat with your PDFs" RAG app with citations + evaluation
2. An agent that uses tools (web search, calculator, SQL database)
3. Fine-tune a small model (LoRA) for a specific task and compare it against prompting

## Phase 7 — MLOps and Deployment (Weeks 19–21)
- **FastAPI** to serve models as REST APIs; **Streamlit/Gradio** for demos
- **Docker** (containerize your app)
- Git workflow, `pytest`, logging, `.env` for secrets
- Experiment tracking: MLflow or Weights & Biases
- Deploy: Hugging Face Spaces (free), Render, or AWS/GCP/Azure basics
- Monitoring: data drift, LLM traces (LangSmith/Langfuse)

**Project:** Dockerize your RAG app with FastAPI + a simple UI and deploy it with a public link.

## Phase 8 — Job Readiness (Weeks 22–24, ongoing)
- [ ] GitHub: 3–4 polished projects with READMEs, demo GIFs/links, and results
- [ ] Resume: impact-focused bullets ("Built a RAG system… reduced X by Y%")
- [ ] Interview prep: ML fundamentals Q&A, system design for ML/LLM apps, Python coding (LeetCode easy/medium, ~50 problems)
- [ ] Write 2–3 blog posts or LinkedIn posts about your projects
- [ ] Kaggle: complete 1–2 competitions (aim for the top 50%)

---

## Daily Routine (Fast-Learning Method)
1. **15 min:** review yesterday's code (active recall)
2. **45 min:** learn one concept (video/book)
3. **90 min:** code it yourself without copy-pasting; break it, then fix it
4. **10 min:** write 3 bullet notes as comments at the top of the step file

## Rules for Learning Fast
- Build first, theory second. Learn theory when a project needs it.
- Don't watch more than one course per topic. Avoid "tutorial hell."
- Use AI assistants to **explain** errors, not to write all your code.
- Ship imperfect projects. Done is better than perfect.
