# NYC Airbnb Data Workflow

## Project Description
This project analyzes the New York City Airbnb Open Data dataset to explore how
price relates to borough, room type, and listing activity. It walks through
loading, cleaning, exploring, and visualizing nearly 49,000 Airbnb listings to
identify pricing patterns across NYC. The workflow is built as a reusable
foundation that could be extended into a machine learning project.

**Dataset:** New York City Airbnb Open Data (`AB_NYC_2019.csv`) — ['https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data']

## How to Run
1. Clone this repository and navigate into the project folder.
2. Install dependencies:
    pip install -r requirements.txt
3. Open `data_workflow.ipynb` in Jupyter Notebook, JupyterLab, or VS Code and run all cells top to bottom.

## Reproducibility
Dependencies are pinned in `requirements.txt` (generated via `pip freeze > requirements.txt`).
All work is tracked in Git, with development done on a separate `development` branch
before merging into `main`, so the commit history documents how the analysis evolved.

## Bias Awareness
Several cleaning decisions could introduce bias if applied carelessly. Dropping the
11 listings priced at $0 assumed they were data errors — if any were real
promotional listings, this systematically removes some low-price data points.
Filling missing `reviews_per_month` values with 0 was verified against
`number_of_reviews` rather than assumed outright, but that verification step is
easy to skip and would otherwise bias any review-activity analysis. More broadly,
reporting only borough-level price averages can mask finer-grained inequality
within neighborhoods, so any downstream use of these aggregates should be paired
with neighborhood-level checks before drawing conclusions about specific areas.

## Future Integration Reflections

**Machine Learning Workflow:** Turning this into a predictive ML workflow (e.g.,
predicting price) would keep the same cleaning/EDA steps, but require a
train/test split before any transformation to avoid data leakage, and encoding
categorical fields like `room_type` and `neighbourhood_group` (e.g., one-hot
encoding) as part of a repeatable pipeline rather than one-off notebook cells.

**Neural Network Preparation:** A neural network would need all categorical
fields numerically encoded (one-hot or embeddings), all numeric features scaled
or normalized, and the `price` target likely log-transformed given the strong
right skew shown in Visualization 2 — raw skewed targets are harder for neural
nets to learn from directly.

**Agentic Automation Potential:** An agentic system could automate the
repetitive parts of this workflow — rerunning the missing-data diagnostics,
applying the established cleaning functions, regenerating the three
visualizations, and flagging new data-quality issues (e.g., new zero-price
listings) whenever the underlying dataset refreshes — only pausing for human
review when something falls outside previously verified assumptions.
