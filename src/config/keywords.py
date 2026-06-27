# keywords.py
# Production keywords (moved from feature)
PRODUCTION_CORE = {"production", "shipped", "deployed", "model serving"}
PRODUCTION_SUPPORT = {"latency", "throughput", "online experiment", "inference optimization"}

# Literal keyword lists for required/preferred (used in JD parsing)
REQUIRED_KEYWORDS = [
    "python",
    "faiss",
    "ranking",
    "retrieval",
    "vector",
    "embedding",
    "pytorch",
    "tensorflow",
    "nlp",
]

PREFERRED_KEYWORDS = [
    "kubernetes",
    "docker",
    "aws",
    "gcp",
    "azure",
    "mlflow",
    "kubeflow",
]