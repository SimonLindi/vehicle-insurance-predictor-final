### Disclaimer

I have hade many problems with the installation of the right version and permission problems. The reason I took so long is that I did not know how to login in the hugging face acces that popped up for everything it is also the reason i made this new repository because i was not able to commit in the end.

# Insurance Premium Prediction

This project aims to predict vehicle insurance premiums based on vehicle characteristics and value development over time. The application uses a machine learning model trained on real-world insurance and automotive data, deployed via an interactive Gradio interface.

## Overview

The prediction model estimates insurance premiums using the following input features:

- Vehicle age at the start of the insurance
- Current vehicle value
- Average yearly depreciation (value loss)
- Horsepower (PS)
- Power-to-weight ratio (PS per tonne)

The app allows users to enter these values and receive an estimated insurance premium in CHF.

## Machine Learning Model

We tested two different regression models:

- **Linear Regression**
- **Random Forest Regression**

After comparing performance metrics like RMSE and R², the **Random Forest Regressor** was selected as the final model because it consistently outperformed linear regression in handling non-linear relationships and interactions between features. It also showed better generalization to unseen data.

## Feature Engineering Highlights

- A new feature, **power-to-weight ratio**, was added to better capture performance-related risk.
- The **estimated original price** of a car was reverse-calculated using exponential depreciation, based on the insured value and the vehicle’s age. This step was crucial because premiums correlate more strongly with a car's starting value than with its current value.
- These custom features required domain understanding and added complexity, but significantly improved model accuracy.

## Technical Challenges

This project encountered several challenges:

- **Data Quality**: It was very difficult to find suitable datasets combining insurance premiums and vehicle specs. We used one insurance dataset and enriched it with external car data, joined on manufacturer and seat capacity.
- **Amortization Modeling**: Finding the right way to calculate the original car value using depreciation required multiple trials. Eventually, we settled on a fixed exponential loss rate per year (e.g. 12%) to approximate this value.
- **Deployment Issues**: Deploying on Hugging Face Spaces required exact version alignment for `scikit-learn`. The final model was trained using `scikit-learn 1.2.2`, but Hugging Face uses `1.6.1`. This led to serialization incompatibility and required setting up a local virtual environment with `1.6.1` to retrain and export the model for compatibility.
- Fixing this issue cost **a significant amount of time** and was a major technical roadblock late in the project.

## Usage

The app is deployed via Gradio and accepts user inputs in a simple UI. To run locally:

```bash
pip install -r requirements.txt
python app.py
