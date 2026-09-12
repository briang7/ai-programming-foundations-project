# A New York City Airbnb Analysis Project

**Overview**

This project breaks down the New York City Airbnb Open Data dataset (AB_NYC_2019.csv), available on Kaggle at ['https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data']. We build a data cleaning, exploratory analysis, and visualization workflow. data_workflow.ipynb implements the workflow, loading nearly 49,000 NYC Airbnb listings, cleaning multiple data-quality issues, exploring pricing patterns across boroughs and room types, and visualizing the results. Future machine learning work can use this as a reusable foundation on the same data. 

**Dataset Description**

The dataset covers New York City's 48,895 Airbnb listings across it's 5 boroughs. 16 columns describing the listings location, host, pricing, and review activity. The main variables include price (nightly rate in USD), neighbourhood_group (borough), room_type (entire home/apt, private room, or shared room), number_of_reviews, reviews_per_month, and availability_365 (days available per year). The snapshot is of the 2019 NYC short-term rental market.

**Workflow Description**

The workflow followed five stages. Ingestion: the CSV was loaded directly with pandas.read_csv. Cleaning: three functions addressed distinct data-quality issues, filling missing reviews_per_month values with 0 (for listings with zero reviews), filling a small number of missing name/host_name fields with a placeholder, and removing 11 listings with an invalid price of $0. Exploratory analysis: a single function computed summary statistics, average price grouped by borough and room type, and a correlation matrix across the key numeric variables. Visualizations: three figures were produced, a bar chart of average price by borough, a log-scale histogram of price distribution, and a correlation heatmap. Summary: a markdown section in the notebook interprets the findings, limitations, and assumptions.

**Key Decisions and Assumptions**

Each cleaning decision was grounded in evidence from the data rather than assumption alone. The $0-price listings were treated as data-entry errors and removed, since a real nightly rate cannot reasonably be zero. Rather than assuming the missingness in reviews_per_month was random, we verified the underlying mechanism before imputing, confirming that all 10,052 missing values corresponded exactly to listings with number_of_reviews == 0. This mattered because naive imputation without understanding the missingness mechanism can introduce systematic bias into a dataset (Zhao et al., 2023). The EDA focused specifically on how price relates to geography (neighbourhood_group) and listing type (room_type), and on whether pricing relates to review activity, a relationship we tested explicitly rather than assumed. The log-scale histogram (Figure 2) was chosen specifically because price is heavily right-skewed (ranging from $10 to $10,000, with 75% of listings under $175). A linear-scale histogram would have compressed nearly all the data into a single bar.

**Results and Interpretation**

Figure 1 shows a clear borough-level price gradient: Manhattan listings average roughly $197/night, more than double Bronx listings at roughly $88/night, with Brooklyn, Staten Island, and Queens forming a middle cluster ($100-$125). Within every borough, room type follows a consistent ordering, entire homes/apartments cost more than private rooms, which cost more than shared rooms. Figure 2 shows the price distribution peaking around $110-$126/night (the single most common price band, ~4,078 listings), staying dense between roughly $70 and $170, and tapering into a long right-skewed tail extending to $10,000. Figure 3's correlation heatmap shows that number_of_reviews and reviews_per_month are strongly correlated (r = 0.589), which is expected since both measure the same underlying review activity. availability_365 and calculated_host_listings_count show a moderate positive correlation (r = 0.226), potentially reflecting professional or multi-listing hosts who keep their properties available year-round. Notably, price shows essentially no correlation with review activity (r = -0.05 across all listings, r = -0.03 restricted to listings with at least one review), a finding we tested explicitly by excluding never-reviewed listings, ruling out the possibility that the ~21% of listings with zero reviews were masking a real relationship.

**Responsible Practice (Bias and Data Quality)**

Several cleaning and analysis decisions carry potential bias risks worth acknowledging. Dropping the 11 zero-priced listings assumed these were data-entry errors. If any were legitimate free or promotional listings, this decision would systematically remove some low-price data points from the dataset. Imputation choices carry real risk of bias if the missing-data mechanism isn't understood before filling values (Zhao et al., 2023). We handled this specific risk by testing our assumption against number_of_reviews rather than filling blindly. More broadly, reporting only borough-level price averages risks masking finer-grained inequality or disparity within individual neighborhoods, so any downstream use of these aggregates should be paired with neighborhood-level analysis before drawing conclusions about specific communities.

**Reproducibility**

This project follows a reproducible workflow modeled in part on the practices described by Danchev (2022), whose learning resource emphasizes documenting the full data-analysis process, including data inputs, code, and narrative interpretation, in a single, reproducible artifact. Following this principle, dependencies for this project are pinned in requirements.txt (generated via pip freeze), allowing anyone to recreate the exact environment used to run data_workflow.ipynb with pip install -r requirements.txt. As Danchev (2022) notes, a requirements.txt file is central to enabling reproducible execution environments (e.g., via tools like MyBinder), minimizing errors caused by package version drift. All project work was also tracked in Git, with development carried out on a separate development branch and merged into main, so the full commit history documents how the analysis evolved over time.

**Sources and Citations**

Danchev, V. (2022). Reproducible data science with Python: An open learning resource. Journal of Open Source Education, 5(56), 156. https://doi.org/10.21105/jose.00156

Zhao, H., Sun, K., Dezfouli, A., & Bonilla, E. V. (2023). Transformed distribution matching for missing value imputation. In Proceedings of the 40th International Conference on Machine Learning (PMLR 202). https://arxiv.org/abs/2302.10363