# 🧬 Expected Offspring Dominant Phenotype Calculator

This project calculates the **expected number of offspring displaying the dominant phenotype** in a population, based on genotype pairings of couples.

## 📘 Problem Description

In classical Mendelian genetics, the dominant allele (represented as **A**) masks the presence of the recessive allele (**a**). Given a list of couples with known genotype pairings, and assuming each couple has exactly two children, this script computes the **expected number of children** who will exhibit the dominant phenotype.

### 🧪 Input Format

The input consists of a single line with six non-negative integers (each ≤ 20,000), representing the number of couples with the following genotype pairings:

1. `AA-AA`
2. `AA-Aa`
3. `AA-aa`
4. `Aa-Aa`
5. `Aa-aa`
6. `aa-aa`

### 🎓 Genetic Assumptions

Each couple produces exactly two offspring. Based on Mendelian inheritance, the probability that a child will show the dominant phenotype (either `AA` or `Aa`) for each couple type is:

| Genotype Pair | Probability of Dominant Phenotype |
|---------------|-----------------------------------|
| AA-AA         | 1                                 |
| AA-Aa         | 1                                 |
| AA-aa         | 1                                 |
| Aa-Aa         | 0.75                              |
| Aa-aa         | 0.5                               |
| aa-aa         | 0                                 |

## 💡 How It Works

The expected number of dominant phenotype offspring is computed by:

```
Expected = Σ (couple_count[i] × 2 × dominant_probability[i])
```

## 👁️ Example

### Input (`sample_dataset.txt`):
```
1 0 0 1 0 1
```

### Output:

```
3.5
```

## 📄 Usage

### Run the script
```bash
python expected_offspring.py
```

Make sure your input file (e.g., `sample_dataset.txt`) is in the same directory.

## 🚀 Features

- Simple Mendelian genetics model
- Reads input from a `.txt` file
- Clean and modular Python code

## 💼 License

This project is licensed under the MIT License.
