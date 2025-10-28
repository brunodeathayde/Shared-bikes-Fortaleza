# 🚲 PCA-Based Suitability Index for Shared Bicycle Use

This project uses **Principal Component Analysis (PCA)** to create a synthetic index that evaluates the suitability of neighborhoods for shared bicycle usage. It combines production and input variables to generate a normalized score for each neighborhood.

---

## 📁 Files

- `PCA.py`: Python script that performs PCA to compute the suitability index.
- `neighborhoods.xlsx`: Input spreadsheet containing raw data for each neighborhood.
- `index.xlsx`: Output spreadsheet with the PCA-based index and transformed variables.

---

## 📊 Methodology

The PCA-based index is calculated using the following variables:

- **Production variable**:
  - Number of shared bicycle trips per neighborhood per year

- **Input variables**:
  - Population density
  - Income-based Human Development Index (HDI)
  - Average number of residents per household

### Steps:
1. **Read and preprocess data** from `neighborhoods.xlsx`
2. **Normalize** all variables to the range [0, 1]
3. **Invert input variables** (lower values are more desirable)
4. **Apply PCA** with one component to extract a synthetic index
5. **Normalize the PCA score** to [0, 1]
6. **Force zero index** for neighborhoods with zero bicycle trips
7. **Export results** to `index.xlsx`

---

## 📦 Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
